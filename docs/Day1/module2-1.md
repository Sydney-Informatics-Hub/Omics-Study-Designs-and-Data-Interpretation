# Module 2 : Data types and core statistical properties

!!! info "Learning objectives" 

    - Describe what omics technologies measure and how they differ from traditional biological experiments
    - Explain the relationship between genomics, transcriptomics, proteomics, and metabolomics as layers of biological information
    - Distinguish between sequences, counts, and abundances as data types and explain why they require different analytical approaches
    - Explain why a sequencing count is a relative measurement rather than an absolute one, and describe the consequences of this for study design and interpretation
    
When working with omics datasets, biological experiments get infinitely more complex than wet lab experiments. 

The most immediate difference is scale. Where a traditional wet lab experiment might measure one gene, one protein, or one metabolite at a time, an omics experiment measures an entire class of biological molecules simultaneously. A single RNAseq experiment doesn't measure one gene, it measures all of them, across every sample in your study. 

This matters for how you think about the data. In a traditional experiment, your dataset may have a handful of measurements per sample. In omics, a single sample can generate hundreds to thousands to millions of data points and you may have only a dozen samples. That inverted ratio, far more variables than observations, is one of the defining features of omics data, and it shapes almost every analytical decision that follows. 

## The omics modalities

TODO make a diagram of central dogma as a data map. DNA > RNA > protein > metabolite > phenotype refer to module 1 diagram if you think suitable. 

- Genomics: DNA sequence > what can the cell do?
- Transcriptomics: RNA sequence and abundances > what is the cell currently doing?
- Proteomics: protein levels > what is being made and used? 
- Metabolomics: small molecules > what are the products of cellular activity? 

!!! tip "Why the layers don't always agree" 

    A critical point for interpretation: measuring one layer doesn't tell you what is happening in another. A gene can be present in the genome but never transcribed. An mRNA can be transcribed but never translated into protein. A protein can be abundant but enzymatically inactive. 

    This is why collecting the right data for your research question is essential Choosing the modality is a scientific question, not a technical one. The research questions you are asking should determine which layer of biology you measure, not the other way around. 

## How does sequencing work? 

Before looking at what omics data looks like, it helps to understand how it is generated. 

TODO create a workflow diagram for common sequencing types: WGS/WTS, DIA/DDA mass spec, anything else you think is relevant. Should follow the order: extracting and preparing biolocal materials > library preparation and amplification > sequencing > raw output 

TODO create a diagram that explains this. 

TODO create an exercise to explore this flow. 

## What kind of data does each modality produce? 

Different modalities produce fundamentally different types of measurements and understanding the differences is required before you can intepret them correctly. 

You will encounter 3 main data types: 

### Sequences 

Raw outputs of DNA and RNA sequencing technologies. A sequencer reads fragments of nucleic acid and returns the order or bases for each fragment. At this stage, the data has no inherent quantity attached to it. A sequence tells you what is present, not how much or what it can do. 

### Counts 

These are gained once sequences have been mapped back to a reference and tallied up. For each gene, you count how many sequencing reads overlap with it. This is the primary data format in RNAseq, a matrix of integers, one row per feature, one column per sample. 

### Abundances 

These are the equivalent measurement of counts in proteomics and metabolomics. Instead of sequencing, you're using mass spectrometry. Here, the instrument measures signal intensity, how much of a given molecule's chemical signature was detected. The output is a continouous value, not a count, and it comes with its own set of assumptions and normalisation challenges. 

!!! tip "Why does this distinction matter?" 
    These distinctions matter because the statistical properties of each data type are different. The sources of technical noise are different, normalisation strategies are different. Treating them as interchangable leads to mistakes. 

## Preparing data for analysis 

TODO something about preprocessing and the sorts of resources you need to do this. To get to counts/abundances. 

## What does a count or abundance represent? 

By the time omics data reaches you as an analyst, it has already been through substantial processing. Raw sequence reads have been assembled into a continuous sequence or aligned to a reference assembly and summarised. Mass spectrometry signals have been detected and quantified. What you're working with in many cases, is often a **count matrix** or **abundance matrix**. 

In most everyday measurements, numbers are absolute. If one patient weighs 80 kg and another weighs 60 kg, the comparison is straightforward. The value doesn’t depend on anything else being measured at the same time.

Unfortunately, neither counts, nor abundances behave like that.

### Count matrices 

A count matrix is the primary data format of RNAseq. It is a table of integers, one row per genomic feature, one column per sample. Each value represents the number of sequencing reads that mapped to a feature in that sample. 

!!! tip "That sounds complicated..." 

    Recall that sequencers don't read every molecule in the library. They will only read up to a fixed total, typically 20-50 million reads for bulk RNAseq and each gene's count is just a share of that total. 

    That means each gene’s count depends on two things:

    - How much RNA it actually produced  
    - How many reads were generated overall

A simple example makes this concrete:

| | Sample A | Sample B |
|---|---|---|
| **Total reads sequenced** | 20 million | 40 million |
| **Gene X raw count** | 100 | 200 |

TODO some visual to explain this.

At first glance, Gene X looks like it doubled in Sample B. But if you look at proportions, both samples show the same value (0.0005% of the library). The difference in counts comes entirely from the difference in sequencing depth, not from changes in biology.

