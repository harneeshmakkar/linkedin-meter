from analyzer import analyze_post


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


post = get_post_from_user()

analysis = analyze_post(post)

if analysis is None:
    print("\nAnalysis failed. Please try again.")
else:
    result, score, category = analysis

    print("\n" + "=" * 50)
    print("LINKEDIN BULLSHIT METER")
    print("=" * 50)

    print(f"\nScore: {score}/100")
    print(f"Category: {category}")

    print("\nDimension scores:")
    print(f"  Vagueness: {result.vagueness}/20")
    print(f"  Exaggeration: {result.exaggeration}/20")
    print(f"  Jargon: {result.jargon}/20")
    print(f"  Evidence gap: {result.evidence_gap}/20")
    print(f"  Filler: {result.filler}/20")

    print("\nWhy:")
    for reason in result.reasons:
        print(f"- {reason}")

    print("\nSuspicious phrases:")
    for phrase in result.suspicious_phrases:
        print(f"- {phrase}")