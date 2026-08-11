from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.predict import router as prediction_router

app = FastAPI(
    title="Food Business Prediction API",
    version="5.0",
    description="AI-powered Food Business Success Prediction System",
)

# -------------------------------------------------
# CORS
# -------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Routes
# -------------------------------------------------

app.include_router(prediction_router)


# -------------------------------------------------
# Root
# -------------------------------------------------

@app.get("/")
async def root():
    return {
        "message": "Food Business Prediction API",
        "version": "5.0",
        "status": "running",
    }


# -------------------------------------------------
# Health
# -------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }