"""
=========================================================
Customer Analysis Service

Version : 6.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class CustomerService:
    """
    Customer Intelligence Engine

    Predicts customer behaviour,
    customer segments,
    loyalty,
    diversity,
    marketing opportunities.
    """

    # =====================================================
    # Generate Customer Analysis
    # =====================================================

    @staticmethod
    def generate(data, probability, analytics):

        # -----------------------------------------------
        # Core Scores
        # -----------------------------------------------

        business_health = analytics["business_health_index"]

        location_quality = analytics["location_quality_index"]

        demand_score = analytics["demand_score"]

        # -----------------------------------------------
        # Customer Segment Scores
        # -----------------------------------------------

        office_score = ScoreEngine.clamp(

            data.nearby_offices_count * 4
            + data.footfall_index * 0.30

        )

        student_score = ScoreEngine.clamp(

            data.nearby_colleges_count * 10
            + data.footfall_index * 0.20

        )

        family_score = ScoreEngine.clamp(

            data.avg_income_area * 2
            + data.nearby_parks_count * 8
            + data.nearby_hospitals_count * 5
            + (100 - data.nearby_restaurants_count * 2)

        )

        walkin_score = ScoreEngine.clamp(

            data.footfall_index * 0.80
            + location_quality * 0.20

        )

        visitor_score = ScoreEngine.clamp(

            location_quality * 0.60
            + demand_score * 0.40

        )

        # -----------------------------------------------
        # Customer Mix
        # -----------------------------------------------

        total = (

            office_score

            + student_score

            + family_score

            + walkin_score

            + visitor_score

        )

        if total <= 0:

            total = 1

        customer_mix = {

            "office":

                round(

                    office_score / total * 100,

                    2

                ),

            "students":

                round(

                    student_score / total * 100,

                    2

                ),

            "families":

                round(

                    family_score / total * 100,

                    2

                ),

            "walkin":

                round(

                    walkin_score / total * 100,

                    2

                ),

            "visitors":

                round(

                    visitor_score / total * 100,

                    2

                )

        }

        primary_segment = max(

            customer_mix,

            key=customer_mix.get

        )
                # =====================================================
        # Customer Diversity
        # =====================================================

        active_segments = len(

            [

                value

                for value in customer_mix.values()

                if value >= 15

            ]

        )

        diversity_score = round(

            active_segments * 20,

            2

        )

        diversity_score = ScoreEngine.clamp(

            diversity_score

        )

        # =====================================================
        # Customer Loyalty
        # =====================================================

        loyalty_score = round(

            (

                business_health * 0.35

                +

                demand_score * 0.25

                +

                location_quality * 0.20

                +

                diversity_score * 0.20

            ),

            2

        )

        loyalty_score = ScoreEngine.clamp(

            loyalty_score

        )

        # =====================================================
        # Overall Customer Score
        # =====================================================

        overall_customer_score = round(

            (

                loyalty_score * 0.50

                +

                diversity_score * 0.20

                +

                demand_score * 0.30

            ),

            2

        )

        overall_customer_score = ScoreEngine.clamp(

            overall_customer_score

        )

        # =====================================================
        # Customer Rating
        # =====================================================

        customer_rating = ScoreEngine.overall_status(

            overall_customer_score

        )

        # =====================================================
        # Peak Business Time
        # =====================================================

        if office_score >= max(

            student_score,

            family_score,

            walkin_score

        ):

            peak_time = "08:00 AM - 11:00 AM"

        elif student_score >= max(

            office_score,

            family_score,

            walkin_score

        ):

            peak_time = "04:00 PM - 08:00 PM"

        elif family_score >= max(

            office_score,

            student_score,

            walkin_score

        ):

            peak_time = "06:00 PM - 10:00 PM"

        else:

            peak_time = "Throughout the Day"

        # =====================================================
        # Weekend Potential
        # =====================================================

        if family_score >= 80:

            weekend = "Excellent"

        elif family_score >= 65:

            weekend = "Good"

        elif family_score >= 50:

            weekend = "Moderate"

        else:

            weekend = "Low"

        # =====================================================
        # Marketing Suggestions
        # =====================================================

        marketing_suggestions = []

        if office_score >= 60:

            marketing_suggestions.append(

                "Launch breakfast and office lunch combo offers."

            )

        if student_score >= 60:

            marketing_suggestions.append(

                "Offer student discounts and evening combo meals."

            )

        if family_score >= 60:

            marketing_suggestions.append(

                "Introduce family packs and weekend special offers."

            )

        if walkin_score >= 70:

            marketing_suggestions.append(

                "Improve outdoor branding and road-side visibility."

            )

        if visitor_score >= 70:

            marketing_suggestions.append(

                "Improve Google Business Profile and collect online reviews."

            )

        if diversity_score < 60:

            marketing_suggestions.append(

                "Target multiple customer segments through local promotions."

            )

        if not marketing_suggestions:

            marketing_suggestions.append(

                "Increase digital marketing and local awareness campaigns."

            )
            # =====================================================
        # Customer Insights
        # =====================================================

        customer_insights = [

            f"Primary customer segment: {primary_segment.title()}.",

            f"Overall customer score: {overall_customer_score:.2f}/100.",

            f"Customer loyalty score: {loyalty_score:.2f}/100.",

            f"Customer diversity score: {diversity_score:.2f}/100.",

            f"Peak business hours: {peak_time}.",

            f"Weekend business potential: {weekend}.",

        ]

        # =====================================================
        # Customer Summary
        # =====================================================

        customer_summary = f"""
CUSTOMER ANALYSIS REPORT

Primary Customer Segment :
{primary_segment.title()}

Overall Customer Score :
{overall_customer_score:.2f}/100

Customer Loyalty :
{loyalty_score:.2f}/100

Customer Diversity :
{diversity_score:.2f}/100

Peak Business Time :
{peak_time}

Weekend Potential :
{weekend}

Overall Rating :
{customer_rating}
""".strip()

        # =====================================================
        # Return Customer Analysis
        # =====================================================

        return {

            "customer_mix": customer_mix,

            "primary_segment": primary_segment.title(),

            "customer_loyalty": {

                "score": round(

                    loyalty_score,

                    2

                ),

                "rating": ScoreEngine.overall_status(

                    loyalty_score

                )

            },

            "customer_diversity": {

                "score": round(

                    diversity_score,

                    2

                ),

                "rating": ScoreEngine.overall_status(

                    diversity_score

                )

            },

            "overall_customer_score": round(

                overall_customer_score,

                2

            ),

            "customer_rating": customer_rating,

            "peak_business_time": peak_time,

            "weekend_potential": weekend,

            "marketing_suggestions": marketing_suggestions,

            "customer_insights": customer_insights,

            "customer_summary": customer_summary

        }

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Customer Service",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

customer_service = CustomerService()