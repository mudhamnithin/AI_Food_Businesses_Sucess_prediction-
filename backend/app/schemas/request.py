"""
=========================================================
Prediction Request Schema

Version : 5.0
=========================================================
"""

from pydantic import BaseModel
from pydantic import Field


class PredictionRequest(BaseModel):

    # =====================================================
    # Area Features
    # =====================================================

    footfall_index: float = Field(..., ge=0, le=100, description="Footfall Index")

    nearby_shops_count: int = Field(..., ge=0)

    nearby_offices_count: int = Field(..., ge=0)

    nearby_colleges_count: int = Field(..., ge=0)

    nearby_hospitals_count: int = Field(..., ge=0)

    nearby_restaurants_count: int = Field(..., ge=0)

    nearby_parks_count: int = Field(..., ge=0)

    distance_to_nearest_brand_chai: float = Field(..., ge=0)

    rent_estimate: float = Field(..., ge=0)

    avg_income_area: float = Field(..., ge=0)
    model_config = {
        "json_schema_extra": {
            "example": {
                "footfall_index": 85,
                "nearby_shops_count": 12,
                "nearby_offices_count": 18,
                "nearby_colleges_count": 4,
                "nearby_hospitals_count": 2,
                "nearby_restaurants_count": 8,
                "nearby_parks_count": 2,
                "distance_to_nearest_brand_chai": 450,
                "rent_estimate": 45,
                "avg_income_area": 18,
            }
        }
    }
