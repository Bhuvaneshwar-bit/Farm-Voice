from fastapi import APIRouter
from datetime import datetime
from app.core.rag import is_knowledge_base_populated
from app.models.database import get_feedback_stats

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "FarmVoice API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "knowledge_base_ready": is_knowledge_base_populated(),
    }


@router.get("/stats")
async def get_stats():
    stats = await get_feedback_stats()
    return {
        "service": "FarmVoice",
        "stats": stats,
        "knowledge_base_populated": is_knowledge_base_populated(),
    }
