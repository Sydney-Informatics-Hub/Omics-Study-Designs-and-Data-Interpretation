# Module 2 : Data modalities

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

TODO create a workflow diagram for common sequencing types: WGS/WTS, DIA/DDA mass spec, anything else you think is relevant. Should follow the order: extracting and preparing biological materials > library preparation and amplification > sequencing > raw output 

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