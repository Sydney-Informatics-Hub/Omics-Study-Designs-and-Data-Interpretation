# Module 4 : Normalisation, Scaling, and Batch Correction

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Select an appropriate transformation for QC visualisation
      based on the omics platform and explain why raw values
      cannot be used directly.
    - Use PCA and a correlation heatmap to assess sample quality
      and identify unexpected sources of variation before
      normalisation proceeds.
    - Interpret distribution plots to flag samples with shifted
      medians, unusual spread, or bimodal patterns.
    - Apply a principled exclusion rule and document the decision
      before examining any results.
    - Identify sample swaps and mislabelling using sex concordance
      and within replicate distance checks.

## Before You Normalise: Reading the QC Signals

Normalisation adjusts for systematic technical differences between
samples. But if a sample is a genuine outlier, due to degraded RNA, a failed
library, a mislabelled tube etc. normalising it does not fix the problem.
It distributes the problem across the dataset.

The correct order is always: **assess first, then normalise**. A small
set of sample level checks take minutes to run and catch the most common
failures before they reach the analysis.

### Transformation before visualisation

Raw or unnormalised values cannot be used directly for QC visualisation
across any omics platform. The core problem is the same everywhere:
variance scales with the mean. Gene/proteins (features) with high abundance/count show much
greater absolute variability than lowly abundant ones, so PCA and
clustering on untransformed values will be dominated by a handful of
highly abundant features not by the biologically or technically interesting structure in the data.

The solution is to apply a transformation that stabilises variance before any QC plot is generated. The transformation is **not** normalisation; it does not remove technical differences between samples. It simply makes the data behave well enough for visualisation.

