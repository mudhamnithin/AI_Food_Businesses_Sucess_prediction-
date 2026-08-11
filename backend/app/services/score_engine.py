"""
=========================================================
AI Score Engine

Centralized Scoring System

Version : 6.0
=========================================================
"""


class ScoreEngine:
    """
    Central AI Scoring Engine

    Every service should use this engine.
    """

    # =====================================================
    # Clamp
    # =====================================================

    @staticmethod
    def clamp(value, minimum=0, maximum=100):

        return max(minimum, min(maximum, value))

    # =====================================================
    # Percentage
    # =====================================================

    @staticmethod
    def percentage(value, maximum):

        if maximum <= 0:

            return 0

        return ScoreEngine.clamp(

            (value / maximum) * 100

        )

    # =====================================================
    # Grade
    # =====================================================

    @staticmethod
    def grade(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "A+"

        if score >= 85:

            return "A"

        if score >= 80:

            return "B+"

        if score >= 75:

            return "B"

        if score >= 70:

            return "C+"

        if score >= 65:

            return "C"

        if score >= 50:

            return "D"

        return "F"

    # =====================================================
    # Risk
    # =====================================================

    @staticmethod
    def risk(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "Very Low"

        if score >= 80:

            return "Low"

        if score >= 70:

            return "Medium"

        if score >= 60:

            return "High"

        return "Very High"

    # =====================================================
    # Decision
    # =====================================================

    @staticmethod
    def decision(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "Excellent Opportunity"

        if score >= 80:

            return "Strong Opportunity"

        if score >= 70:

            return "Good Opportunity"

        if score >= 60:

            return "Average Opportunity"

        return "Poor Opportunity"

    # =====================================================
    # Recommendation
    # =====================================================

    @staticmethod
    def recommendation(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "Highly Recommended"

        if score >= 80:

            return "Recommended"

        if score >= 70:

            return "Consider Investment"

        if score >= 60:

            return "Proceed With Caution"

        return "Avoid Investment"

    # =====================================================
    # Confidence
    # =====================================================

    @staticmethod
    def confidence(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "Very High"

        if score >= 80:

            return "High"

        if score >= 70:

            return "Medium"

        if score >= 60:

            return "Low"

        return "Very Low"

    # =====================================================
    # Overall Status
    # =====================================================

    @staticmethod
    def overall_status(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "Excellent"

        if score >= 80:

            return "Very Good"

        if score >= 70:

            return "Good"

        if score >= 60:

            return "Fair"

        return "Poor"
        # =====================================================
    # Star Rating
    # =====================================================

    @staticmethod
    def stars(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return 5

        if score >= 80:

            return 4

        if score >= 70:

            return 3

        if score >= 60:

            return 2

        return 1

    # =====================================================
    # Dashboard Color
    # =====================================================

    @staticmethod
    def color(score):

        score = ScoreEngine.clamp(score)

        if score >= 90:

            return "#4CAF50"

        if score >= 80:

            return "#8BC34A"

        if score >= 70:

            return "#FFC107"

        if score >= 60:

            return "#FF9800"

        return "#F44336"

    # =====================================================
    # Master Evaluation
    # =====================================================

    @staticmethod
    def evaluate(score):

        score = round(

            ScoreEngine.clamp(score),

            2

        )

        stars = ScoreEngine.stars(score)

        return {

            # =================================================
            # Core
            # =================================================

            "score":

                score,

            "overall_score":

                score,

            "grade":

                ScoreEngine.grade(score),

            # =================================================
            # Risk
            # =================================================

            "risk":

                ScoreEngine.risk(score),

            "risk_level":

                ScoreEngine.risk(score),

            "risk_score":

                round(

                    100 - score,

                    2

                ),

            # =================================================
            # Decision
            # =================================================

            "decision":

                ScoreEngine.decision(score),

            "recommendation":

                ScoreEngine.recommendation(score),

            # =================================================
            # Confidence
            # =================================================

            "confidence":

                ScoreEngine.confidence(score),

            # =================================================
            # Status
            # =================================================

            "overall_status":

                ScoreEngine.overall_status(score),

            # =================================================
            # Dashboard
            # =================================================

            "stars":

                stars,

            "rating":

                f"{stars}/5",

            "color":

                ScoreEngine.color(score),

            # =================================================
            # Metadata
            # =================================================

            "version":

                "6.0"

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Score Engine",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

score_engine = ScoreEngine()