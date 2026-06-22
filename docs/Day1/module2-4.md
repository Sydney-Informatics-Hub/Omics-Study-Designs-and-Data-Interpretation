# Module 2.4: Compositionality: you are always looking at a pie chart

!!! info "Learning objectives" 

    By the end of this section, participants will be able to:  
    
    - Define compositionality and explain why it is a structural property of omics data rather than a technical artefact
    - Demonstrate with a worked example how a genuine biological change in one feature produces apparent changes in others
    - Identify which omics platforms are most severely affected and explain why severity differs across platforms
    - Describe what normalisation does and does not fix in compostional data 
    - Explain why standard normalisation reduces the depth problem but does not remove the compositional constraint

## TIME DURATION NOTE:: TO TO DELETED IN FINAL STAGE [Aimed for 8 mins: activities 4 mins]


In Module 2.2 and 2.3, we established that omics measurements are relative, a count or intensity reflects a share of a technical total, not an absolute molecular quantity. We saw that many entries in omics matrices are zero and that those zeros have different causes and meanings depending on the paltform and context. 

There’s a third structural property that follows directly from how the data is generated, but it’s easy to overlook:  **counts are compositional.**

This means that what you observe in one feature is not determined solely by that feature's biology. It is constrained by everything else being measured at the same time. A genuine change anywhere in the data creates the *appearance* of change everywhere even in features whose
true abundance has not changed at all. 

It appears across all omics platforms, under different names and with different severity. It is a mathematical consequence of measuring many features simultaneously with a fixed total budget.

## What compositionality means

Omics instruments capture molecules up to a total capacity (e.g. a fixed number of reads in sequencing, a finite ion signal in mass spectrometry, a bounded flouresence range in arrays). That total is distributed across all features present in the sample. 

Because all features (genes/proteins) in a given sample share the same budget, their observed values are not independent of one another. Feature compete for a share of the total. If one feature's share increases, the relative share of all
others must decrease, not because their biology changed, but because the total is fixed.

!!! tip "You are always looking at a pie chart" 

    A bar chart shows absolute quantities, each bar stands on its own. A pie chart shows proportions, each slice is defined by its
    relationship to all the others. Omics output with fixed budget gives you a pie chart.

    A larger slice for one gene automatically creates smaller slices for all the others, regardless of what the biology actually did.

## The statistical consequences 

### Noticeable changes that are not real 

Because features share a fixed total, a genuine biological change in one feature changes the relative abundance of other features, even those whose absolute abundance is unchanged. 

A simple example makes this arithmetic concrete: 

| Gene | Sample 1 | Sample 2 | Reality | 
|---|---|---|---|
| A | 100 | **200** | Genuinely doubled|
| B | 100 | 100 | Unchanged |
| C | 100 | 100 | Unchanged |
| **Total reads** | 300 | 400 | Depth increase|

Now expressed as proportions:

| Gene | Sample 1 | Sample 2 | change | 
|---|---|---|---|
| A | 33% | 50% | Increased |
| B | 33% | 25% | Decreased |
| C | 33% | 25% | Decreased|

Genes B and C appear to decrease. Their counts are identical in both samples and nothing about them changed. The decrease is entirely a consequence of Gene A taking a larger share of the total. 

In a real dataset with 20,000 genes, the same effect operates silently across the entire matrix. The distortion is invisible without understanding what is driving it. 

### Correlations become unreliable 

The same constraint that create false fold changes also distorts relationships between features: becuase all features share the same total, they are mathematically constrained against each other. If one feature's relative share increases, the sum of all others must decrease. This introduces artificial correlation and negative correlations between features that have no biological relationship. 

| Gene | Sample 1 | Sample 2 | Sample 3 | Sample 4 |
|------|----------|----------|----------|----------|
| A    | 10%      | 20%      | 30%      | 40%      |
| B    | 45%      | 40%      | 35%      | 30%      |
| C    | 45%      | 40%      | 35%      | 30%      |
|------|----------|----------|----------|----------|
|Total | 100%     |   100%   |    100%  | 100%     |    

