# Module 2.2: Depth, Detection, and Platform Differences

!!! info "Learning objectives"

    By the end of this module, participants will be able to:

        - Explain why omics measurements are relative rather than absolute and describe the implications for comparing samples.
        - Describe how measurement depth influences feature (Genes/Taxa) detection and the appearance of zeros or missing values.
        - Identify the primary statistical challenge associated with major omics platforms and relate it to the underlying biological or technical process.
        - Explain why statistical methods and normalisation strategies cannot be applied uniformly across omics platforms and recognise when technical factors such as    depth, signal intensity, or sample composition may confound biological interpretation.

## TIME DURATION NOTE:: TO TO DELETED IN FINAL STAGE [Aimed for 10 mins; activities 5 mins]

## What the numbers in your data actually represent

By the time omics data reaches you as an analyst, it has already been through substantial processing. Raw sequence reads have been assembled into a continuous sequence or aligned to a reference assembly and summarised. Mass spectrometry signals have been detected and quantified. What you're working with in many cases, is often a **count matrix** or **abundance matrix**. 

In most everyday measurements, numbers are absolute. A patient who weighs 80 kg weighs 80 kg regardless of who else is in the room or how many measurements were taken that day. The value stands on its own. 

Omics data do not behave this way. ***Omics data reflect sampling, not absolute quantity***

Most omics platforms operate under a finite measurement budget, such as a fixed number of reads in sequencing, a fixed ion signal capacity in mass spectrometry, a bounded fluorescence range in arrays. 

As a result, **the count/abundance measured for any feature is relative rather than absolute**. Features effectively compete for a share of the total measurement capacity. Consequently, an increase in one feature can alter the observed abundance of other features, even if their true biological abundance has not changed.

![](module2Figs/02-module2.2-omics-platform-problem.png){width=95%}

Each platform has its own version of the same core problem, and its own specific failure modes on top of that. Summarised:

| Platform | Data type | Core problem | Key additional challenge |
|---|---|---|---|
| Bulk RNA-seq | Integer counts | Depth variation | Gene length bias; sampling zeros |
| Single-cell RNA-seq | UMI counts | Depth per cell | Cells ≠ replicates; dropout |
| Proteomics / metabolomics | Continuous intensity | Ion signal variation | MNAR missing values; detection bias |
| Microbiome (16S / shotgun) | Compositional counts | Compositionality | Contamination in low biomass samples |
| Methylation arrays | Beta values [0–1] | Cell composition | Beta vs M-value; heteroscedasticity |

In mass spectrometry, a sample with lower overall ion signal, from loading
variation, concentration differences, or ionisation efficiency changes
between runs, will appear to have lower abundance across all detected
features. Not because concentrations changed, but because less material
reached the instrument. Whether the currency is reads, UMIs, or ion counts,
the logic is the same: the observed value reflects a share of a total that
varies between samples, not an absolute molecular quantity.

**There is no universal normalisation or statistical method that works across all of these** (Covered in module 4). Applying RNAseq tools and algorithms to proteomics data, or standard differential tests to microbiome data produces wrong results.


## Depth affects detection
Consider the mechanism of gene expression: When a cell expresses a gene, it produces RNA molecules. Some genes are highly active and produce thousands of copies. Others are expressed at very low levels, producing only a handful. This variation in expression level is real biology, it is what makes  a liver cell different from a neuron, and a normal healthy cell different from a cancerous one.

The challenge we face in working with omics data is that our data generation platforms (e.g. sequencers) cannot count every RNA molecule in a sample. Instead it reads a subset of fragments and stops when it reaches a target depth. Each gene's count is therefore a proportion of whatever total happened to be generated for that sample. At shallow sequencing depth, low-abundance genes drop in and out of detection across samples not because their expression changed, 
but because the sampling was too sparse to capture them reliably. Increasing depth often makes these genes reappear. The biology hasn't changed, the measurement has simply improved.

![Shallow vs deep sequencing: how depth affects gene detection](module2Figs/02_shallow_vs_deep_sequencing_v2.jpg){width=100%}

<small>The figure above illustrates this directly. At total 10 reads, a gene present at
1% true abundance receives zero reads and is invisible to the analysis. Another
gene at 5% receives just one read, technically detectable, but statistically
unreliable. A single read cannot be distinguished from noise; in a replicate
experiment, the same gene might receive zero reads entirely, producing a zero
despite genuine expression. At 1,000 reads, the same biological proportions
produce reliable counts for both genes. **The biology did not change between
the two panels. The budget did.** </small>

This has a direct implication for study design: sequencing depth is not an
arbitrary parameter. It is determined by the abundance of the least expressed
feature that needs to be detected reliably. Underpowered depth does not simply
add noise, it converts lowly expressed features into zeros, creating missing
data with a specific technical origin. This is explored in detail in Section 3.

!!! tip "Activity"
     ***Head to webR page and check out Tab** count & Depth [Play with `View` Multigene Detection ]


#### Depth variation is systematic, not random

