
# Module 2.5: Why classical statistics struggle with omics count data

!!! info "Learning objectives" 

    By the end of this section, participants will be able to:  
    
    - Describe the key assumptions of standard statistical tests and identify which are violated by omics count data
    - Explain what overdispersion means in count data and why it
      requires a negative binomial model rather than a normal or
      Poisson approximation
    - Describe how variance borrowing across features (empirical Bayes variance shrinkage) is necessary with small samples sizes
    - Match appropriate statistical frameworks to major omics data types 

Modules 2.1 - 2.4 established structural properties that all omics data share:

- **Omics measurements are relative, not absolute**: every value 
  reflects a share of a technical total that varies 
  between samples
- **Missing values and zeros arise from multiple causes 
  and are not equivalent to each other** 
- **Features are compositionally constrained**: a change 
  in one feature creates apparent changes in all others 
  regardless of what the biology did

Each of these properties is a violation of an assumption that standard statistical tests make.  

Omics data violates these assumptions, but not always in the same way. The specific violations differ by platform, which is why no single statistical method works across all of them. Understanding what fails and why is the foundation for choosing the right approach.

### Assumptions of a standard t-test

!!! tip "What is a t-test?"
    A t-test asks whether the means of two groups differ more than
    would be expected by chance. It divides the difference between
    group means by an estimate of variability: a larger difference
    relative to variability gives a larger test statistic and a
    smaller p-value. It is the most widely taught statistical test,
    which is why understanding exactly where it fails on omics data
    clarifies why purpose-built methods are necessary.  

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


Count data from sequencing platforms violates all four. The following
sections work through what goes wrong at each level of sophistication,
from a naive t-test on raw counts through to the negative binomial
models used in practice.

??? info "Statistical violations by platform"

    The table below summarises which t-test assumptions are violated
    by each major omics data type and the primary additional problem
    each platform introduces.

    **Note: the spatial omics row requires expert verification before
    finalising.**

    | Platform | Violation 1: not absolute | Violation 2: distribution | Violation 3: variance not homogeneous | Violation 4: small n | Primary additional violation |
    |---|---|---|---|---|---|
    | **Bulk RNA-seq** | Counts reflect sequencing depth, not absolute expression. A gene with 200 counts in one sample and 100 in another may represent identical expression at different depths. | Most genes have very low counts. Values of 0, 1, and 2 cannot be approximated by a normal distribution. Count data is discrete and right-skewed. | Lowly expressed genes are systematically more variable than highly expressed ones. Standard tests assume constant variance across the range. | With n = 3, each gene's variance is estimated from 2 degrees of freedom. Estimates are unreliable by chance alone. | **Overdispersion.** Biological replicates show more variability than a Poisson model predicts. A negative binomial distribution is required. |    
    | **Proteomics · metabolomics** | Signal intensity is measured relative to the total ion signal, so loading and ionisation differences shift all features together. | After log2 transformation, intensities are approximately normal, this violation is largely resolved by transformation. | Lower abundance features show higher relative variability. Variance changes systematically across the intensity range even after transformation. | Thousands of features, each with variance estimated from a handful of replicates, produces systematically unreliable test statistics. | **Missing Not At Random (MNAR).** Missing values are concentrated in low abundance features. MAR imputation assigns plausible looking values to systematically absent features, producing biased comparisons. |
    | **Microbiome** 16S · metagenomics | Total microbial biomass is lost during sequencing. Relative abundances sum to 100% regardless of how many organisms are present. | Count data is discrete and overdispersed, as in bulk RNA-seq. | Variance increases at low counts, as in bulk RNA-seq. Low-abundance taxa are systematically more variable. | Same small n problem. Per-taxon variance estimates are unreliable with typical sample sizes. | **Compositional independence violation.** Features are mathematically constrained against each other.  Methods that ignore compositionality may produce misleading inferences, even when the count distribution (like negative binomial model) itself is modeled appropriately, because the independence assumption is violated. |
    | **Single-cell RNA-seq** 10x · SMART-seq2 | Total UMIs per cell varies substantially. Within cell compositionality means dominant transcripts compress apparent signal from all other genes in the same cell. | Count data is discrete, zero inflated, and overdispersed:- more severely than bulk RNAseq due to dropout and shallow per cell depth. | Within cell variance is extreme. The same gene can show counts of 0 and 5 in cells of the same type due to stochastic capture, not biology. | Per gene variance is highly unreliable at the single cell level due to extreme sparsity. | **Pseudoreplication.** Cells from the same donor are not independent biological replicates. Treating 50,000 cells from 5 donors as n = 50,000 inflates degrees of freedom by orders of magnitude. Distributional assumptions alone cannot solve pseudoreplication; donor-level structure must be modeled through pseudobulk aggregation or hierarchical/mixed-effects approaches. |

