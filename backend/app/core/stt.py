import base64
import tempfile
import os
from typing import Tuple, Optional
from app.core.config import settings

_whisper_model = None


# ─── Local Whisper (faster-whisper on CPU) ────────────────────────────────────

def _load_local_model():
    global _whisper_model
    if _whisper_model is None:
        from faster_whisper import WhisperModel
        _whisper_model = WhisperModel(
            settings.WHISPER_MODEL_SIZE,
            device="cpu",
            compute_type="int8",
        )
    return _whisper_model


async def _transcribe_local(audio_bytes: bytes, language_hint: Optional[str]) -> Tuple[str, str]:
    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name
    try:
        model = _load_local_model()
        segments, info = model.transcribe(
            tmp_path,
            language=language_hint if language_hint and language_hint != "auto" else None,
            beam_size=5,
            vad_filter=True,
            vad_parameters={"min_silence_duration_ms": 300},
        )
        transcript = " ".join(seg.text.strip() for seg in segments)
        return transcript.strip(), info.language or "en"
    finally:
        os.unlink(tmp_path)


# ─── Groq Whisper API (open-source Whisper large-v3, free) ────────────────────

async def _transcribe_groq(audio_bytes: bytes, language_hint: Optional[str]) -> Tuple[str, str]:
    from groq import Groq
    from app.core.config import GROQ_STT_MODEL

    client = Groq(api_key=settings.GROQ_API_KEY)

    with tempfile.NamedTemporaryFile(suffix=".webm", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        with open(tmp_path, "rb") as audio_file:
            kwargs = {
                "file": ("audio.webm", audio_file, "audio/webm"),
                "model": GROQ_STT_MODEL,
                "response_format": "verbose_json",
            }
            if language_hint and language_hint != "auto":
                kwargs["language"] = language_hint

            transcription = client.audio.transcriptions.create(**kwargs)

        transcript = transcription.text.strip()
        detected = getattr(transcription, "language", None) or language_hint or "en"
        return transcript, detected
    finally:
        os.unlink(tmp_path)


# ─── Public entry point ───────────────────────────────────────────────────────

async def transcribe_audio(audio_base64: str, language_hint: Optional[str] = None) -> Tuple[str, str]:
    """
    Transcribe base64-encoded audio.
    Uses Groq Whisper API by default (WHISPER_BACKEND=groq),
    or local faster-whisper if WHISPER_BACKEND=local.
    Returns (transcript, detected_language_code).
    """
    audio_bytes = base64.b64decode(audio_base64)

    if settings.WHISPER_BACKEND == "groq" and settings.GROQ_API_KEY:
        return await _transcribe_groq(audio_bytes, language_hint)
    else:
        return await _transcribe_local(audio_bytes, language_hint)
