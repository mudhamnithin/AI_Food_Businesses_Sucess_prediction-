"""
=========================================================
Cloud Kitchen Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class CloudKitchenProfile:

    NAME = "Cloud Kitchen"

    DESCRIPTION = (
        "Suitable for online food delivery businesses "
        "serving nearby residential and office customers."
    )

    # =====================================================
    # Feature Weights
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.10,
        "nearby_offices_count": 0.22,
        "nearby_colleges_count": 0.12,
        "nearby_hospitals_count": 0.08,
        "nearby_restaurants_count": 0.15,
        "nearby_shops_count": 0.08,
        "nearby_parks_count": 0.02,
        "avg_income_area": 0.10,
        "rent_estimate": 0.10,
        "distance_to_nearest_brand_chai": 0.03,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 50,
        "nearby_offices_count": 18,
        "nearby_colleges_count": 6,
        "nearby_hospitals_count": 2,
        "nearby_restaurants_count": 12,
        "nearby_shops_count": 10,
        "nearby_parks_count": 1,
        "avg_income_area": 20,
        "rent_estimate": 40,
        "distance_to_nearest_brand_chai": 250,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("nearby_offices_count", 15, "Strong office delivery demand."),
        ("nearby_restaurants_count", 8, "Established food delivery market."),
        ("avg_income_area", 18, "Customers have good purchasing power."),
        ("rent_estimate", 50, "Affordable operating cost."),
        ("nearby_colleges_count", 5, "Students support online ordering."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("nearby_offices_count", 5, "Limited office delivery demand."),
        ("avg_income_area", 10, "Lower spending capacity."),
        ("rent_estimate", 90, "High operational cost."),
        ("nearby_restaurants_count", 25, "Strong food delivery competition."),
        ("footfall_index", 20, "Weak local commercial activity."),
    ]

    # =====================================================
    # Marketing
    # =====================================================

    MARKETING = [
        "Swiggy & Zomato promotions.",
        "Free delivery offers.",
        "Online combo meals.",
        "Subscription meal plans.",
        "Late-night delivery.",
        "Festival offers.",
        "Corporate lunch packages.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["12:00 - 03:00", "07:00 - 11:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "Office Employees",
        "Students",
        "Families",
        "Online Customers",
        "Night-time Customers",
    ]

    # =====================================================
    # Investment
    # =====================================================

    INVESTMENT = {"low": "₹8L - ₹15L", "medium": "₹15L - ₹30L", "high": "₹30L+"}


cloud_kitchen_profile = CloudKitchenProfile()
