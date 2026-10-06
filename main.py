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


response = client.responses.parse(
    model="gpt-5.6-luna",
    input="""
    Analyze this text as a LinkedIn bullshit detector.

    Text:
    "I am incredibly humbled and excited to announce that
    after countless late nights, our amazing team has achieved
    a truly revolutionary milestone. This is just the beginning
    of our journey to change the world."
    """,
    text_format=BullshitAnalysis,
)


analysis = response.output_parsed

print(f"Score: {analysis.score}/100")
print(f"Category: {analysis.category}")

print("\nReasons:")
for reason in analysis.reasons:
    print(f"- {reason}")

print("\nSuspicious phrases:")
for phrase in analysis.suspicious_phrases:
    print(f"- {phrase}")