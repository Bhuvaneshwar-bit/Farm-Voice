import json
import re
from typing import Optional, Dict, Any
from groq import Groq
from app.core.config import settings, GROQ_LLM_MODEL, GROQ_FAST_MODEL, SUPPORTED_LANGUAGES

client = Groq(api_key=settings.GROQ_API_KEY)

SYSTEM_PROMPT = """You are FarmVoice, an expert agricultural AI assistant helping smallholder farmers in India.

You specialize in:
- Crop disease diagnosis and treatment (rice, wheat, tomato, potato, cotton, maize, vegetables, fruits)
- Pest identification and integrated pest management
- Soil and nutrient deficiency diagnosis
- Regional Indian agricultural knowledge (varieties, local product names, practices)

Your response principles:
1. PRACTICAL: Give specific, actionable steps farmers can take TODAY
2. ACCESSIBLE: Simple language, no jargon. Farmers are not scientists.
3. AFFORDABLE: Prioritize low-cost/organic options; chemical options as fallback
4. ACCURATE: Base diagnosis on evidence from symptoms, weather, visual data
5. SAFE: Always mention basic pesticide safety
6. REGIONAL: Mention locally available products and Indian brand names where known

IMPORTANT: You must always respond with valid JSON only. No markdown, no code fences, no text outside JSON."""


def build_diagnosis_prompt(
    transcript: str,
    visual_analysis: Optional[str],
    weather_info: str,
    rag_context: str,
    language: str,
    latitude: Optional[float],
    longitude: Optional[float],
    season: str,
    crop_hint: Optional[str],
) -> str:
    lang_name = SUPPORTED_LANGUAGES.get(language, SUPPORTED_LANGUAGES["en"])["name"]
    location_str = f"Lat: {latitude:.3f}, Lon: {longitude:.3f}" if latitude and longitude else "Location not provided"

    return f"""
FARMER'S VOICE REPORT (transcribed):
"{transcript}"

VISUAL ANALYSIS OF CROP PHOTO:
{visual_analysis if visual_analysis else "No image provided by farmer."}

CURRENT WEATHER CONDITIONS:
{weather_info}

RELEVANT AGRICULTURAL KNOWLEDGE:
{rag_context}

CONTEXT:
- Location: {location_str}
- Season: {season}
- Crop hint from farmer: {crop_hint or "not specified"}
- Language for response: {lang_name} ({language})

TASK: Diagnose the crop problem and generate a complete actionable response.

Return ONLY valid JSON (no markdown, no extra text) with this exact structure:
{{
  "diagnosis": {{
    "primary_disease": "Disease or problem name in English",
    "local_name": "Name in {lang_name} language",
    "scientific_name": "Scientific name (if applicable)",
    "confidence": <integer 0-100>,
    "severity": <integer 1-5, where 1=minor 5=critical>,
    "affected_crop": "Crop name in English",
    "stage": "early/mid/late stage of disease/infestation"
  }},
  "explanation": {{
    "key_symptoms": ["symptom matched from farmer description 1", "symptom 2"],
    "visual_evidence": ["visual clue from photo if available"],
    "environmental_factors": ["weather or season factor that supports diagnosis"],
    "reasoning": "2-3 sentence explanation in simple language of HOW you reached this diagnosis"
  }},
  "alternatives": [
    {{
      "disease": "Alternative diagnosis 1",
      "confidence": <integer>,
      "differentiator": "What to look for to rule this in or out"
    }}
  ],
  "treatment": {{
    "immediate": ["Urgent action to do within 24 hours - be specific"],
    "organic": ["Organic/natural option with dosage and method"],
    "chemical": [
      {{
        "product": "Generic product name",
        "active_ingredient": "Active ingredient",
        "dosage": "Amount per liter or per acre",
        "frequency": "How often to apply",
        "safety_precautions": "Key safety note"
      }}
    ],
    "cultural_practices": ["Long-term cultural practice to prevent recurrence"],
    "prevention": ["Preventive measure for next season"]
  }},
  "urgency": "critical/high/medium/low",
  "recovery_timeline": "Expected time to recovery if treated",
  "response_audio_text": "2-3 sentence farmer-friendly explanation in {lang_name}. Spoken aloud to the farmer. Include: disease name, one immediate action, one treatment. Simple words only.",
  "english_summary": "One sentence English summary for system logs"
}}
"""


async def run_entity_extraction(transcript: str) -> Dict[str, Any]:
    """
    Fast entity extraction using Llama 3.1 8B (instant model) for better RAG queries.
    """
    try:
        response = client.chat.completions.create(
            model=GROQ_FAST_MODEL,
            max_tokens=150,
            temperature=0.1,
            messages=[{
                "role": "user",
                "content": f"""Extract from this farmer's statement:
1. Crop name (rice/wheat/tomato/potato/cotton/maize/other - pick closest)
2. Main symptoms (3 words each, max 3 symptoms)
3. Urgency (high/medium/low)

Statement: "{transcript}"

Respond as JSON only, no extra text: {{"crop": "...", "symptoms": ["...", "..."], "urgency": "..."}}"""
            }]
        )
        raw = response.choices[0].message.content.strip()
        # Strip markdown if present
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
        return json.loads(raw)
    except Exception:
        return {"crop": None, "symptoms": [], "urgency": "medium"}


async def diagnose(
    transcript: str,
    visual_analysis: Optional[str],
    weather_info: str,
    rag_context: str,
    language: str,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    season: str = "unknown",
    crop_hint: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Full diagnosis using Llama 3.3 70B (via Groq, open-source, free).
    Returns structured diagnosis dict.
    """
    prompt = build_diagnosis_prompt(
        transcript=transcript,
        visual_analysis=visual_analysis,
        weather_info=weather_info,
        rag_context=rag_context,
        language=language,
        latitude=latitude,
        longitude=longitude,
        season=season,
        crop_hint=crop_hint,
    )

    response = client.chat.completions.create(
        model=GROQ_LLM_MODEL,
        max_tokens=2000,
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
    )

    raw = response.choices[0].message.content.strip()

    # Strip markdown fences if model adds them
    raw = re.sub(r"^```[a-z]*\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)

    return json.loads(raw)
