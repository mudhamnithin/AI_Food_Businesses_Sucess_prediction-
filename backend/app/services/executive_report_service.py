"""
=========================================================
Executive Report Service

AI Business Intelligence Report Generator

Version : 6.0
=========================================================
"""

from datetime import datetime

from app.services.score_engine import ScoreEngine

from app.services.explanation_service import explanation_service
from app.services.comparison_service import comparison_service
from app.services.risk_service import risk_service
from app.services.timeline_service import timeline_service
from app.services.action_plan_service import action_plan_service


class ExecutiveReportService:
    """
    Executive AI Report Generator

    Generates the complete
    AI Business Intelligence Report.
    """

    # =====================================================
    # Generate Report
    # =====================================================

    @staticmethod
    def generate(

        prediction,

        analytics,

        customer,

        swot,

        investment,

        roi,

        recommendation,

        data

    ):

        score = prediction["success_probability"]

        evaluation = ScoreEngine.evaluate(score)

        generated_at = datetime.now().strftime("%d-%m-%Y %H:%M")
        best_business = recommendation.get("best_business", {})
        business_name = best_business.get("business", "Business")
                # =====================================================
        # Explainable AI
        # =====================================================

        explanation = explanation_service.generate(

            data,

            recommendation["best_business"]

        )

        feature_importance = (

            explanation_service.feature_importance(

                data

            )

        )

        # =====================================================
        # Business Comparison
        # =====================================================

        comparison = comparison_service.generate(

            recommendation.get(
                "all_businesses",
                []
            )

        )

        comparison_summary = (

            comparison_service.summary(

                recommendation.get(
                    "all_businesses",
                    []
                )

            )

        )
        # =====================================================
        # Risk Analysis
        # =====================================================

        risk_analysis = risk_service.analyze(

            data

        )

        risk_meter = risk_service.meter(

            risk_analysis["risk_score"]

        )

        # =====================================================
        # Business Timeline
        # =====================================================

        timeline = timeline_service.generate(

            recommendation["best_business"]

        )

        milestones = (

            timeline_service.milestones()

        )

        # =====================================================
        # AI Action Plan
        # =====================================================

        action_plan = (

            action_plan_service.generate(

                recommendation["best_business"]

            )

        )

        startup_checklist = (

            action_plan_service.startup_checklist()

        )

        expansion_checklist = (

            action_plan_service.expansion_checklist()

        )
                # =====================================================
        # Executive Summary
        # =====================================================

        executive_summary = f"""
AI BUSINESS INTELLIGENCE EXECUTIVE REPORT

==================================================

Generated At:
{generated_at}

Success Probability:
{prediction['success_probability']:.2f}%

Overall AI Score:
{prediction['overall_ai_score']:.2f}/100

Business Grade:
{prediction['grade']}

Decision:
{prediction['decision']}

Risk Level:
{prediction['risk_level']}

Recommended Business:
{recommendation['best_business']['business']}

Confidence:
{prediction['confidence']}

==================================================
""".strip()

        # =====================================================
        # Key Findings
        # =====================================================

        key_findings = [

            f"Business Health : {analytics['business_health_index']:.2f}/100",

            f"Market Attractiveness : {analytics['market_attractiveness']:.2f}/100",

            f"Customer Score : {customer['overall_customer_score']:.2f}/100",

            f"Investment Score : {investment['investment_score']:.2f}/100",

            f"ROI : {roi['roi_percentage']:.2f}%",

            f"SWOT Score : {swot['swot_score']:.2f}/100",

            f"Ideal Match : {recommendation['best_business']['ideal_match']:.2f}%"

        ]

        # =====================================================
        # Business Highlights
        # =====================================================

        business_highlights = []

        if analytics["business_health_index"] >= 85:

            business_highlights.append(
                "Excellent overall business health."
            )

        if analytics["market_attractiveness"] >= 80:

            business_highlights.append(
                "High market attractiveness."
            )

        if customer["overall_customer_score"] >= 80:

            business_highlights.append(
                "Strong customer demand."
            )

        if investment["investment_score"] >= 80:

            business_highlights.append(
                "Investment feasibility is excellent."
            )

        if roi["overall_business_performance"] >= 80:

            business_highlights.append(
                "Projected ROI is highly attractive."
            )

        if recommendation["best_business"]["score"] >= 85:

            business_highlights.append(
                "Business recommendation confidence is very high."
            )

        # =====================================================
        # Risk Highlights
        # =====================================================

        risk_highlights = []

        if analytics["competition_score"] >= 75:

            risk_highlights.append(
                "Strong local competition."
            )

        if analytics["risk_index"] >= 70:

            risk_highlights.append(
                "Overall business risk is above average."
            )

        if analytics["affordability_score"] <= 40:

            risk_highlights.append(
                "Rental cost may reduce profitability."
            )

        if prediction["risk_level"] in [

            "High",

            "Very High"

        ]:

            risk_highlights.append(
                "Investment requires careful planning."
            )

        if len(risk_analysis["identified_risks"]) > 0:

            for item in risk_analysis["identified_risks"]:

                risk_highlights.append(

                    item["message"]

                )

        if len(risk_highlights) == 0:

            risk_highlights.append(

                "No major business risks identified."

            )

        # =====================================================
        # Executive Recommendations
        # =====================================================

        executive_recommendations = [

            prediction.get(
                "recommendation",
                "No recommendation available."
            ),

            str(
                recommendation.get(
                    "executive_recommendation",
                    ""
                )
            )

        ]

        if investment["investment_score"] >= 80:

            executive_recommendations.append(

                "Proceed with investment."

            )

        elif investment["investment_score"] >= 60:

            executive_recommendations.append(

                "Proceed after detailed financial planning."

            )

        else:

            executive_recommendations.append(

                "Re-evaluate the location before investing."

            )

        executive_recommendations.extend(

            explanation[:3]

        )
                # =====================================================
        # AI Conclusion
        # =====================================================

        ai_conclusion = f"""
==================================================
AI BUSINESS CONCLUSION
==================================================

The AI engine analyzed this location using:

• Machine Learning Prediction
• Customer Analysis
• SWOT Analysis
• Investment Analysis
• ROI Analysis
• Business Recommendation Engine
• Risk Assessment
• Explainable AI

Overall Success Probability

{prediction['success_probability']:.2f}%

Overall AI Score

{prediction['overall_ai_score']:.2f}/100

Recommended Business

{recommendation['best_business']['business']}

Overall Confidence

{prediction['confidence']}

Risk Level

{prediction['risk_level']}

Decision

{prediction['decision']}

==================================================
""".strip()

        # =====================================================
        # Executive Score Card
        # =====================================================

        score_card = {

            "overall_ai_score":
                round(
                    prediction["overall_ai_score"],
                    2
                ),

            "prediction_score":
                round(
                    prediction["success_probability"],
                    2
                ),

            "business_health":
                round(
                    analytics["business_health_index"],
                    2
                ),

            "market_score":
                round(
                    analytics["market_attractiveness"],
                    2
                ),

            "customer_score":
                round(
                    customer["overall_customer_score"],
                    2
                ),

            "investment_score":
                round(
                    investment["investment_score"],
                    2
                ),

            "roi_score":
                round(
                    roi["overall_business_performance"],
                    2
                ),

            "swot_score":
                round(
                    swot["swot_score"],
                    2
                ),

            "risk_score":
                round(
                    risk_analysis["risk_score"],
                    2
                ),

            "ideal_match":
                round(
                    recommendation["best_business"]["ideal_match"],
                    2
                )

        }

     # =====================================================
