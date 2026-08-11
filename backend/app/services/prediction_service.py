"""
=========================================================
Prediction Service
Version : 6.1
=========================================================
"""

import numpy as np
import pandas as pd

from app.ml.model_loader import model_loader

from app.services.score_engine import ScoreEngine
from app.services.analytics_service import analytics_service
from app.services.dashboard_service import dashboard_service
from app.services.customer_service import customer_service
from app.services.swot_service import swot_service
from app.services.investment_service import investment_service
from app.services.roi_service import roi_service
from app.services.business_recommendation_service import (
    business_recommendation_service,
)
from app.services.executive_report_service import (
    executive_report_service,
)


class PredictionService:
    """
    Main AI Prediction Engine
    """

    # =====================================================
    # Predict
    # =====================================================

    @staticmethod
    def predict(data):

        # -------------------------------------------------
        # Validate Model
        # -------------------------------------------------

        if model_loader.model is None:
            raise Exception("ML model is not loaded.")

        if model_loader.scaler is None:
            raise Exception("Scaler is not loaded.")

        # -------------------------------------------------
        # Prepare Features
        # -------------------------------------------------

        features = pd.DataFrame(
            [[
                float(data.footfall_index),
                float(data.nearby_shops_count),
                float(data.nearby_offices_count),
                float(data.nearby_colleges_count),
                float(data.nearby_hospitals_count),
                float(data.nearby_restaurants_count),
                float(data.nearby_parks_count),
                float(data.distance_to_nearest_brand_chai),
                float(data.rent_estimate),
                float(data.avg_income_area),
            ]],
            columns=[
                "footfall_index",
                "nearby_shops_count",
                "nearby_offices_count",
                "nearby_colleges_count",
                "nearby_hospitals_count",
                "nearby_restaurants_count",
                "nearby_parks_count",
                "distance_to_nearest_brand_chai",
                "rent_estimate",
                "avg_income_area",
            ],
        )

        # -------------------------------------------------
        # Scale Features
        # -------------------------------------------------

        scaled_features = model_loader.scaler.transform(
            features
        )

        # -------------------------------------------------
        # ML Prediction
        # -------------------------------------------------

        probability = float(
            model_loader.model.predict_proba(
                scaled_features
            )[0][1] * 100
        )

        probability = ScoreEngine.clamp(
            probability
        )

        evaluation = ScoreEngine.evaluate(
            probability
        )

        # -------------------------------------------------
        # Prediction Result
        # -------------------------------------------------

        prediction = {
            "prediction": (
                1 if probability >= 50 else 0
            ),

            "success_probability": round(
                probability,
                2,
            ),

            "business_score": round(
                probability,
                2,
            ),

            "overall_ai_score": round(
                probability,
                2,
            ),

            "overall_status": (
                evaluation["overall_status"]
            ),

            "grade": (
                evaluation["grade"]
            ),

            "decision": (
                evaluation["decision"]
            ),

            "confidence": (
                evaluation["confidence"]
            ),

            "risk_level": (
                evaluation["risk"]
            ),

            "recommendation": (
                evaluation["recommendation"]
            ),
        }

        # =====================================================
        # Analytics
        # =====================================================

        analytics = analytics_service.generate(
            data,
            probability,
        )

        # =====================================================
        # Dashboard
        # =====================================================

        dashboard = dashboard_service.generate(
            analytics
        )

        # =====================================================
        # Customer Analysis
        # =====================================================

        customer = customer_service.generate(
            data,
            probability,
            analytics,
        )

        # =====================================================
        # SWOT Analysis
        # =====================================================

        swot = swot_service.generate(
            data,
            probability,
            analytics,
        )

        # =====================================================
        # Investment Analysis
        # =====================================================

        investment = investment_service.generate(
            data,
            probability,
            analytics,
        )

        # =====================================================
        # ROI Analysis
        # =====================================================

        roi = roi_service.generate(
            data,
            probability,
            analytics,
            investment,
        )

        # =====================================================
        # Business Recommendation
        # =====================================================

        business_recommendations = (
            business_recommendation_service.generate(
                data,
                probability,
                analytics,
            )
        )

        # =====================================================
        # Executive Report
        # =====================================================

        executive_report = (
            executive_report_service.generate(
                prediction,
                analytics,
                customer,
                swot,
                investment,
                roi,
                business_recommendations,
                data,
            )
        )
            # =====================================================
        # Business Performance
        # =====================================================

        business_performance = {

            "overall_score": round(
                probability,
                2,
            ),

            "grade": prediction["grade"],

            "status": prediction["overall_status"],

            "decision": prediction["decision"],

            "confidence": prediction["confidence"],
        }

        # =====================================================
        # Final Response
        # =====================================================

        result = {

            # -------------------------------------------------
            # Prediction
            # -------------------------------------------------

            **prediction,

            # -------------------------------------------------
            # Analytics
            # -------------------------------------------------

            "analytics": analytics,

            "dashboard": dashboard,

            # -------------------------------------------------
            # Customer Analysis
            # -------------------------------------------------

            "customer_analysis": customer,

            # -------------------------------------------------
            # SWOT Analysis
            # -------------------------------------------------

            "swot_analysis": swot,

            # -------------------------------------------------
            # Investment Analysis
            # -------------------------------------------------

            "investment_analysis": investment,

            # -------------------------------------------------
            # ROI Analysis
            # -------------------------------------------------

            "roi_analysis": roi,

            # -------------------------------------------------
            # Business Recommendations
            # -------------------------------------------------

            "business_recommendations":
                business_recommendations,

            # -------------------------------------------------
            # Executive Report
            # -------------------------------------------------

            "executive_report":
                executive_report,

            # -------------------------------------------------
            # Business Performance
            # -------------------------------------------------

            "business_performance":
                business_performance,

            # -------------------------------------------------
            # Quick Access
            # -------------------------------------------------

            "recommended_business":
                business_recommendations.get(
                    "best_business",
                    {},
                ),

            "top_3_businesses":
                business_recommendations.get(
                    "top_3_businesses",
                    [],
                ),

            "comparison":
                executive_report.get(
                    "business_comparison",
                    [],
                ),

            "risk_analysis":
                executive_report.get(
                    "risk_analysis",
                    {},
                ),

            "action_plan":
                executive_report.get(
                    "action_plan",
                    {},
                ),

            "timeline":
                executive_report.get(
                    "business_timeline",
                    [],
                ),
        }

        return result

    # =====================================================
    # Summary
    # =====================================================

    @staticmethod
    def summary(result):

        business = (
            result.get(
                "business_recommendations",
                {},
            )
            .get(
                "best_business",
                {},
            )
            .get(
                "business",
                "Business",
            )
        )

        return f"""
            AI FOOD BUSINESS PREDICTION

            Success Probability :
            {result['success_probability']:.2f}%

            Business Score :
            {result['business_score']:.2f}/100

            Grade :
            {result['grade']}

            Decision :
            {result['decision']}

            Risk :
            {result['risk_level']}

            Recommended Business :
            {business}

            Overall AI Score :
            {result['overall_ai_score']:.2f}/100
            """.strip()    
        # =====================================================
    # Health
    # =====================================================

    @staticmethod
    def health():

        return {

            "service":
                "Prediction Service",

            "status":
                "Running",

            "model_loaded":
                model_loader.model is not None,

            "scaler_loaded":
                model_loader.scaler is not None,

            "version":
                "6.1",
        }

    # =====================================================
    # Version
    # =====================================================

    @staticmethod
    def version():

        return {

            "name":
                "Food Business Prediction API",

            "version":
                "6.1",

            "engine":
                "Random Forest + AI Business Intelligence",
        }


# =====================================================
# Singleton
# =====================================================

prediction_service = PredictionService()