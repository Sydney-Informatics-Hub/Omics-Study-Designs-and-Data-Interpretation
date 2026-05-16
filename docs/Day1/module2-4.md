
# Module 2.4: Why classical statistics struggle with count data

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  
    
    - Ensure why standard statistical tests fail on omics data 
    - Identify the specific assumption statistical assumptions omics platform violates 
    - Describe how variance borrowing across features is necessary with small samples sizes
    - Match appropriate statistical frameworks to major omics data types 

Modules 2.1, 2.2, and 2.3 established structural properties that all omics data share:

- **Measurements are relative, not absolute**: every value 
  reflects a share of a technical total that varies 
  between samples
- **Missing values and zeros arise from multiple causes 
  and are not equivalent to each other**
- **Features are compositionally constrained**: a change 
  in one feature creates apparent changes in all others 
  regardless of what the biology did

Each of these properties is a violation of an assumption 
that standard statistical tests make. A classical t-test assumes measurements are absolute and independent, that errors are normally distributed, and that variance is stable across the range of the data.

Omics data violates all three, but not always in the same way. The specific violations differ by platform, which is why no single statistical method works across all of them. Understanding what fails and why is the foundation for choosing the right approach.

### Assumptions of a standard t-test

!!! tip "What is a t-test?"
    TODO 

The assumptions of a standard t-test cover: 

1. **Measurements are absolute and independent**:
   each observation stands on its own and is not 
   affected by what else was measured at the same time
2. **Errors are normally distributed**: the 
   variability around the true value follows a 
   bell curve
3. **Variance is homogeneous**: the spread of 
   the data is consistent across the range of 
   values being measured
4. **Variance can be reliably estimated**: 
   enough observations exist per feature to 
   produce a stable variance estimate

TODO a table like this? 

| Platform | Violation 1 — measurements not absolute | Violation 2 — distribution assumption | Violation 3 — variance not homogeneous | Violation 4 — small n problem | Additional violation |
|---|---|---|---|---|---|
| **Sequencing counts** RNA-seq · ATAC-seq · WGS | A gene with 200 counts in one sample and 100 in another may reflect sequencing depth, not biology. The t-test treats counts as absolute quantities. | Most genes have very low counts. Values of 0, 1, and 2 cannot be approximated by a normal distribution. Count data is discrete and right-skewed. | Lowly expressed genes are systematically more variable than highly expressed ones. Standard tests assume homogeneous variance across the data range. | Each gene's variance is estimated from 2 degrees of freedom with n = 3. Estimates are unreliable — some genes appear artificially stable or variable purely by chance. | **Overdispersion.** Count data shows more variability between replicates than a Poisson model predicts. This must be modelled explicitly using a negative binomial distribution. |
| **Proteomics · metabolomics** DDA · DIA · LC-MS | Signal intensity reflects a proportion of total ion signal. Differences in loading, protein concentration, or ionisation efficiency shift all features simultaneously. Raw intensities are not comparable across samples. | After log2 transformation, intensities are approximately normal — this violation is partially resolved by transformation, unlike count data. | Lower-abundance features show higher relative variability than high-abundance ones. Variance changes systematically across the intensity range even after transformation. | Thousands of proteins or metabolites, each with variance estimated from a handful of replicates, produces systematically unreliable test statistics. | **Missing not at random (MNAR).** Missing values are biased toward low-abundance features. Naive imputation treats imputed values as equivalent to measured values — producing systematically biased comparisons. |
| **Microbiome** 16S · metagenomics | Total microbial biomass is lost during sequencing. Relative abundances sum to 100% regardless of how many organisms are actually present. | Count data is discrete and overdispersed, same as bulk RNA-seq. Negative binomial models address this but are not sufficient alone. | Variance increases at low counts, same as bulk RNA-seq. Low-abundance taxa are systematically more variable across samples. | Same small n problem as bulk RNA-seq — per-taxon variance estimates are unreliable with typical sample sizes. | **Compositional independence violation.** Features are mathematically constrained against each other — a correctly specified NB model still produces spurious results because independence is violated. Log-ratio methods (ALDEx2, ANCOM-BC) are required to address both problems. |
| **Methylation arrays** EPIC · 450K | Probe signal reflects a ratio of methylated to total fluorescence. Global methylation shifts affect all probes simultaneously, making raw beta values incomparable across conditions without normalisation. | Beta values are bounded between 0 and 1 and follow a beta distribution, not a normal one. Variance is highest near 0.5 and approaches zero at the extremes. M-value transformation substantially improves normality. | Heteroscedasticity is structural — a mathematical property of the bounded range, not a feature of any particular dataset. M-value transformation reduces but does not fully resolve it. | Same small n problem — thousands of CpG sites each with variance estimated from a small number of samples. Empirical Bayes shrinkage via limma is required. | **Cell type composition confounding.** A sample with different cellular composition shows globally shifted methylation across thousands of probes simultaneously. A test ignoring this estimates differential composition, not differential methylation. |
| **Single-cell RNA-seq** 10x · SMART-seq2 | Total UMIs per cell varies substantially. Within-cell compositionality means dominant transcripts suppress apparent signal from all other genes in the same cell. | Count data is discrete, zero-inflated, and overdispersed — more severely than bulk RNA-seq due to dropout and shallow per-cell depth. | Within-cell variance is extreme — the same gene can show counts of 0 and 5 in cells of the same type due to stochastic capture, not biology. | Per-gene variance is highly unreliable at the single-cell level due to extreme sparsity. Pseudobulk aggregation before applying bulk methods is required. | **Pseudoreplication.** Cells from the same donor are not independent biological replicates. Treating 50,000 cells from 5 donors as n = 50,000 inflates degrees of freedom by orders of magnitude. No distributional model fixes this — it requires aggregating to the donor level before testing. |

