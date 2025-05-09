from fastapi import APIRouter
from pydantic import BaseModel
from utils.llm import ask_llm
from utils.local_search import search_faqs, search_food

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default"

# In-memory chat history (for demo; use DB/Redis for production)
chat_memory = {}

@router.post("/")
async def chat(request: ChatRequest):
    user_id = request.user_id
    user_message = request.message

    # 1. Try to answer from local FAQs
    local_answer = search_faqs(user_message)
    if local_answer:
        return {"response": local_answer}

    # 2. Try to answer from local food data
    local_food = search_food(user_message)
    if local_food:
        return {"response": local_food}

    # 3. Fallback to LLM
    try:
        if user_id not in chat_memory:
            chat_memory[user_id] = [{"role": "system", "content": "You are CampusCopilot, an AI assistant for college life."}]
        chat_memory[user_id].append({"role": "user", "content": user_message})

        response = ask_llm(chat_memory[user_id])
        chat_memory[user_id].append({"role": "assistant", "content": response})

        return {"response": response}
    except Exception as e:
        print("LLM error:", e)
        return {"response": "Sorry, I couldn't process your request right now."}