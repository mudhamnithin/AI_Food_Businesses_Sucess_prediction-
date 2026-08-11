"""
=========================================================
SWOT Analysis Service

Version : 6.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class SWOTService:
    """
    SWOT Intelligence Engine

    Generates:
    - Strengths
    - Weaknesses
    - Opportunities
    - Threats
    """

    # =====================================================
    # Generate SWOT
    # =====================================================

    @staticmethod
    def generate(
        data,
        probability,
        analytics
    ):

        # =====================================================
        # Analytics
        # =====================================================

        business_health = analytics["business_health_index"]

        demand = analytics["demand_score"]

        location = analytics["location_quality_index"]

        competition = analytics["competition_score"]

        affordability = analytics["affordability_score"]

        growth = analytics["growth_score"]

        commercial = analytics["commercial_activity_score"]

        market = analytics["market_attractiveness"]

        strengths = []

        weaknesses = []

        opportunities = []

        threats = []

        # =====================================================
        # Strengths
        # =====================================================

        if business_health >= 85:

            strengths.append(
                "Excellent business success probability."
            )

        if demand >= 80:

            strengths.append(
                "Strong customer demand in the target location."
            )

        if location >= 80:

            strengths.append(
                "Prime commercial business location."
            )

        if affordability >= 70:

            strengths.append(
                "Affordable operating and rental costs."
            )

        if growth >= 80:

            strengths.append(
                "High long-term business growth potential."
            )

        if commercial >= 75:

            strengths.append(
                "Excellent surrounding commercial activity."
            )

        if market >= 80:

            strengths.append(
                "Highly attractive market conditions."
            )

        if data.nearby_offices_count >= 20:

            strengths.append(
                "Large office workforce ensures regular weekday customers."
            )

        if data.nearby_colleges_count >= 5:

            strengths.append(
                "Student population supports recurring business."
            )

        # =====================================================
        # Weaknesses
        # =====================================================

        if affordability <= 40:

            weaknesses.append(
                "High rental expenses reduce profitability."
            )

        if demand <= 45:

            weaknesses.append(
                "Customer demand is currently limited."
            )

        if location <= 45:

            weaknesses.append(
                "Commercial visibility is relatively weak."
            )

        if business_health <= 55:

            weaknesses.append(
                "Overall business viability requires improvement."
            )

        if competition <= 40:

            weaknesses.append(
                "Strong nearby competition may impact market share."
            )

        if commercial <= 40:

            weaknesses.append(
                "Limited surrounding commercial activity."
            )

        if data.avg_income_area <= 12:

            weaknesses.append(
                "Lower purchasing power in the surrounding area."
            )
            # =====================================================
        # Opportunities
        # =====================================================

        if growth >= 80:

            opportunities.append(
                "Strong long-term expansion opportunity."
            )

        if demand >= 70:

            opportunities.append(
                "Growing customer demand can significantly increase revenue."
            )

        if location >= 75:

            opportunities.append(
                "Prime location supports stronger brand visibility."
            )

        if affordability >= 70:

            opportunities.append(
                "Low operating costs improve long-term profitability."
            )

        if commercial >= 70:

            opportunities.append(
                "Growing commercial activity increases customer traffic."
            )

        if market >= 75:

            opportunities.append(
                "Highly attractive market for new business expansion."
            )

        if data.nearby_offices_count >= 15:

            opportunities.append(
                "Nearby offices provide consistent weekday customer flow."
            )

        if data.nearby_colleges_count >= 4:

            opportunities.append(
                "Student population supports recurring daily sales."
            )

        if data.distance_to_nearest_brand_chai >= 600:

            opportunities.append(
                "Low branded competition provides room for market capture."
            )

        # =====================================================
        # Threats
        # =====================================================

        if affordability <= 40:

            threats.append(
                "High rental expenses may reduce profit margins."
            )

        if demand <= 45:

            threats.append(
                "Weak customer demand could affect daily revenue."
            )

        if business_health <= 50:

            threats.append(
                "Business success probability is currently low."
            )

        if commercial <= 40:

            threats.append(
                "Limited commercial activity may slow business growth."
            )

        if data.distance_to_nearest_brand_chai <= 250:

            threats.append(
                "Nearby branded competitors may attract customers."
            )

        if data.nearby_restaurants_count >= 15:

            threats.append(
                "High restaurant density increases local competition."
            )

        if data.rent_estimate >= 75:

            threats.append(
                "High rental costs can reduce overall profitability."
            )

        # =====================================================
        # SWOT Score
        # =====================================================

        swot_score = round(

            (

                business_health * 0.35

                + growth * 0.20

                + demand * 0.15

                + location * 0.15

                + commercial * 0.10

                + market * 0.05

            ),

            2

        )

        swot_score = ScoreEngine.clamp(

            swot_score

        )

        evaluation = ScoreEngine.evaluate(

            swot_score

        )

        swot_grade = evaluation["grade"]

        swot_rating = evaluation["overall_status"]

        # =====================================================
        # Strategic Recommendations
        # =====================================================

        strategic_recommendations = []

        if business_health >= 85:

            strategic_recommendations.append(
                "Proceed confidently with business launch or expansion."
            )

        if growth >= 80:

            strategic_recommendations.append(
                "Prepare a phased expansion strategy."
            )

        if affordability <= 50:

            strategic_recommendations.append(
                "Reduce fixed operating expenses where possible."
            )

        if demand <= 60:

            strategic_recommendations.append(
                "Increase local marketing and promotional activities."
            )

        if commercial <= 50:

            strategic_recommendations.append(
                "Partner with nearby businesses to improve visibility."
            )

        if data.distance_to_nearest_brand_chai <= 300:

            strategic_recommendations.append(
                "Differentiate your products and pricing from nearby brands."
            )

        if not strategic_recommendations:

            strategic_recommendations.append(
                "Maintain current strategy and monitor performance regularly."
            )
            # =====================================================
        # SWOT Matrix
        # =====================================================

        swot_matrix = {

            "strengths": strengths,

            "weaknesses": weaknesses,

            "opportunities": opportunities,

            "threats": threats

        }

        # =====================================================
        # Risk Priorities
        # =====================================================

        risk_priorities = []

        if competition <= 40:

            risk_priorities.append(

                "Competition Strategy"

            )

        if affordability <= 40:

            risk_priorities.append(

                "Rental Cost Optimization"

            )

        if demand <= 45:

            risk_priorities.append(

                "Customer Acquisition"

            )

        if location <= 45:

            risk_priorities.append(

                "Location Visibility"

            )

        if commercial <= 45:

            risk_priorities.append(

                "Commercial Partnerships"

            )

        if not risk_priorities:

            risk_priorities.append(

                "Routine Performance Monitoring"

            )

        # =====================================================
        # Executive Summary
        # =====================================================

        executive_summary = f"""