| Platform | Primary violation | Appropriate framework | Key method |
|---|---|---|---|
| Bulk RNA-seq | Overdispersed counts; heteroscedastic variance | Negative binomial model with empirical Bayes shrinkage | DESeq2, edgeR |
| Bulk RNA-seq (high depth) | Heteroscedastic log-space variance | Weighted linear model with empirical Bayes | limma-voom |
| Proteomics · metabolomics | Heteroscedastic continuous intensity; MNAR missing values | Linear model with empirical Bayes; MNAR-aware imputation | limma, MSstats |
| Methylation arrays | Bounded beta distribution; cell composition confounding | Linear model on M-values with empirical Bayes; cell type deconvolution | limma + minfi/ChAMP |
| Microbiome | Compositional counts; independence violation | Log-ratio transformation; compositional-aware models | ALDEx2, ANCOM-BC |
| Single-cell RNA-seq | Count distribution + pseudoreplication | Pseudobulk aggregation then bulk methods | DESeq2/edgeR on pseudobulk |
| Spatial omics | Count distribution + within-spot mixing | Spatial-aware models; deconvolution | SPARK, SpatialDE, RCTD |


### Level 2: t-test on log-normalised counts (log CPM)

A common next step is:

1. normalise for library size  
2. apply a log transformation  
3. run a t-test  

This fixes some of the obvious issues.

- Normalisation makes samples broadly comparable  
- Log transformation compresses large values and reduces skew  

For moderately and highly expressed genes, this approach can behave reasonably well, especially if you have many replicates.

But two problems remain.

#### Problem 1: low counts still behave poorly

For genes with very low counts, log transformation doesn’t really “fix” the data.

Values like 0, 1, and 2 are still effectively discrete after transformation, and small differences translate into large apparent fold changes. At the same time, lowly expressed genes tend to be more variable between replicates.

You can see this in practice as a characteristic “fan shape” in MA plots:  
at low average expression, the spread of log fold changes becomes very wide.

![MA plot without and with shrinkage (Derakhshani et al. (2020), CC BY)](module2Figs/02_MLE_plot_dispersion_v01.jpg){style="width:90%; height:auto; min-height:500px"}

This variability is not primarily biological — it reflects unstable estimates at low counts.

#### Problem 2: variance is still estimated per gene

Even after transformation, a standard t-test still treats each gene independently.

That means the variance estimate for gene X comes only from its own replicates. With small sample sizes, that estimate is noisy. Some genes will appear artificially stable, others artificially variable, just by chance.

The test has no mechanism to recognise or correct for this.

---

### Level 3: limma-voom — fixing the t-test framework

**limma-voom** keeps the general idea of working with log-transformed data, but changes how variability is handled.

It addresses the two problems above directly.

#### Mean–variance relationship

Across the dataset, variability is not random — it follows a pattern.

Lowly expressed genes are consistently more variable than highly expressed ones. Instead of ignoring this, `voom` estimates the relationship across all genes and uses it to assign **precision weights**.

- Observations expected to be noisy (low counts) get lower weight  
- More stable observations get higher weight  

The model then fits a weighted linear model, rather than treating all points equally.

#### Borrowing information across genes

