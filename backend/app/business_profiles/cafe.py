"""
=========================================================
Cafe Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class CafeProfile:

    NAME = "Cafe"

    DESCRIPTION = (
        "Ideal for students, young professionals, "
        "social gatherings and premium customers."
    )

    # =====================================================
    # Feature Weights
    # Total = 1.00
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.20,
        "nearby_offices_count": 0.15,
        "nearby_colleges_count": 0.25,
        "nearby_hospitals_count": 0.03,
        "nearby_restaurants_count": 0.08,
        "nearby_shops_count": 0.05,
        "avg_income_area": 0.15,
        "rent_estimate": 0.04,
        "distance_to_nearest_brand_chai": 0.05,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 80,
        "nearby_offices_count": 10,
        "nearby_colleges_count": 10,
        "nearby_hospitals_count": 1,
        "nearby_restaurants_count": 12,
        "nearby_shops_count": 10,
        "avg_income_area": 25,
        "rent_estimate": 70,
        "distance_to_nearest_brand_chai": 500,
    }

    # =====================================================
    # Strength Rules
    # =====================================================

    STRENGTHS = [
        ("nearby_colleges_count", 8, "Large student population."),
        ("avg_income_area", 20, "High-income customers nearby."),
        ("footfall_index", 70, "Excellent walk-in customer potential."),
        ("nearby_offices_count", 10, "Office employees support weekday demand."),
        ("distance_to_nearest_brand_chai", 400, "Limited branded cafe competition."),
    ]

    # =====================================================
    # Risk Rules
    # =====================================================

    RISKS = [
        ("nearby_colleges_count", 3, "Limited student customer base."),
        ("avg_income_area", 12, "Lower purchasing power."),
        ("footfall_index", 40, "Low pedestrian traffic."),
        ("rent_estimate", 100, "High rental expenses."),
        ("nearby_restaurants_count", 20, "Strong nearby food competition."),
    ]

    # =====================================================
    # Marketing Suggestions
    # =====================================================

    MARKETING = [
        "Student combo offers.",
        "Free Wi-Fi.",
        "Coffee membership plans.",
        "Instagram-friendly interiors.",
        "Weekend live music events.",
        "Study zone seating.",
        "Digital loyalty rewards.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["09:00 - 11:30", "01:00 - 03:00", "05:00 - 09:00"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "College Students",
        "Young Professionals",
        "Freelancers",
        "Couples",
        "Coffee Enthusiasts",
    ]

    # =====================================================
    # Estimated Investment
    # =====================================================

    INVESTMENT = {"low": "₹8L - ₹12L", "medium": "₹12L - ₹20L", "high": "₹20L+"}


cafe_profile = CafeProfile()
