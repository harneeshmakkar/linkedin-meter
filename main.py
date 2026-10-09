from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI, APIError
from pydantic import BaseModel, Field
from typing import Optional


class BullshitAnalysis(BaseModel):
    score: int = Field(ge=0, le=100)
    category: str

    vagueness: int = Field(ge=0, le=20)
    exaggeration: int = Field(ge=0, le=20)
    jargon: int = Field(ge=0, le=20)
    evidence_gap: int = Field(ge=0, le=20)
    filler: int = Field(ge=0, le=20)

    reasons: list[str]
    suspicious_phrases: list[str]


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def calculate_score(result: BullshitAnalysis) -> int:
    return (
        result.vagueness
        + result.exaggeration
        + result.jargon
        + result.evidence_gap
        + result.filler
    )

def analyze_post(post: str) -> Optional[BullshitAnalysis]:

    try:
        response = client.responses.parse(
            model="gpt-5.6-luna",
            input=f"""
            You are a LinkedIn Bullshit Meter.

            Your job is to estimate how much rhetorical hype, vagueness, and
            low-information language exists in a LinkedIn post.

            Evaluate the post using these five dimensions.

            1. Vagueness (0-20)
            How vague are the claims?
            0 = highly specific and concrete
            20 = almost entirely vague

            2. Exaggeration (0-20)
            How inflated or over-the-top is the language?
            0 = neutral and proportional
            20 = extreme hype and exaggeration

            3. Corporate jargon (0-20)
            How much does the post rely on impressive-sounding but
            low-information corporate language?
            0 = clear, natural language
            20 = heavily dependent on corporate buzzwords

            4. Evidence gap (0-20)
            How much are important claims unsupported by numbers,
            examples, outcomes, or other concrete evidence?
            0 = claims are well supported
            20 = major claims have almost no supporting evidence

            5. Filler / self-congratulation (0-20)
            How much of the post consists of emotional, inspirational,
            or self-congratulatory language rather than useful information?
            0 = almost no filler
            20 = mostly filler

            The overall bullshit score MUST be the sum of the five
            dimension scores and therefore range from 0 to 100.

            Use these overall categories:

            0-20: Substantive
            21-40: Mostly substantive
            41-60: Mixed
            61-80: High bullshit
            81-100: Maximum LinkedIn

            Important:
            Do not punish a post simply because it is positive or enthusiastic.
            Concrete achievements supported by specific numbers, outcomes,
            customers, examples, or evidence should reduce the bullshit score.

            Analyze the following LinkedIn post:

            {post}
            """,
            text_format=BullshitAnalysis,
        )

    except APIError as error:
        print(f"\nOpenAI API error: {error}")
        return None

    result = response.output_parsed

    result.score = calculate_score(result)

    return result

def get_post_from_user() -> str:
    print("Paste a LinkedIn post below.")
    print("When finished, type DONE on a new line.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "DONE":
            break

        lines.append(line)

    return "\n".join(lines)



test_posts = [
    """
    We reduced our customer support response time from 18 hours
    to 4 hours over the last six months.

    We did this by introducing automated ticket routing and
    restructuring our support workflow.

    Customer satisfaction increased from 82% to 91%.
    """,

    """
    I am incredibly humbled and excited to announce that after
    countless late nights, our amazing team has achieved a truly
    revolutionary milestone.

    This is just the beginning of our journey to change the world.
    """,

    """
    I'm proud to share that our team has launched our new analytics platform
    after eight months of development.

    The platform is now being used by 27 customers and has reduced their
    weekly reporting time by an average of 35%.

    A big thank you to the engineering, product, and customer success teams
    who made this possible. We're excited to keep improving it based on
    customer feedback.
    """,

    """
    Today we are thrilled to announce a transformative milestone
    in our mission to redefine the future of business.

    Through relentless innovation and cross-functional collaboration,
    we have unlocked a new era of operational excellence.

    Our platform is empowering organizations to move faster,
    think bigger, and create unprecedented value at scale.

    This is only the beginning.
    """
]


for post in test_posts:
    analysis = analyze_post(post)

    if analysis is None:
        print("Unable to analyze this post.")
        continue

    print("\n" + "=" * 60)
    print(f"Score: {analysis.score}/100")
    print(f"Category: {analysis.category}")

    print(f"Vagueness: {analysis.vagueness}/20")
    print(f"Exaggeration: {analysis.exaggeration}/20")
    print(f"Corporate jargon: {analysis.jargon}/20")
    print(f"Evidence gap: {analysis.evidence_gap}/20")
    print(f"Filler: {analysis.filler}/20")