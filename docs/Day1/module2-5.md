
# Module 2.5: Why classical statistics struggle with omics count data

!!! info "Learning objectives" 

    By the end of this section, participants will be able to:  
    
    - Describe the key assumptions of standard statistical tests and identify which are violated by omics count data
    - Explain what overdispersion means in count data and why it
      requires a negative binomial model rather than a normal or
      Poisson approximation
    - Describe how variance borrowing across features (empirical Bayes variance shrinkage) is necessary with small samples sizes
    - Match appropriate statistical frameworks to major omics data types 

## TIME DURATION NOTE:: TO TO DELETED IN FINAL STAGE [Aimed for 10 mins: activities 5 mins]

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

The progression below uses **bulk RNAseq as the working example** because
it is the most widely used and has the most mature statistical
literature. The core logic, variance shrinkage across features,
applies to all omics platforms, with **platform specific adaptations
noted at the end**.


### Level 1: t-test on raw counts

Applying a standard t-test directly to raw count data fails
immediately on all four assumptions:

- Counts are not absolute, they depend on sequencing depth
- The distribution is discrete and heavily right-skewed, not normal
- Variance is not homogeneous, it scales with the mean
- With n = 3, there are only 2 degrees of freedom per gene, far too
  few for a stable variance estimate

Nothing is fixed. This approach should not be used.

### Level 2: t-test on log-normalised counts (log count per million (CPM))

A common next step is:

1. Normalise for library size (CPM)  
2. Apply a log transformation  
3. Run a t-test  

This fixes some of the obvious issues.

- Normalisation makes samples broadly comparable  
- Log transformation compresses the range (large values) and reduces skew  

For moderately and highly expressed genes, this approach can behave reasonably well, especially if you have many replicates.

But two problems remain.

#### Problem 1: low counts still behave poorly

For genes with very low counts, log transformation doesn’t really “fix” the data.

Values like 0, 1, and 2 are still effectively discrete after transformation, and small differences translate into large apparent fold changes. At the same time, lowly expressed genes tend to be more variable between replicates, independently of biology.

You can see this in practice as a characteristic “fan shape” in MA plots:  
at low average expression, the spread of log fold changes becomes very wide.

![MA plot without and with shrinkage (Derakhshani et al. (2020), CC BY)](module2Figs/02_MLE_plot_dispersion_v01.jpg){style="width:90%; height:auto; min-height:500px"}

This variability is not primarily biological, it reflects unstable estimates at low counts.

#### Problem 2: variance is still estimated per gene

Even after transformation, a standard t-test still treats each gene independently.

That means the variance estimate for gene X comes only from its own replicates. With small sample sizes, that estimate is noisy. Some genes will appear artificially stable, others artificially variable, just by chance.

The test has no mechanism to recognise or correct for this.

---

### Level 3: limma-voom package fixs the t-test framework

**limma-voom** keeps the general idea of working with log-transformed data, but changes how variability is handled.

It addresses the two problems above, directly.

#### Mean–variance weighting

Across the dataset, variability is not random, it follows a pattern.

Lowly expressed genes are consistently more variable than highly expressed ones. Instead of ignoring this, `voom` estimates the relationship across all genes and uses it to assign **precision weights**.

- Observations expected to be noisy (low counts) get lower weight  
- More stable observations get higher weight  

