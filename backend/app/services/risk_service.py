"""
=========================================================
Risk Service

Business Risk Analysis Engine

Version : 2.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class RiskService:
    """
    AI Risk Analysis Service
    """

    # =====================================================
    # Overall Risk Analysis
    # =====================================================

    @staticmethod
    def analyze(data):

        risks = []

        score = 100

        # =====================================================
        # Rent Risk
        # =====================================================

        if data.rent_estimate >= 80:

            risks.append({
                "category": "Financial",
                "level": "High",
                "message": "High rental expenses may reduce profitability."
            })

            score -= 20

        elif data.rent_estimate >= 60:

            risks.append({
                "category": "Financial",
                "level": "Medium",
                "message": "Rental expenses should be monitored."
            })

            score -= 10

        # =====================================================
        # Competition Density
        # =====================================================

        if data.nearby_restaurants_count >= 20:

            risks.append({
                "category": "Competition",
                "level": "High",
                "message": "Very strong local competition."
            })

            score -= 20

        elif data.nearby_restaurants_count >= 10:

            risks.append({
                "category": "Competition",
                "level": "Medium",
                "message": "Moderate nearby competition."
            })

            score -= 10

        # =====================================================
        # Brand Competition
        # =====================================================

        if data.distance_to_nearest_brand_chai <= 200:

            risks.append({
                "category": "Brand Competition",
                "level": "High",
                "message": "Branded competitors are very close."
            })

            score -= 15

        elif data.distance_to_nearest_brand_chai <= 500:

            risks.append({
                "category": "Brand Competition",
                "level": "Medium",
                "message": "Nearby branded competitors may affect sales."
            })

            score -= 8

        # =====================================================
        # Footfall Risk
        # =====================================================

        if data.footfall_index < 40:

            risks.append({
                "category": "Demand",
                "level": "High",
                "message": "Low customer movement."
            })

            score -= 20

        elif data.footfall_index < 60:

            risks.append({
                "category": "Demand",
                "level": "Medium",
                "message": "Customer demand is moderate."
            })

            score -= 10

        # =====================================================
        # Income Risk
        # =====================================================

        if data.avg_income_area < 15:

            risks.append({
                "category": "Market",
                "level": "Medium",
                "message": "Lower purchasing power."
            })

            score -= 10

        # =====================================================
        # Office Risk
        # =====================================================

        if data.nearby_offices_count < 5:

            risks.append({
                "category": "Business",
                "level": "Medium",
                "message": "Limited office population."
            })

            score -= 5

        # =====================================================
        # College Risk
        # =====================================================

        if data.nearby_colleges_count < 2:

            risks.append({
                "category": "Students",
                "level": "Low",
                "message": "Limited student customer base."
            })

            score -= 5

        # =====================================================
        # Clamp Score
        # =====================================================

        score = ScoreEngine.clamp(score)

        # =====================================================
        # Overall Risk
        # =====================================================

        if score >= 85:

            overall = "Low"

        elif score >= 65:

            overall = "Medium"

        else:

            overall = "High"

        # =====================================================
        # Return
        # =====================================================

        return {

            "overall_risk": overall,

            "risk_score": round(score, 2),

            "identified_risks": risks,

            "total_risks": len(risks)

        }

    # =====================================================
    # Risk Meter
    # =====================================================

    @staticmethod
    def meter(score):

        score = ScoreEngine.clamp(score)

        return {

            "score": score,

            "safe_percentage": score,

            "risk_percentage": round(100 - score, 2)

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Risk Service",

            "status": "Running",

            "version": "2.0"

        }


# =====================================================
# Singleton
# =====================================================

risk_service = RiskService()