"""
=========================================================
Investment Analysis Service

Version : 6.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class InvestmentService:
    """
    Investment Intelligence Engine

    Generates:
    - Investment Analysis
    - Revenue
    - Profit
    - ROI
    - Payback
    """

    # =====================================================
    # Generate Investment Analysis
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

        growth = analytics["growth_score"]

        affordability = analytics["affordability_score"]

        market = analytics["market_attractiveness"]

        competition = analytics["competition_score"]

        commercial = analytics["commercial_activity_score"]

        # =====================================================
        # Investment Score
        # =====================================================

        investment_score = round(

            (

                business_health * 0.35

                +

                growth * 0.20

                +

                demand * 0.20

                +

                affordability * 0.15

                +

                market * 0.10

            ),

            2

        )

        investment_score = ScoreEngine.clamp(

            investment_score

        )

        evaluation = ScoreEngine.evaluate(

            investment_score

        )

        # =====================================================
        # Estimated Investment
        # =====================================================

        estimated_investment = round(

            500000

            +

            data.rent_estimate * 18000

            +

            data.nearby_shops_count * 12000

            +

            data.nearby_restaurants_count * 8000,

            2

        )

        # =====================================================
        # Estimated Monthly Revenue
        # =====================================================

        monthly_revenue = round(

            (

                demand * 1800

                +

                market * 1200

                +

                commercial * 800

            ),

            2

        )

        # =====================================================
        # Monthly Profit Margin
        # =====================================================

        if investment_score >= 90:

            profit_margin = 0.30

        elif investment_score >= 80:

            profit_margin = 0.26

        elif investment_score >= 70:

            profit_margin = 0.22

        elif investment_score >= 60:

            profit_margin = 0.18

        else:

            profit_margin = 0.12

        # =====================================================
        # Estimated Monthly Profit
        # =====================================================

        monthly_profit = round(

            monthly_revenue * profit_margin,

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
        # ROI Percentage
        # =====================================================

        if estimated_investment > 0:

            roi_percentage = round(

                (

                    annual_profit

                    /

                    estimated_investment

                ) * 100,

                2

            )

        else:

            roi_percentage = 0

        roi_percentage = ScoreEngine.clamp(

            roi_percentage

        )

        # =====================================================
        # Payback Period
        # =====================================================

        if monthly_profit > 0:

            payback_months = round(

                estimated_investment

                /

                monthly_profit,

                1

            )

        else:

            payback_months = 999

        # =====================================================
        # Profitability Index
        # =====================================================

        profitability_index = round(

            (

                investment_score * 0.60

                +

                roi_percentage * 0.40

            ),

            2

        )

        profitability_index = ScoreEngine.clamp(

            profitability_index

        )

        # =====================================================
        # Break-even Analysis
        # =====================================================

        if payback_months <= 12:

            break_even = "Excellent"

        elif payback_months <= 24:

            break_even = "Good"

        elif payback_months <= 36:

            break_even = "Average"

        else:

            break_even = "Poor"

        # =====================================================
        # Investment Risk
        # =====================================================

        investment_risk = ScoreEngine.risk(

            investment_score

        )

        # =====================================================
        # Investment Rating
        # =====================================================

        investment_rating = ScoreEngine.overall_status(

            investment_score

        )

        investment_grade = ScoreEngine.grade(

            investment_score

        )

        # =====================================================
        # Financial Advice
        # =====================================================

        if investment_score >= 90:

            financial_advice = (

                "Excellent investment opportunity with strong long-term profitability."

            )

        elif investment_score >= 80:

            financial_advice = (

                "Good investment opportunity with manageable financial risk."

            )

        elif investment_score >= 70:

            financial_advice = (

                "Profitable opportunity. Monitor expenses and cash flow."

            )

        elif investment_score >= 60:

            financial_advice = (

                "Proceed carefully after reviewing financial projections."

            )

        else:

            financial_advice = (

                "Investment is currently not recommended."

            )
            # =====================================================
        # Executive Investment Summary
        # =====================================================

        executive_summary = f"""
INVESTMENT ANALYSIS REPORT

