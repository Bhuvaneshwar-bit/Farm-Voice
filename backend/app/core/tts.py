import base64
import tempfile
import os
from typing import Optional
from gtts import gTTS
from app.core.config import SUPPORTED_LANGUAGES


async def text_to_speech(text: str, language_code: str) -> Optional[str]:
    """
    Convert text to speech using gTTS.
    Returns base64-encoded MP3, or None on failure.
    """
    try:
        lang_config = SUPPORTED_LANGUAGES.get(language_code, SUPPORTED_LANGUAGES["en"])
        tts_code = lang_config["tts_code"]

        tts = gTTS(text=text, lang=tts_code, slow=False)

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            tmp_path = tmp.name

        tts.save(tmp_path)

        with open(tmp_path, "rb") as f:
            audio_bytes = f.read()

        os.unlink(tmp_path)
        return base64.b64encode(audio_bytes).decode("utf-8")
    except Exception as e:
        print(f"TTS error: {e}")
        return None
