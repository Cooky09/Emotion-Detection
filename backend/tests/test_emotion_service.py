import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

sys.modules["cv2"] = MagicMock()
sys.modules["cv2"].data.haarcascades = ""

from app.services.emotion_service import EmotionService


def test_detect_returns_error_when_processing_fails():
    service = EmotionService.__new__(EmotionService)

    service.face_detector = MagicMock()
    service.classifier = MagicMock()

    service.face_detector.detect_faces.side_effect = RuntimeError(
        "Face detection failed"
    )

    result = service.detect(b"invalid-image-data")

    assert result["face_count"] == 0
    assert result["predictions"] == []
    assert result["error"] == "Emotion detection failed"