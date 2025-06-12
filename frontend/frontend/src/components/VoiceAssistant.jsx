import React, { useState } from "react";
import axios from "axios";
import SpeechRecognition, { useSpeechRecognition } from "react-speech-recognition";

// 👇 Global speech synthesis reference
const synth = window.speechSynthesis;

const FinanceVoiceAssistant = () => {
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const { transcript, listening, resetTranscript } = useSpeechRecognition();

  const startListening = () => {
    SpeechRecognition.startListening({ continuous: true });
  };

  const stopListeningAndSend = async () => {
    SpeechRecognition.stopListening();

    if (transcript) {
      try {
        setLoading(true);
        setResponse("");  // Clear previous response
        const res = await axios.post("http://127.0.0.1:8000/financial-advice/", {
          text: transcript,
          language: "en"
        });
        setResponse(res.data.text);
        speak(res.data.text);
      } catch (error) {
        console.error("❌ Error fetching AI response:", error);
        if (error.response && error.response.status === 400) {
          setResponse(error.response.data.detail);
        } else {
          setResponse("❌ Something went wrong. Please try again later.");
        }
      } finally {
        setLoading(false);
        resetTranscript();
      }
    }
  };

  const speak = (text) => {
    stopSpeaking();  // Stop any previous speech before starting
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
  };

  const stopSpeaking = () => {
    if (synth.speaking) {
      synth.cancel();
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-white flex flex-col items-center justify-center px-4">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-xl w-full text-center">
        <h1 className="text-3xl font-bold mb-6 text-blue-800">💰 AI Financial Voice Assistant</h1>

        <div className="flex flex-wrap justify-center gap-4 mb-4">
          <button
            onClick={startListening}
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-xl transition"
          >
            🎙️ Start Speaking
          </button>

          <button
            onClick={stopListeningAndSend}
            className="bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-xl transition"
          >
            ✅ Ask for Advice
          </button>

          <button
            onClick={stopSpeaking}
            className="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded-xl transition"
          >
            🔇 Stop Speaking
          </button>
        </div>

        <p className="text-sm text-gray-500 mb-4">
          {listening ? "🟢 Listening..." : "🎤 Click and speak your financial question"}
        </p>

        <div className="bg-gray-100 rounded-xl p-4 mb-4 text-left w-full min-h-[50px]">
          <p className="text-gray-600"><strong>You:</strong> {transcript || "Your speech will appear here."}</p>
        </div>

        <div className="bg-blue-50 rounded-xl p-4 text-left w-full min-h-[100px]">
          <p className="text-blue-900 font-medium"><strong>AI:</strong> {loading ? "Generating advice..." : response}</p>
        </div>
      </div>
    </div>
  );
};

export default FinanceVoiceAssistant;
