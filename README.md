🎭 Emotion Detection AI

A real-time emotion detection system using a webcam feed, built with FastAPI for the backend and React for the frontend. Detects human emotions from faces and overlays emojis corresponding to the detected emotion. Captured frames and predictions can also be logged for analysis.

Features

Real-time face detection and emotion recognition from webcam.

Emoji overlay on live video according to detected emotion.

Confidence threshold to control when emojis appear.

Optional logging: save captured frames with emotion predictions in a CSV.

Easy-to-use frontend with live webcam feed.

Demo Screenshot


(Replace with an actual screenshot of your app with emojis overlaid.)

Supported Emotions
Emotion	Emoji
Happy	😄
Sad	😢
Angry	😠
Neutral	😐
Surprise	😲
Fear	😨
Disgust	🤢
Tech Stack

Backend: Python, FastAPI, OpenCV, NumPy

Frontend: React, Axios

Machine Learning: Your custom emotion detection model (can be trained or pre-trained)

Backend

Clone the repo:

git clone https://github.com/your-username/emotion-detection-ai.git
cd emotion-detection-ai/backend

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate # Mac/Linux
.venv\Scripts\activate    # Windows

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn app.main:app --reload

The backend will start at: http://127.0.0.1:8000

Frontend

Navigate to the frontend folder:

cd ../frontend

Install dependencies:

npm install
# or
yarn install

Start the frontend:

npm run dev
