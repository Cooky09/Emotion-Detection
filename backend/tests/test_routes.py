import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

sys.modules["cv2"] = MagicMock()
sys.modules["cv2"].data.haarcascades = ""

from fastapi.testclient import TestClient

from app.api.routes import emotion_service, router
from fastapi import FastAPI


app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_detect_rejects_non_image_upload():
    response = client.post(
        "/detect",
        files={"file": ("test.txt", b"not an image", "text/plain")},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported file type"


def test_detect_accepts_image_upload():
    expected_result = {
        "face_count": 0,
        "predictions": [],
    }

    with patch.object(
        emotion_service,
        "detect",
        return_value=expected_result,
    ) as mock_detect:
        response = client.post(
            "/detect",
            files={"file": ("test.jpg", b"fake image data", "image/jpeg")},
        )

    assert response.status_code == 200
    assert response.json() == expected_result
    mock_detect.assert_called_once_with(b"fake image data")