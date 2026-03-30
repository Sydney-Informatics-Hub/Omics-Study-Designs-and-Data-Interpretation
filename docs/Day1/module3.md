# Module 3 — Experimental Design Fundamentals for Omics
!!! info "Learning objectives"
    - Define randomisation in the context of omics (processing order, plate position, library batch, sequencing lane) and explain how poor randomisation can act as biological signal.
    -Participants will be able to:
        - Distinguish biological replicates from technical replicates and explain the specific consequence of pseudoreplication — particularly in single-cell contexts — on the validity of statistical claims.
        - Explain why rich, well-structured metadata (biological and technical) is crucial for later bias detection and confounder adjustment, and draft a minimal metadata checklist for their own project. and explain why an unrecorded variable cannot be tested as a confounder.
        - Explain blocking as a design strategy and evaluate why prospective blocking is more reliable than post-hoc batch correction, including situations where correction is impossible.
​

    -- How to design around it — pseudobulk, mixed models
    -- How randomisation prevents it, blocking strategies
    -- Temperature gradient figure - spatial/temporal randomisation mechanics
    -- What to record, minimal metadata checklist
    -- How to do power calculations
    -- How to design replicate structure correctly


Following figure shows randomization of biological replicates across space, time, and batches can reduce experimental bias.

![Batch effect fully confounded with Biology](module1/figs/02_batch_Effect_v02.png){width=90%}

