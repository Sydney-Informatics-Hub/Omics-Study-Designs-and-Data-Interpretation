# Foundations of omics study design, bias, and data interpretation

This interactive workshop spans two days, with 3.5 hour sessions each day. Users will gain the skills to design omics studies that are robust, statistically sound, and analysis ready even before a single sample is processed. Additionally, they will learn to identify and address bias, detect quality issues, and recognize common pitfalls in data.

## Why this course exists

Most omics training focuses on tools and analysis pipelines; how to process 
sequencing data, run differential expression or similar. That 
knowledge is valuable, but it arrives too late.

The decisions that most often determine whether an omics study succeeds or 
fails: platform choice, sample size, batch structure, metadata collection 
are made **before** running samples. Yet there is remarkably 
little structured training that addresses this earlier, more consequential 
stage of the research process.

This course is designed to fill that gap. Rather than starting at the 
computational pipeline, we start at the study design, where the 
opportunities to get things right, and the risks of getting them wrong, 
are greatest.

## Who should attend

This workshop is designed for researchers who generate or interpret omics data 
but want to strengthen their understanding of experimental design and study 
planning before the sample processing begins.

**Reseachers will benefit most if they:**

- Work with or plan to use omics technologies (genomics, transcriptomics, 
  proteomics, metabolomics, or related fields)
- Are involved in study design, sample collection, or data interpretation
- Have no prior bioinformatics or programming experience
  
## Learning objectives

### Module 1: The omics landscape and where studies go wrong
* Match a biological question to the molecular layer that can answer it
* Recognise the common design pitfalls at each stage of a study
* Classify a design weakness as recoverable, limitable, or fatal
* Identify the true unit of replication, and spot pseudoreplication from subsampling or pooling

### Module 2: Experimental design fundamentals for omics
* Decide whether a source of variation calls for blocking, randomisation, or recording 
* Choose a platform that can physically capture the signal of interest, and recognise when one cannot
* Explain what drives sample size in omics: effect size, biological variability, and the multiple-testing burden
* Distinguish what depth buys (detection) from what replication buys (power), and allocate a fixed budget between them
* Draft a minimal metadata checklist for their own project

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

## Developers
- Amarinder Singh Thind
- Georgie Samaha
- Mitchell O'Brien


## Suggested acknowledgement
The authors acknowledge the support provided by the Sydney Informatics Hub, a Core Research Facility of the University of Sydney.  

## Cite us to support us!
##
 