Log2 transformation is commonly used across omics. **log2(x + 1)** adding 1 before log-transformation (the "+1
pseudocount") handles zeros, since log(0) is undefined. This is the most widely applicable, platform agnostic transformation and is the baseline approach across omics. It is interpretable: a difference of 1
on the log2 scale corresponds to a twofold change in the original units.

Its limitation for count based data is low count instability. A gene/protein
expression change from 1 to 2 count produces a log2 fold change of 1.0 (fold change 2), which is same
as a gene expression changing from 1,000 to 2,000. The first difference is almost
entirely sampling noise; the second is reliable signal. log2(x+1)
treats both identically, introducing instability 
for lowly expressed genes that can affect QC visualisation.

This is why platform specific transformations exist for count data:

| Platform | Standard transformation for QC visualisation |
|---|---|
| **Bulk RNA-seq** | log2(count+1) is acceptable; **rlog or VST** (DESeq2) preferred, both shrink noisy low count genes towards the dataset average, making PCA more representative of true biological structure |
| **scRNA-seq** | **log1p** on library size, normalised counts (Seurat/Scanpy default, fast, interpretable); **SCTransform** (Seurat) for variance stabilised Pearson residuals, better PCA/clustering, recommended for datasets with variable depth |
| **Proteomics (MS)** | **log2** of normalised intensities, field standard; continuous data so no pseudocount needed. **VSN (variance stabilising normalisation)** is a more rigorous alternative used in some workflows|
| **Metabolomics** | **log2** or log10** of normalised values; choice depends on dynamic range. Note: Pareto scaling (mean-centre then divide by √SD) is a scaling step applied after transformation — common in metabolomics workflows but distinct from the log transformation itself  |
| **16S / metagenomics** | **CLR (centred log-ratio)** after zero handling, either pseudocount addition (e.g. +0.5) or multiplicative replacement (e.g. zCompositions), handles the compositional constraint; log2(x+1) on raw proportions is not appropriate |

PCA, correlation heatmaps, and distribution plots are used across all platforms. The transformation differs by platform, but the diagnostic logic remains the same. 

!!! warning "Transformation is not normalisation"
    Transformation stabilises variance for visualisation. It does not
    remove systematic technical differences between samples that is
    what normalisation does. Applying a transformation to raw,
    unnormalised data and then running PCA will show you both biological
    and technical structure. That is fine for QC. It is not a substitute
    for normalisation before downstream analysis.

??? info "rlog and VST RNA-seq specific detail"
    Both are implemented in DESeq2 and require a DESeqDataSet object.
    **rlog** uses an empirical Bayes prior to shrink log fold changes
    for lowly expressed genes towards zero. **VST** estimates the
    mean-variance relationship and applies a parametric transformation
    that makes variance approximately independent of the mean. VST is
    faster and preferred for larger datasets (>30 samples); rlog is
    more accurate for smaller ones. 


### Primary QC tools: PCA and hierarchical clustering

The two important plots of sample level QC are **PCA** and a **pairwise
correlation heatmap**. Both apply across omics platforms and answer
the same core question: do biological replicates cluster together, and do 
samples separate by condition rather than by technical factors?

**PCA** was introduced in Module 3 as a tool for diagnosing confounders.
In QC it serves the same function but the question is reversed: rather
than colouring by batch to diagnose a known problem, you colour
systematically by every available metadata variable to find unexpected
sources of variation. The same diagnostic logic applies whether the
data is RNA-seq, proteomics, metabolomics, or microbiome; the input
matrix changes, the interpretation does not.


**Hierarchical clustering heatmap** shows the pairwise Pearson
correlation between all samples on transformed counts. Because
the majority of genes are not differentially expressed, samples generally
show high correlations with each other, values above 0.80 are typical
for high quality RNA-seq (Thresholds vary by platform). Samples below 0.80 may indicate an outlier or
contamination.

The clustering tree reveals which samples are most similar. The
expectation is that biological replicates cluster together and form
clearly separated groups by condition. A sample that clusters with the
wrong group, a case that clusters with controls, a male that clusters
with females, is a candidate for a swap or mislabel.


!!! info "These two plots answer different questions"
    PCA shows the major axes of variation and what drives them.
    The correlation heatmap shows whether individual samples are
    aberrant relative to their group. Use both: PCA for diagnosing
    what is driving variation, heatmap for catching outlier samples
    that may look reasonable on PC1/PC2 but are globally dissimilar
    from their replicates.

### Distribution plots: library size, boxplots, and density

Before transformation and PCA, three simple plots provide a first pass screen.

![Box plot and Violin plots](figures/04_Box_violion_v01.jpg){width=90%}

A basic **boxplot** of log transformed values, one box per sample, shows whether distributions are broadly comparable. You are checking that medians sit at roughly the same level and that interquartile ranges are similar across samples. A sample with a shifted median or a dramatically wider or narrower box than its neighbours is worth investigating before normalisation proceeds.

**Violin plots** extend the boxplot by showing the full distribution shape and crucially, the boxplot inside the violin lets you read both summary statistics and shape simultaneously. They are particularly useful for spotting bimodality: **two distinct peaks in one sample can indicate a mixed population, contamination, or a library preparation failure** that a boxplot alone would summarise into a wide box and miss.

**Density plots** (one curve per sample, all overlaid) show the same distributional information as violins but make comparison across many samples easier. They are the better choice when you want to see whether all curves occupy the same region or whether one sits shifted relative to the others. These plots catch obvious failures quickly. In **methylation array data**, overlaid density plots of beta values are standard QC, a well behaved methylation dataset shows a characteristic bimodal distribution, and a sample deviating from this pattern is immediately visible. They do not replace PCA, their job is to flag gross outliers before those outliers distort the PCA and mislead interpretation.

??? abstract "What about RLE plots?"
    Relative Log Expression (RLE) plots are used in some RNA-seq QC workflows. For each gene, the per sample deviation from the cross sample median is computed and plotted as a boxplot per sample. The expected value under no technical problem is zero for every sample, making systematic shifts immediately visible.

    Most DESeq2-based workflows use PCA and the correlation heatmap instead. RLE is most useful as an additional check when standard plots are inconclusive, or to compare normalisation quality before and after correction.

    Further reading: [EDASeq vignette](https://bioconductor.org/packages/release/bioc/vignettes/EDASeq/inst/doc/EDASeq.html){target="_blank"}


### Outlier detection and the exclusion rule

Two additional checks complement the distribution plots and PCA.

**Genes detected per sample** count the number of features with at
least one count per sample. A sharp drop in gene detection relative
to batch neighbours signals a quality failure, not biology. This is
more sensitive than library size alone because it is not driven by
a handful of highly expressed genes.

**PCA position** a sample sitting far from all others on multiple
principal components is worth investigating regardless of whether a
technical explanation is available. Check metadata for a plausible
cause: processing date, operator, RNA quality metric, extraction batch.
If no explanation exists, the decision to exclude requires documentation
and a prespecified rationale.

!!! danger "The exclusion rule"
    Remove a sample because it has a documented technical failure,
    not because it disagrees with your hypothesis. One may want to retain a sample
    despite some technical failure, if it is irreplaceable and the
    failure is minor and correctable. Document both decisions
    explicitly, before examining the differential expression results.
    Exclusion decisions made **after looking at results** are not QC,
    they are outcome driven filtering, which inflates false positives.

### Sample swap and mislabelling checks

Sample swaps are more common than most researchers expect, particularly
in multi-site studies and large clinical cohorts. A sample labelled as
female that clusters with male samples in expression space is a
diagnostic signal, not a biological finding.

**Sex concordance check**
Plot XIST expression (X-inactivation gene, expressed only in females) 
on one axis against RPS4Y1 or DDX3Y (Y-chromosome genes, expressed 
only in males) on the other, one dot per sample. Females should 
cluster in the high XIST / low Y-gene corner; males in the low XIST / 
high Y-gene corner. A sample landing in the wrong corner is swapped 
or mislabelled.

**Within-replicate distance check**
Technical or biological replicates of the same sample should be among
each other's nearest neighbours in expression space. If a sample is
closer to samples from a different individual than to its own replicate,
a swap is likely.

!!! info "Coming up in the practical"
    The practical for this module includes a simulated dataset with a
    planted outlier and a mislabelled sample. You will use library size,
    gene detection, and sex-marker expression to find both before
    normalisation begins.