## From naive to principled: four levels

The progression below uses **bulk RNA-seq as the working example**
because it is the most widely used and has the most mature statistical
literature. The core logic, **variance shrinkage across features**
applies to all omics platforms, with platform specific adaptations
noted at the end.

---

### Level 1: t-test on raw counts, treating RNA-seq like microarrays (incorrectly)

Applying a standard t-test directly to raw count data fails
immediately on all four assumptions:

- Counts depend on sequencing depth (not directly comparable across samples)
- Data are discrete and heavily skewed (not normally distributed)
- Variance is not homogeneous, it scales with the mean
- With n = 3, variance per gene is extremely unstable

So in practice, this approach produces unreliable results and should not be used.
---

### Level 2: t-test on log-normalised counts (log CPM); partial fix, partial problem

A common next step:

1. Normalise for library size (CPM)
2. Apply a log2 transformation
3. Run a t-test

This helps because:

- Samples become more comparable after normalization
- Log transform reduces skew and stabilises large values

For moderately/highly expressed genes, this often behaves reasonably well.

Two problems remain.

**Problem 1: low counts still behave poorly.** At low expression levels (0–10 counts), small absolute changes become large fold changes after log transformation. This creates the classic “fan shape” in MA plots: high variability at low expression.

Importantly, much of this variability is not biological, it reflects sampling noise.


**Problem 2: variance is still estimated per gene (major issue)** Each gene gets its own variance estimate based only on its few replicates.

With n ≈ 3–5:

some genes appear artificially stable
others appear artificially variable
differences are often just random noise

So we fix mean scaling and distribution shape, but variance remains unreliable.

---

### Level 3: limma-voom; learning which observations we can trust

**limma-voom** retains the idea of working with log-transformed data
but improves the two weakest points: unequal reliability and unstable variance estimates.

#### A) Mean–variance relationship (voom weights)

Across a dataset, variability is not random, it follows a pattern.
Lowly expressed genes are consistently more variable than highly
expressed ones. Rather than ignoring this, `voom` estimates the
mean–variance relationship across all genes and uses it to assign
**precision weights**:

- Observations expected to be noisy (low counts) get lower weight
- More stable observations get higher weight

So the model no longer treats every data point equally.

