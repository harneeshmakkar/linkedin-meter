from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI
from pydantic import BaseModel


class BullshitAnalysis(BaseModel):
    score: int
    category: str
    reasons: list[str]
    suspicious_phrases: list[str]


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_post(post: str) -> BullshitAnalysis:
    """
    Analyze a LinkedIn post for signs of exaggerated or generic content.
    """

    response = client.responses.parse(
        model="gpt-5.6-luna",
        input=f"""
        Analyze this text as a LinkedIn bullshit detector.

        Text:
        {post}
        """,
        text_format=BullshitAnalysis,
    )

    return response.output_parsed


post = """
I am incredibly humbled and excited to announce that
after countless late nights, our amazing team has achieved
a truly revolutionary milestone. This is just the beginning
of our journey to change the world.
"""


analysis = analyze_post(post)


print(f"Score: {analysis.score}/100")
print(f"Category: {analysis.category}")

print("\nReasons:")
for reason in analysis.reasons:
    print(f"- {reason}")

print("\nSuspicious phrases:")
for phrase in analysis.suspicious_phrases:
    print(f"- {phrase}") 