# Module 2.2: Choosing the Right Platform

!!! info "Learning objectives"

    By the end of this section, participants will be able to:

    - Choose a platform that can actually capture the biological signal of
      interest, and recognise when one physically cannot

Module 1 named **wrong platform for the biological question** as one of the design pitfalls, and one of the unrecoverable ones: if the instrument cannot capture the signal, no downstream analysis can put it back. This section is the constructive side of that pitfall. Before looking at what omics data means statistically, the first design decision is which platform to run at all, because that choice fixes everything that follows.

The chain is short and it runs one way only:

> **research question → biological molecule → measurement platform → data type → statistical analysis**

Each decision constrains the next. Once samples are collected on a particular platform, you cannot move back up the chain without collecting new data.

---

### Start from the molecule

Different biological molecules require different measurement technologies. DNA and RNA can be sequenced directly, whereas proteins and metabolites generally cannot and are instead measured using approaches such as mass spectrometry or affinity-based assays. The molecule determines the platform, not the other way around.

The figure below maps each biological layer to the molecule it targets, the current platforms available to measure it, examples of analyses each enables, and in the final column when you would choose one platform over another within the same layer.

![](figs_m2/02_omics-platforms.png){width=100%}

Read the figure left to right, but note that the rightmost column is where the design decision actually lives. The same pattern recurs down every row: the choice is almost always **discovery versus targeted** (can the platform see things you didn't specify in advance?) or **resolution versus average** (does it resolve individual cells or locations, or only their pooled signal?). 

!!! tip "The question chooses the layer; the layer chooses the platform"
    As in Module 1, the research question should decide which layer of biology you measure, not the other way around. A platform adopted because it is current, then pointed at a question it does not fit, is one of the most common and most expensive versions of this pitfall.
---

### The platform you choose sets your data type

### The platform you choose sets your data type

Omics platforms broadly fall into two families, distinguished by what the instrument measures. Sequencing-based platforms determine the nucleotide sequence of DNA or RNA molecules. Non-sequencing platforms measure a physical signal, such as fluorescence or ion intensity, that is used to infer a molecule's abundance or identity.

That split carries directly into the data, because the two families produce different kinds of measurement. **Choosing the platform is therefore also choosing the statistical world you will be working in.**

**Sequencing-based platforms produce counts.** A sequencer reads millions of short or long fragments of DNA or RNA and reports the sequence of each. Those raw sequences, the FASTQ files coming off the instrument, are not yet analysable as measurements. They become counts only after computational processing: each read is aligned or otherwise assigned to a feature (a gene, transcript, or taxon), and the number of reads per feature is tallied. The result is **a matrix of counts**, one row per feature, one column per sample, every cell a whole number. RNA-seq, single-cell RNA-seq, ATAC-seq, and microbiome sequencing all produce this format.

**Many non-sequencing platforms produce intensities.** Rather than reading sequences, these instruments measure molecular signal directly: the strength of a fluorescence signal, or the abundance of detected ions. The output is typically a **continuous measurement** rather than an integer count. Mass spectrometry (proteomics, metabolomics) measures ion signal intensity; microarrays measure fluorescence from hybridised probes; many imaging-based assays begin as fluorescence intensity across cells or tissue regions. The numbers look different from counts, and their statistical properties are different too.

![](figs_m2/02_sequencing_vs_nonSequencing_v01.png){width=100%}

This distinction is not cosmetic. Normalisation and statistical tests appropriate for counts are not appropriate for intensities (discussed in Module 4). Treating them as interchangeable produces systematic errors downstream. **The correct analysis follows from the data type, and the data type follows from the platform.**

!!! note "Discovery is a design choice, not a family"
    Sequencing platforms are often used for discovery, and many signal-based platforms measure predefined targets — but the two don't always line up. Untargeted mass spectrometry can also support broad discovery, while targeted sequencing panels interrogate only pre-selected regions. Whether an assay is discovery-driven or targeted is set during study design, not by whether it sequences.
---

### Read length: the one sequencing choice the figure doesn't settle

The figure lists sequencing platforms but does not distinguish the single most consequential choice within DNA and RNA sequencing: **read length**.

**Short-read sequencing** (e.g. Illumina) reads fragments of roughly 50–300 bases. It is cheap, high-throughput, and highly accurate per base, which makes it the default for quantifying known features such as gene expression across many samples. Its limitation is structural: anything longer than a single fragment has to be reconstructed computationally, and some things cannot be reconstructed reliably at all.

**Long-read sequencing** (e.g. PacBio, Oxford Nanopore) produces single reads spanning thousands of bases. Because a read can cover a whole molecule, long reads resolve full-length isoforms, structural variants, and repetitive regions directly, rather than inferring them. The trade-off is higher cost per base and lower throughput.

The decision follows from the question, not the budget: if you need to see full-length molecules or structural features, no amount of short-read depth substitutes for read length. If you are quantifying known features cheaply and at scale, short reads are the better fit. This is a read-length limit, not a coverage one, which is why it cannot be fixed after sequencing.

!!! danger "The unrecoverable rule"
    If the platform cannot capture the biological signal of interest, no analysis method can recover it. The choice has to be made before data collection, not revisited after. This is why platform choice sits in study design, alongside sample size and randomisation, not in analysis.

### Live Activity

***[Click here to join the activity](https://www.menti.com/aluadu62pnrb)***

---

!!! info "Spatial omics sits across both families"
    Spatial transcriptomics is a useful test of the framing above, because which family a platform belongs to determines the measurement it produces. Visium captures RNA by **sequencing barcoded spots** on a tissue section and produces count data. **Imaging-based platforms** such as Xenium and MERFISH detect fluorescently labelled RNA directly within intact tissue; although fluorescence intensities are measured during acquisition, the pipelines typically decode these into transcript counts per cell. The biology being measured is similar; the measurement process, and therefore the data type, is not.

---

Choosing the right platform gets the right *kind* of number into your hands. Section 2 examines what those numbers actually represent once they arrive, and why the same count in two different samples can mean very different things.