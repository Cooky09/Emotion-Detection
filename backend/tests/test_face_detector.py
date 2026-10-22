import sys
from pathlib import Path
from unittest.mock import MagicMock

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

sys.modules["cv2"] = MagicMock()
sys.modules["cv2"].data.haarcascades = ""

from app.services.face_detector import FaceDetector


def test_detect_faces_returns_scaled_coordinates():
    detector = FaceDetector()

    image = np.zeros((480, 640, 3), dtype=np.uint8)

    detector.face_cascade.detectMultiScale.return_value = np.array(
        [[50, 60, 100, 120]],
        dtype=np.int32,
    )

    faces = detector.detect_faces(image)

    assert faces == [(100, 120, 200, 240)]