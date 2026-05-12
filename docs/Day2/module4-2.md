## Section 2 : Normalisation and Scaling

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Explain why raw counts cannot be compared across samples and
      identify the three sources of technical variation that
      normalisation addresses.
    - Distinguish normalisation from scaling, explain their different
      purposes, and describe the consequences of applying them in the
      wrong order.
    - Select an appropriate normalisation method for bulk RNA-seq,
      scRNA-seq, proteomics, metabolomics, and microbiome data and
      justify that choice.

---

### Why normalisation is required

Section 1 established that transformation makes data behave well enough
for visualisation. Normalisation is a different step with a different
purpose: it corrects for systematic technical differences *between*
samples so that values are directly comparable across the dataset.

Three distinct sources of technical variation require correction,
each operating differently across platforms.

**Library size variation**

In **sequencing based platforms**, samples routinely vary in total read
count by 2 fold or more within the same experiment, even with identical
input material and careful handling. A gene with 200 counts in a sample
sequenced to 40 million reads is not more expressed than the same gene
with 100 counts in a sample sequenced to 20 million reads; both
represent the same 0.0005% of their respective libraries. Without
normalisation, this depth difference appears as differential expression.

**Composition effects**

Library size correction alone is not sufficient. If a small number of
genes/proteins are extremely highly expressed, dominating the sequencing
budget, every other feature in that sample appears artificially lower
in relative terms, even if its true abundance has not changed. This is
the compositionality problem introduced in Module 2. A naive
per million scaling that treats total library size as comparable across
samples will be misled when the composition of that library differs.

![Bias normalization](figures/04_Bias_normalization_v01.jpg){width=90%}

**Platform specific technical artefacts**

In **mass spectrometry based platforms**, the equivalent of library size
variation is run to run variability in total ion signal. Differences in
sample concentration, injection volume, and ionisation efficiency
introduce systematic shifts in measured abundance across runs. The
problem is **structurally identical to sequencing depth variation**; the
methods used to correct it differ because the data structure differs.

---

### Normalisation vs scaling — two different steps

Section 1 introduced the distinction that transformation is not
normalisation. Scaling is a third operation, different from both.

**Normalisation** corrects for systematic technical differences
*between samples*. After normalisation, a count of 100 in Sample A
and 100 in Sample B represents the same relative abundance. Before
normalisation, it does not.

**Scaling** adjusts the relative contribution of each *feature* across
all samples. After log transformation, features may still differ
substantially in variance — highly variable features can dominate
multivariate analyses such as PCA simply because their variance is
large, not because they carry more biological information. Scaling
addresses this by dividing each feature by some measure of its
variability (standard deviation in auto-scaling, √SD in Pareto scaling)
so that features contribute more equally.

These are sequential steps with different purposes:

1. **Normalise** — make samples technically comparable
2. **Transform** — stabilise variance for visualisation and modelling
3. **Scale** — equalise feature contributions for multivariate analysis

!!! warning "Order matters"
    Scaling before normalising does not remove library size differences —
    it standardises them. A sample that was 2× deeper than its neighbours
    remains 2× more influential after scaling. The technical difference
    is preserved and locked in.

    Equally important: not every workflow requires scaling. RNA-seq
    differential expression tools (DESeq2, edgeR) work on normalised
    counts without feature scaling. Scaling before PCA is standard in
    metabolomics but optional in RNA-seq workflows. Applying
    inappropriate scaling for the platform and analysis goal can distort
    downstream interpretation rather than improve it.

!!! info "Scaling means different things in different platforms"
    In metabolomics, scaling refers to feature-level operations such as
    Pareto or auto-scaling applied before PCA. In RNA-seq and scRNA-seq,
    "scaling" often refers to z-scoring genes across cells after
    variance stabilisation — a different operation applied to features
    for a different purpose. The word is used loosely in the literature;
    always check what is actually being divided by what.

---

### Choosing a normalisation approach

There is no universal normalisation method. The correct choice depends
on the platform, the experimental design, and the downstream analysis.
Applying the wrong method introduces new artefacts rather than simply
failing to correct existing ones.

---

#### Bulk RNA-seq

Bulk RNA-seq has the most mature normalisation landscape and the most
common misunderstandings. The key distinction is between metrics
appropriate for visualisation and those appropriate for differential
expression testing.

| Method | Corrects for | Use | Not appropriate for |
|---|---|---|---|
| **CPM** | Sequencing depth | Comparing same gene between replicates | Within-sample gene comparisons; DE testing |
| **TPM** | Depth + gene length | Within-sample gene comparisons; same gene across samples | DE testing |
| **RPKM / FPKM** | Depth + gene length | Legacy reporting only | Between-sample comparisons; DE testing |
| **TMM** (edgeR) | Depth + composition | DE analysis | Within-sample comparisons |
| **DESeq2 size factors** | Depth + composition | DE analysis | Within-sample comparisons |

**CPM** and **TPM** are widely used for reporting and visualisation but
neither corrects for composition effects. If a small set of highly
expressed genes dominates one sample's library, CPM will suppress the
apparent expression of everything else in that sample. CPM and TPM
should not be used as input to differential expression testing.

