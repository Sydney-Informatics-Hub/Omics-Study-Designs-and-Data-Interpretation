# Module 2.2: Omics Platforms and Technology 

<-  TRACK BACK TO PITFALL 2- WRONG PLATFORM CHOICE.  -> 

!!! info "Learning objectives" 

    - Distinguish between sequencing and intensities platforms
    - Describe what happens to raw instrument output before it reaches an analyst as a matrix of numbers

Module 1 focused on study design pitfalls. Module 2 shifts to various types of omics platforms and data types.

### The omics platforms

In module 1, we learned each layer targets a different class of molecule and answers a different
biological question. These layers do not map cleanly onto each other, and that matters for
interpretation. To answer the omics related questions, we need to consider, both by the biological layer and the instrument used. 

Each omics field is enabled by a distinct family of laboratory 
platforms, because different molecules require different instruments 
to measure them. DNA and RNA can be sequenced directly. Proteins and 
metabolites cannot, they are measured mostly by mass spectrometry or 
by antibody and affinity-based methods. The figure below maps each 
biological layer to the molecule it targets, the platforms used to 
measure it, and the biological questions it can address.

![](figs_m1/2.1-omics-types-platfomrs.png){width=100%}


### Two main data types, determined by the instrument
Module 1 introduced two broad families of omics technology: **sequencing based** approaches and **non sequencing** approaches. That distinction carries directly into the data, because the two families generally produce different kinds of measurements.

**Sequencing based platforms produce counts**. A sequencer reads millions of short/long fragments of DNA or RNA and reports the sequence of each. Those raw sequences: the FASTQ files coming off the instrument, are not yet analysable as measurements. They become counts only after alignment or assignment: each fragment is mapped back to a reference genome, transcriptome, or other feature (genes/taxa) set, and the number of fragments associated with each feature is tallied. The results [raw matrix] **a matrix of counts**, one row per feature, one column per sample, where every cell contains a whole number. RNAseq, single-cell RNAseq, ATACseq, and microbiome sequencing all commonly produce this format.

**Many non-sequencing platforms produce intensities**. Rather than reading sequences, these instruments measure molecular signal directly. For example, the strength of a fluorescence signal or the abundance of detected ions. The output is typically a **continuous value** rather than a count. Mass spectrometry platforms (proteomics and metabolomics) measure ion signal intensity. Microarrays measure fluorescence from hybridised probes. Many imaging based assays begin as fluorescence intensity measurements recorded across cells or tissue regions. The numbers look different from counts, and their statistical properties are different too.


 ![](figs_m2/02_sequencing_vs_nonSequencing_v01.png){width=100%}  

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
