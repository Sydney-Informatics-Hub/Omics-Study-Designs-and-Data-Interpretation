# Module 2.1: Data types  

## Section 1: What the data actually is

!!! info "Learning objectives" 

    - Distinguish between sequencing counts and intensities as the two primary omics data types, connect each to the instrument family that
      produces it, and explain why the two require different analytical approaches
    - Describe what happens to raw instrument output before it reaches an analyst as a matrix of numbers

## TIME DURATION NOTE:: TO TO DELETED IN FINAL STAGE [Aimed for 5 mins; activities: 2 mins]

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
them. That framework matters, because the type of number an experiment produces is determined both by the biological layer being measured and by the instrument used to measure it. 

Each layer targets a different class of molecule and answers a different
biological question. These layers do not map cleanly onto each other, and that matters for
interpretation.


!!! tip "Why the layers don't always agree" 

    A critical point for interpretation: measuring one layer doesn't tell you what is happening in another. A gene can be present in the genome but never transcribed. An mRNA can be transcribed but never translated into protein. A protein can be abundant but enzymatically inactive. 

    This is why collecting the right data for your research question is essential. Choosing the modality is a scientific question, not a technical one. The research questions you are asking should determine which layer of biology you measure, not the other way around. 


### Two main data types, determined by the instrument
Module 1 introduced two broad families of omics technology: **sequencing based** approaches and **non sequencing** approaches. That distinction carries directly into the data, because the two families generally produce different kinds of measurements.

**Sequencing based platforms produce counts**. A sequencer reads millions of short/long fragments of DNA or RNA and reports the sequence of each. Those raw sequences: the FASTQ files coming off the instrument, are not yet analysable as measurements. They become counts only after alignment or assignment: each fragment is mapped back to a reference genome, transcriptome, or other feature (genes/taxa) set, and the number of fragments associated with each feature is tallied. The results [raw matrix] **a matrix of counts**, one row per feature, one column per sample, where every cell contains a whole number. RNAseq, single-cell RNAseq, ATACseq, and microbiome sequencing all commonly produce this format.

**Many non-sequencing platforms produce intensities**. Rather than reading sequences, these instruments measure molecular signal directly. For example, the strength of a fluorescence signal or the abundance of detected ions. The output is typically a **continuous value** rather than a count. Mass spectrometry platforms (proteomics and metabolomics) measure ion signal intensity. Microarrays measure fluorescence from hybridised probes. Many imaging based assays begin as fluorescence intensity measurements recorded across cells or tissue regions. The numbers look different from counts, and their statistical properties are different too.


 ![](module2Figs/02_sequencing_vs_nonSequencing_v01.png){width=100%}  

### Live Activity

***[Click here to join the activity](https://www.menti.com/aluadu62pnrb)***



!!! info "Spatial omics sits across both families"
    Spatial transcriptomics platforms differ in which family they belong to, and therefore what type of measurement they generate. Visium captures RNA by **sequencing barcoded spots** on a tissue section and produces count data. **Imaging-based platforms** such as Xenium and MERFISH detect fluorescently labelled RNA molecules directly within intact tissue. Although fluorescence intensities are measured during image acquisition, image-processing pipelines typically decode these signals into transcript counts assigned to individual cells. 
    
    The biology being measured is similar across these platforms, but the measurement process differs.

#### Why does this distinction between various Instrument based data types matter?
These distinctions matter because the sources of technical noise are different. Normalisation strategies appropriate for read counts are not appropriate for intensities (discussed in module 4). Treating them as interchangable leads to systematic errors that create issues for downstream data analysis. The correct normalization and statistical test follow from data types.

!!! tip "A note on methylation arrays"
    Methylation arrays measure fluorescence intensity at two probes per CpG site, one for the methylated state, one for the unmethylated state. The beta value reported is the ratio of methylated signal to total signal, bounded between 0 and 1. It is derived from intensities but is not itself an intensity, its statistical properties (beta distribution, variance highest in the middle of the range) are distinct from both raw intensities and counts.

Section 2 examines what those numbers actually represent once they arrive, and why the same count in two different samples can mean very different things.
