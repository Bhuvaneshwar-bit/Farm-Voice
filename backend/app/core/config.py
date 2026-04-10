from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Groq API key — get a free key at https://console.groq.com
    GROQ_API_KEY: str = ""

    # OpenWeatherMap API key (optional — for weather context)
    OPENWEATHER_API_KEY: str = ""

    APP_ENV: str = "development"
    SECRET_KEY: str = "dev-secret-key"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    # Whisper: "local" uses faster-whisper on CPU; "groq" uses Groq Whisper API (free)
    WHISPER_BACKEND: str = "groq"
    WHISPER_MODEL_SIZE: str = "small"  # used when WHISPER_BACKEND=local

    DATABASE_URL: str = "sqlite+aiosqlite:///./farmvoice.db"
    CHROMA_DB_PATH: str = "./chroma_db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

# ─── Open-source model IDs on Groq ───────────────────────────────────────────
GROQ_LLM_MODEL    = "llama-3.3-70b-versatile"      # 70B, great for diagnosis
GROQ_FAST_MODEL   = "llama-3.1-8b-instant"         # 8B, fast entity extraction
GROQ_VISION_MODEL = "llama-3.2-11b-vision-preview" # multimodal, for crop photos
GROQ_STT_MODEL    = "whisper-large-v3"             # open-source Whisper large

SUPPORTED_LANGUAGES = {
    "ta": {"name": "Tamil",    "tts_code": "ta", "native": "தமிழ்" },
    "hi": {"name": "Hindi",    "tts_code": "hi", "native": "हिंदी"  },
    "kn": {"name": "Kannada",  "tts_code": "kn", "native": "ಕನ್ನಡ" },
    "te": {"name": "Telugu",   "tts_code": "te", "native": "తెలుగు"},
    "bn": {"name": "Bengali",  "tts_code": "bn", "native": "বাংলা" },
    "mr": {"name": "Marathi",  "tts_code": "mr", "native": "मराठी" },
    "en": {"name": "English",  "tts_code": "en", "native": "English"},
}

SEASONS = {
    "kharif": {"months": [6, 7, 8, 9, 10], "crops": ["rice", "cotton", "maize", "groundnut"]},
    "rabi":   {"months": [11, 12, 1, 2, 3], "crops": ["wheat", "mustard", "chickpea", "potato"]},
    "zaid":   {"months": [3, 4, 5, 6],      "crops": ["cucumber", "watermelon", "vegetables"]},
}


def get_current_season(month: int) -> str:
    for season, data in SEASONS.items():
        if month in data["months"]:
            return season
    return "unknown"
