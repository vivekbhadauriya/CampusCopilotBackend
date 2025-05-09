from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers import chat, reminders, food, forms

app = FastAPI(
    title="CampusCopilot Backend",
    description="Backend for CampusCopilot - AI-powered campus assistant",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(reminders.router, prefix="/api/reminders", tags=["Reminders"])
app.include_router(food.router, prefix="/api/food", tags=["Food"])
app.include_router(forms.router, prefix="/api/forms", tags=["Forms"])

@app.get("/")
def read_root():
    return {"message": "CampusCopilot backend is running!"}