from analyzer import analyze_post
from evaluation import evaluation_dataset



def calculate_range_distance(
    score: int,
    expected_min: int,
    expected_max: int,
) -> int:

    if score < expected_min:
        return expected_min - score

    if score > expected_max:
        return score - expected_max

    return 0



passed_count = 0
failed_count = 0
total_distance = 0

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

    distance = calculate_range_distance(
        score,
        test["expected_min"],
        test["expected_max"],
    )

    total_distance += distance

    print("\n" + "=" * 60)
    print(f"Test: {test['name']}")
    print(f"Actual score: {score}/100")
    
    print("Dimension scores:")
    print(f"  Vagueness: {result.vagueness}/20")
    print(f"  Exaggeration: {result.exaggeration}/20")
    print(f"  Jargon: {result.jargon}/20")
    print(f"  Evidence gap: {result.evidence_gap}/20")
    print(f"  Filler: {result.filler}/20")

    print(
        f"Expected range: "
        f"{test['expected_min']}-{test['expected_max']}"
    )
    print(f"Category: {category}")
    print(f"Distance from expected range: {distance}")

    if passed:
        print("Result: PASS")
        passed_count += 1
    else:
        print("Result: FAIL")
        failed_count += 1


total_tests = passed_count + failed_count
pass_rate = (passed_count / total_tests) * 100
average_distance = total_distance / total_tests

print("\n" + "=" * 60)
print("Evaluation Summary")
print(f"Total tests: {total_tests}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Pass rate: {pass_rate:.1f}%")
print(f"Average distance from expected range: {average_distance:.1f}")