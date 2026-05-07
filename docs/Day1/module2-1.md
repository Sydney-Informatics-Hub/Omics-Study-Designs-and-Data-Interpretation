# Module 2 : Data types and core statistical properties

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  

    - Describe what omics technologies measure and how they differ from traditional biological experiments
    - Explain the relationship between genomics, transcriptomics, proteomics, and metabolomics as layers of biological information
    - Recognise the key features of omics data, including high dimensionality and the implications for study design
    
When working with omics datasets, biological experiements get infinitely more complex, not because the principles change but because the scale does. 

Where a traditional wet lab experiment may measure one gene, one protein, or one metabolite at a time, an omics experiment measures tens of thousands, simultaneously. You form a hypothesis, choose a variable and collect enough observations to test it. Omics experiments work differently. 

Instead of measuring one or a few things, omics technologies measure an entire class of biolgical molecules in one go. A single RNA sequencing experiment doesn't measure one gene, it measures all of them at once, across every sample in your study. Proteomics doesn't target one protein, it catalogues thousands simultaneously. The scale is different from what most biology training prepares you for. 

This matters for how you think about the data. In a traditional experiment, your dataset may have a handful of measurements per sample. In omics, a single sample can generate hundreds to millions of data points and you may have only a dozen samples. That inverted ratio, far more variables than observations, is one of the defining features of omics data, and it shapes almost every analytical decision that follows. 

## What are the most common omics modalities? 

TODO make this a table or refer to diagram from module 1 

- Genomics: DNA sequence > what can the cell do?
- Transcriptomics: RNA sequence and abundances > what is the cell currently doing?
- Proteomics: protein levels > what is being made and used? 
- Metabolomics: small molecules > what are the products of cellular activity? 

Importantly, these layers dont always tell the same story. A gene can be present in the genome but never transcribed. An mRNA can be transcribed but never translated into protein. A protein can be abundant but enzymatically inactive. 

## What kind of data does each modality produce? 

Different modalities produce fundamentally different types of measurements and understanding the differences is required before you can intepret them correctly. 

You will encounter 3 main data types: 

### Sequences 

Raw outputs of DNA and RNA sequencing technologies. A sequencer reads fragments of nucleic acid and returns the order or bases for each fragment. At this stage, the data has no inherent quantity attached to it. A sequence tells you what is present, not how much or what it can do. 

### Counts 

These are gained once sequences have been mapped back to a reference and tallied up. For each gene, you count how many sequencing reads overlap with it. This is the primary data format in RNAseq, a matrix of integers, one row per feature, one column per sample. 

### Abundances 

These are the equivalent measurement of counts in proteomics and metabolomics. Instead of sequencing, you're using mass spectrometry. Here, the instrument measures signal intensity, how much of a given molecule's chemical signature was detected. The output is a continouous value, not a count, and it comes with its own set of assumptions and normalisation challenges. 

!!! warning "Who cares?" 
    These distinctions matter because the statistical properties of each data type are different. The sources of technical noise are different, normalisation strategies are different. Treating them as interchangable leads to mistakes. 

## What does a count represent? 

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