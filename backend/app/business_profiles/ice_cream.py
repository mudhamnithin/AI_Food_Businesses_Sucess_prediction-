"""
=========================================================
Ice Cream Shop Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class IceCreamProfile:

    NAME = "Ice Cream Shop"

    DESCRIPTION = (
        "Suitable for family areas, parks, students, "
        "and high evening customer traffic."
    )

    # =====================================================
    # Feature Weights
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.28,
        "nearby_offices_count": 0.05,
        "nearby_colleges_count": 0.15,
        "nearby_hospitals_count": 0.03,
        "nearby_restaurants_count": 0.10,
        "nearby_shops_count": 0.08,
        "nearby_parks_count": 0.15,
        "avg_income_area": 0.10,
        "rent_estimate": 0.03,
        "distance_to_nearest_brand_chai": 0.03,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 90,
        "nearby_offices_count": 5,
        "nearby_colleges_count": 8,
        "nearby_hospitals_count": 1,
        "nearby_restaurants_count": 10,
        "nearby_shops_count": 10,
        "nearby_parks_count": 4,
        "avg_income_area": 20,
        "rent_estimate": 60,
        "distance_to_nearest_brand_chai": 350,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("footfall_index", 75, "Excellent customer movement."),
        ("nearby_parks_count", 3, "Nearby parks attract families and children."),
        ("nearby_colleges_count", 5, "Good student customer base."),
        ("avg_income_area", 18, "Strong purchasing power."),
        ("nearby_restaurants_count", 8, "Popular food destination."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("footfall_index", 40, "Low customer movement."),
        ("nearby_parks_count", 1, "Limited family recreation nearby."),
        ("nearby_colleges_count", 2, "Limited student customers."),
        ("rent_estimate", 90, "High rental expenses."),
        ("nearby_restaurants_count", 20, "Strong dessert competition."),
    ]

    # =====================================================
    # Marketing
    # =====================================================

    MARKETING = [
        "Family combo offers.",
        "Weekend specials.",
        "Buy 2 Get 1 Free.",
        "Seasonal flavours.",
        "Student discounts.",
        "Festival offers.",
        "Loyalty reward cards.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["04:00 - 06:00", "06:00 - 10:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = ["Families", "Children", "Students", "Young Adults", "Tourists"]

    # =====================================================
    # Investment
    # =====================================================

    INVESTMENT = {"low": "₹5L - ₹10L", "medium": "₹10L - ₹20L", "high": "₹20L+"}


ice_cream_profile = IceCreamProfile()