**RPKM/FPKM** are not recommended for new analyses. Unlike TPM, RPKM
totals differ between samples, making direct between-sample comparisons
unreliable. TPM is the preferred alternative when length correction is
needed.

**TMM (Trimmed Mean of M-values)** calculates a scaling factor for
each sample by trimming the most extreme log-fold-changes and computing
a weighted mean of the remainder — removing the genes most likely to be
compositionally dominant. TMM is the normalisation method built into
edgeR.

**DESeq2 size factors** achieve similar correction through a different
route: for each gene, the ratio of its count to the geometric mean
across all samples is calculated, and the median of those ratios becomes
the size factor for that sample. The median is robust to differentially
expressed genes. DESeq2 applies this normalisation internally — raw
counts are the correct input; providing CPM or TPM values to DESeq2
means normalising already-normalised data.

!!! info "TMM vs DESeq2 size factors"
    Both correct for depth and composition and perform similarly in
    practice. The choice is usually determined by which DE tool you
    are using: TMM with edgeR, size factors with DESeq2. Applying
    TMM factors before running DESeq2 is double-normalising and
    should be avoided.

---

#### Single-cell RNA-seq

scRNA-seq inherits all the depth-variation problems of bulk RNA-seq
and adds two more: per-cell library sizes that vary by 10–100× even
within the same experiment, and extreme sparsity (>90% zeros in
droplet-based data). Bulk normalisation methods were not designed for
this and perform poorly when applied directly to cell-level data.

**Library size normalisation (log-normalisation)** divides each cell's
counts by that cell's total UMI count, multiplies by a scale factor
(typically 10,000), then applies log1p transformation. Fast,
interpretable, and the default in Seurat and Scanpy. The limitation
is that size factors estimated from a single sparse cell are noisy
when total UMI counts vary substantially across cells.

**SCTransform** (Seurat v3+, now default in Seurat v5) uses regularised
negative binomial regression to model the relationship between
sequencing depth and gene expression, then extracts Pearson residuals.
These residuals are approximately variance-stabilised — gene variance
no longer scales with mean expression — which produces more stable
PCA and clustering, particularly when depth varies substantially
across cells.

**Scran** uses a pooling-based approach: cells are pooled, size factors
estimated at pool level, then deconvolved back to individual cells. The
pool-level estimates are more stable than single-cell estimates because
they average over more counts. Commonly used in Bioconductor-based
workflows.

!!! warning "Do not apply TMM or DESeq2 size factors to scRNA-seq cell-level data"
    Both methods assume the majority of features are not differentially
    abundant — an assumption that approximately holds across biological
    samples in bulk RNA-seq but not across individual cells with very
    different transcriptional states. For pseudobulk differential
    expression (aggregated to donor level), TMM and DESeq2 size factors
    are appropriate.

---

#### Proteomics (label-free MS)

Missing values interact directly with normalisation in label-free
proteomics: proteins absent from some samples will distort
sample-level statistics if included. Standard practice is to filter
proteins with excessive missingness before normalising on the retained
features.

**Median normalisation** divides each sample's intensities by the
sample median (or subtracts on the log scale). Assumes the median
protein abundance is consistent across samples — analogous to the
majority-unchanged assumption in TMM. Fast and effective when the
assumption holds.

**Quantile normalisation** forces the distribution of intensities to
be identical across samples. Powerful when technical variation is
large and the design is balanced, but it removes genuine biological
variation in abundance distributions. Should not be applied when
global abundance shifts are possible or expected.

**Reference sample normalisation (pooled QC)** is standard practice
when samples are acquired across multiple MS runs. A pooled QC sample
— a mixture of equal aliquots from all study samples — is injected
repeatedly throughout the acquisition sequence. Intensities are
normalised relative to the nearest QC injection, correcting for both
between-run drift and within-run variability. This must be prepared
before the study begins; it cannot be added retrospectively.

---

#### Metabolomics

Metabolomics normalisation faces the same structural challenges as
proteomics — run-to-run signal variability, missing values, and
extreme dynamic range — but with greater biological variability
between samples due to diet, circadian effects, and fasting status.

**Pooled QC normalisation** is the recommended approach for
MS-based untargeted metabolomics for the same reasons as in
proteomics: repeated injections of a pooled reference throughout
the run enable correction for instrument drift.

**Median / PQN (Probabilistic Quotient Normalisation)** are
sample-level methods that correct for overall concentration
differences between samples. PQN calculates the most probable
dilution factor by comparing each sample to a reference
distribution, making it robust to metabolites that are genuinely
differentially abundant.

**Scaling** in metabolomics — Pareto, auto-scaling — is applied
*after* normalisation and transformation as a separate step for
multivariate analysis. As noted in Section 1, Pareto scaling
(mean-centre then divide by √SD) adjusts the relative contribution
of features to PCA; it is not a normalisation method.

---

#### 16S amplicon and metagenomics

