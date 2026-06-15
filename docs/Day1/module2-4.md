# Module 2.4: Compositionality: you are always looking at a pie chart

!!! info "Learning objectives" 

    By the end of this section, participants will be able to:  
    
    - Define compositionality and explain why it is a structural property of omics data rather than a technical artefact
    - Demonstrate with a worked example how a genuine biological change in one feature produces apparent changes in others
    - Identify which omics platforms are most severely affected and explain why severity differs across platforms
    - Describe what normalisation does and does not fix in compostional data 
    - Explain why standard normalisation reduces the depth problem but does not remove the compositional constraint

## TIME DURATION NOTE:: TO TO DELETED IN FINAL STAGE [Aimed for 8 mins: activities 4 mins]


In Module 2.1, we established that omics measurements are relative, a count or intensity reflects a share of a technical total, not an absolute molecular quantity. In module 2.2, we saw that many entries in omics matrices are zero and that those zeros hve different causes and meanings. 

There’s a third property that follows directly from how the data is generated, but it’s easy to overlook:  **counts are compositional.**

This means that what you observe in one feature is not determined solely by that feature's biology. It is constrained by everything else being measured at the same time. A change anywhere in the data creates the appearance of change everywhere, even when nothing has happened. This is a structural consequence of measuring a large number of features simultaneously with a finite technical budget. It appears across all omics platforms, under different names and with different severity. 

## The biological reality 

Omics instruments capture molecules up to a total capacity (e.g. a fixed number of reads, a finite ion signal, a bounded flouresence range). That total is distributed across all features present in the sample. 

The distribution is not independent. Features compete for the same budget, and their observed values are all shares of the same whole. As such, it is important to keep in mind, you are measuring proprotions not absolute quantities. And proportions are constrained to sum to a total, which means they are not independent of one another. 

In practical terms, this means that if one gene takes up a larger share of the reads, the relative share of other genes must decrease, even if their actual expression hasn’t changed.

!!! tip "You are always looking at a pie chart" 
    A useful way to think about it is that you are always looking at a pie chart, not a bar chart. A bar chart shows absolute quantities. A pie chart shows proportions. Sequencing data gives you proportions.

    Once you start looking at proportions, it becomes easy to misinterpret what’s changing.

## The statistical consequences 

### Apparent changes that are not real 

Because features share a fixed total, a genuine biological change in one feature changes the apparent relative abundance of other features, even those whose absolute abundance is unchanged. 

A simple example makes this arithmetic visible to us: 

| Gene | Sample 1 | Sample 2 | Reality | 
|---|---|---|---|
| A | 100 | 200 | Genuinely doubled|
| B | 100 | 100 | Unchanged |
| C | 100 | 100 | Unchanged |
| **Total reads** | 300 | 400 | Depth increase|

Now expressed as proportions:

| Gene | Sample 1 | Sample 2 | Apparent change | 
|---|---|---|---|
| A | 33% | 50% | Increased |
| B | 33% | 25% | Decreased |
| C | 33% | 25% | Decreased|

Genes B and C appear to decrease. Their counts are identical in both samples and nothing about them changed. The apparent decrease is entirely a consequence of Gene A taking a larger share of the total. 

In a real dataset with 20,000 genes, the same effect operates across the entire matrix but it is invisible without understanding what is driving it. 

### Correlations become unreliable 

Compositionality also distorts relationships between features. Because all features share the same total, they are mathematically constrained against each other. If one feature's relative share increases, the sum of all others must decrease. This introduces artificial negative correlations between features that have no biological relationship. 

TODO add an example like above? 

!!! danger "Standard normalisation does not fix this"
    Normalisation methods such as CPM, TPM, and DESeq2 size factors adjust for differences in total library size between samples. This makes samples more comparable. But after normalisation the data is still compositional. 
    
    You still have proportions of a total, and the same constraints still apply. Normalisation reduces the depth problem from module 2.1. It does not remove the compositional constraint.

## A worked example: antibiotic experiment 

