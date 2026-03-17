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

## Standard Downstream Analyses for various omics

For each omics there are range of platforms and techiques are available each one of those has its own advatages and disadvantages. 
Some of those method are images based, other are sequencing based ? Some library prep works better with one tissue other may suffer issues.


- When to choose one platform over another based on the biological question​? 
- Examples includes :

    - 1) What analysis are you after? mutations/DEG/Methylation
    - 2) Do I need whole Genome/transcriptomics? or WES/target panel is enough?
    - 3) establish accuarcy of one omics over other? e.g. Copy number alteration (CNA) analysis using WGS/WES vs total RNAseq ? 
    - 4) If tissue preservation is suitbale for one technique but not for other.
    - 5) Can we capture all biology with short read? or need long read method? e.g. structural variant analysis.
    - 6) 

Clinical focused study need more accurate method, while exploratory study allowed to use less accuracy methods with certain advantages.

Here is an overview of some standard analysis currently used in omics studies:


![](module1/figs/01_Various_data_analysis_v1.png){width=90%}

Ref: [Next-generation sequencing technology: current trends and advancements." Biology 12.7 (2023): 997.
](https://www.mdpi.com/2079-7737/12/7/997)

Apart from standard analysis used by majority of reseach studies, there is possibility to perform some less popular analyses, which has the potential to provide extra information at no cost of sequencing. They provide, new angle how we think generally for e..g RNAdeq.

​
## Why studies fail​

The cost reality: omics experiments are expensive in time, money, and irreplaceable samples​

Three categories of failure: studies that cannot be analysed, results that mislead, and data that cannot be published​

Real-world documented examples — batch-confounded clinical cohorts, underpowered discovery studies, lost metadata

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