Microbiome normalisation has been actively debated, and the choice
of method has a larger impact on downstream results than in most
other platforms.

**Rarefaction** — subsampling all samples to the same read depth —
was the field standard for many years and remains appropriate for
**alpha diversity** calculations, where equalising depth makes
samples directly comparable. For differential abundance testing,
rarefaction discards real data and is now generally considered
inferior to model-based approaches.
<small>[McMurdie & Holmes. *PLOS Computational Biology* 2014](https://doi.org/10.1371/journal.pcbi.1003531){target="_blank"}</small>

**CLR (Centred Log-Ratio)** is the theoretically motivated approach
for compositional data and is appropriate for **beta diversity** and
ordination. Requires zero handling before transformation (pseudocount
addition or multiplicative replacement — see Section 1 table).

**Model-based approaches** (ANCOM-BC, ALDEx2, DESeq2 with
appropriate settings) are preferred for differential abundance
testing. They handle the compositional constraint directly within
the statistical model rather than attempting to normalise it away.

!!! info "A practical guide by analysis type"
    - **Alpha diversity** → rarefy first; diversity metrics are
      depth-sensitive
    - **Beta diversity / ordination** → CLR + Aitchison distance
    - **Differential abundance testing** → ANCOM-BC, ALDEx2, or
      DESeq2; do not use rarefied data

---

### Order of operations

The correct sequence — from raw data to analysis-ready values — is
the same across platforms, even if the specific methods differ:

1. **QC checks** (Section 1) — identify and resolve outliers,
   swaps, and depth confounds before touching the data
2. **Normalise** — correct for between-sample technical differences
3. **Transform** — stabilise variance for visualisation and modelling
4. **Scale** (where applicable) — equalise feature contributions
   for multivariate analysis

Each step depends on the previous one being done correctly. Normalising
a dataset that contains an undetected outlier distributes that
outlier's signal across the dataset. Scaling before normalising
preserves the technical differences that normalisation was meant to
remove. The order is not a convention — it reflects the statistical
logic of each step.

!!! info "Coming up in Section 3"
    Once data is normalised and QC-checked, a further source of
    systematic variation may remain: batch effects. Section 3 covers
    when batch correction is appropriate, which methods to use, and
    how to verify that correction has removed technical signal without
    destroying biological signal.

---

??? abstract "Further Reading · Normalisation Methods"

    **Bulk RNA-seq**

    Robinson MD, Oshlack A. A scaling normalization method for
    differential expression analysis of RNA-seq data.
    *Genome Biology* 2010; 11: R25.
    [doi:10.1186/gb-2010-11-3-r25](https://link.springer.com/article/10.1186/gb-2010-11-3-r25){target="_blank"}
    *(TMM — introduces the composition problem and its correction)*

    Love MI, Huber W, Anders S. Moderated estimation of fold change
    and dispersion for RNA-seq data with DESeq2. *Genome Biology*
    2014; 15: 550.
    [doi:10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8){target="_blank"}

    ---

    **Single-cell RNA-seq**

    Hafemeister C, Satija R. Normalization and variance stabilization
    of single-cell RNA-seq data using regularized negative binomial
    regression. *Genome Biology* 2019; 20: 296.
    [doi:10.1186/s13059-019-1874-1](https://doi.org/10.1186/s13059-019-1874-1){target="_blank"}
    *(SCTransform — original paper)*

    Lun ATL, Bach K, Marioni JC. Pooling across cells to normalize
    single-cell RNA sequencing data with many zero counts.
    *Genome Biology* 2016; 17: 75.
    [doi:10.1186/s13059-016-0947-7](https://doi.org/10.1186/s13059-016-0947-7){target="_blank"}
    *(scran pooling-based normalisation)*

    ---

    **Proteomics**

    Välikangas T, Suomi T, Elo LL. A systematic evaluation of
    normalization methods in quantitative label-free proteomics.
    *Briefings in Bioinformatics* 2018; 19(1): 1–11.
    [doi:10.1093/bib/bbw095](https://doi.org/10.1093/bib/bbw095){target="_blank"}

    ---

    **Metabolomics**

    van den Berg RA et al. Centering, scaling, and transformations:
    improving the biological information content of metabolomics data.
    *BMC Genomics* 2006; 7: 142.
    [doi:10.1186/1471-2164-7-142](https://doi.org/10.1186/1471-2164-7-142){target="_blank"}
    *(Foundational reference distinguishing transformation from scaling)*

    ---

    **16S / metagenomics**

    McMurdie PJ, Holmes S. Waste not, want not: why rarefying
    microbiome data is inadmissible.
    *PLOS Computational Biology* 2014; 10(4): e1003531.
    [doi:10.1371/journal.pcbi.1003531](https://doi.org/10.1371/journal.pcbi.1003531){target="_blank"}

    Gloor GB et al. Microbiome datasets are compositional: and this
    is not optional. *Frontiers in Microbiology* 2017; 8: 2224.
    [doi:10.3389/fmicb.2017.02224](https://doi.org/10.3389/fmicb.2017.02224){target="_blank"} 