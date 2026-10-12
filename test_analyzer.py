
import unittest

from analyzer import (
    BullshitAnalysis,
    calculate_score,
    calculate_category,
)


class TestScoring(unittest.TestCase):

    def test_calculate_score(self):
        result = BullshitAnalysis(
            vagueness=10,
            exaggeration=5,
            jargon=4,
            evidence_gap=14,
            filler=11,
            reasons=[],
            suspicious_phrases=[],
        )

        self.assertEqual(calculate_score(result), 44)

    def test_minimum_score(self):
        result = BullshitAnalysis(
            vagueness=0,
            exaggeration=0,
            jargon=0,
            evidence_gap=0,
            filler=0,
            reasons=[],
            suspicious_phrases=[],
        )

        self.assertEqual(calculate_score(result), 0)

    def test_maximum_score(self):
        result = BullshitAnalysis(
            vagueness=20,
            exaggeration=20,
            jargon=20,
            evidence_gap=20,
            filler=20,
            reasons=[],
            suspicious_phrases=[],
        )

        self.assertEqual(calculate_score(result), 100)

    def test_category_boundaries(self):
        self.assertEqual(calculate_category(20), "Substantive")
        self.assertEqual(calculate_category(21), "Mostly substantive")
        self.assertEqual(calculate_category(40), "Mostly substantive")
        self.assertEqual(calculate_category(41), "Mixed")
        self.assertEqual(calculate_category(60), "Mixed")
        self.assertEqual(calculate_category(61), "High bullshit")
        self.assertEqual(calculate_category(80), "High bullshit")
        self.assertEqual(calculate_category(81), "Maximum LinkedIn")


if __name__ == "__main__":
    unittest.main()
