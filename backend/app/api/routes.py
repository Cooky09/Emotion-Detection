from fastapi import APIRouter, UploadFile, File
from app.services.emotion_service import EmotionService

router = APIRouter()
emotion_service = EmotionService()

@router.post("/detect")
async def detect_emotion(file: UploadFile = File(...)):
    image_bytes = await file.read()
    results = emotion_service.detect(image_bytes)
    return results