#!/usr/bin/env python3
"""
Quick pairwise relationship check between two variables.
Usage: python quick_relationship_check.py "treatment variable" "outcome variable"
"""

import sys
import logging
from causal import ModelSuggester

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    if len(sys.argv) < 3:
        print("Usage: python quick_relationship_check.py 'treatment' 'outcome'")
        print("Example: python quick_relationship_check.py 'smoking' 'lung cancer'")
        sys.exit(1)

    treatment = sys.argv[1]
    outcome = sys.argv[2]

    logger.info(f"Analyzing causal relationship: {treatment} → {outcome}")

    # Initialize modeler
    modeler = ModelSuggester('gpt-5.1-mini')

    # Generate domain experts
    factors = [treatment, outcome]
    experts = modeler.suggest_domain_expertises(factors, n_experts=3)
    logger.info(f"Domain experts: {experts}")

    # Check relationship
    result = modeler.suggest_pairwise_relationship(experts, treatment, outcome)

    print("\n" + "="*60)
    print(f"CAUSAL RELATIONSHIP ANALYSIS")
    print("="*60)
    print(f"Treatment: {treatment}")
    print(f"Outcome: {outcome}")
    print(f"Experts: {', '.join(experts)}")
    print("\nResult:")
    print(result)
    print("="*60)


if __name__ == "__main__":
    main()
