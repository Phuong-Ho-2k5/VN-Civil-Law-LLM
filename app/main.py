from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)
from scripts.legal_bot import get_answer

app = FastAPI(title="VN-Civil-Law-LLM API")

class ChatRequest(BaseModel):
    user_id: str
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
async def chat_api(request: ChatRequest):
    try:
        res = get_answer(request.user_id, request.question)
        return ChatResponse(answer=res)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)