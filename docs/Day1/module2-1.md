# Module 2: Data types and core statistical properties

## Section 1: What the data actually is

!!! info "Learning objectives" 

    - Distinguish between counts and intensities as the two primary omics data types, connect each to the instrument family that
      produces it, and explain why the two require different analytical approaches
    - Explain why measuring one omics layer does not predict what is happening in another
    - Describe what happens to raw instrument output before it reaches an analyst as a matrix of numbers
    - Recognise that counts and intensities are relative rather than absolute measurements, and understand why this shapes every
      analytical decision that follows


Module 1 focused on study design: decisions made before any data is
generated, and the failure modes that follow from getting those decisions
wrong. Module 2 shifts to the data itself.

Before asking what omics data means statistically, it helps to ask a
more basic question: **what kind of number are you actually looking at,
and how did it get there?** The answer is less obvious than it seems,
and getting it wrong early leads to systematic errors that no amount of
downstream analysis can fix.

### The omics layers: a brief recap

Module 1 introduced the major omics platforms and when to choose between
them. That framework is worth keeping in view as we move into the data, because the type of number an experiment produces is determined both by the biological layer being measured and by the instrument used to measure it. 

Each layer targets a different class of molecule and answers a different
biological question. These layers do not map cleanly onto each other, and that matters for
interpretation.


!!! tip "Why the layers don't always agree" 

    A critical point for interpretation: measuring one layer doesn't tell you what is happening in another. A gene can be present in the genome but never transcribed. An mRNA can be transcribed but never translated into protein. A protein can be abundant but enzymatically inactive. 

    This is why collecting the right data for your research question is essential Choosing the modality is a scientific question, not a technical one. The research questions you are asking should determine which layer of biology you measure, not the other way around. 




 +++++++++++++++++++++++++++++++++++++++++++++

## How does sequencing work? 

Before looking at what omics data looks like, it helps to understand how it is generated. 

TODO create a workflow diagram for common sequencing types: WGS/WTS, DIA/DDA mass spec, anything else you think is relevant. Should follow the order: extracting and preparing biological materials > library preparation and amplification > sequencing > raw output 

TODO create a diagram that explains this. 

TODO create an exercise to explore this flow. 

 +++++++++++++++++++++++++++++++++++++++++++++

### Two data types, determined by the instrument
Module 1 introduced two broad families of omics technology: **sequencing based** approaches and **non sequencing** approaches. That distinction carries directly into the data, because the two families generally produce different kinds of measurements.

**Sequencing based platforms produce counts**. A sequencer reads millions of short/long fragments of DNA or RNA and reports the sequence of each. Those raw sequences: the FASTQ files coming off the instrument, are not yet analysable as measurements. They become counts only after alignment or assignment: each fragment is mapped back to a reference genome, transcriptome, or other feature (genes/proteins) set, and the number of fragments associated with each feature is tallied. The results [raw matrix] **a matrix of counts**, one row per feature, one column per sample, where every cell contains a whole number. RNAseq, single-cell RNAseq, ATACseq, and microbiome sequencing all commonly produce this format.

**Many non-sequencing platforms produce intensities**. Rather than reading sequences, these instruments measure molecular signal directly. For example, the strength of a fluorescence signal or the abundance of detected ions. The output is typically a **continuous value** rather than a count. Mass spectrometry platforms (proteomics and metabolomics) measure ion signal intensity. Microarrays measure fluorescence from hybridised probes. Many imaging based assays begin as fluorescence intensity measurements recorded across cells or tissue regions. The numbers look different from counts, and their statistical properties are different too.

 
|Instrument family|	Typical primary measurement|	Format [Raw matrix]	| Platforms|
|---|---|---|---|
| Sequencing based	| Feature level counts (post alignment)|	Count matrix (non negative integers)|	Bulk RNA-seq · scRNA-seq · ATAC-seq · 16S · metagenomics|
| Non-sequencing	| Continuous signal (intensity or ion abundance)	|Continuous matrix |	Proteomics MS · metabolomics MS · microarrays · many imaging-based assays|

!!! info "Mass spectrometry is not imaging, but it produces intensities"
    Module 1 discussed non-sequencing methods in the context of spatial imaging technologies. Mass spectrometry, which underlies most proteomics and metabolomics workflows is a detection and ionisation technology rather than an imaging technology. Despite these differences, **both generate signal-intensity measurements** rather than sequencing read counts. The underlying instrument physics differs substantially, but many of the statistical challenges associated with intensity based data are shared.

!!! info "Spatial omics sits across both families"
    Spatial transcriptomics platforms differ in which family they belong to, and therefore what type of measurement they generate. Visium captures RNA by **sequencing barcoded spots** on a tissue section and produces count data. **Imaging-based platforms** such as Xenium and MERFISH detect fluorescently labelled RNA molecules directly within intact tissue. Although fluorescence intensities are measured during image acquisition, image-processing pipelines typically decode these signals into transcript counts assigned to individual cells. 
    
The biology being measured is similar across these platforms, but the measurement process differs.

##### Why does this distinction between data types matter?
    These distinctions matter because the statistical properties of each data type are different. The sources of technical noise are different, normalisation strategies are different. Treating them as interchangable leads to mistakes. 

!!! Tip "A note on methylation arrays"
    Methylation arrays measure fluorescence intensity at two probes per CpG site, one for the methylated state, one for the unmethylated state. The beta value reported is the ratio of methylated signal to total signal, bounded between 0 and 1. It is derived from intensities but is not itself an intensity, its statistical properties (beta distribution, variance highest in the middle of the range) are distinct from both raw intensities and counts.
_______________________________________________________
## Preparing data for analysis 

TODO something about preprocessing and the sorts of resources you need to do this. To get to counts/abundances. 

## What does a count or abundance represent? 

By the time omics data reaches you as an analyst, it has already been through substantial processing. Raw sequence reads have been assembled into a continuous sequence or aligned to a reference assembly and summarised. Mass spectrometry signals have been detected and quantified. What you're working with in many cases, is often a **count matrix** or **abundance matrix**. 

In most everyday measurements, numbers are absolute. If one patient weighs 80 kg and another weighs 60 kg, the comparison is straightforward. The value doesn’t depend on anything else being measured at the same time.

Unfortunately, neither counts, nor abundances behave like that.