Investment Score :
{investment_score:.2f}/100

Investment Grade :
{investment_grade}

Investment Rating :
{investment_rating}

Estimated Investment :
₹{estimated_investment:,.0f}

Estimated Monthly Revenue :
₹{monthly_revenue:,.0f}

Estimated Monthly Profit :
₹{monthly_profit:,.0f}

Annual Profit :
₹{annual_profit:,.0f}

ROI :
{roi_percentage:.2f}%

Payback Period :
{payback_months} Months

Risk Level :
{investment_risk}

Recommendation :
{financial_advice}
""".strip()

        # =====================================================
        # Investment Metrics
        # =====================================================

        investment_metrics = {

            "investment_score":

                round(

                    investment_score,

                    2

                ),

            "roi_percentage":

                round(

                    roi_percentage,

                    2

                ),

            "payback_months":

                payback_months,

            "profitability_index":

                round(

                    profitability_index,

                    2

                )

        }

        # =====================================================
        # Financial Indicators
        # =====================================================

        financial_indicators = {

            "estimated_investment":

                estimated_investment,

            "estimated_monthly_revenue":

                monthly_revenue,

            "estimated_monthly_profit":

                monthly_profit,

            "annual_profit":

                annual_profit

        }

        # =====================================================
        # ROI Dashboard
        # =====================================================

        roi_dashboard = {

            "roi":

                round(

                    roi_percentage,

                    2

                ),

            "investment_grade":

                investment_grade,

            "investment_rating":

                investment_rating,

            "risk":

                investment_risk

        }

        # =====================================================
        # Cash Flow Summary
        # =====================================================

        cash_flow = {

            "monthly_income":

                monthly_revenue,

            "monthly_profit":

                monthly_profit,

            "annual_profit":

                annual_profit

        }

        # =====================================================
        # Investment Timeline
        # =====================================================

        if payback_months <= 12:

            timeline = "0 - 1 Year"

        elif payback_months <= 24:

            timeline = "1 - 2 Years"

        elif payback_months <= 36:

            timeline = "2 - 3 Years"

        else:

            timeline = "More than 3 Years"

        # =====================================================
        # Funding Recommendation
        # =====================================================

        if investment_score >= 90:

            funding = "Suitable for Bank Loan, Venture Capital or Private Investment"

        elif investment_score >= 80:

            funding = "Suitable for Bank Loan with Strong Financial Planning"

        elif investment_score >= 70:

            funding = "Suitable for Moderate Funding or Partnership"

        else:

            funding = "Prefer Self Funding or Low Risk Investment"

        # =====================================================
        # Return Investment Analysis
        # =====================================================

        return {

            "investment_score":

                round(

                    investment_score,

                    2

                ),

            "investment_grade":

                investment_grade,

            "investment_rating":

                investment_rating,

            "estimated_investment":

                estimated_investment,

            "estimated_monthly_revenue":

                monthly_revenue,

            "estimated_monthly_profit":

                monthly_profit,

            "annual_profit":

                annual_profit,

            "roi_percentage":

                round(

                    roi_percentage,

                    2

                ),

            "payback_period_months":

                payback_months,

            "break_even":

                break_even,

            "profitability_index":

                round(

                    profitability_index,

                    2

                ),

            "investment_risk":

                investment_risk,

            "financial_advice":

                financial_advice,

            "investment_metrics":

                investment_metrics,

            "financial_indicators":

                financial_indicators,

            "roi_dashboard":

                roi_dashboard,

            "cash_flow":

                cash_flow,

            "investment_timeline":

                timeline,

            "funding_recommendation":

                funding,

            "executive_summary":

                executive_summary,

            "overall_score":

                round(

                    (

                        investment_score

                        +

                        business_health

                    ) / 2,

                    2

                )

        }

    # =====================================================
    # Investment Summary
    # =====================================================

    @staticmethod
    def summary(investment):

        return investment["executive_summary"]

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Investment Service",

            "status": "Running",

            "version": "6.0"

        }


# =====================================================
# Singleton
# =====================================================

investment_service = InvestmentService()        