# Foundations of Omics Study Design, Bias, and Data Interpretation

This interactive workshop spans two days, with 3.5-hour sessions each day. You will gain the skills to design omics experiments that are robust, statistically sound, and analysis-ready even before a single sample is processed. Additionally, you will learn to identify and address bias, detect quality issues, and recognize common pitfalls in data interpretation that can mislead even experienced researchers.

## Why This Course Exists

Most omics training focuses on tools and analysis pipelines — how to process 
sequencing data, run differential expression, interpret a PCA plot. That 
knowledge is valuable, but it arrives too late.

The decisions that most often determine whether an omics study succeeds or 
fails — platform choice, sample size, batch structure, metadata collection — 
are made **before** a single sample is sequenced. Yet there is remarkably 
little structured training that addresses this earlier, more consequential 
stage of the research process.

This course is designed to fill that gap. Rather than starting at the 
computational pipeline, we start at the experimental design — where the 
opportunities to get things right, and the risks of getting them wrong, 
are greatest.

## Who Should Attend

This workshop is designed for researchers who generate or interpret omics data 
but want to strengthen their understanding of experimental design and study 
planning — before the sequencing run begins.

**You will benefit most if you:**

- Work with or plan to use omics technologies (genomics, transcriptomics, 
  proteomics, metabolomics, or related fields)
- Are involved in study design, sample collection, or data interpretation
- Have no prior bioinformatics or programming experience — none is required

## Learning objectives

By the end of this workshop, participants will be able to: 

- Compare major omics technologies and select the most appropriate platform for a given biological question 

- Design an omics experiment that is statistically sound, minimises technical bias, and is fit for downstream bioinformatics analysis — before data is generated 

- Identify and anticipate sources of bias, confounding, and batch effects in experimental setup, and evaluate whether these can be corrected after the fact 

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

## Acknowledgements/citations/credits
Acknowledgements (and co-authorship, where appropriate) are an important way for us to demonstrate the value we bring to your research. Your research outcomes are vital for ongoing funding of the Sydney Informatics Hub and national compute facilities.

## Lead Developer:
Amarinder Singh Thind (Sydney Informatics Hub, University of Sydney)
##

## Suggested acknowledgement
The authors acknowledge the support provided by the Sydney Informatics Hub, a Core Research Facility of the University of Sydney.  

## Cite us to support us!
##
 review checkpoint