<small>Ref: [ How thoughtful experimental design can empower biologists in the omics era](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"}</small>

## Biological vs. Technical Replicates — The Most Confused Distinction in Omics (CROSS SKILL PPT; figure)



## practical solution to pseudoreplication bias in single-cell studies (Also check cross skill ppt)
https://www.nature.com/articles/s41467-021-21038-1 : In Figure, 
As you increase the number of subjects from 5 to 20, power increases dramatically. 

But as you increase the number of cells per person from 25 to 500, power barely changes. 

This is the empirical proof, in scRNA-seq terms, of the same principle that applies to all omics: more patients, not more reads or more cells, is what drives power.

## discuss Pseudo bulk approach or mixed model


!!! tip "Further reading"
    - Sample size considerations for omics: 
    [Power and Sample Size for Omics (OHSU)](https://www.ohsu.edu/sites/default/files/2024-02/pss4omics.pdf)
    - Reproducibility considerations in ageing research *(add reference)*

    ## When Technical Replicates Are an Asset: RUVIII and Principled Correction (cross skilling ppt)

  Power analysis and sample size estimation for RNA-Seq differential expression https://pmc.ncbi.nlm.nih.gov/articles/PMC4201821/   
 How many biological replicates are needed in an RNA-seq experiment and which differential expression tool should you use?  https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/

Nice Table : https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/table/SCHURCHRNA053959TB2/ 

!!! info "Sample size requirement"
    In many omics studies, sample size is determined by budget rather than
    by statistical power. This is particularly consequential in omics, where
    thousands of features are tested simultaneously — multiple testing
    correction substantially reduces effective power per feature.

    In practice, n = 3 biological replicates per condition remains the
    field norm — but benchmarking studies consistently show this is
    insufficient:

    - **n ≥ 6 per condition** is the minimum for reliable detection of moderate-to-high fold-change DEGs
    - **n ≥ 12** is recommended when low fold-change genes matter
    - Experiments with n = 4 or fewer are shown to be highly misleading, given the high false positive rate and lack of discovery of genes later found with higher n
    - The greatest impact of decreased sample number is seen below seven samples per group, where more heterogeneity in workflow performance is observed

    <small>

    - Atwal et al. (2025). *Nature Communications* 16, 10173.
    [doi:10.1038/s41467-025-65022-5](https://www.nature.com/articles/s41467-025-65022-5){target="_blank"}

    - Degen & Medo (2025). *PLOS Computational Biology*.
    [doi:10.1371/journal.pcbi.1011630](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011630){target="_blank"}

    - Baccarella et al. (2018). *BMC Bioinformatics*.
    [doi:10.1186/s12859-018-2445-2](https://link.springer.com/article/10.1186/s12859-018-2445-2){target="_blank"}

    - Schurch et al. (2016). *RNA* 22(6), 839–851.
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}

    </small>

    Proteomics sample size vs machine learning:https://pmc.ncbi.nlm.nih.gov/articles/PMC11566501/ 



    - **Metabolomics:** biological variation between individuals is 
  inherently high, meaning small sample sizes conflate inter-individual 
  noise with true treatment or condition effects. In differential 
  abundance analysis, low n leads to unstable variance estimates, 
  reduced detection of true metabolite changes, and a high false 
  discovery rate — with detected metabolite sets that are often 
  study-specific and fail to replicate. <small>[Anwardeen et al. *BMC Bioinformatics* 2023](doi:10.1186/s12859-023-05383-0){target="_blank"}
  [Guo et al. *Metabolites* 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9782571/){target="_blank"}

_ _ _
#### The sequencing depth trap
Compensating for small n with deeper sequencing is almost always wrong. Liu et al. 2014: adding 3 more samples recovers far more DE genes than doubling depth with the same 3 samples. More patients, not more reads. adding more reads improves detection of very lowly-expressed genes but the gain plateaus quickly. 

#### legitimate exceptions

- For rare transcripts — genes expressed at very low levels— depth genuinely matters and more reads will detect things that shallow sequencing misses. 
- Single Cell RNAseq – more cells/Sample are required to study some rare cell, researcher are interested in especially in immunology or T-cell type therapy design studies. 
- Similarly for somatic mutation calling in cancer, where the minor allele fraction (MAF) can be 1–5% in a tumour biopsy, meaning you need 200× or 300× coverage to detect the variant above noise. 

In these specific cases, depth is the right investment. 

#### Modern solutions

**Targeted long-read sequencing (ONT)**
For known rare variants or Genes: use targeted genome coordinates in Oxford Nanopore. Combine depth where the biology demands it with long reads that resolve complex regions short-read WGS cannot.

**Cell type enrichment before library prep**
For rare cell types: enrich by FACS or MACS sorting before sequencing. Standard n × deeper sequencing will not recover a cell population at 0.1% frequency — enrichment will.



_ _ _


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


    ## Example: of what can be often be missed
- Consideration of reproducibility in aging research :
- Sample size considerations: https://www.ohsu.edu/sites/default/files/2024-02/pss4omics.pdf 


## Wrong Platform for the Biological Question

Platform choice is a design decision — not a technical afterthought.
Selecting the wrong platform upstream cannot be compensated for by
better analysis downstream. The data simply does not contain the
information required to answer the question.

**Resolution mismatch — bulk where single-cell was needed**

When cellular heterogeneity is the biological question, bulk RNA-seq
averages signal across all cell types in a sample. Rare cell
populations, cell-type-specific responses, and subpopulation
differences are permanently averaged away. Computational deconvolution
can partially estimate cell-type proportions, but cannot recover
cell-level expression profiles that were never measured.

*Example:* A study of tumour-infiltrating immune cells using bulk
RNA-seq will produce a single averaged signal across cancer cells,
T cells, macrophages, and stromal cells — with no ability to
distinguish which population is driving the observed differences.

**Sequencing technology mismatch — short-read where long-read is needed**

Short-read sequencing (Illumina) cannot reliably resolve structural
variants, full-length transcript isoforms, or sequences in repetitive
genomic regions — regardless of sequencing depth. These limitations
are inherent to read length, not coverage. Long-read technologies
(PacBio, Oxford Nanopore) are required for these questions.

*Example:* Using whole-exome short-read sequencing to detect
structural variants in a rare disease cohort will miss the majority
of pathogenic SVs in repeat-rich regions — producing a false negative
result that deeper sequencing cannot fix.

**Proteomics acquisition mode mismatch — DDA where DIA is needed**

In mass spectrometry-based proteomics, how the instrument *selects*
which proteins to measure is itself a critical design choice — made
at the point of data acquisition, not analysis.

**DDA (Data-Dependent Acquisition)** — the instrument scans the
sample and automatically selects the most abundant peptides to
fragment and identify. This means low-abundance proteins are
frequently skipped entirely. The selection is random across runs,
making quantitative comparisons between samples less reproducible.
DDA is suitable for exploratory discovery of abundant proteins but
is not appropriate when consistent, sensitive quantification of
the full proteome — including rare proteins — is needed.

**DIA (Data-Independent Acquisition)** — the instrument
systematically fragments *all* peptides within defined mass windows,
regardless of abundance. This produces more complete and reproducible
coverage across samples, including low-abundance proteins. DIA
requires more complex data analysis but is the preferred approach
for quantitative studies.

**Targeted platforms (e.g. Olink, SRM/PRM)** — measure a
pre-defined panel of proteins with very high sensitivity and
reproducibility. Suitable when specific proteins of interest are
known in advance (e.g. cytokines, biomarkers) but not designed
for discovery.

*Example:* A study investigating low-abundance immune signalling
proteins (cytokines, transcription factors) using DDA will
systematically miss the targets of interest — not because of
poor analysis, but because the instrument never selected them
for measurement in the first place. Switching to DIA or a
targeted platform at the design stage would have avoided this.

**The cost of platform excitement over biological fit**

Single-cell omics is powerful and increasingly accessible — but it
is not always the right choice. Studies that adopt single-cell
platforms primarily because they are current, then analyse the data
as bulk (ignoring cell-level structure, collapsing cells per sample),
represent a significant waste of cost and sample. The added resolution
of single-cell data is only valuable if the study design, statistical
approach, and biological question are matched to it.

!!! danger "The unrecoverable rule"
    If the platform cannot capture the biological signal of interest,
    no analysis method can recover it. The choice must be made
    before data collection — not revisited after.

 

---Confounding by indication — in clinical studies, the reason a patient received a treatment is correlated with their outcome (e.g. sicker patients get drug A). Common in retrospective omics studies. But this may belong in Module 3.
