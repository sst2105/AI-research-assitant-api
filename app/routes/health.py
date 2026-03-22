from fastapi import APIRouter
from app.model.schemas import HealthResponse

router = APIRouter()

@router.get("/health", response_model = HealthResponse)
async def health_check():
    return HealthResponse(
        status = "online",
        version = "1.0.0",
        message = "AI Research Assistant API is running")