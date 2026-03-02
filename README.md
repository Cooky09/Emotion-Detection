🎭 Emotion Detection AI (Real-Time Webcam Based)

A full-stack real-time Emotion Detection Web Application that uses a webcam feed to detect facial emotions and display corresponding emojis live on the screen.

This project combines:

🧠 Machine Learning (Emotion Classification)

🎥 OpenCV Face Detection

⚡ FastAPI Backend

⚛️ React Frontend

📊 Optional CSV Logging for captured predictions

📌 What This Project Does

Captures webcam frames in the browser (React frontend).

Sends frames to a FastAPI backend.

Backend detects faces using OpenCV.

Emotion model predicts emotion per detected face.

The frontend overlays the corresponding emoji on the video feed.

(Optional) Saves captured images and logs predictions in CSV format.

🎬 Live Features

✅ Real-time webcam emotion detection
✅ Emoji overlay (😄 😢 😠 😐 😲 😨 🤢)
✅ Adjustable confidence threshold
✅ Handles no-face detection safely
✅ Optional dataset logging for captured frames

🧠 Supported Emotions
Emotion	Emoji
Happy	😄
Sad	😢
Angry	😠
Neutral	😐
Surprise	😲
Fear	😨
Disgust	🤢
🏗️ Project Architecture
Frontend (React)
        ↓
Captures Webcam Frame
        ↓
POST /detect
        ↓
Backend (FastAPI)
        ↓
OpenCV Face Detection
        ↓
Emotion Model Prediction
        ↓
Return JSON Response
        ↓
Frontend Displays Emoji Overlay
📂 Project Structure
Emotion-Detection/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   ├── services/
│   │   │   └── emotion_service.py
│   │   └── main.py
│   ├── captured_frames/        # Optional saved images + CSV
│   └── requirements.txt
│
├── frontend/
│   ├── app.jsx
│   ├── package.json
│
└── README.md
⚙️ Prerequisites

Before running this project, make sure you have:

Python 3.9+ installed

Node.js 16+ installed

npm or yarn

A working webcam

pip (Python package manager)

🚀 Backend Setup (FastAPI)
1️⃣ Navigate to Backend
cd backend
2️⃣ Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt

If you don’t have requirements.txt, install manually:

pip install fastapi uvicorn opencv-python numpy python-multipart
4️⃣ Start Backend Server
uvicorn app.main:app --reload

Backend runs at:

http://127.0.0.1:8000

Test health endpoint:

http://127.0.0.1:8000/health

You should see:

{"status":"healthy"}
💻 Frontend Setup (React)
1️⃣ Navigate to Frontend
cd frontend
2️⃣ Install Dependencies
npm install

or

yarn install
3️⃣ Start Frontend
npm start

Open:

http://localhost:3000

Allow webcam permission when prompted.
