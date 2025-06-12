import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ No Groq API key found! Make sure it's in the .env file.")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}


class AdviceRequest(BaseModel):
    text: str
    language: str = "en"

FINANCE_KEYWORDS = [
    "money", "investment", "invest", "save", "saving", "savings", "budget",
    "loan", "credit", "retirement", "income", "expenses", "mutual fund",
    "insurance", "debt", "tax", "financial", "finance", "emi", "stock",
    "crypto", "bank", "account", "interest", "fund", "dividend", "portfolio"
]

def is_probably_financial(text: str) -> bool:
    text = text.lower()
    return any(keyword in text for keyword in FINANCE_KEYWORDS)


def is_financial_question_via_ai(user_input: str) -> bool:
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "user",
                "content": f"Is the following question about finance or money? Answer only Yes or No:\n\n{user_input}"
            }
        ]
    }
    try:
        response = requests.post(GROQ_API_URL, headers=HEADERS, json=data, timeout=10)
        response.raise_for_status()
        result = response.json()
        answer = result["choices"][0]["message"]["content"].strip().lower()
        return "yes" in answer
    except Exception:
        return False  


@app.post("/financial-advice/")
async def get_financial_advice(request: AdviceRequest):
    user_question = request.text.strip()

    if not user_question:
        raise HTTPException(status_code=400, detail="No input provided")

    if not is_probably_financial(user_question):
        
        if not is_financial_question_via_ai(user_question):
            raise HTTPException(
                status_code=400,
                detail="This question doesn't appear to be about finance. Please ask finance-related questions only."
            )

    try:
        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a financial expert. Provide accurate and useful financial advice in {request.language} language."
                },
                {
                    "role": "user",
                    "content": user_question
                }
            ]
        }

        response = requests.post(GROQ_API_URL, headers=HEADERS, json=data, timeout=15)
        response.raise_for_status()
        response_json = response.json()

        if "choices" not in response_json or not response_json["choices"]:
            raise HTTPException(status_code=500, detail="Invalid response from AI model.")

        return {"text": response_json["choices"][0]["message"]["content"]}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