SWOT ANALYSIS REPORT

Overall SWOT Score :
{swot_score:.2f}/100

SWOT Grade :
{swot_grade}

Business Rating :
{swot_rating}

Strengths :
{len(strengths)}

Weaknesses :
{len(weaknesses)}

Opportunities :
{len(opportunities)}

Threats :
{len(threats)}
""".strip()

        # =====================================================
        # Return SWOT Analysis
        # =====================================================

        return {

            "strengths":

                strengths,

            "weaknesses":

                weaknesses,

            "opportunities":

                opportunities,

            "threats":

                threats,

            "swot_score":

                round(

                    swot_score,

                    2

                ),

            "swot_grade":

                swot_grade,

            "swot_rating":

                swot_rating,

            "swot_matrix":

                swot_matrix,

            "strategic_recommendations":

                strategic_recommendations,

            "risk_priorities":

                risk_priorities,

            "executive_summary":

                executive_summary,

            "overall_strength":

                len(

                    strengths

                ),

            "overall_weakness":

                len(

                    weaknesses

                ),

            "overall_opportunity":

                len(

                    opportunities

                ),

            "overall_threat":

                len(

                    threats

                ),

            "overall_score":

                round(

                    (

                        swot_score

                        +

                        business_health

                    ) / 2,

                    2

                )

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "SWOT Service",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

swot_service = SWOTService()                