In practice, samples within the same experiment routinely vary in total library
size by **2-fold or more**, even with identical input material and careful
handling. Sources include variation in RNA quality and extraction yield,
differences in library preparation efficiency between batches, multiplexing
imbalances across sequencing lanes, and stochastic variation inherent to
sequencing itself.

This variation is technical, not biological. But it does not always distribute
randomly across experimental groups. **When one tissue type consistently yields
lower RNA quality, or when a sequencing run fails partially for one batch,
depth variation becomes correlated with the biological variable of interest.**
At that point it is no longer just noise: **it becomes a systematic confounder
that mimics or masks biological signal.**

!!! danger "Recoverable vs unrecoverable"
    Depth variation distributed randomly across conditions can largely be corrected by normalisation. Depth variation that correlates with biological groups cannot be corrected. It is confounded with the signal of interest and cannot be separated from it analytically. This is a design failure, not an analysis problem. It is discussed in module 3. 


!!! info "Activity: when depth confounds differential expression"
     ***Head to webR page and check out Tab** count & Depth [Play with `View` Apparent FC vs True FC ]

## The same constraint across platforms
The finite measurement budget appears in different forms across all major omics platforms. The currency (reads, Fluorescence/Peak intensities, ion counts) changes; the underlying constraint does not.

#### Single-cell sequencing data

 In bulk RNA-seq, the sequencing budget is shared across all genes in a
sample. In single-cell RNAseq, it is shared across all genes in **each
individual cell** and the per cell budget is far smaller.

Standard 10x Chromium protocols capture approximately [10–30% of transcripts per cell](https://kb.10xgenomics.com/s/article/360001539051-What-fraction-of-mRNA-transcripts-are-captured-per-cell){target="_blank"}. Most RNA molecules are lost before sequencing begins. A gene
expressed at low levels in a cell may produce zero counts not because it is
off, but because none of its transcripts were captured. The result is a count
matrix with zero entries in more than 70% of gene cell combinations, a
direct consequence of the per cell sequencing budget, not a failure of data
quality.

A cell that was captured poorly will have more zeros than a cell of equivalent biology that was captured efficiently.

!!! info "Types of zeros (Sparsity)"
    This property, is covered in detail in **Section 3 of this module**.

!!! warning "Cells are not biological replicates"
    Cells from the same individual share a common genetic background, cellular
    environment, and processing history. They are subsamples of a donor, not
    independent biological observations. The consequences of treating cells as
    independent replicates are covered in **Module 3: Experimental Design
    Fundamentals**.

#### Proteomics and metabolomics abundance data

Mass spectrometry detects ions and measures signal intensity. The budget here is **total ion signal**: a sample run at lower
concentration, or with different ionisation efficiency between runs, will show lower apparent signal across all detected features, not because concentrations
changed, but because less material was detected.

Missing values in label free proteomics are not distributed the way zeros are in RNAseq. A protein is absent from a sample not because its biology changed
but because its signal fell below the instrument's detection threshold, a pattern called **Missing Not At Random (MNAR)**. This means the features most
likely to be missing are systematically the least abundant, precisely the features that can be most biologically relevant in discovery experiments.
Imputation strategies that assume random missingness are not appropriate here. 

#### 16S amplicon sequencing and metagenomics

In microbiome data, sequencing reads are shared across all taxa present in a
sample. Rare taxa, those making up a small fraction of the community, face
the same underdetection risk as lowly expressed genes in RNAseq: at typical
depths, they may produce zero counts by chance even when genuinely present.

Microbiome data carries an additional structural property beyond this detection
problem: because only relative proportions are measured, a genuine biological
change in one taxon alters the apparent abundance of all others, even those
that did not change. This property, **compositionality** is distinct from
the depth problem and is covered in detail in **Section 4 of this module**.

#### Methylation arrays

Methylation arrays measure a ratio of probe intensities rather than a count
or raw intensity, and their detection properties differ from the other
platforms. Zeros in methylation data, beta values of 0 are biologically
meaningful (a fully unmethylated CpG site), not detection artefacts.

The primary technical challenge in methylation data is not missing values or
depth but **cellular composition**: different cell types carry systematically
different methylation profiles. **A sample with different proportions of cell
types will look globally shifted relative to another**, even if the biology of
each individual cell type is identical.  

!!! info "Coming up in Section 3"
    Not all zeros have the same origin, and treating them identically leads
    to analytical errors that cascade through every downstream step. **Section 3**
    examines the different types of zero that appear in omics count matrices,
    where each comes from, and why the distinction matters for interpretation.


!!! info "Coming up in Module 4"
    Normalisation strategies appropriate to each platform and how to choose between them based 
    on your data and experimental design are covered in **Module 4: Normalisation and Scaling**.

## Key takeaways

Every omics measurement is a relative signal captured under a finite technical budget. The budget differs by platform: reads for sequencing, ion signal for mass spectrometry, probe fluorescence for arrays, but the consequence is universal: raw numbers cannot be compared across samples without normalisation appropriate to that platform's specific properties.
