"""
=========================================================
Comparison Service

Compares all business recommendations

Version : 1.0
=========================================================
"""


class ComparisonService:

    """
    Business Comparison Engine
    """

    # =====================================================
    # Generate Comparison Table
    # =====================================================

    @staticmethod
    def generate(businesses):

        comparison = []

        for business in businesses:

            comparison.append({

                "rank": business["rank"],

                "business": business["business"],

                "score": business["score"],

                "grade": business["grade"],

                "recommendation": business["recommendation"],

                "confidence": business["confidence"],

                "ideal_match": business["ideal_match"],

                "customer_demand": business["customer_demand"],

                "competition_score": business["competition_score"],

                "strengths": len(business["strengths"]),

                "risks": len(business["risks"]),

                "investment": business["investment"]["medium"]

            })

        return comparison

    # =====================================================
    # Best Business
    # =====================================================

    @staticmethod
    def best(businesses):

        return max(

            businesses,

            key=lambda x: x["score"]

        )

    # =====================================================
    # Top Three Businesses
    # =====================================================

    @staticmethod
    def top_three(businesses):

        return sorted(

            businesses,

            key=lambda x: x["score"],

            reverse=True

        )[:3]

    # =====================================================
    # Average Score
    # =====================================================

    @staticmethod
    def average_score(businesses):

        if not businesses:

            return 0

        return round(

            sum(

                x["score"]

                for x in businesses

            ) / len(businesses),

            2

        )

    # =====================================================
    # Highest Confidence
    # =====================================================

    @staticmethod
    def highest_confidence(businesses):

        return max(

            businesses,

            key=lambda x: x["confidence"]

        )

    # =====================================================
    # Lowest Risk
    # =====================================================

    @staticmethod
    def lowest_risk(businesses):

        return min(

            businesses,

            key=lambda x: len(x["risks"])

        )

    # =====================================================
    # Summary
    # =====================================================

    @staticmethod
    def summary(businesses):

        best = ComparisonService.best(businesses)

        return {

            "recommended_business": best["business"],

            "score": best["score"],

            "grade": best["grade"],

            "average_score":

                ComparisonService.average_score(

                    businesses

                ),

            "businesses_compared":

                len(businesses)

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Comparison Service",

            "status": "Running",

            "version": "1.0"

        }


# =====================================================
# Singleton
# =====================================================

comparison_service = ComparisonService()