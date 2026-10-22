from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.emotion_service import EmotionService

router = APIRouter()
emotion_service = EmotionService()

ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}


@router.post("/detect")
async def detect_emotion(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type",
        )

    image_bytes = await file.read()
    results = emotion_service.detect(image_bytes)

    return results