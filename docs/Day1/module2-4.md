
## Section 4: Why classical statistics struggle with count data

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  
    
    - Recognise that omics count data violates the core assumptions of
      classical statistical tests, and understand why this necessitates
      platform specific approaches such as DESeq2 and edgeR. 

Up to this point, we’ve built up three properties of omics count data:

- counts depend on sequencing depth  
- zeros arise from multiple processes  
- features are compositionally constrained  

None of these are edge cases. They are structural.

So the natural question is:

**what happens if you apply a standard statistical test anyway?**

The answer is not simply “it fails.” It’s more useful to think in terms of progressively better approximations — each step fixing a specific problem that the previous one leaves behind.

---

### Level 1: t-test on raw counts

This is the most direct approach, and also the least defensible.

A t-test on raw counts breaks down for several reasons at once:

- **Counts are not comparable across samples**  
  Differences in library size mean that the same gene can have higher counts in one sample purely due to deeper sequencing (Section 1)

- **The data are discrete and highly skewed**  
  Many genes have counts of 0, 1, or 2. The normality assumption underlying the t-test is not reasonable at this scale

- **Variance estimates are unstable at small n**  
  With 3 replicates per group, each gene’s variance is estimated from just 2 degrees of freedom. That estimate can easily be off by a large factor

Taken together, this produces unreliable test statistics and inflated false positives.

This is not a borderline case — it is simply the wrong model for the data.

---

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