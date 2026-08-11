"""
=========================================================
Tea Shop Business Profile

Business Recommendation Engine

Version : 3.0.0
=========================================================
"""


class TeaShopProfile:

    NAME = "Tea Shop"

    DESCRIPTION = (
        "Suitable for office employees, students, "
        "hospital visitors and walk-in customers."
    )

    # =====================================================
    # Feature Weights
    # Total = 1.00
    # =====================================================

    WEIGHTS = {
        "footfall_index": 0.30,
        "nearby_offices_count": 0.25,
        "nearby_colleges_count": 0.10,
        "nearby_hospitals_count": 0.15,
        "nearby_restaurants_count": 0.05,
        "nearby_shops_count": 0.05,
        "avg_income_area": 0.05,
        "rent_estimate": 0.03,
        "distance_to_nearest_brand_chai": 0.02,
    }

    # =====================================================
    # Ideal Values
    # =====================================================

    IDEAL = {
        "footfall_index": 85,
        "nearby_offices_count": 18,
        "nearby_colleges_count": 5,
        "nearby_hospitals_count": 3,
        "nearby_restaurants_count": 8,
        "nearby_shops_count": 12,
        "avg_income_area": 18,
        "rent_estimate": 55,
        "distance_to_nearest_brand_chai": 400,
    }

    # =====================================================
    # Strength Conditions
    # =====================================================

    STRENGTHS = [
        ("footfall_index", 70, "Excellent pedestrian movement."),
        ("nearby_offices_count", 15, "Large office employee population."),
        ("nearby_colleges_count", 4, "Strong student customer base."),
        ("nearby_hospitals_count", 2, "Hospital visitors create regular demand."),
        ("distance_to_nearest_brand_chai", 300, "Limited branded tea competition."),
        ("rent_estimate", 60, "Affordable rental cost."),
    ]

    # =====================================================
    # Risk Conditions
    # =====================================================

    RISKS = [
        ("footfall_index", 40, "Low customer footfall."),
        ("nearby_offices_count", 5, "Limited office customers."),
        ("nearby_restaurants_count", 20, "High food competition."),
        ("rent_estimate", 90, "High rental expenses."),
        ("distance_to_nearest_brand_chai", 150, "Nearby branded tea competitor."),
    ]

    # =====================================================
    # Marketing Suggestions
    # =====================================================

    MARKETING = [
        "Corporate tea subscription plans.",
        "Morning breakfast combos.",
        "Evening snack offers.",
        "Student combo discounts.",
        "Digital loyalty rewards.",
        "QR-based payment cashback.",
        "Quick takeaway counter.",
    ]

    # =====================================================
    # Peak Hours
    # =====================================================

    PEAK_HOURS = ["07:30 - 10:00", "12:30 - 03:00", "05:00 - 08:30"]

    # =====================================================
    # Target Customers
    # =====================================================

    TARGET_CUSTOMERS = [
        "Office Employees",
        "Students",
        "Hospital Visitors",
        "Shop Owners",
        "Walk-in Customers",
    ]

    # =====================================================
    # Estimated Investment
    # =====================================================

    INVESTMENT = {"low": "₹3L - ₹5L", "medium": "₹5L - ₹8L", "high": "₹8L+"}


tea_shop_profile = TeaShopProfile()
