# Foundations of Omics Study Design, Bias, and Data Interpretation
 

## Pre-requisites 
-  No progrsmming skills are required

## Learning objectives

By the end of this workshop, participants will be able to: 

- Compare major omics technologies and select the most appropriate platform for a given biological question 

- Design an omics experiment that is statistically sound, minimises technical bias, and is fit for downstream bioinformatics analysis — before data is generated 

- Identify and anticipate sources of bias, confounding, and batch effects in their own experimental setup, and evaluate whether these can be corrected after the fact 

- Interpret key QC and exploratory visualisations (PCA, UMAP) correctly, and avoid the most common misinterpretation traps 

- Select appropriate normalisation and batch correction strategies for their omics data type and study design 

# For developers 

To render docs: 

1. Install mkdocs

```
pip install mkdocs
mkdocs --version # confirm install
```

2. Render docs locally at http://127.0.0.1:8000/: 

```
mkdocs serve
```

All content merged to main will be rendered at github.io pages by [`mkdocs_deploy.yml`](https://github.com/Sydney-Informatics-Hub/nextflow-hpc-workshop/blob/main/.github/workflows/mkdocs_deploy.yml) github action.  