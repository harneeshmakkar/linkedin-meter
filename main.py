from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI, APIError
from pydantic import BaseModel, Field
from typing import Optional

from evaluation import evaluation_dataset
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

        prompt = build_analysis_prompt

        response = client.responses.parse(
            model="gpt-5.6-luna",
            input=prompt,
            text_format=BullshitAnalysis,
        )

    except APIError as error:
        print(f"\nOpenAI API error: {error}")
        return None

    result = response.output_parsed

    score = calculate_score(result)
    category = calculate_category(score)

    return result, score, category

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



passed_count = 0
failed_count = 0

for test in evaluation_dataset:
    analysis = analyze_post(test["post"])

    if analysis is None:
        print(f"\n{test['name']}")
        print("Unable to analyze this post.")
        failed_count += 1
        continue

    result, score, category = analysis

    passed = (
        test["expected_min"]
        <= score
        <= test["expected_max"]
    )

    print("\n" + "=" * 60)
    print(f"Test: {test['name']}")
    print(f"Actual score: {score}/100")
    print(
        f"Expected range: "
        f"{test['expected_min']}-{test['expected_max']}"
    )
    print(f"Category: {category}")

    if passed:
        print("Result: PASS")
        passed_count += 1
    else:
        print("Result: FAIL")
        failed_count += 1


total_tests = passed_count + failed_count
pass_rate = (passed_count / total_tests) * 100

print("\n" + "=" * 60)
print("Evaluation Summary")
print(f"Total tests: {total_tests}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Pass rate: {pass_rate:.1f}%")