This turns the analysis into a [weighted linear model](https://link.springer.com/article/10.1186/gb-2014-15-2-r29), where unreliable measurements contribute less to the final result.

#### B) Empirical Bayes variance shrinkage

limma stabilises variance estimates using an **empirical Bayes**
approach. Instead of relying entirely on the variance of a single
gene, it shrinks each gene's estimate toward a global trend derived
from all genes in the dataset.

!!! tip "What empirical Bayes does and does not do"
    Empirical Bayes does not change the model structure. It improves
    how the model parameters are estimated, by drawing on information
    from all genes rather than each gene in isolation.

In practice this means noisy estimates from small sample sizes are
stabilised, the effective degrees of freedom increase, and test
statistics become more reliable. This borrowing of strength across
genes is the key conceptual shift that separates modern omics methods
from naive approaches.

![Schematic illustration](figs_m2/02_limma-voom-deseq2-cpm-raw_v01.png){style="width:100%; height:auto; min-height:500px"}

<small>**Figure** Conceptual illustration of how successive methodological improvements in RNA-seq analysis increase the separation of biological signal from noise. Point locations represent simulated ground truth rather than software output. The visual progression is schematic and reflects variance moderation, information sharing across genes, and (where applied) effect-size shrinkage.
</small>

### Level 4: DESeq2 and edgeR, modelling counts directly

Rather than transforming the data to approximate normality, **DESeq2**
and **edgeR** model the raw counts directly using a **negative
binomial distribution**.

Why this matters:

RNAseq variability is not purely Poisson (technical sampling noise). There is also:

biological variability between samples
library preparation effects
unobserved heterogeneity

This extra variability is called overdispersion, and the negative binomial explicitly models it.

Var(Y) = μ + ϕμ²

Where:

μ = mean expression
φ = dispersion (extra biological variability)
The key idea is the same as limma:

Both methods:

estimate a mean–variance relationship across all genes
shrink gene-specific dispersion estimates toward that trend
borrow information across the entire dataset

Difference is only in representation:

limma: works on log-expression (Gaussian model)
DESeq2/edgeR: works on counts (negative binomial GLM)

Rather than transforming the data to approximate normality, DESeq2 and edgeR model the counts directly using a negative binomial distribution. This is particularly helpful at low expression levels, where log-transformed data can exhibit unstable fold changes and sampling noise can be amplified by the transformation. Modelling counts directly avoids many of these artefacts.

Much of the practical improvement comes from estimating dispersion more accurately by borrowing information across genes. The distinction between Poisson and negative binomial models becomes increasingly important at higher expression levels, where biological overdispersion, represented by the φμ² term dominates the variance. In this regime, a pure Poisson model can substantially underestimate variability between biological replicates.

!!! note "Fold-change shrinkage is a separate step"
    Empirical Bayes dispersion shrinkage improves standard errors,
    variance estimates, and p-values, but it does not itself pull
    fold-change estimates toward zero.

    The Level 4 panel is a conceptual illustration of improved
    signal-to-noise separation rather than the exact output of a
    DESeq2 analysis. In practice, additional shrinkage of
    log-fold-change estimates requires a separate step. In DESeq2,
    this is performed using `lfcShrink()` and is not part of the
    default `DESeq()` → `results()` workflow.
---

## Putting it all together

| Method | What it fixes | What still breaks |
|---|---|---|
| t-test on raw counts | nothing | everything (scale, distribution, variance) |
| t-test on log CPM | scaling + skew | unstable variance; poor low-count behaviour |
| limma-voom | unequal reliability + variance shrinkage | still approximate at very low counts |
| DESeq2 / edgeR | full count model + shrinkage | Very low count genes still require filtering; sensitive to extreme outliers (Cook's distance) |

## The key conceptual shift (most important takeaway)

Across all modern methods, the improvement is not "a better test."

It is this:

> **We stop estimating variance independently for each gene. Instead,
> we learn the variance structure from all genes and share information
> across them.**

This is what makes RNAseq analysis statistically stable with small
sample sizes.

## Practical message (for biologists)

Most RNAseq experiments have too few replicates to estimate gene-wise
variability reliably.

Modern methods (limma-voom, DESeq2, edgeR) work because they:

- recognise that gene-wise variability cannot be estimated reliably
  from small sample sizes
- borrow information across thousands of genes to stabilise those
  estimates

That is why they outperform simple t-tests, not because they are
more complex, but because they are more statistically honest about
what can and cannot be estimated from the data.

---

## The same principle applies across platforms

The core challenge is widespread across high dimensional omics data:
the number of measured features far exceeds the number of biological
replicates, making feature-specific variance estimates unstable and
unreliable.

Although the statistical models differ across platforms, successful
modern methods share a common principle:

> **Information is not estimated independently for each feature.**

Instead, features collectively inform the estimation of variance,
dispersion, compositional structure, missingness patterns, or other
parameters that cannot be reliably estimated from a single feature
alone. This is what makes modern methods work at typical omics sample
sizes, not just a better distributional assumption, but a
fundamentally different way of using the data.

- **Single-cell RNAseq**: individual cells are not independent
  biological replicates. Pseudobulk aggregation to the donor level
  before applying bulk methods (DESeq2, edgeR) is a widely recommended
  approach because it avoids pseudoreplication and performs well in
  benchmarking studies.

- **Microbiome**: sequencing data are compositional, only relative
  abundances are observed, and the observed total is determined by the
  sampling process rather than the true total microbial load.
  Applying count-based differential abundance methods without
  accounting for compositionality can produce spurious differential
  abundance calls. Methods based on log-ratio transformations or
  compositionally aware models are generally preferred.

- **Proteomics and metabolomics**: after log transformation, intensity
  measurements are often reasonably approximated by continuous models,
  and limma's empirical Bayes framework is widely used. Missing values
  require careful handling, particularly when missingness is likely to
  be non-random (MNAR); several modern workflows handle this within
  the model rather than through imputation.

- **Methylation arrays**: linear models on M-values with empirical
  Bayes shrinkage (limma) are standard. In heterogeneous tissues such
  as blood, estimated cell-type composition is commonly included as a
  covariate to reduce confounding with methylation state.

| Platform | Primary challenge | Appropriate framework | Key methods |
|---|---|---|---|
| Bulk RNA-seq | Overdispersed counts | Negative binomial model with empirical Bayes shrinkage | DESeq2, edgeR |
| Bulk RNA-seq | Mean-dependent variance after log transformation | Weighted linear model with empirical Bayes | limma-voom |
| Proteomics · metabolomics | Heteroscedastic continuous intensities; missing values | Linear model with empirical Bayes; careful handling of missingness | limma, MSstats |
| Methylation arrays | Non-constant variance of β-values; cell composition confounding in heterogeneous tissues | Linear model on M-values with empirical Bayes; cell-type covariates where appropriate | limma, minfi, ChAMP |
| Microbiome | Compositional data | Log-ratio transformation; compositionally aware models | ALDEx2, ANCOM-BC |
| Single-cell RNA-seq | Pseudoreplication; count overdispersion | Pseudobulk aggregation followed by bulk RNAseq methods | DESeq2, edgeR |
| Spatial omics *(emerging)* | Spatial dependence; spot-level cell-type mixing | Spatially aware statistical models (active research area) | SPARK, SpatialDE (spatially variable genes); RCTD, cell2location (spot deconvolution) |

---

## What to take forward

The takeaway is not that classical statistics are wrong. It is that
they rely on assumptions that do not hold for this type of data,
especially at low counts and small sample sizes.

> **Modern methods do not just change the distributional assumptions
> of the model. They change how information is shared across the
> dataset to produce stable inference where a feature-by-feature
> approach cannot.**

!!! info "Coming up in Module 4"
    Normalisation mechanics, how TMM, size factors, CPM, and
    variance-stabilising transformations work and when each is
    appropriate are covered in **Module 4**.

---

## Module 2 summary

The five sections of this module have built a connected picture of
why omics data requires its own analytical framework:

- **Section 2-1**: counts and intensities are the two primary data
  types; how they are generated determines their statistical
  properties
- **Section 2-2**: sequencing counts are relative measurements
  constrained by a finite sequencing budget; depth variation must be
  corrected before cross-sample comparison is valid
- **Section 2-3**: zeros have four distinct causes- biological,
  technical, sampling, and analytical; misclassifying them propagates
  errors into differential expression, imputation, and correlation
  analyses
- **Section 2-4**: features are compositionally constrained; a genuine
  change in one feature creates apparent changes in all others, and
  standard normalisation does not remove this constraint
- **Section 2-5**: classical t-tests fail on count data not simply
  because the distribution is non-normal, but because per-feature
  variance cannot be reliably estimated from small n; limma-voom,
  DESeq2, and edgeR solve this by borrowing variance information
  across all features simultaneously

!!! tip "Practical"
    For the practical exercises, download and open the `.html` file
    in Chrome or Edge.
