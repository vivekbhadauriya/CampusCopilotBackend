from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers import chat, reminders, food, forms
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

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

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for all unhandled exceptions."""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred"}
    )

# Routers
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(reminders.router, prefix="/api/reminders", tags=["Reminders"])
app.include_router(food.router, prefix="/api/food", tags=["Food"])
app.include_router(forms.router, prefix="/api/forms", tags=["Forms"])

@app.get("/")
async def read_root():
    """Root endpoint to check if the server is running."""
    return {
        "message": "CampusCopilot backend is running!",
        "status": "healthy",
        "llm_provider": "Google Generative AI (via LangChain)"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "llm_provider": "Google Generative AI (via LangChain)"
    }

@app.get("/model/status")
async def model_status_check():
    """Check the status of the LLM provider."""
    # For cloud LLMs, we can't check model status directly, but we can show config
    return {
        "status": "cloud",
        "llm_provider": "Google Generative AI (via LangChain)"
    }