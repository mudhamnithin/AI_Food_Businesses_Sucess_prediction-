"""
=========================================================
ROI Analysis Service

Version : 6.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class ROIService:
    """
    ROI Intelligence Engine

    Calculates:
    - ROI
    - Revenue Forecast
    - Profit Forecast
    - Cash Flow
    - Business Performance
    """

    # =====================================================
    # Generate ROI Analysis
    # =====================================================

    @staticmethod
    def generate(
        data,
        probability,
        analytics,
        investment
    ):

        # =====================================================
        # Analytics
        # =====================================================

        business_health = analytics["business_health_index"]

        growth = analytics["growth_score"]

        demand = analytics["demand_score"]

        market = analytics["market_attractiveness"]

        roi_percentage = investment["roi_percentage"]

        monthly_profit = investment["estimated_monthly_profit"]

        monthly_revenue = investment["estimated_monthly_revenue"]

        investment_amount = investment["estimated_investment"]

        # =====================================================
        # Overall Business Performance
        # =====================================================

        overall_performance = round(

            (

                business_health * 0.35

                +

                growth * 0.25

                +

                demand * 0.20

                +

                market * 0.10

                +

                roi_percentage * 0.10

            ),

            2

        )

        overall_performance = ScoreEngine.clamp(

            overall_performance

        )

        evaluation = ScoreEngine.evaluate(

            overall_performance

        )

        # =====================================================
        # Annual Revenue
        # =====================================================

        annual_revenue = round(

            monthly_revenue * 12,

            2

        )

        # =====================================================
        # Annual Profit
        # =====================================================

        annual_profit = round(

            monthly_profit * 12,

            2

        )

        # =====================================================
        # Yearly Growth Rate
        # =====================================================

        yearly_growth = round(

            growth * 0.15,

            2

        )

        # =====================================================
        # Five-Year Projection
        # =====================================================

        growth_factor = (

            1 + yearly_growth / 100

        )

        five_year_revenue = round(

            annual_revenue *

            (growth_factor ** 5),

            2

        )

        five_year_profit = round(

            annual_profit *

            (growth_factor ** 5),

            2

        )
                # =====================================================
        # Cash Flow
        # =====================================================

        cash_flow = {

            "monthly_revenue":

                monthly_revenue,

            "monthly_profit":

                monthly_profit,

            "annual_revenue":

                annual_revenue,

            "annual_profit":

                annual_profit

        }

        # =====================================================
        # Break-even Progress
        # =====================================================

        if investment_amount > 0:

            break_even_progress = round(

                (

                    annual_profit

                    /

                    investment_amount

                ) * 100,

                2

            )

        else:

            break_even_progress = 0

        break_even_progress = ScoreEngine.clamp(

            break_even_progress

        )

        # =====================================================
        # ROI Rating
        # =====================================================

        roi_rating = ScoreEngine.overall_status(

            roi_percentage

        )

        roi_grade = ScoreEngine.grade(

            roi_percentage

        )

        # =====================================================
        # Financial KPIs
        # =====================================================

        financial_kpis = {

            "roi":

                round(

                    roi_percentage,

                    2

                ),

            "overall_business_performance":

                round(

                    overall_performance,

                    2

                ),

            "business_grade":

                evaluation["grade"],

            "business_status":

                evaluation["overall_status"]

        }

        # =====================================================
        # Revenue Forecast
        # =====================================================

        revenue_forecast = {

            "monthly":

                monthly_revenue,

            "annual":

                annual_revenue,

            "five_year":

                five_year_revenue

        }

        # =====================================================
        # Profit Forecast
        # =====================================================

        profit_forecast = {

            "monthly":

                monthly_profit,

            "annual":

                annual_profit,

            "five_year":

                five_year_profit

        }

        # =====================================================
        # Business Performance
        # =====================================================

        performance = {

            "score":

                round(

                    overall_performance,

                    2

                ),

            "grade":

                evaluation["grade"],

            "status":

                evaluation["overall_status"],

            "recommendation":

                evaluation["recommendation"]

        }
            # =====================================================
        # Growth Timeline
        # =====================================================

        growth_timeline = {

            "year_1":

                round(

                    annual_profit,

                    2

                ),

            "year_2":

                round(

                    annual_profit * 1.10,

                    2

                ),

            "year_3":

                round(

                    annual_profit * 1.22,

                    2

                ),

            "year_4":

                round(

                    annual_profit * 1.35,

                    2

                ),

            "year_5":

                round(

                    five_year_profit,

                    2

                )

        }

        # =====================================================
        # Performance Insights
        # =====================================================

        performance_insights = []

        if overall_performance >= 90:

            performance_insights.append(

                "Business performance is excellent."

            )

        elif overall_performance >= 80:

            performance_insights.append(

                "Business performance is very good."

            )

        elif overall_performance >= 70:

            performance_insights.append(

                "Business performance is stable with good growth."

            )

        else:

            performance_insights.append(

                "Business performance requires improvement."

            )

        if roi_percentage >= 80:

            performance_insights.append(

                "ROI indicates an attractive investment opportunity."

            )

        if annual_profit >= 1000000:

            performance_insights.append(

                "Strong annual profitability is expected."

            )

        if growth >= 80:

            performance_insights.append(

                "Long-term expansion potential is promising."

            )

        # =====================================================
        # Financial Recommendations
        # =====================================================

        financial_recommendations = []

        if roi_percentage >= 80:

            financial_recommendations.append(

                "Proceed confidently with the investment."

            )

        elif roi_percentage >= 60:

            financial_recommendations.append(

                "Proceed after preparing a detailed financial plan."

            )

        else:

            financial_recommendations.append(

                "Review the business model before investing."

            )

        if growth >= 80:

            financial_recommendations.append(

                "Plan business expansion after the first profitable year."

            )

        if investment_amount >= 3000000:

            financial_recommendations.append(

                "Consider phased investment to reduce financial risk."

            )

        # =====================================================
        # Executive ROI Summary
        # =====================================================

        executive_summary = f"""
