# Module 2 : Data types and core statistical properties

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  

    - Explain what a sequencing count represents and why raw counts
      cannot be compared directly across samples without accounting for
      sequencing depth.  
    - Distinguish between a biological zero (a feature genuinely absent)
      and a technical zero (a feature below detection), and explain why
      treating both identically leads to incorrect biological conclusions.  
    - Explain compositionality and relative abundance in intuitive terms
      and describe why naive fold change and correlation analyses can be
      misleading in compositional data.  
    - Recognise that omics count data violates the core assumptions of
      classical statistical tests, and understand why this necessitates
      platform specific approaches such as DESeq2 and edgeR.  

## Section 1: What a count actually is ?

Before jumping into interpretation, it helps to pause on a simpler question: what does a number in a count matrix actually represent?

In most everyday measurements, numbers are absolute. If one patient weighs 80 kg and another weighs 60 kg, the comparison is straightforward. The value doesn’t depend on anything else being measured at the same time.

Sequencing counts don’t behave like that.

### Counts reflect sampling, not absolute quantity

When you sequence an RNA-seq library, the machine isn’t counting every RNA molecule in the sample. Instead, it samples a fixed number of fragments — say 20 million or 40 million reads, depending on how deeply the library was sequenced.

In practice, that means each gene’s count is just a share of the total reads you happened to collect. So a gene’s observed count depends on two things:

- How much RNA it actually produced  
- How many reads were generated overall

A simple example makes this concrete:

| | Sample A | Sample B |
|---|---|---|
| **Total reads sequenced** | 20 million | 40 million |
| **Gene X raw count** | 100 | 200 |


At first glance, Gene X looks like it doubled in Sample B. But if you look at proportions, both samples show the same value (0.0005% of the library). The difference in counts comes entirely from the difference in sequencing depth.

You’ll see this kind of pattern all the time in real data. Without accounting for depth, it’s easy to call changes that aren’t actually there.

### Depth affects detection, especially for lowly expressed genes

Depth doesn’t affect all genes equally.

Highly expressed genes tend to show up reliably even when sequencing is relatively shallow. Lowly expressed genes are a different story. At lower depth, they might show up as small counts in one sample and zeros in another, simply because there weren’t enough reads to capture them consistently.

This is where interpretation gets tricky. A zero doesn’t always mean absence. Sometimes it just means the gene wasn’t picked up in that particular sequencing run.

If you sequence more deeply, those same genes often appear more consistently. The biology hasn’t changed, you’re just getting a better look at it.

![Shallow vs deep sequencing: how depth affects gene detection](module2Figs/02_shallow_vs_deep_sequencing_v2.jpg){width=100%}


From a study design perspective, this matters more than people expect. The depth you need depends on the weakest signal you care about. If depth is too low, low-abundance features start dropping in and out of detection, and that shows up later as zeros.

### Where the problem starts: before sequencing even begins

Depth is only part of the story.

Before sequencing even happens, the library preparation step can shift what ends up being measured. PCR amplification is necessary to generate enough material, but it isn’t perfectly even. Some fragments amplify more efficiently than others, especially early on.

Small differences at that stage can get amplified quickly. By the time the library is sequenced, some molecules are over-represented while others are under-represented, regardless of their original abundance. So by the time you see a count, two things have already happened:

- molecules were unevenly amplified
- a subset of them was sampled during sequencing

Both introduce variability before any analysis begins.

