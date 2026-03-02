**🎭 Emotion Detection AI**

A real-time Emotion Detection Web Application that captures webcam input, detects facial emotions using a FastAPI backend, and overlays corresponding emojis on the live video feed using React.

This project demonstrates full-stack integration between computer vision, machine learning, and a modern frontend interface.

**🚀 Features**

🎥 Real-time webcam emotion detection

😀 Live emoji overlay based on detected emotion

📊 Adjustable confidence threshold

🧠 Face detection using OpenCV

⚡ FastAPI backend API

⚛️ React frontend

📝 Optional CSV logging for captured frames

**🧠 Supported Emotions**
Emotion	Emoji
Happy	😄
Sad	😢
Angry	😠
Neutral	😐
Surprise😲
Fear	😨
Disgust	🤢

**🏗️ Project Architecture**

React Frontend
      ↓
Captures Webcam Frame
      ↓
POST /detect (FastAPI)
      ↓
OpenCV Face Detection
      ↓
Emotion Model Prediction
      ↓
JSON Response
      ↓
Emoji Overlay on Video

**⚙️ Installation Guide**
✅ Prerequisites

Make sure you have installed:

Python 3.9+

Node.js 16+

npm or yarn

A working webcam

pip (Python package manager)

🔧 Backend Setup (FastAPI)
1️⃣ Navigate to Backend Folder
cd backend
2️⃣ Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install Dependencies

If requirements.txt exists:

pip install -r requirements.txt

Otherwise install manually:

pip install fastapi uvicorn opencv-python numpy python-multipart
4️⃣ Run Backend Server
uvicorn app.main:app --reload

Backend runs at:

http://127.0.0.1:8000

Test health endpoint:

http://127.0.0.1:8000/health

Expected response:

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

Allow webcam access when prompted.

🎛️ Configuration
🔹 Adjust Confidence Threshold

Open frontend/app.jsx and modify:

const CONFIDENCE_THRESHOLD = 50;
Value	Behavior
0	Shows emoji for all detections
30	Moderate strictness
50	Balanced
70+	Only very confident predictions
🔹 Optional CSV Logging

If logging is enabled in the backend:

Captured frames are saved in:

backend/captured_frames/

Predictions are stored in:

emotions.csv

CSV format:

filename,emotion,confidence,emoji