ROI ANALYSIS REPORT

Overall Performance :
{overall_performance:.2f}/100

Business Grade :
{evaluation['grade']}

Business Status :
{evaluation['overall_status']}

ROI :
{roi_percentage:.2f}%

Annual Revenue :
₹{annual_revenue:,.0f}

Annual Profit :
₹{annual_profit:,.0f}

5-Year Revenue :
₹{five_year_revenue:,.0f}

5-Year Profit :
₹{five_year_profit:,.0f}

Recommendation :
{evaluation['recommendation']}
""".strip()

        # =====================================================
        # Return ROI Analysis
        # =====================================================

        return {

            "roi_percentage":

                round(

                    roi_percentage,

                    2

                ),

            "roi_grade":

                roi_grade,

            "roi_rating":

                roi_rating,

            "overall_business_performance":

                round(

                    overall_performance,

                    2

                ),

            "business_grade":

                evaluation["grade"],

            "business_status":

                evaluation["overall_status"],

            "business_recommendation":

                evaluation["recommendation"],

            "annual_revenue":

                annual_revenue,

            "annual_profit":

                annual_profit,

            "five_year_revenue":

                five_year_revenue,

            "five_year_profit":

                five_year_profit,

            "cash_flow":

                cash_flow,

            "financial_kpis":

                financial_kpis,

            "revenue_forecast":

                revenue_forecast,

            "profit_forecast":

                profit_forecast,

            "growth_timeline":

                growth_timeline,

            "performance":

                performance,

            "break_even_progress":

                break_even_progress,

            "performance_insights":

                performance_insights,

            "financial_recommendations":

                financial_recommendations,

            "executive_summary":

                executive_summary,

            "overall_score":

                round(

                    (

                        overall_performance

                        +

                        business_health

                    ) / 2,

                    2

                )

        }

    # =====================================================
    # ROI Summary
    # =====================================================

    @staticmethod
    def summary(roi):

        return roi["executive_summary"]

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "ROI Service",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

roi_service = ROIService()    