# =====================================================
# Final Verdict
# =====================================================

        final_verdict = {

            "grade":
                evaluation["grade"],

            "status":
                evaluation["overall_status"],

            "decision":
                prediction["decision"],

            "recommendation":
                str(
                    recommendation.get(
                        "executive_recommendation",
                        "No recommendation available."
                    )
                ),

            "risk":
                prediction["risk_level"],

            "recommended_business":
                business_name

        }
        # =====================================================
        # Metadata
        # =====================================================

        metadata = {

            "generated_at":
                generated_at,

            "report_version":
                "6.0",

            "prediction_engine":
                "Random Forest Classifier",

            "recommendation_engine":
                "Business Recommendation Engine v6",

            "report_type":
                "AI Business Intelligence Report"

        }

        # =====================================================
        # Professional Summary
        # =====================================================

        professional_summary = f"""
BUSINESS INTELLIGENCE SUMMARY

Business Grade
--------------
{prediction['grade']}

Overall AI Score
----------------
{prediction['overall_ai_score']:.2f}/100

Recommended Business
--------------------
{recommendation['best_business']['business']}

Investment Rating
-----------------
{investment['investment_rating']}

ROI
---
{roi['roi_percentage']:.2f}%

Business Health
---------------
{analytics['business_health_index']:.2f}/100

Customer Score
--------------
{customer['overall_customer_score']:.2f}/100

SWOT Score
----------
{swot['swot_score']:.2f}/100

Final Verdict
-------------
{prediction['decision']}
""".strip()

        # =====================================================
        # Business Intelligence Summary
        # =====================================================

        business_intelligence = {

            "top_business":
                business_name,

            "business_score":
                recommendation["best_business"].get(
                    "score",
                    0
                ),

            "risk_level":
                risk_analysis.get(
                    "overall_risk",
                    "Medium"
                ),

            "overall_confidence":
                prediction.get(
                    "confidence",
                    "Medium"
                ),

            "businesses_compared":
                len(
                    recommendation.get(
                        "all_businesses",
                        []
                    )
                )

        }
                # =====================================================
        # Return Executive Report
        # =====================================================

        return {

            # Executive

            "executive_summary":
                executive_summary,

            "professional_summary":
                professional_summary,

            "ai_conclusion":
                ai_conclusion,

            # Scores

            "overall_score":
                round(
                    prediction["overall_ai_score"],
                    2
                ),

            "overall_grade":
                evaluation["grade"],

            "overall_rating":
                evaluation["overall_status"],

            "score_card":
                score_card,

            "final_verdict":
                final_verdict,

            # Business Recommendation

            "recommended_business"  :
                recommendation.get(
                    "best_business",
                    {}
                ),

            "top_3_businesses":
                recommendation.get(
                    "top_3_businesses",
                    []
                ),

            "all_businesses":
                recommendation.get(
                    "all_businesses",
                    []
                ),
            # SWOT

            "swot":
                swot,

            # Analytics

            "analytics":
                analytics,

            "customer_analysis":
                customer,

            "investment_analysis":
                investment,

            "roi_analysis":
                roi,

            # Explainable AI

            "explanation":
                explanation,

            "feature_importance":
                feature_importance,

            # Comparison

            "business_comparison":
                comparison,

            "comparison_summary":
                comparison_summary,

            # Risk

            "risk_analysis":
                risk_analysis,

            "risk_meter":
                risk_meter,

            # Timeline

            "business_timeline":
                timeline,

            "business_milestones":
                milestones,

            # Action Plan

            "action_plan":
                action_plan,

            "startup_checklist":
                startup_checklist,

            "expansion_checklist":
                expansion_checklist,

            # Report Sections

            "key_findings":
                key_findings,

            "business_highlights":
                business_highlights,

            "risk_highlights":
                risk_highlights,

            "executive_recommendations":
                executive_recommendations,

            "business_intelligence":
                business_intelligence,

            # Metadata

            "metadata":
                metadata

        }

    # =====================================================
    # Executive Summary
    # =====================================================

    @staticmethod
    def summary(report):

        return report["professional_summary"]

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service":
                "Executive Report Service",

            "status":
                "Running",

            "version":
                "6.0"

        }


# =====================================================
# Singleton
# =====================================================

executive_report_service = ExecutiveReportService()