![PCR amplification and sampling zeros (Jiang et al. 2022, Fig 3)](module2Figs/02_zero_Toy_Examplle_v1.png){width=90%}. 
<small>. 
Ref: [Jiang et al. *Genome Biology* 2022](https://link.springer.com/article/10.1186/s13059-022-02601-5){target="_blank"}</small>

The figure above (Jiang et al. 2022, Fig 3) shows this concretely. Five
genes start at equal cDNA concentrations. After PCR amplification, their
relative proportions have shifted not because of biology, but because
of stochastic amplification differences. When sequencing is then limited
to a fixed depth, Gene 1 receives zero reads in three out of five
hypothetical experiments. It was present. It was amplified. It was simply
unlucky enough to be underrepresented at the moment the reads were
sampled.


### Depth differences are common, and not always random

In real datasets, samples rarely have identical library sizes. Two-fold differences are quite common, even with careful protocols. There are a few usual reasons for this:

- variation in RNA quality
- differences in library prep efficiency
- sequencing variability across runs or lanes

In principle, these are technical effects. In practice, they don’t always distribute evenly across your conditions.

For example, one tissue type might consistently yield lower quality RNA, or one batch might perform worse during library prep. When that happens, sequencing depth ends up correlated with the biological groups you’re trying to compare.

That’s where problems start.


A typical scenario looks like this: one group has systematically lower depth, and genes appear downregulated across the board. It can look like a strong biological signal, but it’s really just fewer reads being assigned overall.

A quick check, like plotting library sizes by condition, often makes this obvious. If the distributions don’t overlap much, it’s something you need to deal with before moving forward.

Normalisation helps, but it doesn’t fully fix cases where depth is tightly confounded with biology. At that point, it’s more of a design issue than an analysis problem.


### The same logic applies across omics platforms: the terminology differs, not the principle

The same idea shows up across other omics platforms.

- In single-cell RNA-seq, each cell has its own sequencing depth, often measured as total UMI counts, and the variation can be substantial.
- In microbiome data, total reads per sample vary widely, especially in low biomass settings.
- In proteomics and metabolomics, the equivalent is total ion signal rather than read count.

Different technologies, same underlying issue: the numbers reflect how much of the total signal was captured, not an absolute quantity.

### What this means before you touch the analysis?

Raw counts must be normalised before any cross sample comparison is
valid. The appropriate normalisation strategy depends on the platform,
the experimental design, and the biological question being asked.
Choosing the wrong approach introduces new artefacts. This is covered
in full in **Module 5: Normalisation and Scaling**.

### What to take forward

The main point to carry forward is simple:

> A count is not an absolute measurement. It reflects how much of a sample was    captured under a particular sequencing budget.

Because that budget varies between samples, raw counts can’t be compared directly. Some form of normalisation is needed before making cross-sample comparisons.

We’ll get into how to do that later. For now, the important thing is to keep in mind what these numbers actually represent — and what they don’t.

## Section 2: Sparsity and zero inflation — not all zeros mean the same thing

In Section 1, we saw that counts reflect a limited sampling process rather than absolute quantities. A direct consequence of that is something you’ll notice immediately in real datasets:

**most entries in an omics count matrix are zero.**

This often feels alarming at first, especially if you’re coming from bulk measurements. In reality, it’s expected. The challenge is not the presence of zeros — it’s understanding what they actually represent.

## Sparsity is normal

Omics datasets are sparse because you’re trying to measure a very large number of features with a finite budget. How sparse things get depends on the platform:

| Platform | Typical zero rate | Main reason |
|---|---|---|
| Bulk RNA-seq | 10–40% | Many genes genuinely not expressed |
| 10x scRNA-seq | >90% | Shallow depth per cell + capture inefficiency |
| SMART-seq2 | 60–80% | Better detection per cell, but still limited |
| 16S / metagenomics | 50–90% | True absence + undersampling of rare taxa |
| Proteomics (DDA) | 10–50% missing | Below detection limit |
| Metabolomics | 20–50% missing | Detection limits + ionisation variability |

If you’re working with single-cell data, the numbers can look extreme. Seeing >90% zeros is completely normal for droplet-based platforms like 10x. It’s not a quality issue. It’s how the technology works.

## Not all zeros mean the same thing

A zero in the matrix just means “nothing was detected.” It does **not** tell you why. In practice, there are three main reasons a zero can appear:

### 1. Biological zeros

These are the straightforward ones. The feature really is absent.

- A gene is not expressed in a given cell type  
- A microbe is not present in a sample  
- A protein is not produced under certain conditions  

These zeros carry biological meaning and should be preserved.


### 2. Technical zeros

Here, the molecule exists, but it never makes it into the data. 
- In single-cell RNA-seq, for example, only a fraction of transcripts are captured during library preparation. Capture efficiency can be as low as 10–15%, so most molecules are simply lost before sequencing.

The result: zeros that reflect **failure to capture**, not true absence.

### 3. Sampling zeros

These arise later in the process. A molecule may be present and even successfully amplified, but still not get sequenced because:

- it was rare to begin with  
- amplification didn’t favour it  
- sequencing depth was limited  

This is essentially bad luck in the sampling step.


![Sources of zeros in scRNAseq data: biological, technical, and sampling](module2Figs/01_zero_technical_Biological_v1.png){width=90%}

<small>Adapted from: [Jiang et al. *Genome Biology* 2022](https://link.springer.com/article/10.1186/s13059-022-02601-5){target="_blank"} (CC BY 4.0)</small>

## The tricky part: they look identical

In the count matrix, all three cases are just zeros.

There’s no flag that tells you whether a zero is biological, technical, or due to sampling. Interpreting them requires context:   
- how highly the feature is expressed elsewhere  
- the sequencing depth  
- the platform you’re using  
- what you expect biologically  

This is why zero handling isn’t something you can fully automate.

## A simple example

Consider a gene measured across four single cells:

| Cell 1 | Cell 2 | Cell 3 | Cell 4 |
|---|---|---|---|
| 0 | 0 | 3 | 0 |

It’s tempting to say the gene is “off” in most cells.

But with typical single-cell capture rates, it’s just as plausible that the gene is expressed at low levels in all four cells, and only one of them happened to register counts.

You can’t resolve that ambiguity from this table alone.

## Same zero, different meaning

Context changes everything.

- If a gene known to be T-cell specific is zero across B cells, that’s almost certainly a biological zero.  
- If the same gene shows patchy detection across T cells, that pattern is more consistent with sampling or technical zeros.  

Treating both situations the same leads to incorrect conclusions.

## Platform matters

What a zero *likely* means depends heavily on the technology.

- **Bulk RNA-seq:** most zeros are biological, since expression is averaged across many cells.  
- **Droplet-based scRNA-seq (e.g. 10x):** many zeros come from limited capture and shallow depth.  
- **SMART-seq2:** higher sensitivity per cell, but amplification noise plays a larger role.  
- **Microbiome data:** zeros can reflect both true absence and undersampling of rare taxa.  
- **Proteomics/metabolomics:** missing values often mean “below detection limit,” not absence.  

The same number (0) carries different implications depending on where it came from.

## What goes wrong if you ignore this

Treating all zeros as the same causes problems downstream.

- **Differential expression:** differences in detection rates can look like biological changes  
- **Correlation analysis:** shared zeros can create artificial relationships between features  
- **Imputation:** filling in values can introduce signals that were never actually there  

These issues don’t show up immediately, but they can distort results in subtle ways.

## What to take forward

The key point is simple:

> **A zero is not a single thing. It’s an observation with multiple possible explanations.**

Before deciding how to handle zeros, you need to think about:  
- the platform  
- the depth  
- the biology you expect  

Zeros aren’t just missing data to “fix.” They’re part of the measurement process, and interpreting them correctly is essential for everything that follows.


??? abstract "Further reading, Zero inflation and sparsity in omics"

    **Conceptual framework, applies across all platforms**

    Jiang R, Sun T, Song D, Li JJ. Statistics or biology: the
    zero-inflation controversy about scRNA seq data. *Genome Biology*
    2022; 23: 31.
    [doi:10.1186/s13059-022-02601-5](https://doi.org/10.1186/s13059-022-02601-5){target="_blank"}

    Silverman JD, Roche K, Mukherjee S, David LA. Naught all zeros
    in sequence count data are the same. *Computational and Structural
    Biotechnology Journal* 2020; 18: 2789–2798.
    [doi:10.1016/j.csbj.2020.09.014](https://doi.org/10.1016/j.csbj.2020.09.014){target="_blank"}
    *(Covers both transcriptomics and microbiome zeros in a single framework)*

    ---

    **Single cell RNAseq**

    Svensson V. Droplet scRNA-seq is not zero-inflated. *Nature
    Biotechnology* 2020; 38(2): 147–150.
    [doi:10.1038/s41587-019-0379-5](https://doi.org/10.1038/s41587-019-0379-5){target="_blank"}

    Wang X, He Y, Zhang Q, Ren X, Zhang Z. Direct comparative analyses
    of 10X Genomics Chromium and Smart-seq2. *Genomics Proteomics
    Bioinformatics* 2021; 19(2): 253–266.
    [doi:10.1016/j.gpb.2020.02.005](https://doi.org/10.1016/j.gpb.2020.02.005){target="_blank"}

    Ding J et al. Systematic comparison of single-cell and
    single-nucleus RNA-sequencing methods. *Nature Biotechnology*
    2020; 38: 737–746.
    [doi:10.1038/s41587-020-0465-8](https://doi.org/10.1038/s41587-020-0465-8){target="_blank"}

    Hou W et al. A systematic evaluation of single-cell RNA-sequencing
    imputation methods. *Genome Biology* 2020; 21: 218.
    [doi:10.1186/s13059-020-02132-x](https://doi.org/10.1186/s13059-020-02132-x){target="_blank"}

    ---

    **16S amplicon and metagenomics**

    Kaul A, Mandal S, Davidov O, Peddada SD. Analysis of microbiome
    data in the presence of excess zeros. *Frontiers in Microbiology*
    2017; 8: 2114.
    [doi:10.3389/fmicb.2017.02114](https://doi.org/10.3389/fmicb.2017.02114){target="_blank"}

    ---

    **Proteomics**

    Lazar C, Gatto L, Ferro M, Bruley C, Burger T. Accounting for the
    multiple natures of missing values in label-free quantitative
    proteomics data sets to compare imputation strategies.
    *Journal of Proteome Research* 2016; 15(4): 1116–1125.
    [doi:10.1021/acs.jproteome.5b00981](https://doi.org/10.1021/acs.jproteome.5b00981){target="_blank"}
    *(Foundational paper on MNAR/MAR classification, the conceptual basis
    for why not all missing values in proteomics should be treated the same)*

    Kong W, Hui HWH, Peng H, Goh WWB. Dealing with missing values in
    proteomics data. *Proteomics* 2022; 22(23–24): e2200092.
    [doi:10.1002/pmic.202200092](https://doi.org/10.1002/pmic.202200092){target="_blank"}
    *(Practical decision chart for method selection, recommended reading
    before the imputation)*

    ---

    **Metabolomics**

    Do KT, Wahl S, Raffler J et al. Characterization of missing values
    in untargeted MS-based metabolomics data and evaluation of missing
    data handling strategies. *Metabolomics* 2018; 14: 128.
    [doi:10.1007/s11306-018-1420-2](https://doi.org/10.1007/s11306-018-1420-2){target="_blank"}

## Section 3: Compositionality — you are always looking at a pie chart

In Section 1, we established that counts depend on sequencing depth. In Section 2, we saw that many entries are zero, and that those zeros are not all the same.

There’s a third property that follows directly from how the data is generated, but it’s easy to overlook:  **counts are compositional.**

## The fixed total problem

When you sequence a sample, you generate a fixed number of reads. Every read assigned to one feature is a read that cannot go to another.

So the counts are not independent. They are all competing for the same total.

In practical terms, this means that if one gene takes up a larger share of the reads, the relative share of other genes must decrease, even if their actual expression hasn’t changed.

A useful way to think about it:

> You are always looking at a pie chart, not a bar chart.

A bar chart shows absolute quantities. A pie chart shows proportions. Sequencing data gives you proportions.

## A simple example

Imagine a sample with three genes:

| Gene | Sample 1 | Sample 2 |
|---|---|---|
| A | 100 | 200 |
| B | 100 | 100 |
| C | 100 | 100 |
| **Total reads** | 300 | 400 |

Gene A doubled in absolute counts. Genes B and C stayed the same.

Now look at proportions:

| Gene | Sample 1 | Sample 2 |
|---|---|---|
| A | 33% | 50% |
| B | 33% | 25% |
| C | 33% | 25% |

Genes B and C appear to decrease, even though nothing about them actually changed.

This isn’t a measurement error. It’s just arithmetic.

## Why this matters in practice

Once you start looking at proportions, it becomes easy to misinterpret what’s changing.

### Apparent increases may not be real

A gene can appear to increase simply because other genes decreased.

You’ll see this often in microbiome data. If most species drop after a treatment, the remaining ones automatically take up a larger fraction of the total, even if their absolute abundance stayed the same.


### Apparent decreases may not be real

The reverse also happens.

A gene can genuinely increase in absolute terms, but still look flat or even decreased if other features increased more strongly. This can make real biological signals harder to detect.

## Correlation becomes tricky

Compositional data also affects how features relate to each other.

Because everything shares the same total, features are constrained. If one goes up, others must go down in relative terms.

This creates artificial negative correlations.

Two genes with no biological relationship can appear negatively correlated simply because they are competing for the same pool of reads. If you build networks directly from these correlations, you can end up with edges that reflect this constraint rather than real biology.

## Normalisation doesn’t remove this

It’s important to be clear about what normalisation does and does not do.

Normalisation methods (CPM, TPM, size factors, etc.) adjust for differences in total library size between samples. They make samples comparable. But after normalisation, the data is still compositional. You still have proportions of a total, and the same constraints apply.

## Where this shows up most strongly

Compositional effects are most obvious in:

- **Microbiome data (16S, metagenomics):** proportions are often the primary output  
- **Low biomass samples:** where a few features dominate the signal  
- **Single-cell data:** where shallow depth exaggerates competition between features  

But the same principle applies to bulk RNA-seq and other sequencing-based assays as well. It’s just sometimes less visible.

## What to take forward

The key point here is subtle but important:

> **A change in proportion is not the same as a change in absolute abundance.**

When working with count data, you are always dealing with relative measurements. That shapes how differences and relationships should be interpreted.

If this isn’t taken into account, it’s easy to:
- overstate increases  
- misinterpret decreases  
- infer relationships that aren’t actually there  


> **You are always looking at a pie chart, not a bar chart.**
> A bar chart shows you absolute quantities. A pie chart shows you
> proportions. Sequencing gives you a pie chart, and a larger slice
> for one gene automatically means smaller slices for all the others,
> regardless of what the biology actually did.

### A worked example: when proportions mislead

??? example "Case study: The antibiotic experiment that wasn't what it looked like"

    A researcher is studying the gut microbiome of mice before and after
    a heavy dose of antibiotics. They sequence stool samples from both
    time points.

    ![ anitbiotic_example](module2Figs/02_compositionality_v01.jpg){width=98%}
    ## Species Composition Summary

    | Species    | Before | After  | Reality                                                   |
    |------------|--------|--------|------------------------------------------------------------|
    | Species A  | 20%    | 80% ↑  | Unchanged, same absolute numbers                          |
    | Species B  | 30%    | 0%     | Below detection, not necessarily absent                   |
    | Species C  | 50%    | 20% ↓  | Reduced, but proportions distorted by biomass loss         |

    The researcher runs a standard statistical test on these percentages.
    Species A shows a dramatic and highly significant increase.

    **The published conclusion:** *"Antibiotic X acts as a growth booster
    for Species A."*

    ---

    **What actually happened:**

    The antibiotics killed 99% of all bacteria in the gut. Species A did
    not grow, its absolute numbers stayed the same. But because everything
    else was wiped out, Species A now represents 80% of what remains. The
    pie shrank dramatically; Species A's slice simply got bigger by
    default.

## Looking ahead

So far, we’ve seen three structural properties of omics data:

- counts depend on sequencing depth  
- zeros have multiple causes  
- features are compositionally constrained  

The next step is to bring these together and ask a practical question:

**what does this mean for statistical testing?**

That’s where standard approaches start to break down, and where specialised methods come in.


??? abstract "Further Reading · Compositionality in Omics Data"

    **Foundational framework**

    Gloor GB, Macklaim JM, Pawlowsky-Glahn V, Egozcue JJ.
    Microbiome datasets are compositional: and this is not optional.
    *Frontiers in Microbiology* 2017; 8: 2224.
    [doi:10.3389/fmicb.2017.02224](https://doi.org/10.3389/fmicb.2017.02224){target="_blank"}
    *(The accessible entry point, argues compositionality applies
    broadly, not only to microbiome data)*

    Quinn TP, Erb I, Richardson MF, Crowley TM. Understanding
    sequencing data as compositions: an outlook and review.
    *Bioinformatics* 2018; 34(16): 2870–2878.
    [doi:10.1093/bioinformatics/bty175](https://academic.oup.com/bioinformatics/article/34/16/2870/4956011){target="_blank"}
    *(Extends the compositional argument explicitly to RNA seq
    and other sequencing based platforms)*

    ---

    **The microbiome case, most extensively studied**

    Weiss S et al. Normalization and microbial differential abundance
    strategies depend upon data characteristics.
    *Microbiome* 2017; 5: 27.
    [doi:10.1186/s40168-017-0237-y](https://doi.org/10.1186/s40168-017-0237-y){target="_blank"}
    *(Practical benchmark showing how compositional structure
    affects normalization method choice)*

## Section 4: Why classical statistics struggle with count data

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

 !!! warning "Log transformation is not sufficient on its own"
    Log transforming count data before a t-test improves things but
    leaves two core problems unsolved: the normal approximation still
    fails for lowly expressed genes, and per gene variance estimates
    from small n remain unreliable. limma voom, DESeq2 and edgeR all
    include the moderation step that stabilises those estimates by
    borrowing information across genes, something a plain
    log + t-test cannot do.

??? abstract "Further Reading: Statistical models for omics count data"

    **The foundational tools**

    Love MI, Huber W, Anders S. Moderated estimation of fold change
    and dispersion for RNA seq data with DESeq2. *Genome Biology*
    2014; 15: 550.
    [doi:10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8){target="_blank"}
    *(DESeq2 , introduces shrinkage estimation for dispersions and fold
    changes; methods section explains why per gene variance estimation
    fails at small n)*

    Robinson MD, McCarthy DJ, Smyth GK. edgeR: a Bioconductor package
    for differential expression analysis of digital gene expression data.
    *Bioinformatics* 2010; 26(1): 139–140.
    [doi:10.1093/bioinformatics/btp616](https://doi.org/10.1093/bioinformatics/btp616){target="_blank"}
    *(edgeR , empirical Bayes moderation of tagwise dispersions toward
    a common value across genes)*

    Ritchie ME, Phipson B, Wu D, Hu Y, Law CW, Shi W, Smyth GK.
    limma powers differential expression analyses for RNA sequencing
    and microarray studies. *Nucleic Acids Research* 2015; 43(7): e47.
    [doi:10.1093/nar/gkv007](https://doi.org/10.1093/nar/gkv007){target="_blank"}
    *(limma voom , precision weights for heteroscedasticity plus
    empirical Bayes moderation; bridges RNA seq, microarray and
    proteomics in a single framework)*

    ---

    **Empirical validation**

    Schurch NJ et al. How many biological replicates are needed in an
    RNA seq experiment and which differential expression tool should
    you use? *RNA* 2016; 22(6): 839–851.
    [doi:10.1261/rna.053959.115](https://doi.org/10.1261/rna.053959.115){target="_blank"}
    *(48-replicate benchmark , n = 3 detects only 20–40% of true DE
    genes; tools with information sharing across genes outperform
    those without)*

    Gierliński M et al. Statistical models for RNA-seq data derived
    from a two-condition 48-replicate experiment. *Bioinformatics*
    2015; 31(22): 3625–3630.
    [doi:10.1093/bioinformatics/btv425](https://doi.org/10.1093/bioinformatics/btv425){target="_blank"}
    *(Empirical confirmation that per-gene counts are consistent with
    both NB and log-normal distributions; establishes the mean-variance
    relationship in real RNA-seq data)*

    Squair JW et al. Confronting false discoveries in single-cell
    differential expression. *Nature Communications* 2021; 12: 5692.
    [doi:10.1038/s41467-021-25960-2](https://doi.org/10.1038/s41467-021-25960-2){target="_blank"}
    *(Pseudobulk benchmark for scRNA-seq , 46 datasets showing why
    treating cells as independent replicates produces false discoveries)*

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

!!! info "End of Day 1 theory: coming up: practical session"
    The Day 1 practical session gives you the opportunity to observe
    these properties directly in a real dataset: examining count
    distributions, library depth variation, zero rates, and the
    mean variance relationship that motivates the tools covered in
    this section. The concepts from Modules 1, 2, and 3 will all
    appear in the data.

    Github Folder: For ***practical*** download and open .html file in Chrome/Edge Browser.