"""
=========================================================
Dashboard Service

Version : 5.0
=========================================================
"""

from app.services.score_engine import ScoreEngine


class DashboardService:
    """
    Dashboard Generator

    Uses Analytics Service outputs.

    Does NOT calculate business scores.

    Only visualizes them.
    """

    # =====================================================
    # Generate Dashboard
    # =====================================================

    @staticmethod
    def generate(analytics):

        health = analytics["business_health_index"]

        location = analytics["location_quality_index"]

        demand = analytics["demand_score"]

        competition = analytics["competition_score"]

        affordability = analytics["affordability_score"]

        growth = analytics["growth_score"]

        market = analytics["market_attractiveness"]

        risk = analytics["risk_index"]

        evaluation = ScoreEngine.evaluate(health)

        status = evaluation["overall_status"]

        color = evaluation["color"]

        stars = evaluation["stars"]
        # =====================================================
        # KPI Cards
        # =====================================================

        kpi_cards = [
            {
                "title": "Business Health",
                "value": round(health, 2),
                "unit": "/100",
                "icon": "health",
            },
            {
                "title": "Demand",
                "value": round(demand, 2),
                "unit": "/100",
                "icon": "people",
            },
            {
                "title": "Competition",
                "value": round(competition, 2),
                "unit": "/100",
                "icon": "store",
            },
            {
                "title": "Growth",
                "value": round(growth, 2),
                "unit": "/100",
                "icon": "trending_up",
            },
        ]

        # =====================================================
        # Business Meter
        # =====================================================

        business_meter = {

            "health": round(health,2),

            "location": round(location,2),

            "market": round(market,2),

            "risk": round(risk,2),

            "demand": round(demand,2),

            "growth": round(growth,2)

        }

        # =====================================================
        # Progress Data
        # =====================================================

        progress_data = [
            {"label": "Demand", "value": round(demand, 2)},
            {"label": "Competition", "value": round(competition, 2)},
            {"label": "Affordability", "value": round(affordability, 2)},
            {"label": "Growth", "value": round(growth, 2)},
            {"label": "Business Health", "value": round(health, 2)},
        ]

        # =====================================================
        # Radar Chart
        # =====================================================

        radar_chart = {

            "labels":[

                "Health",

                "Location",

                "Demand",

                "Competition",

                "Growth",

                "Market"

            ],

            "values":[

                round(health,2),

                round(location,2),

                round(demand,2),

                round(competition,2),

                round(growth,2),

                round(market,2)

            ]

        }

        # =====================================================
        # Gauge
        # =====================================================

        gauge = {
            "value": round(health, 2),
            "min": 0,
            "max": 100,
            "label": "Business Health",
        }

        # =====================================================
        # Health Indicator
        # =====================================================

        if health >= 80:

            health_indicator = {
                "icon": "check_circle",
                "message": "Excellent business opportunity.",
            }

        elif health >= 60:

            health_indicator = {"icon": "info", "message": "Moderate opportunity."}

        else:

            health_indicator = {
                "icon": "warning",
                "message": "High-risk location. Review before investing.",
            }
            # =====================================================
        # Alerts
        # =====================================================

        alerts = []

        if competition >= 80:

            alerts.append(
                {
                    "type": "warning",
                    "title": "High Competition",
                    "message": "Nearby competition is extremely high.",
                }
            )
        if risk >= 70:

            alerts.append({

                "type":"danger",

                "title":"High Risk",

                "message":"Overall investment risk is high."

            })
        if affordability <= 40:

            alerts.append(
                {
                    "type": "warning",
                    "title": "High Rental Cost",
                    "message": "Rental cost may affect profitability.",
                }
            )

        if demand <= 40:

            alerts.append(
                {
                    "type": "warning",
                    "title": "Low Customer Demand",
                    "message": "Expected customer demand is currently low.",
                }
            )

        # =====================================================
        # Insights
        # =====================================================

        insights = []

        if health >= 85:

            insights.append("Overall business environment is excellent.")

        if market >= 80:

            insights.append("Market attractiveness is very high.")

        if location >= 80:

            insights.append("Location has strong commercial potential.")

        if growth >= 80:

            insights.append("Business growth potential is excellent.")
        if demand >= 85:

            insights.append(

                "Customer demand is exceptionally strong."

            )

        if affordability >= 80:

            insights.append(

                "Operational costs are highly affordable."

            )    

        # =====================================================
        # Priority Actions
        # =====================================================

        priority_actions = []

        if demand < 60:

            priority_actions.append("Increase local marketing campaigns.")

        if competition > 70:

            priority_actions.append("Differentiate products and pricing.")

        if affordability < 60:

            priority_actions.append("Optimize rental and operational costs.")

        if health >= 85:

            priority_actions.append("Proceed with investment planning.")

        # =====================================================
        # Quick Statistics
        # =====================================================

        quick_statistics = {
            "Business Health": round(health, 2),
            "Demand": round(demand, 2),
            "Competition": round(competition, 2),
            "Growth": round(growth, 2),
            "Risk": round(risk, 2),
            "Market": round(market, 2),
        }

        # =====================================================
        # Dashboard Summary
        # =====================================================

        dashboard_summary = f"""
BUSINESS DASHBOARD SUMMARY

Business Health:
{health:.2f}/100

Location Quality:
{location:.2f}/100

Market Attractiveness:
{market:.2f}/100

Demand:
{demand:.2f}/100

Competition:
{competition:.2f}/100

Growth:
{growth:.2f}/100

Business Status:
{status}
""".strip()

        # =====================================================
        # Executive Dashboard
        # =====================================================

        executive_dashboard = {

            "headline":"Business Performance Dashboard",

            "overall_status":status,

            "status_color":color,

            "health":round(health,2),

            "location":round(location,2),

            "demand":round(demand,2),

            "competition":round(competition,2),

            "growth":round(growth,2),

            "market":round(market,2),

            "risk":round(risk,2),

            "stars":stars

        }
        # =====================================================
        # Return Dashboard
        # =====================================================

        return {
            "overall_status": status,
            "status_color": color,
            "performance_level": status,
            "kpi_cards": kpi_cards,
            "badges": [
                {"title": evaluation["grade"], "color": color},
                {"title": evaluation["recommendation"], "color": color},
            ],
            "business_meter": business_meter,
            "progress_data": progress_data,
            "radar_chart": radar_chart,
            "gauge": gauge,
            "health_indicator": health_indicator,
            "alerts": alerts,
            "insights": insights,
            "priority_actions": priority_actions,
            "quick_statistics": quick_statistics,
            "dashboard_summary": dashboard_summary,
            "executive_dashboard": executive_dashboard,
        }
        # =====================================================

    # Dashboard Health
    # =====================================================

    @staticmethod
    def health():

        return {"service": "Dashboard Service", "status": "Running", "version": "5.0"}


dashboard_service = DashboardService()
