# scripts_ci_cd_pipeline

A CI/CD pipeline to validate and check the changes I make to my data-ingestion and data-transformation scripts.

Tools:
CI/CD: Github Actions
Language: Jupyter Notebooks -> Python Scripts via %%write
Testing and linting: pytest (example-based testing and termial feedback), 
                     ruff (linting and static analysis), 
                     Hypothesis (python property-testing package)

All checks passed: ![CI](https://github.com/sipho-mz/my-scripts/actions/workflows/ci.yml/badge.svg)
