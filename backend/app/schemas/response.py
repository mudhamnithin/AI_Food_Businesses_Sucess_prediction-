"""
=========================================================
Prediction Response Schema

Version : 5.0
=========================================================
"""

from typing import Any
from typing import Dict
from typing import List

from pydantic import BaseModel
from pydantic import Field


class PredictionResponse(BaseModel):

    # =====================================================
    # Core Prediction
    # =====================================================

    prediction: int

    success_probability: float

    business_score: float

    grade: str

    decision: str

    risk_level: str

    confidence: str

    recommendation: str

    overall_ai_score: float

    overall_status: str
    # =====================================================
    # Analytics
    # =====================================================

    analytics: Dict[str, Any]

    dashboard: Dict[str, Any]

    customer_analysis: Dict[str, Any]

    swot_analysis: Dict[str, Any]

    investment_analysis: Dict[str, Any]

    business_performance: Dict[str, Any]
    # =====================================================
    # Recommendation
    # =====================================================

    business_recommendations: Dict[str, Any]

    roi_analysis: Dict[str, Any]

    executive_report: Dict[str, Any]
    # =====================================================
    # Config
    # =====================================================

    model_config = {
        "extra": "allow",
        "json_schema_extra": {
            "example": {
                "prediction": 1,
                "success_probability": 91.45,
                "business_score": 91.45,
                "grade": "A+",
                "decision": "Excellent Opportunity",
                "risk_level": "Low",
                "confidence": "Very High",
                "recommendation": "Highly Recommended",
                "overall_ai_score": 91.45,
                "overall_status": "Excellent",
            }
        },
    }
    # =====================================================


# Health Response
# =====================================================


class HealthResponse(BaseModel):

    service: str

    status: str

    version: str


# =====================================================
# Version Response
# =====================================================


class VersionResponse(BaseModel):

    name: str

    version: str

    engine: str
