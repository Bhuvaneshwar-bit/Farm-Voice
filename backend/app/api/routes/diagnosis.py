import uuid
from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.models.schemas import DiagnoseRequest, DiagnoseResponse, ErrorResponse
from app.core import stt, tts, vision, llm, rag, weather as weather_module
from app.core.config import settings, get_current_season
from app.models.database import save_diagnosis

router = APIRouter()


@router.post("/diagnose", response_model=DiagnoseResponse)
async def diagnose_crop(request: DiagnoseRequest):
    session_id = str(uuid.uuid4())

    # ── Step 1: Get transcript ──────────────────────────────────────
    if request.audio_base64:
        try:
            transcript, detected_language = await stt.transcribe_audio(
                request.audio_base64,
                language_hint=request.language if request.language != "auto" else None,
            )
        except Exception as e:
            raise HTTPException(status_code=422, detail=f"Audio transcription failed: {str(e)}")
    elif request.text_input:
        transcript = request.text_input.strip()
        detected_language = request.language if request.language != "auto" else "en"
    else:
        raise HTTPException(status_code=400, detail="Provide either audio_base64 or text_input.")

    if not transcript:
        raise HTTPException(status_code=422, detail="Could not extract speech from audio. Please try again.")

    language = detected_language if request.language == "auto" else request.language

    # ── Step 2: Visual analysis ─────────────────────────────────────
    visual_analysis = None
    if request.image_base64:
        visual_analysis = await vision.analyze_crop_image(request.image_base64)

    # ── Step 3: Weather context ─────────────────────────────────────
    weather_data = None
    if request.latitude is not None and request.longitude is not None:
        weather_data = await weather_module.get_weather(request.latitude, request.longitude)
    weather_str = weather_module.format_weather_for_prompt(weather_data)

    # ── Step 4: Extract entities → RAG query ───────────────────────
    entities = await llm.run_entity_extraction(transcript)
    crop_hint = entities.get("crop") or request.crop_type
    symptom_query = f"{crop_hint or ''} {' '.join(entities.get('symptoms', []))} {transcript}"
    rag_context = rag.query_knowledge_base(symptom_query, crop_hint=crop_hint, n_results=5)

    # ── Step 5: Main diagnosis ──────────────────────────────────────
    month = datetime.utcnow().month
    season = get_current_season(month)

    diagnosis_data = await llm.diagnose(
        transcript=transcript,
        visual_analysis=visual_analysis,
        weather_info=weather_str,
        rag_context=rag_context,
        language=language,
        latitude=request.latitude,
        longitude=request.longitude,
        season=season,
        crop_hint=crop_hint,
    )

    # ── Step 6: TTS audio response ──────────────────────────────────
    audio_text = diagnosis_data.get("response_audio_text", "")
    audio_b64 = await tts.text_to_speech(audio_text, language) if audio_text else None

    # ── Step 7: Persist to DB ───────────────────────────────────────
    diag = diagnosis_data.get("diagnosis", {})
    await save_diagnosis(
        session_id=session_id,
        transcript=transcript,
        detected_language=language,
        primary_disease=diag.get("primary_disease", "Unknown"),
        confidence=diag.get("confidence", 0),
        severity=diag.get("severity", 1),
        urgency=diagnosis_data.get("urgency", "medium"),
        latitude=request.latitude,
        longitude=request.longitude,
        diagnosis_json=diagnosis_data,
    )

    # ── Step 8: Build response ──────────────────────────────────────
    treatment_raw = diagnosis_data.get("treatment", {})
    chem_list = [
        {
            "product": c.get("product", ""),
            "active_ingredient": c.get("active_ingredient", ""),
            "dosage": c.get("dosage", ""),
            "frequency": c.get("frequency", ""),
            "safety_precautions": c.get("safety_precautions", ""),
        }
        for c in treatment_raw.get("chemical", [])
    ]

    weather_ctx = None
    if weather_data:
        weather_ctx = {
            "temperature": weather_data.get("temperature"),
            "humidity": weather_data.get("humidity"),
            "rainfall_mm": weather_data.get("rainfall_mm"),
            "wind_speed": weather_data.get("wind_speed"),
            "description": weather_data.get("description"),
            "location_name": weather_data.get("location_name"),
            "disease_risk_note": weather_data.get("disease_risk_note"),
        }

    return DiagnoseResponse(
        session_id=session_id,
        transcript=transcript,
        detected_language=language,
        diagnosis={
            "primary_disease": diag.get("primary_disease", "Unknown"),
            "local_name": diag.get("local_name", diag.get("primary_disease", "Unknown")),
            "scientific_name": diag.get("scientific_name", ""),
            "confidence": diag.get("confidence", 0),
            "severity": max(1, min(5, diag.get("severity", 1))),
            "affected_crop": diag.get("affected_crop", ""),
            "stage": diag.get("stage", "unknown"),
        },
        explanation={
            "key_symptoms": diagnosis_data.get("explanation", {}).get("key_symptoms", []),
            "visual_evidence": diagnosis_data.get("explanation", {}).get("visual_evidence", []),
            "environmental_factors": diagnosis_data.get("explanation", {}).get("environmental_factors", []),
            "reasoning": diagnosis_data.get("explanation", {}).get("reasoning", ""),
        },
        alternatives=diagnosis_data.get("alternatives", []),
        treatment={
            "immediate": treatment_raw.get("immediate", []),
            "organic": treatment_raw.get("organic", []),
            "chemical": chem_list,
            "cultural_practices": treatment_raw.get("cultural_practices", []),
            "prevention": treatment_raw.get("prevention", []),
        },
        urgency=diagnosis_data.get("urgency", "medium"),
        recovery_timeline=diagnosis_data.get("recovery_timeline", "1-2 weeks with treatment"),
        weather_context=weather_ctx,
        audio_response_base64=audio_b64,
        response_text=diagnosis_data.get("response_audio_text", ""),
        english_summary=diagnosis_data.get("english_summary", ""),
    )
