from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI, APIError
from pydantic import BaseModel, Field

from prompts import build_analysis_prompt

class BullshitAnalysis(BaseModel):
    
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


def calculate_category(score: int) -> str:
    if score <= 20:
        return "Substantive"
    elif score <= 40:
        return "Mostly substantive"
    elif score <= 60:
        return "Mixed"
    elif score <= 80:
        return "High bullshit"
    else:
        return "Maximum LinkedIn"


def analyze_post(post: str):

    try:

        prompt = build_analysis_prompt(post)

        response = client.responses.parse(
            model="gpt-5.6-luna",
            input=prompt,
            text_format=BullshitAnalysis
        )

    except APIError as error:
        print(f"\nOpenAI API error: {error}")
        return None

    result = response.output_parsed

    score = calculate_score(result)
    category = calculate_category(score)

    return result, score, category