limma also uses an **empirical Bayes** approach to stabilise variance estimates.

Instead of relying entirely on the variance of a single gene, it shrinks each estimate toward a global trend derived from all genes.

In practice, this means:

- noisy estimates from small sample sizes are stabilised  
- the effective degrees of freedom increase  
- test statistics become more reliable  

This “borrowing strength” across genes is one of the key ideas that makes modern methods work.

---

### Level 4: DESeq2 and edgeR — modelling counts directly

Rather than transforming the data, **DESeq2** and **edgeR** model the counts themselves.

They use the **negative binomial distribution**, which is well suited to count data with biological variability. This distribution has two parameters:

- a mean (expected count)  
- a dispersion term (extra variability between replicates)

This is important because real RNA-seq data is more variable than a simple Poisson model would predict.

Like limma, both methods:

- estimate a mean–variance (mean–dispersion) relationship across all genes  
- shrink individual gene estimates toward that trend  
- effectively share information across the dataset  

They also incorporate normalisation internally and fit **generalised linear models**, which makes it straightforward to handle more complex experimental designs.

This approach is particularly important for **lowly expressed genes**, where log-based methods are least stable.

---

### Putting it together

| Approach | What it fixes | What remains wrong |
|---|---|---|
| t-test on raw counts | Nothing | Not comparable; discrete; normal approximation fails; variance estimates are unstable |
| t-test on log CPM | Makes samples comparable; improves behaviour at higher counts | Breaks down at low counts; per-gene variance still unreliable with small n |
| limma-voom | Accounts for mean–variance relationship; stabilises variance using empirical Bayes | Less reliable for very low counts |
| DESeq2 / edgeR | All of the above, and NB model for count data  | Best for low count genes; equivalent to limma voom at higher counts |

The difference between these methods is not just the distribution they assume.

The key shift is this:

> **variance is no longer estimated gene-by-gene in isolation.**

Instead, each gene’s behaviour is interpreted in the context of all others.

---

!!! info "The practical message"
    With typical RNA-seq experiments (n ≈ 3–5 per group), per-gene variance estimates are inherently unstable. Methods like limma-voom, DESeq2, and edgeR make reliable inference possible by borrowing information across genes. A plain t-test does not.

---

### The same principle applies beyond RNA-seq

This is not unique to bulk RNA-seq.

- **Single-cell RNA-seq:** individual cells are not independent biological replicates; pseudobulk approaches are commonly used  
- **Microbiome data:** compositional structure adds another layer, often requiring log-ratio methods  
- **Proteomics and metabolomics:** data are heteroscedastic; moderated models (e.g. limma) perform better than naive tests  

The details differ, but the underlying issue is the same:

small sample sizes + high dimensional data → unstable variance estimates.

---

### What to take forward

The takeaway is not that classical statistics are “wrong.”

It’s that they rely on assumptions that don’t hold for this type of data — especially at low counts and small sample sizes.

Modern methods don’t just tweak the model. They change how information is used.

> Instead of analysing each feature in isolation, they use the structure of the entire dataset to stabilise inference.

That shift is what makes the difference.

---

### Looking ahead

We’ve now covered:

- what counts represent  
- why zeros appear  
- how compositionality affects interpretation  
- and why standard statistical tests need to be adapted  

 !!! info "What Module 5 covers"
    The mechanics of normalisation , how TMM, RLE, CPM, and variance 
    stabilising transformations work and when each is appropriate , are
    covered in **Module 5**. The full DESeq2 and edgeR analysis pipeline,
    including dispersion estimation, GLM fitting, and interpretation of
    results, is covered in a dedicated downstream workshop.

   
    

---

### Module 2: Summary

The four sections of this module have built a connected picture of why
omics data requires its own analytical framework:

- **Counts are proportions** of a fixed sequencing budget :raw counts
  cannot be compared across samples without accounting for depth
- **Zeros are not all the same**:biological absence, technical
  dropout, and sampling failure produce identical zeros but require
  different responses
- **Features are compositionally constrained**: proportions not
  absolute quantities are measured, making naive fold change and
  correlation analyses unreliable
- **Classical t-tests fail on count data: but the reason is not simply
  that the data is non normal.** The core problem is that per gene
  variance cannot be reliably estimated from small n. limma voom,
  DESeq2, and edgeR all solve this by borrowing information about
  variance structure across all genes simultaneously. That shared
  structure is what makes inference possible with three replicates.


    Github Folder: For ***practical*** download and open .html file in Chrome/Edge Browser.