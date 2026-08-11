class InsightService:

    @staticmethod
    def generate(data: dict, probability: float):

        strengths = []
        risks = []
        improvements = []

        # =====================================================
        # Footfall Analysis
        # =====================================================

        if data["footfall_index"] >= 80:
            strengths.append("Excellent customer footfall")
        elif data["footfall_index"] >= 60:
            strengths.append("High customer footfall")
        elif data["footfall_index"] >= 40:
            strengths.append("Moderate customer footfall")
            improvements.append("Increase local advertising and customer engagement.")
        else:
            risks.append("Low customer footfall")
            improvements.append("Consider a location with higher pedestrian movement.")

        # =====================================================
        # Office Analysis
        # =====================================================

        if data["nearby_offices_count"] >= 30:
            strengths.append("Excellent office employee population")

        elif data["nearby_offices_count"] >= 15:
            strengths.append("Strong office employee population")

        elif data["nearby_offices_count"] >= 8:
            strengths.append("Moderate office presence")

        else:
            risks.append("Limited office customers")
            improvements.append("Target residential customers and delivery orders.")

        # =====================================================
        # College Analysis
        # =====================================================

        if data["nearby_colleges_count"] >= 3:
            strengths.append("Large student customer base")

        elif data["nearby_colleges_count"] >= 1:
            strengths.append("Nearby student population")

        # =====================================================
        # Restaurant Competition
        # =====================================================

        if data["nearby_restaurants_count"] >= 30:

            risks.append("Very high food competition")

            improvements.append("Offer unique menu items and attractive pricing.")

        elif data["nearby_restaurants_count"] >= 15:

            risks.append("Moderate food competition")

        elif data["nearby_restaurants_count"] >= 5:

            strengths.append("Active commercial food zone")

        # =====================================================
        # Shops
        # =====================================================

        if data["nearby_shops_count"] <= 5:

            strengths.append("Lower nearby shop competition")

        elif data["nearby_shops_count"] >= 15:

            risks.append("High nearby shop competition")

        # =====================================================
        # Rent
        # =====================================================

        if data["rent_estimate"] >= 95:

            risks.append("High rental cost")

            improvements.append(
                "Increase average order value to offset rental expenses."
            )

        elif data["rent_estimate"] <= 60:

            strengths.append("Affordable rental cost")

        # =====================================================
        # Income
        # =====================================================

        if data["avg_income_area"] >= 18:

            strengths.append("High purchasing power")

        elif data["avg_income_area"] >= 12:

            strengths.append("Moderate purchasing power")

        else:

            risks.append("Low purchasing power")

            improvements.append("Introduce affordable pricing and combo offers.")

        # =====================================================
        # Brand Competition
        # =====================================================

        if data["distance_to_nearest_brand_chai"] >= 300:

            strengths.append("Limited branded chai competition")

        elif data["distance_to_nearest_brand_chai"] <= 100:

            risks.append("Nearby branded chai competitor")

            improvements.append("Develop a unique brand identity.")

        # =====================================================
        # Scores
        # =====================================================

        business_score = round(probability / 10, 1)

        total_strengths = len(strengths)

        total_risks = len(risks)

        # =====================================================
        # Grade
        # =====================================================

        if probability >= 90:
            grade = "A+"

        elif probability >= 80:
            grade = "A"

        elif probability >= 70:
            grade = "B+"

        elif probability >= 60:
            grade = "B"

        elif probability >= 50:
            grade = "C"

        else:
            grade = "D"

        # =====================================================
        # Final Recommendation Logic
        # =====================================================

        if probability >= 90 and total_risks <= 1:

            prediction = "Highly Successful"

            decision = "Excellent Opportunity"

            recommendation = "Highly Recommended"

        elif probability >= 80 and total_risks <= 2:

            prediction = "Successful"

            decision = "Very Good Opportunity"

            recommendation = "Recommended"

        elif probability >= 65 and total_risks <= 4:

            prediction = "Borderline"

            decision = "Good Opportunity"

            recommendation = "Recommended with Improvements"

        elif probability >= 50:

            prediction = "Risky"

            decision = "Moderate Opportunity"

            recommendation = "Needs Major Improvements"

        else:

            prediction = "Not Recommended"

            decision = "High Risk Opportunity"

            recommendation = "Avoid This Location"

        # =====================================================
        # Executive Summary
        # =====================================================

        summary = f"""
Business Analysis Report

Predicted Success Probability : {probability:.2f}%

Business Score : {business_score}/10

Business Grade : {grade}

Strengths Identified : {total_strengths}

Potential Risks : {total_risks}

Overall Decision :

{decision}

Recommendation :

{recommendation}
""".strip()

        # =====================================================
        # Score Card
        # =====================================================

        score_card = {
            "Footfall": min(10, round(data["footfall_index"] / 10)),
            "Competition": max(
                1, 10 - min(9, round(data["nearby_restaurants_count"] / 5))
            ),
            "Office Population": min(10, round(data["nearby_offices_count"] / 4)),
            "Income": min(10, round(data["avg_income_area"] / 2)),
            "Rent": max(1, 10 - round(data["rent_estimate"] / 15)),
        }

        return {
            "prediction": prediction,
            "business_score": business_score,
            "grade": grade,
            "decision": decision,
            "recommendation": recommendation,
            "summary": summary,
            "strengths": strengths,
            "risks": risks,
            "improvements": improvements,
            "score_card": score_card,
        }


insight_service = InsightService()
