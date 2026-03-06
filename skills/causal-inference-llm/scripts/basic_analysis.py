#!/usr/bin/env python3
"""
Basic causal analysis example script.
Usage: python basic_analysis.py
"""

import asyncio
import logging
from causal import ModelSuggester, plot_interactive_graph
import networkx as nx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    # Initialize modeler with LLM
    modeler = ModelSuggester('gpt-5.1-mini')

    # Define variables
    all_factors = ["smoking", "lung cancer", "air pollution exposure", "genetic predisposition"]
    treatment = "smoking"
    outcome = "lung cancer"

    # Step 1: Get domain expertise
    logger.info("Step 1: Identifying domain experts...")
    domain_expertises = modeler.suggest_domain_expertises(all_factors, n_experts=3)
    logger.info(f"Domain experts: {domain_expertises}")

    # Step 2: Discover latent confounders
    logger.info(f"\nStep 2: Discovering latent confounders between '{treatment}' and '{outcome}'...")
    _, latent_confounders = modeler.suggest_latent_confounders(treatment, outcome, domain_expertises)
    logger.info(f"Latent confounders: {latent_confounders}")

    # Step 3: Build complete factor list
    all_factors += latent_confounders
    all_factors = list(set([f.lower() for f in all_factors]))
    logger.info(f"\nStep 3: Complete factor list: {all_factors}")

    # Step 4: Discover pairwise relationships
    logger.info("\nStep 4: Analyzing pairwise causal relationships...")
    pairwise_edges = await modeler._suggest_pairwise_relationships(
        expert=str(domain_expertises),
        all_factors=all_factors,
        analysis_context="medical causal model"
    )

    logger.info("\nDiscovered causal relationships:")
    for edge, (confidence, _) in pairwise_edges.items():
        source, target = edge
        logger.info(f"  {all_factors[source]} → {all_factors[target]} (confidence: {confidence})")

    # Step 5: Build and visualize graph
    logger.info("\nStep 5: Building causal graph...")
    G = nx.MultiDiGraph()

    for idx, label in enumerate(all_factors):
        G.add_node(idx, desc=label)

    for edge, (confidence, thinking) in pairwise_edges.items():
        G.add_edge(edge[0], edge[1], relationship=confidence, thinking=thinking)

    output_file = "causal_graph.html"
    plot_interactive_graph(G, filename=output_file)
    logger.info(f"\nInteractive graph saved to: {output_file}")


if __name__ == "__main__":
    asyncio.run(main())
