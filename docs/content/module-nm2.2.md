# Module 2.2: Choosing the Right Platform

<-  TRACK BACK TO PITFALL 2 — WRONG PLATFORM CHOICE  ->

!!! info "Learning objectives"

    By the end of this section, participants will be able to:

    - Choose a platform that can actually capture the biological signal of
      interest, and recognise when one physically cannot
    - Explain why that choice is a design decision that cannot be recovered
      by better analysis downstream

Module 1 named **wrong platform for the biological question** as one of the design pitfalls, and one of the unrecoverable ones: if the instrument cannot capture the signal, no downstream analysis can put it back. This section is the constructive side of that pitfall. Before looking at what omics data means statistically, the first design decision is which platform to run at all, because that choice fixes everything that follows.

The chain is short and it runs one way only:

> **research question → biological molecule → measurement platform → data type → statistical analysis**

Each decision constrains the next. Once samples are collected on a particular platform, you cannot move back up the chain without collecting new data.

---

### Start from the molecule

Different biological molecules require different measurement technologies. DNA and RNA can be sequenced directly, whereas proteins and metabolites generally cannot and are instead measured using approaches such as mass spectrometry or affinity-based assays. The molecule determines the platform, not the other way around.

The figure below maps each biological layer to the molecule it targets, the platforms used to measure it, and the biological questions it can address.

![](figs_m2/02_omics-platforms.png){width=100%}



!!! tip "The question chooses the layer; the layer chooses the platform"
    As in Module 1, the research question should decide which layer of biology you measure, not the other way around. A platform adopted because it is current, then pointed at a question it does not fit, is one of the most common and most expensive versions of this pitfall.

---

### The platform you choose sets your data type

The sequencing-vs-non-sequencing split introduced in Module 1 carries directly into the data, because the two families produce different kinds of measurements. **Choosing the platform is therefore also choosing the statistical world you will be working in.**

**Sequencing-based platforms produce counts.** A sequencer reads millions of short or long fragments of DNA or RNA and reports the sequence of each. Those raw sequences, the FASTQ files coming off the instrument, are not yet analysable as measurements. They become counts only after alignment or assignment: each fragment is mapped back to a reference genome, transcriptome, or feature set (genes, taxa), and the number of fragments per feature is tallied. The result is **a matrix of counts**, one row per feature, one column per sample, every cell a whole number. RNA-seq, single-cell RNA-seq, ATAC-seq, and microbiome sequencing all produce this format.

**Many non-sequencing platforms produce intensities.** Rather than reading sequences, these instruments measure molecular signal directly: the strength of a fluorescence signal, or the abundance of detected ions. The output is a **continuous value** rather than a count. Mass spectrometry (proteomics, metabolomics) measures ion signal intensity; microarrays measure fluorescence from hybridised probes; many imaging-based assays begin as fluorescence intensity across cells or tissue regions. The numbers look different from counts, and their statistical properties are different too.

![](figs_m2/02_sequencing_vs_nonSequencing_v01.png){width=100%}

This distinction is not cosmetic. Normalisation and statistical tests appropriate for counts are not appropriate for intensities (discussed in Module 4). Treating them as interchangeable produces systematic errors downstream. **The correct analysis follows from the data type, and the data type follows from the platform.**

### Live Activity

***[Click here to join the activity](https://www.menti.com/aluadu62pnrb)***

---

### Matching the platform to the question

Within a family, the platform still has to fit the specific question. These are the choices that most often go wrong, framed as the design question to ask rather than the failure to regret.

| Ask this before choosing | Because the platform must have | Failure mode if ignored |
|---|---|---|
| Do I need cell-type-specific signal, or is an average acceptable? | Single-cell resolution vs bulk | Bulk permanently averages across cell types; rare populations and cell-type-specific responses cannot be recovered by deconvolution alone |
| Does my question involve structural variants, full-length isoforms, or repetitive regions? | Long-read length | Short reads cannot resolve these regardless of depth; this is a read-length limit, not a coverage one |
| Are there molecules I can't afford to miss? | An acquisition mode that captures them | Some mass-spec acquisition modes systematically miss low-abundance proteins by design, so key targets are absent entirely, not just under-quantified |
| Is this platform chosen because it fits, or because it is current? | Fit to the biological question | Novelty-driven choices waste cost and sample for no scientific gain over a cheaper approach that fits |

!!! danger "The unrecoverable rule"
    If the platform cannot capture the biological signal of interest, no analysis method can recover it. The choice has to be made before data collection, not revisited after. This is why platform choice sits in study design, alongside sample size and randomisation, not in analysis.

---

!!! info "Spatial omics sits across both families"
    Spatial transcriptomics is a useful test of the framing above, because which family a platform belongs to determines the measurement it produces. Visium captures RNA by **sequencing barcoded spots** on a tissue section and produces count data. **Imaging-based platforms** such as Xenium and MERFISH detect fluorescently labelled RNA directly within intact tissue; although fluorescence intensities are measured during acquisition, the pipelines typically decode these into transcript counts per cell. The biology being measured is similar; the measurement process, and therefore the data type, is not.

!!! tip "A note on methylation arrays"
    <!-- SCOPE FLAG: non-sequencing intensity example. Keep as a brief aside
         illustrating a third data type, or cut for strict sequencing-only
         scope — your call. -->
    Methylation arrays measure fluorescence intensity at two probes per CpG site, one methylated, one unmethylated. The reported beta value is the ratio of methylated signal to total signal, bounded between 0 and 1. It is derived from intensities but is not itself an intensity: its statistical properties (beta distribution, variance highest in the middle of the range) are distinct from both raw intensities and counts. A third data type, a third set of rules.

---

Choosing the right platform gets the right *kind* of number into your hands. Section 2 examines what those numbers actually represent once they arrive, and why the same count in two different samples can mean very different things.