In above table, **only feature A increases** while features B and C remain unchanged in absolute abundance, the relative abundances of B and C must decrease because all features share a fixed total. Across samples this creates negative correlations between A and B/C, and positive correlations between B and C, despite no underlying biological relationship among them. This phenomenon arises solely from the compositional constraint


## A worked example: antibiotic experiment 

Compositionality is most visible in microbiome data. If most species drop after a treatment, the remaining ones automatically take up a larger fraction of the total, even if their absolute abundance stayed the same.

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

    This is not a growth efeect. It is a compositional artefact.

## Compositionality across omics platforms 
A compositional constraint is present to varying degrees across most omics platforms, although its mathematical form differs between sequencing based and signal based technologies.
The table below summarises how the fixed total constraint manifests across platforms and We will discuss in module 4, whether standard normalisation addresses it or not.

<!-- TODO a table like this?-->
<!-- This is not that simple with the proposed details initially, I will keep only what is relevant for this module .... Fixed by stansdard col required ....carefull evaluation and not relevant to this module... we will explain some normalization in the module 4. While, I am pretty familiat with transcriptomics related normalization but I may need to get some more knowledge for normalization in various omics field like proteomics, metabolomics etc
-->
<!-- -->
| Platform | The budget | How compositionality manifests | Severity |  
|---|---|---|---|
| **RNA-seq · ATAC-seq** | Total reads sequenced | Features compete for a fixed read pool. A highly upregulated gene reduces the proportional share of all others, including unchanged ones. Under conditions of global expression shifts, such as  global transcriptional amplification or broad transcriptional reprogramming, compositional bias can be substantial regardless of feature count. | Moderate-Severe  |
| **Microbiome** 16S · metagenomics · shotgun WGS | Total reads sequenced | Information about total microbial biomass is not retained in standard relative abundance sequencing. A decrease in the absolute abundance of a dominant taxon forces the relative abundances of all remaining taxa upward, even when their absolute counts are unchanged. | Severe |
| **Single-cell RNA-seq** 10x · SMART-seq2 | Total UMIs per cell | Operates at two levels: between cells (variable total UMIs reflecting capture efficiency) and within each cell (all genes compete for a small, highly variable per-cell UMI budget). Highly abundant transcripts occupy a larger share of the finite UMI budget, reducing the proportional representation of other transcripts. High sparsity amplifies the effect. | Severe | 
| **Proteomics · metabolomics** DDA · DIA · LC-MS | Total ion signal per injection | Signal intensity is proportional to abundance but also depends on molecule specific ionization efficiency and instrument response. Without external standards, absolute concentrations are generally not directly observable. Note: in DDA acquisition, stochastic precursor selection introduces an additional and distinct dynamic range bias — separate from, but compounding, the compositional constraint. | Moderate | 
 
## What to take forward

The key point here is subtle but important:

> **A change in proportion is not the same as a change in absolute abundance.**

When working with most high throughput omics measurements, the observed data are primarily relative rather than absolute. That shapes how differences and relationships should be interpreted.

If this isn’t taken into account, it’s easy to:
- overstate increases  
- misinterpret decreases  
- infer relationships that aren’t actually there  


> **You are always looking at a pie chart, not a bar chart.**
> A bar chart shows you absolute quantities. A pie chart shows you
> proportions. Sequencing gives you a pie chart, and a larger slice
> for one gene automatically means smaller slices for all the others,
> regardless of what the biology actually did.


## Looking ahead

So far, we’ve seen three structural properties of omics data:

- counts depend on sequencing depth  
- zeros have multiple causes  
- features are compositionally constrained  

The next step is to bring these together and ask a practical question:

**what does this mean for statistical testing?**

That’s where standard approaches start to break down, and where specialised methods come in.

