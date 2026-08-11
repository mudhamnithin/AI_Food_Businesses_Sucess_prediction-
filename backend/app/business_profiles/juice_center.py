"""
=========================================================
Juice Center Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class JuiceCenterProfile:

    NAME = "Juice Center"

    DESCRIPTION = (
        "Suitable for students, families, "
        "hospital visitors and health-conscious customers."
    )

    # =====================================================
    # Feature Weights
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.25,
        "nearby_offices_count": 0.10,
        "nearby_colleges_count": 0.18,
        "nearby_hospitals_count": 0.15,
        "nearby_restaurants_count": 0.08,
        "nearby_shops_count": 0.08,
        "nearby_parks_count": 0.06,
        "avg_income_area": 0.05,
        "rent_estimate": 0.03,
        "distance_to_nearest_brand_chai": 0.02,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 85,
        "nearby_offices_count": 12,
        "nearby_colleges_count": 8,
        "nearby_hospitals_count": 4,
        "nearby_restaurants_count": 10,
        "nearby_shops_count": 10,
        "nearby_parks_count": 2,
        "avg_income_area": 18,
        "rent_estimate": 60,
        "distance_to_nearest_brand_chai": 300,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("footfall_index", 70, "Excellent customer movement."),
        ("nearby_colleges_count", 6, "Large student customer base."),
        ("nearby_hospitals_count", 3, "Hospital visitors increase juice demand."),
        ("nearby_offices_count", 10, "Healthy office customer base."),
        ("nearby_parks_count", 2, "Family recreation supports weekend demand."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("footfall_index", 40, "Low customer movement."),
        ("nearby_colleges_count", 2, "Limited student demand."),
        ("nearby_hospitals_count", 1, "Low hospital customer base."),
        ("rent_estimate", 90, "High rental expenses."),
        ("nearby_restaurants_count", 20, "Strong nearby food competition."),
    ]

    # =====================================================
    # Marketing
    # =====================================================

    MARKETING = [
        "Fresh fruit combo offers.",
        "Healthy breakfast packages.",
        "Gym membership discounts.",
        "Summer special juices.",
        "Sugar-free menu.",
        "Fresh seasonal fruits.",
        "Loyalty reward program.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["08:00 - 11:00", "01:00 - 03:00", "05:00 - 08:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "Students",
        "Hospital Visitors",
        "Office Employees",
        "Families",
        "Fitness Enthusiasts",
    ]

    # =====================================================
    # Investment
    # =====================================================

    INVESTMENT = {"low": "₹4L - ₹7L", "medium": "₹7L - ₹12L", "high": "₹12L+"}


juice_center_profile = JuiceCenterProfile()
