"""
=========================================================
Bakery Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class BakeryProfile:

    NAME = "Bakery"

    DESCRIPTION = (
        "Suitable for residential areas, families, "
        "daily bread buyers and evening snack customers."
    )

    # =====================================================
    # Feature Weights
    # Total = 1.00
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.22,
        "nearby_offices_count": 0.08,
        "nearby_colleges_count": 0.08,
        "nearby_hospitals_count": 0.07,
        "nearby_restaurants_count": 0.10,
        "nearby_shops_count": 0.15,
        "nearby_parks_count": 0.10,
        "avg_income_area": 0.12,
        "rent_estimate": 0.05,
        "distance_to_nearest_brand_chai": 0.03,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 75,
        "nearby_offices_count": 8,
        "nearby_colleges_count": 4,
        "nearby_hospitals_count": 2,
        "nearby_restaurants_count": 10,
        "nearby_shops_count": 15,
        "nearby_parks_count": 3,
        "avg_income_area": 18,
        "rent_estimate": 60,
        "distance_to_nearest_brand_chai": 350,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("footfall_index", 65, "Good daily customer movement."),
        ("nearby_shops_count", 12, "Strong neighborhood shopping activity."),
        ("nearby_parks_count", 2, "Family visitors increase bakery demand."),
        ("avg_income_area", 18, "Residents have good purchasing power."),
        ("nearby_restaurants_count", 8, "Commercial food area attracts visitors."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("footfall_index", 35, "Low daily customer movement."),
        ("nearby_shops_count", 5, "Limited shopping activity."),
        ("avg_income_area", 10, "Lower purchasing power."),
        ("rent_estimate", 90, "High rental cost."),
        ("nearby_restaurants_count", 20, "Strong nearby food competition."),
    ]

    # =====================================================
    # Marketing
    # =====================================================

    MARKETING = [
        "Fresh morning bread offers.",
        "Birthday cake promotions.",
        "Festival special cakes.",
        "Family combo offers.",
        "Online cake ordering.",
        "Weekend bakery discounts.",
        "Loyalty reward cards.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["07:00 - 10:00", "04:00 - 06:00", "06:00 - 09:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "Families",
        "School Children",
        "Office Employees",
        "Residents",
        "Walk-in Customers",
    ]

    # =====================================================
    # Investment
    # =====================================================

    INVESTMENT = {"low": "₹6L - ₹10L", "medium": "₹10L - ₹18L", "high": "₹18L+"}


bakery_profile = BakeryProfile()
