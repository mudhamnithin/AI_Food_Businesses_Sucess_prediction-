"""
=========================================================
Prediction API
Version : 5.0
=========================================================
"""

from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.request import PredictionRequest

from app.services.prediction_service import (
    prediction_service
)


router = APIRouter(
    prefix="/api/predict",
    tags=["Prediction"]
)


# =====================================================
# Prediction Endpoint
# =====================================================

@router.post(
    "/",
    summary="AI Business Prediction"
)
async def predict_business(
    request: PredictionRequest
):

    try:

        result = prediction_service.predict(
            request
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# Health
# =====================================================

@router.get("/health")
async def health():

    return prediction_service.health()


# =====================================================
# Version
# =====================================================

@router.get("/version")
async def version():

    return prediction_service.version()