
"""
=========================================================
Timeline Service

Business Growth Timeline Generator

Version : 1.0
=========================================================
"""


class TimelineService:

    """
    AI Business Growth Timeline
    """

    # =====================================================
    # Generate Timeline
    # =====================================================

    @staticmethod
    def generate(business):

        if isinstance(business, dict):

            business = business.get(

                "business_name",

                "Business"

            )

        timeline = [

            {
                "phase": "Month 1",
                "title": "Business Setup",
                "activities": [
                    "Complete business registration",
                    "Finalize shop interiors",
                    "Purchase equipment",
                    "Hire initial staff",
                    "Create Google Business Profile"
                ]
            },

            {
                "phase": "Month 2-3",
                "title": "Customer Acquisition",
                "activities": [
                    "Launch opening offers",
                    "Promote on Instagram & Facebook",
                    "Collect Google reviews",
                    "Build repeat customers",
                    "Improve customer service"
                ]
            },

            {
                "phase": "Month 4-6",
                "title": "Business Stabilization",
                "activities": [
                    "Optimize pricing",
                    "Reduce unnecessary expenses",
                    "Increase customer retention",
                    "Track monthly revenue",
                    "Improve inventory management"
                ]
            }

        ]

        if business == "Tea Shop":

            timeline.append({

                "phase": "Month 7-12",

                "title": "Tea Shop Growth",

                "activities": [

                    "Launch breakfast combos",

                    "Introduce evening snacks",

                    "Corporate tea subscriptions",

                    "Festival offers",

                    "Expand takeaway services"

                ]

            })

        elif business == "Restaurant":

            timeline.append({

                "phase": "Month 7-12",

                "title": "Restaurant Expansion",

                "activities": [

                    "Launch buffet",

                    "Partner with Swiggy",

                    "Partner with Zomato",

                    "Private party bookings",

                    "Family combo meals"

                ]

            })

        elif business == "Cafe":

            timeline.append({

                "phase": "Month 7-12",

                "title": "Cafe Growth",

                "activities": [

                    "Coffee membership",

                    "Study zone",

                    "Live music evenings",

                    "Premium beverages",

                    "Loyalty program"

                ]

            })

        elif business == "Bakery":

            timeline.append({

                "phase": "Month 7-12",

                "title": "Bakery Expansion",

                "activities": [

                    "Birthday cake orders",

                    "Festival specials",

                    "Home delivery",

                    "Custom cakes",

                    "Corporate orders"

                ]

            })

        else:

            timeline.append({

                "phase": "Month 7-12",

                "title": "Business Expansion",

                "activities": [

                    "Partner with Swiggy",

                    "Partner with Zomato",

                    "Increase marketing",

                    "Launch loyalty program",

                    "Expand customer base"

                ]

            })

        timeline.append({

            "phase": "Year 2",

            "title": "Long Term Growth",

            "activities": [

                "Open second branch",

                "Expand product range",

                "Hire additional employees",

                "Increase digital marketing",

                "Improve customer experience"

            ]

        })

        return timeline
        # =====================================================
    # Milestones
    # =====================================================

    @staticmethod
    def milestones():

        return [

            "Business Launch",

            "100 Customers",

            "500 Customers",

            "1000 Customers",

            "Break-even",

            "Monthly Profit",

            "Second Branch"

        ]

    # =====================================================
    # Health
    # =====================================================

    @staticmethod
    def health():

        return {

            "service": "Timeline Service",

            "status": "Running",

            "version": "1.0"

        }
timeline_service = TimelineService()