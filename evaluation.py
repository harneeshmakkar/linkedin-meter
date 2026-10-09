evaluation_dataset = [
    {
        "name": "Concrete operational result",
        "post": """
        We reduced our customer support response time from 18 hours
        to 4 hours over the last six months.

        We did this by introducing automated ticket routing and
        restructuring our support workflow.

        Customer satisfaction increased from 82% to 91%.
        """,
        "expected_min": 0,
        "expected_max": 20
    },

    {
        "name": "Pure corporate hype",
        "post": """
        Today we are thrilled to announce a transformative milestone
        in our mission to redefine the future of business.

        Through relentless innovation and cross-functional collaboration,
        we have unlocked a new era of operational excellence.

        Our platform is empowering organizations to move faster,
        think bigger, and create unprecedented value at scale.

        This is only the beginning.
        """,
        "expected_min": 80,
        "expected_max": 100
    },

    {
        "name": "Evidence-based promotion",
        "post": """
        I'm proud to share that our team has launched our new analytics
        platform after eight months of development.

        The platform is now being used by 27 customers and has reduced
        their weekly reporting time by an average of 35%.

        A big thank you to the engineering, product, and customer success
        teams who made this possible. We're excited to keep improving it
        based on customer feedback.
        """,
        "expected_min": 0,
        "expected_max": 25
    },

    {
        "name": "Buzzword salad",
        "post": """
        We are thrilled to announce a transformative milestone
        in our journey to redefine what's possible.

        Through relentless innovation, strategic alignment,
        and cross-functional collaboration, we are unlocking
        unprecedented value and driving operational excellence
        at scale.

        Our visionary platform empowers organizations to
        accelerate growth, embrace disruption, and create
        meaningful impact.

        The future is here.
        """,
        "expected_min": 80,
        "expected_max": 100
    },

    {
        "name": "Specific personal achievement",
        "post": """
        I completed my first marathon this weekend in 3 hours and 47 minutes.

        I trained for 18 weeks, averaging 42 kilometres per week.
        My previous best was 4 hours and 12 minutes, so I'm especially
        happy with the improvement.

        Thanks to everyone who supported me during training.
        """,
        "expected_min": 0,
        "expected_max": 20
    },

    {
        "name": "Vague leadership announcement",
        "post": """
        Excited to step into a new chapter of leadership.

        I'm incredibly grateful for the opportunity to make a bigger
        impact, inspire teams, and help shape the future of our industry.

        There is so much exciting work ahead.
        """,
        "expected_min": 45,
        "expected_max": 80
    },

    {
        "name": "Numbers-heavy business update",
        "post": """
        We grew monthly recurring revenue from $420K to $610K
        between January and September.

        The biggest driver was expansion within existing accounts,
        which increased from 18% to 31% of monthly revenue.

        We also reduced customer churn from 4.2% to 2.8%.
        """,
        "expected_min": 0,
        "expected_max": 20
    },

    {
        "name": "Inspirational filler",
        "post": """
        Success isn't about having all the answers.

        It's about believing in yourself, embracing challenges,
        and continuing to move forward when the path isn't clear.

        Keep showing up. Keep pushing boundaries.
        Your breakthrough could be just around the corner.
        """,
        "expected_min": 65,
        "expected_max": 100
    },

    {
        "name": "Balanced company update",
        "post": """
        Six months ago we launched our new onboarding process.

        Since then, the average time for a new customer to complete
        setup has fallen from 11 days to 6 days.

        We still have work to do. The biggest remaining issue is
        customers getting stuck during data migration, so that's
        where we're focusing next.
        """,
        "expected_min": 0,
        "expected_max": 25
    },

    {
        "name": "Corporate announcement with little information",
        "post": """
        We are proud to announce an exciting new chapter for our company.

        This milestone represents years of dedication, innovation,
        and an unwavering commitment to excellence.

        Together, we are building a brighter future and creating
        extraordinary opportunities for our customers, partners,
        and community.

        More to come soon.
        """,
        "expected_min": 65,
        "expected_max": 95
    },
]