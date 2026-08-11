"""
=========================================================
Business Recommendation Service

Version : 7.0
AI Business Intelligence Engine
=========================================================
"""

from app.services.score_engine import ScoreEngine

from app.business_profiles.tea_shop import tea_shop_profile
from app.business_profiles.restaurant import restaurant_profile
from app.business_profiles.bakery import bakery_profile
from app.business_profiles.cafe import cafe_profile
from app.business_profiles.juice_center import juice_center_profile
from app.business_profiles.ice_cream import ice_cream_profile
from app.business_profiles.cloud_kitchen import cloud_kitchen_profile


class BusinessRecommendationService:
    """
    AI Business Recommendation Engine
    """

    def __init__(self):

        self.business_profiles = [

            tea_shop_profile,

            restaurant_profile,

            bakery_profile,

            cafe_profile,

            juice_center_profile,

            ice_cream_profile,

            cloud_kitchen_profile,

        ]

    # =====================================================
    # Normalize Features
    # =====================================================

    @staticmethod
    def normalize_features(data):

        return {

            "footfall_index":
                ScoreEngine.clamp(
                    data.footfall_index
                ),

            "nearby_offices_count":
                ScoreEngine.clamp(
                    data.nearby_offices_count * 5
                ),

            "nearby_colleges_count":
                ScoreEngine.clamp(
                    data.nearby_colleges_count * 10
                ),

            "nearby_hospitals_count":
                ScoreEngine.clamp(
                    data.nearby_hospitals_count * 20
                ),

            "nearby_restaurants_count":
                ScoreEngine.clamp(
                    100 -
                    (data.nearby_restaurants_count * 4)
                ),

            "nearby_shops_count":
                ScoreEngine.clamp(
                    data.nearby_shops_count * 6
                ),

            "nearby_parks_count":
                ScoreEngine.clamp(
                    data.nearby_parks_count * 20
                ),

            "avg_income_area":
                ScoreEngine.clamp(
                    data.avg_income_area * 4
                ),

            "rent_estimate":
                ScoreEngine.clamp(
                    100 -
                    data.rent_estimate
                ),

            "distance_to_nearest_brand_chai":
                ScoreEngine.clamp(
                    data.distance_to_nearest_brand_chai / 10
                )

        }

    # =====================================================
    # Compare With Ideal Profile
    # =====================================================

    @staticmethod
    def ideal_match(profile, data):

        score = 0

        total = 0

        for feature, ideal in profile.IDEAL.items():

            if not hasattr(data, feature):

                continue

            value = getattr(data, feature)

            if feature == "distance_to_nearest_brand_chai":

                percentage = min(

                    (value / max(ideal, 1)) * 100,

                    100

                )

            elif feature == "rent_estimate":

                if value <= ideal:

                    percentage = 100

                else:

                    percentage = max(

                        0,

                        100 -

                        ((value - ideal) / max(ideal, 1)) * 100

                    )

            else:

                difference = abs(

                    value - ideal

                )

                percentage = max(

                    0,

                    100 -

                    (difference / max(ideal, 1)) * 100

                )

            score += percentage

            total += 1

        if total == 0:

            return 0

        return round(

            score / total,

            2

        )

    # =====================================================
    # Score Helpers
    # =====================================================

    @staticmethod
    def grade(score):

        return ScoreEngine.grade(score)

    @staticmethod
    def recommendation(score):

        return ScoreEngine.recommendation(score)

    @staticmethod
    def confidence(score):

        return ScoreEngine.confidence(score)
        # =====================================================
    # Calculate Business Suitability Score
    # =====================================================

    @staticmethod
    def calculate_score(profile, data):

        weights = profile.WEIGHTS

        score = 0
        total_weight = 0

        for feature, weight in weights.items():

            if not hasattr(data, feature):
                continue

            value = getattr(data, feature)

            if feature == "footfall_index":

                normalized = ScoreEngine.clamp(value)

            elif feature == "avg_income_area":

                normalized = ScoreEngine.clamp(value * 4)

            elif feature == "rent_estimate":

                normalized = ScoreEngine.clamp(
                    100 - value
                )

            elif feature == "nearby_restaurants_count":

                normalized = ScoreEngine.clamp(
                    100 - value * 4
                )

            elif feature == "nearby_offices_count":

                normalized = ScoreEngine.clamp(
                    value * 5
                )

            elif feature == "nearby_colleges_count":

                normalized = ScoreEngine.clamp(
                    value * 10
                )

            elif feature == "nearby_hospitals_count":

                normalized = ScoreEngine.clamp(
                    value * 20
                )

            elif feature == "nearby_shops_count":

                normalized = ScoreEngine.clamp(
                    value * 6
                )

            elif feature == "nearby_parks_count":

                normalized = ScoreEngine.clamp(
                    value * 20
                )

            elif feature == "distance_to_nearest_brand_chai":

                normalized = ScoreEngine.clamp(
                    value / 10
                )

            else:

                normalized = ScoreEngine.clamp(value)

            score += normalized * weight
            total_weight += weight

        if total_weight == 0:
            return 0

        return round(
            score / total_weight,
            2
        )

    # =====================================================
    # Evaluate Business
    # =====================================================

    def evaluate_business(

        self,

        profile,

        data,

        probability

    ):

        business_score = self.calculate_score(

            profile,

            data

        )

        customer_score = self.customer_demand(

            profile,

            data

        )

        competition_score = self.competition_score(

            profile,

            data

        )

        revenue = self.revenue_prediction(

            profile,

            data

        )

        profit = self.profit_prediction(

            profile,

            revenue

        )

        ideal_score = self.ideal_match(

            profile,

            data

        )

        analytics_score = round(

            (

                business_score * 0.30 +

                ideal_score * 0.20 +

                customer_score * 0.20 +

                competition_score * 0.15 +

                probability * 0.15

            ),

            2

        )

        analytics_score = ScoreEngine.clamp(

            analytics_score

        )

        bonus = 0

        if customer_score >= 85:
            bonus += 2

        if competition_score >= 80:
            bonus += 2

        if ideal_score >= 90:
            bonus += 1

        final_score = ScoreEngine.clamp(

            round(

                analytics_score + bonus,

                2

            )

        )

        strengths = self.generate_strengths(

            profile,

            data

        )

        risks = self.generate_risks(

            profile,

            data

        )

        opportunities = self.opportunities(

            profile,

            data,

            strengths

        )

        insights = self.business_insights(

            profile,

            data

        )

        improvements = self.improvement_suggestions(

            profile,

            data

        )

        evaluation = ScoreEngine.evaluate(

            final_score

        )

        return {

            "business": profile.NAME,

            "description": profile.DESCRIPTION,

            "score": final_score,

            "business_score": business_score,

            "ideal_match": ideal_score,

            "ml_probability": probability,

            "rank": 0,

            "grade": evaluation["grade"],

            "recommendation": evaluation["recommendation"],

            "confidence": evaluation["confidence"],

            "strengths": strengths,

            "risks": risks,

            "customer_demand": customer_score,

            "competition_score": competition_score,

            "revenue_prediction": revenue,

            "profit_prediction": profit,

            "business_insights": insights,

            "improvement_suggestions": improvements,

            "opportunities": opportunities,

            "marketing": profile.MARKETING,

            "target_customers": profile.TARGET_CUSTOMERS,

            "peak_hours": profile.PEAK_HOURS,

            "investment": profile.INVESTMENT,

            "summary": self.ai_summary(

                profile.NAME,

                final_score,

                strengths,

                risks,

                ideal_score

            )

        }
        # =====================================================
    # Generate Strengths
    # =====================================================

    @staticmethod
    def generate_strengths(profile, data):

        strengths = []

        if data.footfall_index >= 80:
            strengths.append("Excellent customer footfall")

        if data.nearby_offices_count >= 15:
            strengths.append("High office employee population")

        if data.nearby_colleges_count >= 3:
            strengths.append("Strong student customer base")

        if data.nearby_hospitals_count >= 2:
            strengths.append("Consistent hospital visitors")

        if data.avg_income_area >= 20:
            strengths.append("Good purchasing power")

        if data.distance_to_nearest_brand_chai >= 500:
            strengths.append("Low competition from branded tea chains")

        if data.nearby_parks_count >= 1:
            strengths.append("Nearby recreational area")

        if data.nearby_shops_count >= 10:
            strengths.append("Busy commercial surroundings")

        if data.rent_estimate <= 50:
            strengths.append("Affordable rental cost")

        if len(strengths) == 0:
            strengths.append("Average business environment")

        return strengths

    # =====================================================
    # Generate Risks
    # =====================================================

    @staticmethod
    def generate_risks(profile, data):

        risks = []

        if data.footfall_index < 50:
            risks.append("Low customer footfall")

        if data.rent_estimate > 70:
            risks.append("High monthly rental expense")

        if data.nearby_restaurants_count > 15:
            risks.append("Heavy restaurant competition")

        if data.avg_income_area < 12:
            risks.append("Low purchasing power in locality")

        if data.distance_to_nearest_brand_chai < 250:
            risks.append("Strong branded competitor nearby")

        if data.nearby_offices_count < 5:
            risks.append("Limited office customers")

        if data.nearby_colleges_count == 0:
            risks.append("No nearby student population")

        if len(risks) == 0:
            risks.append("No major business risks identified")

        return risks

    # =====================================================
    # Business Opportunities
    # =====================================================

    @staticmethod
    def opportunities(profile, data, strengths):

        opportunities = []

        if data.nearby_offices_count >= 15:
            opportunities.append(
                "Launch office lunch and evening snack combos"
            )

        if data.nearby_colleges_count >= 3:
            opportunities.append(
                "Offer student discounts and combo meals"
            )

        if data.nearby_hospitals_count >= 2:
            opportunities.append(
                "Provide quick takeaway service"
            )

        if data.footfall_index >= 80:
            opportunities.append(
                "Increase seating capacity"
            )

        if data.avg_income_area >= 20:
            opportunities.append(
                "Introduce premium products"
            )

        if data.distance_to_nearest_brand_chai >= 500:
            opportunities.append(
                "Capture local market before competitors arrive"
            )

        if len(opportunities) == 0:
            opportunities.append(
                "Focus on improving customer acquisition"
            )

        return opportunities

    # =====================================================
    # AI Summary
    # =====================================================

    @staticmethod
    def ai_summary(

        business,

        score,

        strengths,

        risks,

        ideal_match

    ):

        return (
            f"{business} achieved an AI score of "
            f"{score:.2f}/100 with an ideal location "
            f"match of {ideal_match:.2f}%. "
            f"Major strengths include "
            f"{', '.join(strengths[:3])}. "
            f"Primary risks include "
            f"{', '.join(risks[:2])}."
        )
        # =====================================================
    # Customer Demand Score
    # =====================================================

    @staticmethod
    def customer_demand(profile, data):

        score = 0

        score += min(data.footfall_index * 0.40, 40)

        score += min(data.nearby_offices_count * 1.20, 15)

        score += min(data.nearby_colleges_count * 2.50, 15)

        score += min(data.nearby_hospitals_count * 3.00, 10)

        score += min(data.nearby_shops_count * 0.80, 10)

        score += min(data.avg_income_area * 0.40, 10)

        score += min(data.nearby_parks_count * 2.50, 5)

        score += min(
            data.distance_to_nearest_brand_chai / 250,
            5
        )

        return round(

            min(score, 100),

            2

        )

    # =====================================================
    # Competition Score
    # =====================================================

    @staticmethod
    def competition_score(profile, data):

        score = 100

        score -= min(

            data.nearby_restaurants_count * 3,

            45

        )

        if data.distance_to_nearest_brand_chai < 200:

            score -= 25

        elif data.distance_to_nearest_brand_chai < 500:

            score -= 15

        elif data.distance_to_nearest_brand_chai < 1000:

            score -= 8

        if data.nearby_shops_count > 20:

            score += 5

        return round(

            max(

                min(score, 100),

                0

            ),

            2

        )

    # =====================================================
    # Revenue Prediction
    # =====================================================

    @staticmethod
    def revenue_prediction(profile, data):

        base_revenue = 50000

        footfall_factor = data.footfall_index / 100

        office_factor = 1 + (data.nearby_offices_count * 0.02)

        college_factor = 1 + (data.nearby_colleges_count * 0.03)

        income_factor = 1 + (data.avg_income_area * 0.01)

        rent_factor = max(

            0.60,

            1 - (data.rent_estimate * 0.005)

        )

        revenue = (

            base_revenue *

            footfall_factor *

            office_factor *

            college_factor *

            income_factor *

            rent_factor

        )

        return round(

            revenue,

            2

        )

    # =====================================================
    # Profit Prediction
    # =====================================================

    @staticmethod
    def profit_prediction(profile, revenue):

        estimated_expense = revenue * 0.65

        profit = revenue - estimated_expense

        margin = (profit / revenue) * 100

        return {

            "monthly_profit": round(

                profit,

                2

            ),

            "profit_margin": round(

                margin,

                2

            ),

            "estimated_expense": round(

                estimated_expense,

                2

            )

        }
        # =====================================================
    # Business Insights
    # =====================================================

    @staticmethod
    def business_insights(profile, data):

        insights = []

        if data.footfall_index >= 80:
            insights.append(
                "Excellent customer movement throughout the day."
            )

        elif data.footfall_index >= 60:
            insights.append(
                "Moderate customer footfall with good growth potential."
            )

        else:
            insights.append(
                "Customer footfall is below average."
            )

        if data.nearby_offices_count >= 15:
            insights.append(
                "Office employees can generate strong weekday demand."
            )

        if data.nearby_colleges_count >= 3:
            insights.append(
                "Students can become repeat customers."
            )

        if data.nearby_hospitals_count >= 2:
            insights.append(
                "Hospitals generate steady visitor demand throughout the day."
            )

        if data.avg_income_area >= 20:
            insights.append(
                "Residents have good purchasing power."
            )

        if data.rent_estimate > 60:
            insights.append(
                "Rental cost is relatively high."
            )

        if data.distance_to_nearest_brand_chai >= 500:
            insights.append(
                "Limited branded competition nearby."
            )

        return insights

    # =====================================================
    # Improvement Suggestions
    # =====================================================

    @staticmethod
    def improvement_suggestions(profile, data):

        suggestions = []

        if data.footfall_index < 70:
            suggestions.append(
                "Increase local marketing to improve customer visits."
            )

        if data.nearby_restaurants_count > 10:
            suggestions.append(
                "Differentiate with unique menu and pricing."
            )

        if data.avg_income_area < 15:
            suggestions.append(
                "Offer budget-friendly products."
            )

        if data.rent_estimate > 60:
            suggestions.append(
                "Negotiate rent or maximize seating utilization."
            )

        if data.distance_to_nearest_brand_chai < 300:
            suggestions.append(
                "Strengthen branding against nearby competitors."
            )

        if len(suggestions) == 0:

            suggestions.append(
                "Current location has strong fundamentals. Focus on execution."
            )

        return suggestions

    # =====================================================
    # Executive Recommendation
    # =====================================================

    @staticmethod
    def executive_recommendation(best_business):

        score = best_business["score"]

        if score >= 90:

            decision = "Highly Recommended"

        elif score >= 80:

            decision = "Recommended"

        elif score >= 70:

            decision = "Consider with Improvements"

        else:

            decision = "Not Recommended"

        return {

            "recommended_business":
                best_business["business"],

            "decision":
                decision,

            "score":
                round(score, 2),

            "grade":
                best_business["grade"],

            "confidence":
                best_business["confidence"],

            "summary":
                best_business["summary"]

        }

    # =====================================================
    # Rank Businesses
    # =====================================================

    def rank_businesses(

        self,

        data,

        probability

    ):

        businesses = []

        normalized = self.normalize_features(data)

        for profile in self.business_profiles:

            business = self.evaluate_business(

                profile,

                data,

                probability

            )

            businesses.append(

                business

            )

        businesses.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        for index, business in enumerate(

            businesses,

            start=1

        ):

            business["rank"] = index

        return businesses
        # =====================================================
    # Business Comparison
    # =====================================================

    @staticmethod
    def comparison_table(businesses):

        comparison = []

        for business in businesses:

            comparison.append(

                {

                    "rank": business["rank"],

                    "business": business["business"],

                    "score": round(
                        business["score"],
                        2
                    ),

                    "grade": business["grade"],

                    "recommendation":
                        business["recommendation"],

                    "ideal_match":
                        round(
                            business["ideal_match"],
                            2
                        ),

                    "customer_demand":
                        round(
                            business["customer_demand"],
                            2
                        ),

                    "competition":
                        round(
                            business["competition_score"],
                            2
                        ),

                    "strengths":
                        len(
                            business["strengths"]
                        ),

                    "risks":
                        len(
                            business["risks"]
                        )

                }

            )

        return comparison

    # =====================================================
    # Generate Complete Recommendation
    # =====================================================

    def generate(

        self,

        data,

        probability,

        analytics

    ):

        ranked = self.rank_businesses(

            data,

            probability

        )

        best = ranked[0]

        score_distribution = {

            "excellent": 0,

            "very_good": 0,

            "good": 0,

            "average": 0,

            "poor": 0

        }

        for business in ranked:

            score = business["score"]

            if score >= 90:

                score_distribution["excellent"] += 1

            elif score >= 80:

                score_distribution["very_good"] += 1

            elif score >= 70:

                score_distribution["good"] += 1

            elif score >= 60:

                score_distribution["average"] += 1

            else:

                score_distribution["poor"] += 1

        return {

            "best_business": best,

            "top_3_businesses": ranked[:3],

            "all_businesses": ranked,

            "comparison":

                self.comparison_table(

                    ranked

                ),

            "score_distribution":

                score_distribution,

            "analytics_summary": {

                "businesses_evaluated":

                    len(

                        ranked

                    ),

                "highest_score":

                    ranked[0]["score"],

                "lowest_score":

                    ranked[-1]["score"],

                "average_score":

                    round(

                        sum(

                            x["score"]

                            for x in ranked

                        ) / len(ranked),

                        2

                    ),

                "recommended_business":

                    best["business"]

            },

            "executive_recommendation":

                self.executive_recommendation(

                    best

                )

        }

    # =====================================================
    # Summary
    # =====================================================

    @staticmethod
    def summary(report):

        best = report["best_business"]

        return {

            "business":

                best["business"],

            "score":

                best["score"],

            "grade":

                best["grade"],

            "recommendation":

                best["recommendation"],

            "confidence":

                best["confidence"]

        }

    # =====================================================
    # Health
    # =====================================================

    @staticmethod
    def health():

        return {

            "service":

                "Business Recommendation Service",

            "status":

                "Running",

            "version":

                "7.0"

        }


# =====================================================
# Singleton
# =====================================================

business_recommendation_service = BusinessRecommendationService()