You’ll see this often in microbiome data. If most species drop after a treatment, the remaining ones automatically take up a larger fraction of the total, even if their absolute abundance stayed the same.

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

## Compositionality across omics platforms 

The fixed-total constraint is present in all omics platforms. What changes between platforms is the unit of the budget, the severity of effect, and how visible it is in the data. 

TODO a table like this? 

| Platform | The "budget" | How compositionality manifests | Severity | Distinctive feature | Fixed by standard normalisation? |
|---|---|---|---|---|---|
| **Sequencing counts** RNA-seq · ATAC-seq · WGS | Total reads sequenced | Features compete for a fixed read pool. A strongly upregulated gene reduces the apparent share of all others, even unchanged ones. | Moderate | Diluted across 20,000+ features so less visible, but not absent. Highly expressed genes that change strongly exert the most distortion on surrounding features. | **No.** Depth normalisation (CPM, size factors) corrects between-sample depth variation but data remains compositional after normalisation. |
| **Microbiome** 16S amplicon · metagenomics | Total reads sequenced | Total microbial biomass is entirely lost during sequencing. Collapse of dominant taxa makes survivors appear to increase. A taxon can look like it grew when nothing about it changed. | Severe | Biomass information is unrecoverable without spike-ins or qPCR. Standard methods cannot distinguish absolute increase from relative re-scaling. | **No.** Rarefaction and relative abundance conversion do not remove the compositional constraint. Log-ratio methods (ALDEx2, ANCOM-BC) are required. |
| **Single-cell RNA-seq** 10x Chromium · SMART-seq2 | Total UMIs per cell | Operates at two levels: between cells (variable total UMIs) and within cells (all genes compete for a small per-cell budget). Dominant transcripts suppress apparent signal from everything else in the same cell. | Severe | Within-cell compositionality is distinct from dropout. A cell dominated by one highly expressed gene has its entire transcriptional profile distorted as a result. | **No.** Single-cell normalisation (scran, sctransform) corrects depth variation between cells but does not remove the within-cell compositional constraint. |
| **Proteomics · metabolomics** DDA · DIA · LC-MS | Total ion signal in injection | Signal intensity reflects a proportion of total ions detected. Inconsistent sample loading or concentration differences shift apparent abundances of all features simultaneously. | Moderate | In DDA mode, highly abundant proteins actively suppress detection of low-abundance ones at the isolation window — compositionality operates before quantification begins. | **Partially.** Total protein normalisation (proteomics) and global median normalisation (metabolomics) correct for loading differences, equivalent to depth normalisation in sequencing. |
| **Methylation arrays** EPIC · 450K | Methylated / total probe signal ratio | Each beta value is itself a composition (methylated ÷ total signal). Global methylation shifts — such as the hypomethylation common in cancer — distort all probes simultaneously. | Lower | The compositional constraint is explicit at the probe level. Global hypomethylation changes the reference point against which every probe in the array is interpreted. | **No.** Standard array normalisation (quantile, BMIQ) corrects technical variation but does not account for genuine global methylation differences between conditions. |
| **Spatial omics** Visium · Xenium · MERFISH | Total capture per spot or panel genes | Within each spot, cell types compete for the fixed capture budget. Dominant cell types suppress signal from minority populations. In targeted panels, a small gene set means each marker has a proportionally larger distorting effect on the others. | Moderate | Targeted panels (Xenium, MERFISH) amplify compositional effects — fewer features sharing the budget means each feature has a larger proportional influence on the rest. | **No.** Between-spot depth normalisation is standard but within-spot compositional mixing requires deconvolution methods (RCTD, STdeconvolve), not normalisation. |

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


## Looking ahead

So far, we’ve seen three structural properties of omics data:

- counts depend on sequencing depth  
- zeros have multiple causes  
- features are compositionally constrained  

The next step is to bring these together and ask a practical question:

**what does this mean for statistical testing?**

That’s where standard approaches start to break down, and where specialised methods come in.

