from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
import uuid


class DiagnoseRequest(BaseModel):
    audio_base64: Optional[str] = None
    text_input: Optional[str] = None  # fallback if no audio
    image_base64: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    language: str = "auto"
    crop_type: Optional[str] = None  # hint from user


class ChemicalTreatment(BaseModel):
    product: str
    active_ingredient: str
    dosage: str
    frequency: str
    safety_precautions: str


class Treatment(BaseModel):
    immediate: List[str] = []
    organic: List[str] = []
    chemical: List[ChemicalTreatment] = []
    cultural_practices: List[str] = []
    prevention: List[str] = []


class DiagnosisDetail(BaseModel):
    primary_disease: str
    local_name: str
    scientific_name: str
    confidence: int = Field(ge=0, le=100)
    severity: int = Field(ge=1, le=5)
    affected_crop: str
    stage: str  # early / mid / late


class Explanation(BaseModel):
    key_symptoms: List[str]
    visual_evidence: List[str]
    environmental_factors: List[str]
    reasoning: str


class AlternativeDiagnosis(BaseModel):
    disease: str
    confidence: int
    differentiator: str


class WeatherContext(BaseModel):
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    rainfall_mm: Optional[float] = None
    wind_speed: Optional[float] = None
    description: Optional[str] = None
    location_name: Optional[str] = None
    disease_risk_note: Optional[str] = None


class DiagnoseResponse(BaseModel):
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    transcript: str
    detected_language: str
    diagnosis: DiagnosisDetail
    explanation: Explanation
    alternatives: List[AlternativeDiagnosis]
    treatment: Treatment
    urgency: str  # critical / high / medium / low
    recovery_timeline: str
    weather_context: Optional[WeatherContext] = None
    audio_response_base64: Optional[str] = None
    response_text: str
    english_summary: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class FeedbackRequest(BaseModel):
    session_id: str
    feedback_type: str  # correct / incorrect / partial
    actual_disease: Optional[str] = None
    farmer_note: Optional[str] = None
    helpful_rating: Optional[int] = Field(None, ge=1, le=5)


class FeedbackResponse(BaseModel):
    success: bool
    message: str


class HistoryItem(BaseModel):
    session_id: str
    transcript: str
    primary_disease: str
    confidence: int
    severity: int
    urgency: str
    timestamp: datetime
    feedback_type: Optional[str] = None


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    session_id: Optional[str] = None
