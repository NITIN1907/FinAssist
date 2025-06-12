# 💰 AI Financial Voice Assistant

🎙️ A voice-enabled AI assistant built with **FastAPI** and **React** that listens to your spoken **finance-related queries** and responds with smart, multilingual advice — powered by **Groq's LLaMA3** model.

> 🗣️ Speak your question. Let the AI handle the rest.

---

## 🚀 Features

- ✅ **Voice-to-text** using Web Speech API (React + `react-speech-recognition`)
- 🧠 **Financial query detection** with keyword filtering + AI relevance check
- 🗣️ **Text-to-speech** responses using `SpeechSynthesis`
- 🔐 **Secure API integration** with Groq (LLaMA 3 8B) via FastAPI
- 🌍 **Multilingual support** (e.g., Hindi, Spanish, French)
- 🌐 **CORS-enabled** for seamless local frontend-backend development

---

## 🧩 Tech Stack

### 🖥️ Frontend
- **React.js** (Vite)
- **Tailwind CSS** – modern UI styling
- **react-speech-recognition** – real-time voice transcription

### 🧠 Backend
- **FastAPI** (Python)
- `requests`, `dotenv`, `pydantic`
- **Groq API** (LLaMA 3 8B)
- Financial query detection logic (keyword + AI)

---

## 📸 Preview

![main page](https://github.com/user-attachments/assets/db29b5dc-594e-4385-be2b-829fb3a04418)
![use case](https://github.com/user-attachments/assets/41ba99dc-d691-40ec-b3b7-0312b36463ed)
![output](https://github.com/user-attachments/assets/8146d23e-f415-4689-98fa-72d729aeec87)

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/finance-voice-assistant.git
cd finance-voice-assistant

2️⃣ Backend (FastAPI)
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

▶ Run the server:
uvicorn main:app --reload --port 8000

3️⃣ Frontend (React)
cd ../frontend
npm install
npm run dev

🧠 How It Works
User clicks "Start Speaking" to begin voice input.

Browser uses SpeechRecognition to generate a live transcript.

When the user clicks "Ask for Advice", the transcript is analyzed:

If relevant to finance, it's passed to the backend

Backend queries Groq's LLaMA3 for advice using the API key.

Response is returned and spoken aloud using SpeechSynthesis.
