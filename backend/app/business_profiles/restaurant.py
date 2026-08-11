"""
=========================================================
Restaurant Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class RestaurantProfile:

    NAME = "Restaurant"

    DESCRIPTION = (
        "Suitable for commercial areas with high "
        "footfall, office employees and families."
    )

    # =====================================================
    # Feature Weights
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.28,
        "nearby_offices_count": 0.18,
        "nearby_colleges_count": 0.08,
        "nearby_hospitals_count": 0.08,
        "nearby_restaurants_count": 0.10,
        "nearby_shops_count": 0.07,
        "nearby_parks_count": 0.05,
        "avg_income_area": 0.12,
        "rent_estimate": 0.02,
        "distance_to_nearest_brand_chai": 0.02,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 90,
        "nearby_offices_count": 20,
        "nearby_colleges_count": 5,
        "nearby_hospitals_count": 3,
        "nearby_restaurants_count": 15,
        "nearby_shops_count": 12,
        "nearby_parks_count": 2,
        "avg_income_area": 22,
        "rent_estimate": 80,
        "distance_to_nearest_brand_chai": 250,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("footfall_index", 75, "Excellent customer movement."),
        ("nearby_offices_count", 15, "Strong office lunch crowd."),
        ("avg_income_area", 18, "Customers can afford premium dining."),
        ("nearby_restaurants_count", 8, "Established food destination."),
        ("nearby_shops_count", 10, "Commercial shopping activity."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("footfall_index", 45, "Low pedestrian traffic."),
        ("nearby_offices_count", 5, "Limited office customers."),
        ("avg_income_area", 12, "Lower customer spending power."),
        ("rent_estimate", 100, "High rental expenses."),
        ("nearby_restaurants_count", 25, "Very strong restaurant competition."),
    ]

    # =====================================================
    # Marketing
    # =====================================================

    MARKETING = [
        "Family combo meals.",
        "Weekend buffet.",
        "Corporate lunch packages.",
        "Online food delivery.",
        "Festival special menu.",
        "Loyalty membership.",
        "Birthday party packages.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["12:00 - 03:00", "07:00 - 10:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "Office Employees",
        "Families",
        "Students",
        "Tourists",
        "Walk-in Customers",
    ]

    # =====================================================
    # Investment
    # =====================================================

    INVESTMENT = {"low": "₹15L - ₹25L", "medium": "₹25L - ₹50L", "high": "₹50L+"}


restaurant_profile = RestaurantProfile()
