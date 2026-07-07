# The omics landscape

!!! info "Learning objectives"
    By the end of this section, participants will be able to:  
    - Match a biological question to the most suitable omics platform and justify that choice.


**[Tell us about your study datatyp here](https://www.menti.com/alocqhrd8oet)**  or go to [mentimeter.com](https://mentimeter.com) and enter code **1234 567**


Modern biology has undergone a fundamental shift from measuring one molecule at a time to profiling entire classes of biological molecules simultaneously. This collective approach, broadly termed "omics" operates across multiple layers of biological organisation, each revealing a different dimension of how living systems function. Every living system, whether that's a bacterium, a migratory bird, or person, can be interrogated at the molecular level across these multiple layers. 

These layers have different names, each with distinct molecular targets, and a defined scope of what it can and cannot answer:  

Crucially, no single omics layer tells the complete story; each captures a different molecular dimension of biological systems, and the choice of which layer, or combination of layers to investigate is one of the most consequential decisions a researcher will make before an experiment begins.

The figure below shows how each layer sits within the broader molecular hierarchy of a cell. 

![](figs_m1/1-1_landscape.png){width=100%}

## Choosing the right platform

Each omics domain includes multiple platforms, and no single approach fits every question. Platforms differ not only in what 
they measure, but in how they measure it, which directly shapes what you can and cannot conclude from your data.

At a broad level, omics technologies fall into two methodological families:

- **Sequencing based approaches** (e.g., DNAseq, RNAseq, ATACseq, 16S amplicon sequencing) quantify molecules by converting them into sequence reads. The primary analytical output is typically a **count** matrix obtained by assigning reads to genes, genomic regions, or taxa.
- **Non-sequencing approaches** measure molecular signals directly. This family includes mass spectrometry platforms (proteomics, metabolomics), fluorescence arrays (microarrays, methylation arrays), and spatial imaging technologies. Many of these platforms produce **continuous** intensity measurements. However, some imaging based transcriptomics technologies, such as Xenium, MERFISH, and CosMx, use image processing algorithms to convert fluorescence signals into **counts** of individual transcript molecules. As a result, their final analytical output may **resemble a count matrix** rather than an intensity matrix.


!!! question "Group Activity: Match the platform to the question"

    Each group takes one case study. Discuss:

    1. What is the biological question actually asking, in one sentence?
    2. Sequencing-based or non-sequencing? Why?
    3. Which specific platform would you choose, and what's the *next best* platform you rejected?
    4. What in the study's collection conditions (storage, timing, sample type) constrains your platform choice, independent of the biology?

    Report back: platform choice + the one constraint that ruled out your rejected alternative.

??? Example "Clincal: colorectal cancer"
    
    Tissue biopsies are collected from 40 patients undergoing surgery for colorectal cancer, one sample from the tumour and one from adjacent normal tissue per patient. Samples are collected across two hospitals over 24 months. The goal is to identify gene expression differences between tumour and normal tissue.

??? Example "Wildlife: koala chlamydia"

    Swabs are collected from 60 wild koalas across a fragmented landscape over 18 months, comparing animals with and without chlamydial infection. Samples are stored in the field before being transported to the lab.


??? Example "Aquaculture: salmon gut microbiome"

    Gut contents are collected from Atlantic salmon at three farms using different feed formulations. Twenty fish per farm are sampled over a single harvest day. The goal is to understand how diet shapes the gut microbial community.

??? Example "Agriculture: wheat heat stress"

    Leaf tissue is harvested from six wheat varieties at two timepoints, before and during a simulated drought, in a glasshouse trial. The aim is to identify genes associated with drought tolerance.


<!--
??? success "Answers"

    **Colorectal cancer (tumour vs normal, gene expression)**
    Sequencing-based → bulk RNAseq. Rejected alternative: single-cell 
    RNAseq, richer resolution but not needed to answer "which genes 
    differ," and biopsy logistics across two hospitals over 24 months 
    favour a simpler, more batch-tolerant bulk workflow.

    **Koala chlamydia (infection status, field swabs)**
    Sequencing-based → 16S amplicon (or shotgun metagenomics if budget 
    allows) on the swab microbiome/pathogen load. Rejected alternative: 
    metabolomics, informative but field storage before lab transport 
    risks degrading labile metabolites; nucleic acids tolerate the delay 
    better.

    **Salmon gut microbiome (diet effect)**
    Sequencing-based → 16S or shotgun metagenomics. Rejected alternative: 
    metaproteomics, could show functional activity, not just composition, 
    but cost/throughput for 20 fish × 3 farms favours amplicon sequencing 
    as the first pass.

    **Wheat heat stress (drought-responsive genes)**
    Sequencing-based → bulk RNAseq (leaf tissue, defined timepoints). 
    Rejected alternative: metabolomics, would capture downstream stress 
    response but the question is explicitly about *genes* associated with 
    tolerance, which points to the transcriptome first.
-->
