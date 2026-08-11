"""
=========================================================
Analytics Service

Version : 6.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class AnalyticsService:
    """
    Generates all business analytics using the
    ML prediction score as the single source
    of truth.
    """

    # =====================================================
    # Generate Analytics
    # =====================================================

    @staticmethod
    def generate(data, probability):

        # =====================================================
        # Base Business Health
        # =====================================================

        score = ScoreEngine.clamp(probability)

        business_health = round(score, 2)

        # =====================================================
        # Location Quality
        # =====================================================

        location_quality = round(

            (

                data.footfall_index * 0.30

                + data.avg_income_area * 2.0

                + data.nearby_offices_count * 1.20

                + data.nearby_colleges_count * 1.00

                + data.nearby_hospitals_count * 1.50

                + data.nearby_shops_count * 0.80

                + data.nearby_parks_count * 0.80

                + min(
                    data.distance_to_nearest_brand_chai / 10,
                    100
                ) * 0.20

            )

            / 2.40,

            2

        )

        location_quality = ScoreEngine.clamp(

            location_quality

        )

        # =====================================================
        # Demand Score
        # =====================================================

        demand_score = round(

            (

                data.footfall_index * 0.50

                + data.nearby_offices_count * 1.60

                + data.nearby_colleges_count * 1.20

                + data.nearby_hospitals_count * 1.30

                + data.avg_income_area * 1.40

            )

            / 2.20,

            2

        )

        demand_score = ScoreEngine.clamp(

            demand_score

        )

        # =====================================================
        # Competition Score
        # =====================================================

        distance_score = min(

            data.distance_to_nearest_brand_chai / 10,

            100

        )

        restaurant_penalty = min(

            data.nearby_restaurants_count * 3,

            100

        )

        competition_score = round(

            (

                distance_score * 0.60

                +

                (100 - restaurant_penalty) * 0.40

            ),

            2

        )

        competition_score = ScoreEngine.clamp(

            competition_score

        )
            # =====================================================
        # Affordability Score
        # =====================================================

        affordability_score = round(

            max(

                0,

                100 - (data.rent_estimate * 1.20)

            ),

            2

        )

        affordability_score = ScoreEngine.clamp(

            affordability_score

        )

        # =====================================================
        # Commercial Activity
        # =====================================================

        commercial_activity = round(

            (

                data.nearby_shops_count * 2.0

                + data.nearby_offices_count * 2.5

                + data.nearby_restaurants_count * 1.5

                + data.nearby_colleges_count * 1.2

                + data.footfall_index * 0.8

            )

            / 2.5,

            2

        )

        commercial_activity = ScoreEngine.clamp(

            commercial_activity

        )

        # =====================================================
        # Growth Score
        # =====================================================

        growth_score = round(

            (

                location_quality * 0.30

                + demand_score * 0.25

                + competition_score * 0.20

                + commercial_activity * 0.15

                + affordability_score * 0.10

            ),

            2

        )

        growth_score = ScoreEngine.clamp(

            growth_score

        )

        # =====================================================
        # Market Attractiveness
        # =====================================================

        market_attractiveness = round(

            (

                location_quality * 0.25

                + demand_score * 0.25

                + competition_score * 0.20

                + commercial_activity * 0.15

                + affordability_score * 0.15

            ),

            2

        )

        market_attractiveness = ScoreEngine.clamp(

            market_attractiveness

        )
            # =====================================================
        # Business Health
        # =====================================================

        business_health = round(

            (

                score * 0.40

                + growth_score * 0.25

                + demand_score * 0.20

                + location_quality * 0.15

            ),

            2

        )

        business_health = ScoreEngine.clamp(

            business_health

        )

        # =====================================================
        # Risk Index
        # =====================================================

        risk_index = round(

            (

                (100 - business_health) * 0.45

                + (100 - competition_score) * 0.25

                + (100 - affordability_score) * 0.15

                + (100 - demand_score) * 0.15

            ),

            2

        )

        risk_index = ScoreEngine.clamp(

            risk_index

        )

        # =====================================================
        # Opportunity Analysis
        # =====================================================

        # Overall business opportunity follows
        # the ML success probability.

        overall_opportunity = ScoreEngine.evaluate(
            business_health
        )

        opportunity_level = overall_opportunity["decision"]

        # Market-specific opportunity is calculated
        # separately from market attractiveness.

        market_opportunity = ScoreEngine.evaluate(
            market_attractiveness
        )

        market_opportunity_level = (
            market_opportunity["decision"]
        )

        # =====================================================
        # Business Readiness
        # =====================================================

        readiness = ScoreEngine.evaluate(

            business_health

        )

        business_readiness = readiness["overall_status"]

        # =====================================================
        # Investment Category
        # =====================================================

        investment_category = ScoreEngine.grade(

            business_health

        )

        # =====================================================
        # Area Rating
        # =====================================================

        area_rating = {

            "stars":

                ScoreEngine.stars(

                    location_quality

                ),

            "label":

                ScoreEngine.overall_status(

                    location_quality

                )

        }

        # =====================================================
        # Dashboard
        # =====================================================

        dashboard = {

            "health":

                business_health,

            "location":

                location_quality,

            "demand":

                demand_score,

            "competition":

                competition_score,

            "affordability":

                affordability_score,

            "growth":

                growth_score,

            "commercial_activity":

                commercial_activity,

            "market":

                market_attractiveness,

            "risk":

                risk_index

        }

        # =====================================================
        # Return Analytics
        # =====================================================

        return {

            "business_health_index":

                business_health,

            "location_quality_index":

                location_quality,

            "demand_score":

                demand_score,

            "competition_score":

                competition_score,

            "affordability_score":

                affordability_score,

            "growth_score":

                growth_score,

            "commercial_activity_score":

                commercial_activity,

            "market_attractiveness":

                market_attractiveness,

            "risk_index":

                risk_index,

            "opportunity_level": opportunity_level,

            "market_opportunity_level":
                market_opportunity_level,

            "business_readiness":

                business_readiness,

            "investment_category":

                investment_category,

            "area_rating":

                area_rating,

            "dashboard":

                dashboard

        }

    # =====================================================
    # Analytics Summary
    # =====================================================

    @staticmethod
    def summary(analytics):

        return f"""
BUSINESS ANALYTICS REPORT

Business Health :
{analytics['business_health_index']:.2f}/100

Location Quality :
{analytics['location_quality_index']:.2f}/100

Demand Score :
{analytics['demand_score']:.2f}/100

Competition Score :
{analytics['competition_score']:.2f}/100

Affordability :
{analytics['affordability_score']:.2f}/100

Growth Score :
{analytics['growth_score']:.2f}/100

Commercial Activity :
{analytics['commercial_activity_score']:.2f}/100

Market Attractiveness :
{analytics['market_attractiveness']:.2f}/100

Risk Index :
{analytics['risk_index']:.2f}/100

Overall Business Opportunity :
{analytics['opportunity_level']}

Market Opportunity :
{analytics['market_opportunity_level']}

Business Readiness :
{analytics['business_readiness']}

Investment Category :
{analytics['investment_category']}
""".strip()

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Analytics Service",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

analytics_service = AnalyticsService()