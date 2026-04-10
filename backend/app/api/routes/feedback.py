from fastapi import APIRouter, HTTPException
from app.models.schemas import FeedbackRequest, FeedbackResponse
from app.models.database import save_feedback, get_history

router = APIRouter()


@router.post("/feedback", response_model=FeedbackResponse)
async def submit_feedback(request: FeedbackRequest):
    if request.feedback_type not in ("correct", "incorrect", "partial"):
        raise HTTPException(status_code=400, detail="feedback_type must be correct, incorrect, or partial")

    await save_feedback(
        session_id=request.session_id,
        feedback_type=request.feedback_type,
        actual_disease=request.actual_disease,
        farmer_note=request.farmer_note,
        helpful_rating=request.helpful_rating,
    )
    return FeedbackResponse(
        success=True,
        message="Thank you for your feedback! It helps us improve FarmVoice.",
    )


@router.get("/history")
async def get_diagnosis_history(limit: int = 20):
    history = await get_history(limit=min(limit, 100))
    return {"history": history, "count": len(history)}
