# The omics landscape

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Identify the seven common failure modes in omics study design and classify each by recoverability.
    - Recognise when a platform choice, sample size, or metadata decision creates an unrecoverable flaw.
    - Match a biological question to the most suitable omics platform and justify that choice.

Modern biology has undergone a fundamental shift from measuring one molecule at a time to profiling entire classes of biological molecules simultaneously. This collective approach, broadly termed "omics" operates across multiple layers of biological organisation, each revealing a different dimension of how living systems function. Every living system, whether that's a bacterium, a migratory bird, or person, can be interrogated at the molecular level across these multiple layers. 

These layers have different names, each with distinct molecular targets, and a defined scope of what it can and cannot answer:  

| Layer | Function |
|---|--------------------------|
| **Genomics** | Reveals what genes an organism carries and what they could encode | 
| **Epigenomics** | Reveals how gene activity is regulated through chemical modification to DNA and its packaging proteins |
| **Transcriptomics** | Captures which genes are turned on or off under a given condition | 
| **Proteomics** | Measures the proteins actually present in a cell or tissue |
| **Metabolomics** | Captures small molecule metabolites that are downstream readout of biochemical activity | 

Crucially, no single omics layer tells the complete story; each captures a different molecular dimension of biological systems, and the choice of which layer, or combination of layers to investigate is one of the most consequential decisions a researcher will make before an experiment begins.

The figure below shows how each layer sits within the broader molecular hierarchy of a cell. 

![](module1/figs/1-1_landscape.png){width=100%}

## Choosing the right platform

Each omics domain includes multiple platforms, and no single approach fits every question. Platforms differ not only in what 
they measure, but in how they measure it, which directly shapes what you can and cannot conclude from your data.

At a broad level, omics technologies fall into two methodological families:

- **Sequencing-based approaches** (e.g., DNA-seq, RNA-seq, ATAC-seq) quantify 
  molecules by converting them into readable sequence, offering high throughput 
  and genome-wide coverage
- **Imaging-based approaches** (e.g., spatial transcriptomics, microscopy-based 
  proteomics) preserve the physical location of molecules within tissue, adding a 
  spatial dimension that sequencing-based methods cannot capture

The figure below provides an overview:

![](module1/figs/01_Various_data_analysis_v2.png){width=100% height=50%}

### What else can 'omics data tell us

Many omics pipelines focus on a single primary output (i.e. differential gene expression from RNA-seq, variant calling from Whole Genome Sequencing). But the same raw data often contains additional layers of biological information that aren't commonly interrogated.

A growing set of secondary analyses can be applied to existing datasets, often without additional sequencing cost. Take bulk RNA-seq as an example: beyond standard differential expression, the same dataset can be interrogated for alternative splicing, RNA editing events, transcript fusions, and more. These approaches provide complementary insights and can substantially increase the return on investment from a single experiment.

The catch is that many of these analyses depend on decisions made before sequencing begins including: 

- Library preparation 
- Sequencing depth 
- Read length 
- Metadata 

By the time the data exists, it is often too late to recover an option that was designed out. Knowing what your data type is capable of before the experiment is designed means you can keep those options open from the start.

![Range of analysis approaches available from a single bulk RNA-seq dataset](module1/figs/01_RNAseq_based_analysis_v1.png){width=90%}

<small>Ref: [Thind et.al. *Briefings in Bioinformatics* 22.6 
(2021).](https://academic.oup.com/bib/article/22/6/bbab259/6330938){target="_blank"}</small>

TODO replace image with custom diagram as above.

!!! Question "Activity: planning your study" 

    TODO Prepare activity that summarises takeaways from above, consider using mentimeter for this in the live workshop. e.g. 

    Pick one of the example studies below. You don't need to know anything about bioinformatics to do this. Read the study description and answer these questions:

    1. What biological question is the study trying to answer? 
    2. Which omics layer or combination of layers would best address it?
    3. What would the primary analysis output be? 
    4. What decisions made before data collection could limit what you can extract from this data later?

??? Example "Clincal: colorectal cancer"
    
    Tissue biopsies are collected from 40 patients undergoing surgery for colorectal cancer, one sample from the tumour and one from adjacent normal tissue per patient. Samples are collected across two hospitals over 24 months. The goal is to identify gene expression differences between tumour and normal tissue.

??? Example "Wildlife: koala chlamydia"

    Swabs are collected from 60 wild koalas across a fragmented landscape over 18 months, comparing animals with and without chlamydial infection. Samples are stored in the field before being transported to the lab.


??? Example "Aquaculture: salmon gut microbiome"

    Gut contents are collected from Atlantic salmon at three farms using different feed formulations. Twenty fish per farm are sampled over a single harvest day. The goal is to understand how diet shapes the gut microbial community.

??? Example "Agriculture: wheat heat stress"

    Leaf tissue is harvested from six wheat varieties at two timepoints, before and during a simulated drought, in a glasshouse trial. The aim is to identify genes associated with drought tolerance.
