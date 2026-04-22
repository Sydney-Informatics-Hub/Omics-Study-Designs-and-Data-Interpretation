# Lesson 1 : The omics landscape

!!! info "Learning objectives"
    By the end of this module, participants will be able to:

    - Identify the seven common failure modes in omics study design
      and classify each by recoverability.
    - Recognise when a platform choice, sample size, or metadata
      decision creates an unrecoverable flaw.
    - Match a biological question to the most suitable omics
      platform and justify that choice.

## The omics landscape​

Modern biology has undergone a fundamental shift from measuring one molecule at a time to profiling entire classes of biological molecules simultaneously. This collective approach, broadly terms "omics" operates across multiple layers of biological organisation, each revealing a different dimension of how living systems function. Every living system, whether it be bacterium, wheat, migratory birds, or people, can be interrogated at the molecular level across these multiple layers so we can understand how they function and respond to their environments. 

These layers have different names, distinct molecular targets, and a distinct set of questions that they can and cannot answer:  

| Layer | Function |
|---|--------------------------|
| **Genomics** | Interrogate DNA blueprint, revealing what an organism can do based on its inherited DNA sequence | 
| **Epigenomics** | Reveals how gene activity is regulated without changes to the underlying sequence |
| **Transcriptomics** | Captures which genes are turned on or off under a given condition | 
| **Proteomics** | Measures the proteins actually present in a cell or tissue |
| **Metabolomics** | Captures small molecule metabolites that are downstream readout of biochemical activity | 

Crucially, no single omics layer tells the complete story; each captures a different molecular dimension of biological systems, and the choice of which layer, or combination of layers, to interrogate is one of the most consequential decisions a researcher will make before an experiment begins.

Each omics layer captures a different molecular dimension of biological systems: 

![](module1/figs/1-1_landscape.png){width=100%}

## From research question to platform: navigating technologies

Each omics domain encompasses a growing ecosystem of platforms and techniques 
and no single approach fits every question. Platforms differ not only in what 
they measure, but in how they measure it, which directly shapes what you can 
and cannot conclude from your data.

At a broad level, omics technologies fall into two methodological families:

- **Sequencing-based approaches** (e.g., DNA-seq, RNA-seq, ATAC-seq) quantify 
  molecules by converting them into readable sequence — offering high throughput 
  and genome-wide coverage.
- **Imaging-based approaches** (e.g., spatial transcriptomics, microscopy-based 
  proteomics) preserve the physical location of molecules within tissue, adding a 
  spatial dimension that sequencing-based methods cannot capture.

The figure below provides an overview of commonly used analysis approaches 
across major omics domains:

![](module1/figs/01_Various_data_analysis_v1.png){width=90%}

<small> Ref: [Satam, Heena, et al. **Biology** 2023
](https://www.mdpi.com/2079-7737/12/7/997){target="_blank"} </small>

TODO replace image with custom diagram as above. 

### What else can 'omics data tell us

Many 'omics pipelines focus on a single primary output (i.e differential gene expression from RNA-seq, variant calling from DNA-seq). The same raw data often contains additional layers of biological information beyond the primary analysis.

A growing set of secondary and emerging analyses can be applied to existing datasets, often without additional sequencing cost. These approaches provide complementary insights and can substantially increase the return on investment from a single experiment.

However, their applicability depends on study design, data quality, and sequencing characteristics (e.g. depth, read length, library preparation), and results should be interpreted with appropriate caution.

Take bulk RNA-seq as an example: beyond standard differential expression, the same dataset can be interrogated for  alternative splicing, RNA editing events, transcript fusions, and more.

![Range of analysis approaches available from a single bulk RNA-seq dataset](module1/figs/01_RNAseq_based_analysis_v1.png){width=90%}

<small>Ref: [Thind et.al. *Briefings in Bioinformatics* 22.6 
(2021).](https://academic.oup.com/bib/article/22/6/bbab259/6330938){target="_blank"}</small>

TODO replace image with custom diagram as above.

??? Activity placeholder 
    Prepare activity that summarises content above. 

---



??? abstract "Further Reading · Emerging Omics Technologies"

    ** Spatial Transcriptomics**
    Entry-level overview, platform comparison, experimental design guidance 
    - [Williams CG et. al *Genome Medicine* 2022](https://link.springer.com/article/10.1186/s13073-022-01075-1){target="_blank"}
     
    spatial + single-cell integration, computational strategies
    - [Vandereyken K et. al *Nature Reviews Genetics* 2023](https://www.nature.com/articles/s41576-023-00580-2){target="_blank"}

    ---

    ** Long-Read Sequencing & Isoform Biology**
    
    Isoform resolution at single-cell level, library prep + bioinformatics
    - [Kumari P et.al 
      *Human Genetics* 2024.](https://link.springer.com/article/10.1007/s00439-024-02678-x){target="_blank"}
    
    Comprehensive guide: tools, applications, challenges
    - [Parker MT et. al *Nature Reviews Genetics* 2025](https://www.nature.com/articles/s41576-025-00828-z){target="_blank"}

    ---
---
