"""
=========================================================
Action Plan Service

AI Business Growth Action Planner

Version : 1.0
=========================================================
"""


class ActionPlanService:
    """
    AI Business Action Planner
    """

    # =====================================================
    # Generate Action Plan
    # =====================================================

    @staticmethod
    def generate(business):

        # =====================================================
        # Resolve Business Name
        # =====================================================

        if isinstance(business, dict):

            business_name = (

                business.get("business")

                or business.get("business_name")

                or business.get("name")

                or "Business"

            )

        else:

            business_name = getattr(

                business,

                "NAME",

                getattr(

                    business,

                    "business_name",

                    "Business"

                )

            )

        # =====================================================
        # Common Plans
        # =====================================================

        common = {

            "first_30_days": [

                "Complete business registration",

                "Set up Google Business Profile",

                "Install QR payment methods",

                "Hire and train employees",

                "Launch opening offers"

            ],

            "next_90_days": [

                "Build repeat customers",

                "Collect online reviews",

                "Improve customer service",

                "Optimize inventory",

                "Track monthly profit"

            ],

            "next_180_days": [

                "Expand menu",

                "Partner with Swiggy",

                "Partner with Zomato",

                "Launch loyalty program",

                "Increase digital marketing"

            ]

        }

        # =====================================================
        # Business Specific Plans
        # =====================================================

        business_specific = {

            "Tea Shop": [

                "Launch breakfast combo",

                "Corporate tea subscription",

                "Evening snacks",

                "Quick takeaway counter"

            ],

            "Restaurant": [

                "Weekend buffet",

                "Family combo offers",

                "Online delivery",

                "Private party bookings"

            ],

            "Cafe": [

                "Free Wi-Fi",

                "Study zone",

                "Coffee membership",

                "Live music evenings"

            ],

            "Bakery": [

                "Birthday cake orders",

                "Festival specials",

                "Fresh morning bread",

                "Custom cake delivery"

            ],

            "Juice Center": [

                "Healthy detox menu",

                "Seasonal fruit specials",

                "Gym partnerships",

                "Sugar-free options"

            ],

            "Ice Cream": [

                "Family packs",

                "Summer promotions",

                "Weekend offers",

                "Home delivery"

            ],

            "Cloud Kitchen": [

                "Food delivery optimization",

                "Cloud branding",

                "Packaging improvement",

                "Delivery partnerships"

            ]

        }

        # =====================================================
        # Return
        # =====================================================

        return {

            "business": business_name,

            "30_day_plan": common["first_30_days"],

            "90_day_plan": common["next_90_days"],

            "180_day_plan": common["next_180_days"],

            "business_specific": business_specific.get(

                business_name,

                []

            )

        }

    # =====================================================
    # Startup Checklist
    # =====================================================

    @staticmethod
    def startup_checklist():

        return [

            "Business Registration",

            "GST Registration",

            "FSSAI License",

            "Trade License",

            "Fire Safety Certificate",

            "Google Business Profile",

            "UPI Payments",

            "POS Machine",

            "CCTV Installation",

            "Staff Training"

        ]

    # =====================================================
    # Expansion Checklist
    # =====================================================

    @staticmethod
    def expansion_checklist():

        return [

            "Increase seating",

            "Introduce premium menu",

            "Expand staff",

            "Online ordering",

            "Second outlet planning",

            "Customer loyalty program",

            "Business analytics review"

        ]

    # =====================================================
    # Health Check
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Action Plan Service",

            "status": "Running",

            "version": "1.0"

        }


# =====================================================
# Singleton
# =====================================================

action_plan_service = ActionPlanService()