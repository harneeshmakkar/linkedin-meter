evaluation_dataset = [
    {
        "name": "Specific cost-saving result",
        "post": """
        We changed our warehouse picking process in March.

        Average order processing time fell from 14 minutes to 9 minutes,
        and picking errors decreased from 3.1% to 1.4% over the next
        three months.

        We achieved this by reorganizing high-volume inventory and
        introducing barcode checks at two stages.
        """,
        "expected_min": 0,
        "expected_max": 20,
    },
    

    {
        "name": "Vague transformation announcement",
        "post": """
        Today marks a defining moment in our evolution.

        We are reimagining what's possible through bold thinking,
        a relentless commitment to excellence, and a shared vision
        for a better tomorrow.

        Together, we are breaking barriers and unlocking new possibilities.
        Stay tuned.
        """,
        "expected_min": 80,
        "expected_max": 100,
    },

    {
        "name": "Promotional post with measurable outcomes",
        "post": """
        Our new scheduling tool launched in April and is now used by
        14 clinics.

        In a six-week pilot, missed appointments fell by 18% compared
        with the previous six weeks. The pilot was small, so we're
        expanding it before drawing broader conclusions.

        Thanks to the clinic teams who helped us test it.
        """,
        "expected_min": 0,
        "expected_max": 25,
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

    {
        "name": "Positive but specific",
        "post": """
        Proud of what the team accomplished this quarter.

        We shipped three major product updates, reduced average
        onboarding time from 9 days to 5 days, and increased
        weekly active users by 17%.

        There is still plenty to improve, but the progress has been
        encouraging.
        """,
        "expected_min": 0,
        "expected_max": 25,
    },

    {
        "name": "Positive but vague",
        "post": """
        What an incredible quarter for the team.

        We pushed ourselves beyond our limits, embraced new challenges,
        and created meaningful momentum across the organization.

        I'm incredibly proud of what we've achieved together and
        excited for everything that's ahead.
        """,
        "expected_min": 45,
        "expected_max": 80,
    },

    {
        "name": "Evidence plus hype",
        "post": """
        I'm thrilled to announce a truly transformational milestone
        for our company.

        Over the past year, our platform has helped 140 businesses
        automate their reporting and collectively save an estimated
        25,000 hours.

        This is a groundbreaking step toward redefining how modern
        organizations operate, and we're only getting started.
        """,
        "expected_min": 30,
        "expected_max": 65,
    },

    {
        "name": "Jargon with real numbers",
        "post": """
        We are excited to accelerate our digital transformation journey
        through a more scalable, data-driven operating model.

        Our new workflow reduced processing time by 32% and increased
        team throughput by 21% during our three-month pilot.

        We're now working on expanding the initiative across the business.
        """,
        "expected_min": 15,
        "expected_max": 45,
    },

    {
        "name": "Very short announcement",
        "post": """
        Excited to announce that we've launched something new.

        More details coming soon!
        """,
        "expected_min": 35,
        "expected_max": 75,
    }
]