TODO some diagram and exercise that explores this 

!!! danger "Common source of misleading results"
    This is one of the most common sources of misleading results in omics. Without accounting for sequencing depth, its easy to mistakenly call differences that aren't actually there. 

### Abundance matrices 

In proteomics and metabolomics, the instrument used to generate data is a mass spectrometer rather than a sequencer. Rather than counting reads, the machine measures signal intensity, that is, how strongly a given molecule's chemical signature was detected in a sample. 

The output is a continuous value, rather than an integer and it sits in an abundance matrix structured the same way as a count matrix: one row per feature, one column per sample. 

Abundances have the same fundamental problem as counts: they are relative, not absolute. The signal intensity for any given molecule depends not just one how much of it was present as it went through the mass spectrometer, but on the total amount of material loaded onto the instrument and how well that molecule ionised. A protein that appears less abundant in one sample may simply have been detected less efficiently, not necessarily been less present. 

!!! tip "Different data type, same issue" 

    Counts and abundances differ in their statistical properties, counts are discrete and follow specific distributional assumptions, abundances are continuous and often skewed. This matters for which tools you choose to analyse them. 
    
    But both share the same core problem: the numbers reflect how much of the total signal was captured, not an absolute molecular quantity. Both require normalisation before cross-sample comparisons can reliably be made. 

## Counts are unreliable without normalisation 

Sequencing depth affects detection, especially for lowly expressed genes. 

Sequencing depth doesn't affect all genes equally. 

Highly expressed genes tend to show up reliably even when sequencing is relatively shallow. Lowly expressed genes are a different story. At lower depth, they might show up as small counts in one sample and zeros in another, simply because there weren’t enough reads to capture them consistently.

This is where interpretation gets tricky. A zero doesn’t always mean absence. Sometimes it just means the gene wasn’t picked up in that particular sequencing run.

If you sequence more deeply, those same genes often appear more consistently. The biology hasn’t changed, you’re just getting a clearer look at it.

TODO convert this to figure standard, use excalidraw 

![Shallow vs deep sequencing: how depth affects gene detection](module2Figs/02_shallow_vs_deep_sequencing_v2.jpg){width=100%}

From a study design perspective, your choice of sequencing depth has real consequences. The depth you need depends on the weakest signal you care about. If depth is too low, low-abundance features start dropping in and out of detection, and that shows up later as zeros.

### The problems start before sequencing

Depth is only part of the story. As described above (TODO will be described above, just isnt yet), library preparation introduces its own variability. 

PCR amplification is necessary to generate enough material, but it isn’t perfectly even across cycles. By the time the library reaches the sequencer, some molecules are overrepresented and others are underrepresented relative ot their original abundance. While they're being sequenced, some fragments will amplify more efficiently than others, especially early on. So by the time you see a count, two things have already happened:

1. Some molecules are overrepresented
2. A subset of them was sampled during sequencing

Both introduce variability before any analysis begins.

TODO create a different version of this diagram that explains library preparation. 

![PCR amplification and sampling zeros (Jiang et al. 2022, Fig 3)](module2Figs/02_zero_Toy_Examplle_v1.png){width=90%}. 
<small>. 
Ref: [Jiang et al. *Genome Biology* 2022](https://link.springer.com/article/10.1186/s13059-022-02601-5){target="_blank"}</small>

The figure above (Jiang et al. 2022, Fig 3) shows this. Five
genes start at equal cDNA concentrations. After PCR amplification, their
relative proportions have shifted not because of biology, but because
of stochastic amplification differences. When sequencing is then limited
to a fixed depth, Gene 1 receives zero reads in three out of five
hypothetical experiments. It was present. It was amplified. It was simply
unlucky enough to be underrepresented at the moment the reads were
sampled.

TODO create an exercise to explore this.

### Depth differences are common, and not always random

In real datasets, samples rarely have identical library sizes. Two-fold differences are quite common, no matter how careful you are. 

!!! warning "What causes differences in read depth?"

    TODO flesh this out

    - variation in RNA quality
    - differences in library prep efficiency
    - sequencing variability across runs or lanes

    In principle, these are technical effects. In practice, they don’t always distribute evenly across your conditions.

For example, one tissue type might consistently yield lower quality RNA, or one batch might perform worse during library prep. When that happens, sequencing depth ends up correlated with the biological groups you’re trying to compare.

!!! note "Scenario" 

    One group has systematically lower depth, and genes appear downregulated across the board. It can look like a strong biological signal, but it’s really just fewer reads being assigned overall.

    A quick check, like plotting library sizes by condition, often makes this obvious. If the distributions don’t overlap much, it’s something you need to deal with before moving forward.

    Normalisation helps, but it doesn’t fully fix cases where depth is tightly confounded with biology. At that point, it’s more of a design issue than an analysis problem.


### The same princple applies across all omics platforms

The underlying issue that your measurements reflect how much of the total signal was captured rather than absolute molecular quantity, appears across every platform, under different names: 

- In single-cell RNA-seq, each cell has its own sequencing depth, often measured as total UMI counts, and the variation can be substantial
- In microbiome data, total reads per sample vary widely, especially in low biomass samples
- In proteomics and metabolomics, the equivalent is total ion signal rather than read count

Different technologies, same underlying problem.

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