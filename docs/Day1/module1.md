# Module 1 : The Omics Landscape and Why Studies Fail

!!! info "Learning objectives" 
    - By the end of this module, participants will be able to:
        - Match a biological question to the most suitable omics platform and justify that choice.
        - Get to know poor experiment design and what they may miss
        - What kind of experiemental issues are hard to overcome later on. 

## The omics landscape​

- Overview of major omics types: genomics, bulk transcriptomics, single-cell transcriptomics, proteomics, metabolomics,
metagenomics​

Each 'omics' layer captures a different molecular dimension of biological systems

![](module1/figs/01_Omics_types_v1.png){width=90%}

Ref: [New diagnostic molecular markers and biomarkers in odontogenic tumors." Molecular biology reports 48.4 (2021): 3617-3628.](https://link.springer.com/article/10.1007/s11033-021-06286-0)

# Standard Downstream Analyses for Various Omics

For each omics domain (e.g., genomics, transcriptomics, epigenomics, proteomics), a wide range of platforms and techniques are available. Each has its own advantages, limitations, and suitability depending on the biological question and sample type.

Some approaches are imaging-based (e.g., spatial transcriptomics, microscopy-based proteomics), while others are sequencing-based (e.g., DNA-seq, RNA-seq). Additionally, library preparation protocols can perform differently depending on tissue type, input quality, and preservation method (e.g., fresh vs FFPE).

## Key Considerations When Choosing a Platform

- What biological question are you addressing?

        - Variant detection (e.g., SNPs, indels)

        - Differential expression (DEG analysis)

        - DNA methylation or other epigenetic modifications

        - Structural variation or copy number alterations

- What level of coverage is required?

        - Whole transcriptome vs gene panels

        - Whole exome sequencing (WES) vs whole genome sequencing (WGS)

- What is the expected accuracy and resolution?

        - For example, copy number alteration (CNA) detection is generally more robust using WGS than WES, and RNA-seq–based CNA inference is indirect and less reliable.

        - Similarly, variant calling accuracy differs across platforms and depths.

- What are the sample constraints?

        - Tissue preservation method (e.g., FFPE vs fresh frozen)

        - RNA/DNA quality and quantity

        - Compatibility of protocols with specific sample types

- Are short-read technologies sufficient?

        - Short-read sequencing (e.g., Illumina) is effective for many applications

        - Long-read technologies (e.g., PacBio, Oxford Nanopore) are preferable for:

            - Structural variant detection

            - Isoform resolution

            - Complex genomic regions

- Is spatial or single-cell resolution required?

    - Bulk omics may mask cellular heterogeneity

    - Single-cell or spatial methods may be necessary for certain biological questions

## Study Context Matters

- Clinical studies typically require:

    - High accuracy, reproducibility, and validation

    - Standardised and regulatory-compliant methods

- Exploratory research studies may prioritise:

    - Broader coverage

    - Novel discovery potential

    - Cost-effectiveness, even if some methods are less precise

# Here is an overview of some standard analysis currently used in omics studies:


![](module1/figs/01_Various_data_analysis_v1.png){width=90%}

Ref: [Next-generation sequencing technology: current trends and advancements." Biology 12.7 (2023): 997.
](https://www.mdpi.com/2079-7737/12/7/997)


Apart from standard analysis used by majority of reseach studies, there is possibility to perform some less popular analyses, which has the potential to provide extra information at no cost of sequencing. They provide, new angle how we think generally for e..g RNAdeq.

- Here is an example of a range of possible analysis based on total bulk RNAseq, 

![](module1/figs/01_RNAseq_based_analysis_v1.png){width=90%}

Ref: [Demystifying emerging bulk RNA-Seq applications: the application and utility of bioinformatic methodology. Briefings in bioinformatics 22.6 (2021).
](https://academic.oup.com/bib/article/22/6/bbab259/6330938)
​
Other useful links about growing omics techniques and methods:
1) Spatial omics (xenium)? 
2) Long read based single cell  RNA-Seq : https://link.springer.com/article/10.1007/s00439-024-02678-x 
3) Spatial Proteomics/epigenomics etc
4) other exampless???

# When Omics Studies Fail — and Why It Matters


Despite rapid advances in omics technologies, not all studies succeed. In fact, omics studies can fail at multiple stages — from experimental design to data analysis and interpretation.

## The Cost Reality

Omics experiments are expensive in terms of:

    Financial cost (sequencing, reagents, platforms)

    Time investment (sample processing, analysis, validation)

    Irreplaceable samples (e.g., clinical biopsies, rare cohorts)

Failures are therefore not just technical — they represent lost opportunities that often cannot be recovered.

Three Common Categories of Failure
1) Studies That Cannot Be Analysed

These are datasets that become unusable due to fundamental issues:

Poor sample quality (e.g., degraded RNA from FFPE without proper QC)

Missing or inconsistent metadata

Batch effects that are completely confounded with biological groups

Incompatible or failed library preparation

👉 Outcome: Data exists, but meaningful analysis is not possible.

2) Studies That Produce Misleading Results

These studies generate results — but the conclusions are incorrect or biased:

Batch effects mistaken for biology

Inappropriate normalisation methods (e.g., applying microarray-style methods like quantile normalisation to RNA-seq)

Underpowered sample sizes leading to false positives/negatives

Platform limitations not considered (e.g., inferring CNAs from RNA-seq without validation)

👉 Outcome: Results look convincing but are scientifically unreliable.

3) Studies That Cannot Be Published or Reproduced

Even technically sound studies may fail at the final stage:

Lack of reproducibility (missing code, undocumented pipelines)

Poor statistical design or insufficient validation

Incomplete reporting of methods or metadata

Failure to meet journal or regulatory standards

👉 Outcome: Data and results exist but cannot be trusted, shared, or published.

## Why Do These Failures Happen?

Most failures trace back to decisions made early in the study design phase, including:

Misalignment between biological question and chosen technology

Lack of statistical planning (e.g., no power calculation)

Ignoring sample and batch structure

Underestimating data complexity and analysis requirements

## Real-World Examples (Commonly Observed Issues)

- Batch-confounded clinical cohorts

Cases and controls processed in different batches → impossible to disentangle biology from technical effects

- Underpowered discovery studies

Too few samples → unstable differential expression or variant associations

- Lost or incomplete metadata

Missing sample annotations → unusable datasets despite high-quality sequencing

- Technology mismatch

Using short-read sequencing for problems requiring long-read resolution (e.g., structural variants, isoforms)


## Real-world documented examples — batch-confounded clinical cohorts, underpowered discovery studies, lost metadata

## Example of studies with in appropriate study design 

## What cannot be fixed after data generation​​

Batch fully correlated with biological groups — the two signals cannot be separated​​
Insufficient sample size for the question being asked​​
Missing or unrecorded metadata​​
Wrong omics platform chosen for the question​​
Samples pooled where individual-level inference was needed

## Example: of what can be often be missed
- Consideration of reproducibility in aging research :
- Sample size considerations: https://www.ohsu.edu/sites/default/files/2024-02/pss4omics.pdf 

 ## Activity : 
 - Briefly describe a study you are planning or have been involved in.
 - In small groups, identify one design risk. 
 - We will records risks on a whiteboard — revisit at the end of the day to check which modules addressed each one.