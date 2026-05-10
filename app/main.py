from fastapi import FastAPI, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.openai_service import ask_openai

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "FastAPI OpenAI API is running"
    }
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        reply = ask_openai(request.message)

        return ChatResponse(reply=reply)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )