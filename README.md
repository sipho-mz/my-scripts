# scripts_ci_cd_pipeline

__A CI/CD pipeline to validate and check the changes I make to my data-ingestion and data-transformation scripts.__       

## Tools:    
### CI/CD:   
- Github Actions   
   
### Language:   
- Python: Jupyter Notebooks -> *.py via __%%write__
   
### Testing and linting:    
- pytest (example-based testing and termial feedback),     
- ruff (linting and static analysis),       
- Hypothesis (python property-testing package)        

## Repo Status:   
All checks passed:   
![CI](https://github.com/sipho-mz/my-scripts/actions/workflows/ci.yml/badge.svg)