The model then fits a [weighted linear model](https://link.springer.com/article/10.1186/gb-2014-15-2-r29), rather than treating all points equally.

#### Empirical Bayes variance shrinkage (Borrowing information across genes)

limma also uses an **empirical Bayes** approach to stabilise variance estimates.

Instead of relying entirely on the variance of a single gene, it shrinks each estimate toward a global trend derived from all genes.

In practice, this means:

- noisy estimates from small sample sizes are stabilised  
- the effective degrees of freedom increase  
- test statistics become more reliable  

This “borrowing strength” across genes is one of the key ideas that makes modern methods work.


### Level 4: DESeq2 and edgeR, modelling counts directly

Rather than transforming the data, **DESeq2** and **edgeR** model the counts themselves.

They use the **negative binomial distribution**, which is well suited to count data with biological variability. This distribution has two parameters:

- a mean (expected count)  
- a dispersion term (extra variability between replicates)

This is important because real RNAseq data is more variable than a simple Poisson model would predict.

Like limma, both methods:

- estimate a mean–variance (mean–dispersion) relationship across all genes  
- shrink individual gene estimates toward that trend  
- effectively share information across the dataset  

They also incorporate normalisation internally and fit **generalised linear models**, which makes it straightforward to handle more complex experimental designs.

This approach is particularly important for **lowly expressed genes**, where log-based methods are least stable.

Most improvement comes from better estimation of variability, not just better distributions.

### Putting it together

| Approach | What it fixes | What remains wrong |
|---|---|---|
| t-test on raw counts | Nothing | Not comparable; discrete; normal approximation fails; variance estimates are unstable |
| t-test on log CPM | Makes samples comparable; improves behaviour at higher counts | Breaks down at low counts; per-gene variance still unreliable with small n |
| limma-voom | Accounts for mean–variance relationship; stabilises variance using empirical Bayes | Less reliable for very low counts |
| DESeq2 / edgeR | All of the above, and NB model for count data; Best for low count genes; equivalent to limma voom at higher counts  | ------------ |

The difference between these methods is not just the distribution they assume.

The key shift is this:

> **variance is no longer estimated gene by gene in isolation.**

Instead, each gene’s behaviour is interpreted in the context of all others.  

**edgeR vs limma-voom: what is actually different?**


| Component                  | limma-voom                         | edgeR                  |
| -------------------------- | ---------------------------------- | ---------------------- |
| Data scale                 | logCPM (continous)                 | raw counts (integers)  |
| Variance object            | residual variance (σ²)             | dispersion (φ)         |
| Model type                 | Gaussian linear model              | Negative Binomial GLM  |
| EB acts on                 | Gene wise variances.               | Gene wise dispersions  |
| Mean–variance relationship | estimated from data (Voom weights) | modeled in NB          |


### The same principle applies across platforms

The core problem, small sample sizes combined with thousands of
features gives unstable per-feature variance estimates is universal.
The distributional solutions differ by platform.

- **Single-cell RNA-seq**: cells are not independent biological
  replicates. Pseudobulk aggregation to the donor level before
  applying bulk methods (DESeq2, edgeR) is the principled approach.
- **Microbiome**: the compositional constraint means that
  even a well-specified count model still produces spurious results
  if independence is assumed. Log-ratio methods are required
  in addition to handling overdispersion.
- **Proteomics and metabolomics**: data are continuous after log
  transformation and approximately normal; limma's empirical Bayes
  framework applies directly. MNAR aware imputation strategies are
  needed before modelling.
- **Methylation arrays**: linear models on M-values with empirical
  Bayes shrinkage (limma) are standard; cell type deconvolution is
  needed to avoid confounding composition with methylation state.

The framework table below summarises the recommended approach for
each platform.

| Platform | Primary violation | Appropriate framework | Key methods |
|---|---|---|---|
| Bulk RNA-seq | Overdispersed counts; heteroscedastic variance | Negative binomial model with empirical Bayes shrinkage | DESeq2, edgeR |
| Bulk RNA-seq (high depth / many replicates) | Heteroscedastic log-space variance | Weighted linear model with empirical Bayes | limma-voom |
| Proteomics · metabolomics | Heteroscedastic continuous intensity; MNAR missing values | Linear model with empirical Bayes; MNAR-aware imputation | limma, MSstats |
| Methylation arrays | Bounded beta distribution; cell composition confounding | Linear model on M-values with empirical Bayes; cell type deconvolution | limma + minfi / ChAMP |
| Microbiome | Compositional counts; independence violation | Log-ratio transformation; compositionally aware models | ALDEx2, ANCOM-BC |
| Single-cell RNA-seq | Count overdispersion + pseudoreplication | Pseudobulk aggregation then bulk methods | DESeq2 / edgeR on pseudobulk |
| Spatial omics | Count distribution + within-spot mixing | Spatial-aware models; deconvolution [VERIFY WITH EXPERT] | SPARK, SpatialDE |

## What to take forward

The takeaway is not that classical statistics are wrong. It is that
they rely on assumptions that do not hold for this type of data,
especially at low counts and small sample sizes.

Modern methods do not just tweak the model. They change how
information is used across the dataset to produce stable inference
where a gene-by-gene approach cannot.

!!! info "Coming up in Module 4"
    Normalisation mechanics, how TMM, size factors, CPM, and
    transformations work and when each is
    appropriate, are covered in **Module 4**.

---

## Module 2 summary

The five sections of this module have built a connected picture of
why omics data requires its own analytical framework:

- **Section 2-1**: counts and intensities are the two primary data
  types; how they are generated determines their statistical
  properties
- **Section 2-2**: counts are relative measurements constrained by a
  finite sequencing budget; depth variation must be corrected before
  cross-sample comparison is valid
- **Section 2-3**: zeros have four distinct causes:- biological,
  technical, sampling, and analytical; misclassifying them propagates
  errors into differential expression, imputation, and correlation
  analyses
- **Section 2-4**: features are compositionally constrained;
  a genuine change in one feature creates apparent changes in all
  others, and standard normalisation does not remove this constraint
- **Section 2-5**: classical t-tests fail on count data not simply
  because the distribution is non-normal, but because per-feature
  variance cannot be reliably estimated from small n; limma-voom,
  DESeq2, and edgeR solve this by borrowing variance information
  across all features simultaneously

!!! tip "Practical"
    For the practical exercises, download and open the `.html` file
    in Chrome or Edge.
