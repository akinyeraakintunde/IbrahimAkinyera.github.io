"""
Demo script for NxtAbroad AI Core.

Loads sample leads from data/sample_leads.csv,
runs them through the rules engine and lead scorer,
and prints a simple report.
"""

import csv
from pathlib import Path

from nxtabroad_ai_core import EligibilityRulesEngine, LeadScorer


DATA_PATH = Path(__file__).parent / "data" / "sample_leads.csv"


def main() -> None:
    engine = EligibilityRulesEngine()
    scorer = LeadScorer(engine)

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Could not find sample data at {DATA_PATH}")

    with DATA_PATH.open(newline="") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            result = scorer.score_lead(row)
            print("-" * 60)
            print(f"Lead #{idx}")
            print(f"Country: {row.get('country')} | Programme: {row.get('programme_level')}")
            print(f"Score: {result.score} / 100 | Risk: {result.risk_label} | Eligible: {result.is_eligible}")
            print("Reasons:")
            for exp in result.explanations:
                print(f"  - {exp}")


if __name__ == "__main__":
    main()