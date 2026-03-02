import cv2
import numpy as np
from PIL import Image
from transformers import pipeline
from app.services.face_detector import FaceDetector


class EmotionService:
    def __init__(self):
        self.face_detector = FaceDetector()
        self.classifier = pipeline(
            "image-classification",
            model="dima806/facial_emotions_image_detection"
        )

    # ✅ FIX: Properly indented inside class
    def detect(self, image_bytes):
        try:
            nparr = np.frombuffer(image_bytes, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if image is None:
                print("Failed to decode image!")
                return {"face_count": 0, "predictions": []}

            faces = self.face_detector.detect_faces(image)
            print("Detected faces:", len(faces))

            results = []

            for (x, y, w, h) in faces:
                face = image[y:y+h, x:x+w]

                if face.size == 0:
                    continue

                face_pil = Image.fromarray(
                    cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                )

                prediction = self.classifier(face_pil)[0]
                print("Prediction:", prediction)

                results.append({
                    "emotion": prediction["label"].lower(),
                    "confidence": round(float(prediction["score"]), 3)
                })

            print("Results sent:", results)

            return {
                "face_count": len(results),
                "predictions": results
            }

        except Exception as e:
            print("ERROR in detect:", str(e))
            return {"face_count": 0, "predictions": []}