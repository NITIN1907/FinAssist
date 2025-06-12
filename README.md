💰 AI Financial Voice Assistant
🎙️ A voice-enabled AI assistant built with FastAPI and React that listens to your spoken finance-related queries and responds with smart financial advice — powered by the Groq AI (LLaMA3) model.

Speak your question. Let the AI handle the rest.

🚀 Features
✅ Voice-to-text using Web Speech API (React + react-speech-recognition)

🧠 Finance detection using keyword filters + AI verification

🗣️ Text-to-speech response using SpeechSynthesis

🔐 Secure API with FastAPI + GROQ

🌍 Multilingual support (specify language in request)

🌐 CORS-enabled for local frontend-backend development

🧩 Tech Stack
🖥 Frontend
React.js (Vite)

Tailwind CSS for elegant UI

react-speech-recognition for real-time voice input

🧠 Backend
FastAPI (Python)

requests, dotenv, pydantic

GROQ API (LLaMA 3 8B model)

Financial query filtering using AI + keywords

📸 Preview
![main page](https://github.com/user-attachments/assets/db29b5dc-594e-4385-be2b-829fb3a04418)
![use case](https://github.com/user-attachments/assets/41ba99dc-d691-40ec-b3b7-0312b36463ed)
![output](https://github.com/user-attachments/assets/8146d23e-f415-4689-98fa-72d729aeec87)



📦 Setup Instructions
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/finance-voice-assistant.git
cd finance-voice-assistant
2️⃣ Backend (FastAPI)
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
📄 Create a .env file:
env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
▶ Run the server
bash
Copy
Edit
uvicorn main:app --reload --port 8000
3️⃣ Frontend (React)
bash
Copy
Edit
cd frontend
npm install
npm run dev
The frontend runs at http://localhost:5173
The backend runs at http://localhost:8000

🧠 How It Works
User clicks Start Speaking to begin recording voice.

Transcript is generated live using the browser’s SpeechRecognition API.

On Ask for Advice, transcript is validated for financial relevance.

Valid input is passed to Groq's LLaMA3 model for advice generation.

The response is read aloud using browser’s speechSynthesis.

