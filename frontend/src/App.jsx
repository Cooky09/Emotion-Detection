import { useEffect, useRef, useState } from "react";
import axios from "axios";

const EMOJI_MAP = {
  happy: "😄",
  sad: "😢",
  angry: "😠",
  neutral: "😐",
  surprise: "😲",
  fear: "😨",
  disgust: "🤢"
};

export default function App() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [emotionData, setEmotionData] = useState({ label: null, emoji: null, confidence: null });

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => { videoRef.current.srcObject = stream; })
      .catch(err => console.error("Camera error:", err));

    const interval = setInterval(captureAndSend, 1000);
    return () => clearInterval(interval);
  }, []);

  const captureAndSend = async () => {
    if (!videoRef.current || videoRef.current.readyState !== 4) return;

    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(async (blob) => {
      if (!blob) return;
      const formData = new FormData();
      formData.append("file", blob, "frame.jpg");

      try {
        const response = await axios.post("http://127.0.0.1:8000/detect", formData);
        const data = response.data;

        if (data.predictions && data.predictions.length > 0) {
          const top = data.predictions[0];
          setEmotionData({
            label: top.emotion,
            // Fallback: use emoji from backend OR look up in local map
            emoji: top.emoji || EMOJI_MAP[top.emotion.toLowerCase()],
            confidence: (top.confidence * 100).toFixed(1)
          });
        } else {
          setEmotionData({ label: null, emoji: null, confidence: null });
        }
      } catch (err) {
        console.error("API error:", err);
      }
    }, "image/jpeg");
  };

  return (
    <div style={styles.container}>
      <h1>Emotion Detection AI 🎭</h1>
      <div style={styles.videoContainer}>
        <video ref={videoRef} autoPlay playsInline style={styles.video} />
        <canvas ref={canvasRef} style={{ display: "none" }} />

        {emotionData.label && (
          <div style={styles.overlay}>
            <div style={styles.emoji}>{emotionData.emoji}</div>
            <div style={styles.text}>
              {emotionData.label.toUpperCase()} ({emotionData.confidence}%)
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: { textAlign: "center", fontFamily: "Arial", padding: "20px" },
  videoContainer: { position: "relative", display: "inline-block" },
  video: { width: "640px", borderRadius: "12px", border: "3px solid #444" },
  overlay: {
    position: "absolute", bottom: "20px", left: "50%", transform: "translateX(-50%)",
    backgroundColor: "rgba(0,0,0,0.7)", padding: "10px 20px", borderRadius: "12px",
    color: "white", textAlign: "center"
  },
  emoji: { fontSize: "50px" },
  text: { fontSize: "18px", marginTop: "5px" }
};