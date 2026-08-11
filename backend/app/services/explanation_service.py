"""
=========================================================
Explanation Service

Provides Explainable AI (XAI) for Business Recommendations

Version : 1.0
=========================================================
"""


class ExplanationService:

    """
    Explainable AI Service
    """

    # =====================================================
    # Overall Explanation
    # =====================================================

    @staticmethod
    def generate(data, business):

        explanation = []

        # Footfall
        if data.footfall_index >= 80:

            explanation.append(
                "High customer footfall significantly increases business potential."
            )

        elif data.footfall_index >= 60:

            explanation.append(
                "Moderate customer movement supports stable business growth."
            )

        else:

            explanation.append(
                "Low customer movement may reduce daily sales."
            )

        # Income
        if data.avg_income_area >= 25:

            explanation.append(
                "The surrounding population has strong purchasing power."
            )

        elif data.avg_income_area >= 15:

            explanation.append(
                "The area has moderate purchasing power."
            )

        else:

            explanation.append(
                "Lower income levels require affordable pricing."
            )

        # Rent
        if data.rent_estimate <= 40:

            explanation.append(
                "Affordable rental costs improve profitability."
            )

        elif data.rent_estimate >= 70:

            explanation.append(
                "High rental costs may reduce profit margins."
            )

        # Competition
        if data.nearby_restaurants_count <= 5:

            explanation.append(
                "Low nearby competition improves market opportunity."
            )

        elif data.nearby_restaurants_count >= 15:

            explanation.append(
                "Strong nearby competition requires differentiation."
            )

        # Offices
        if data.nearby_offices_count >= 15:

            explanation.append(
                "Office employees create strong weekday demand."
            )

        # Colleges
        if data.nearby_colleges_count >= 5:

            explanation.append(
                "Students create repeat customer opportunities."
            )

        # Hospitals
        if data.nearby_hospitals_count >= 3:

            explanation.append(
                "Hospitals generate steady customer traffic."
            )

        # Parks
        if data.nearby_parks_count >= 3:

            explanation.append(
                "Parks increase evening and weekend customer visits."
            )

        # Brand Competition
        if data.distance_to_nearest_brand_chai >= 500:

            explanation.append(
                "Limited branded competition improves expansion opportunities."
            )

        return explanation

    # =====================================================
    # Feature Contribution
    # =====================================================

    @staticmethod
    def feature_importance(data):

        return {

            "Footfall":
                round(data.footfall_index, 2),

            "Income":
                round(data.avg_income_area * 4, 2),

            "Competition":
                round(
                    max(
                        0,
                        100 - data.nearby_restaurants_count * 4
                    ),
                    2
                ),

            "Rent":
                round(
                    max(
                        0,
                        100 - data.rent_estimate
                    ),
                    2
                ),

            "Offices":
                round(data.nearby_offices_count * 5, 2),

            "Colleges":
                round(data.nearby_colleges_count * 10, 2),

            "Hospitals":
                round(data.nearby_hospitals_count * 20, 2),

            "Shops":
                round(data.nearby_shops_count * 6, 2),

            "Parks":
                round(data.nearby_parks_count * 20, 2)

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Explanation Service",

            "status": "Running",

            "version": "1.0"

        }


# =====================================================
# Singleton
# =====================================================

explanation_service = ExplanationService()