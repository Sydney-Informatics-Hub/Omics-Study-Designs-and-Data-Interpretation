# Module 2.1: Core statistical problems

!!! info "Learning objectives"

    By the end of this module, participants will be able to:

    - Explain why omics measurements are relative rather than absolute and describe what this means for cross-sample comparison
    - Identify the primary statistical challenge associated with each major omics data type and connect it to the biological or technical process that causes it
    - Distinguish between a sampling zero and a biological zero, and explain why this distinction affects interpretation
    - Recognise when depth, signal, or composition confounding is likely to produce misleading results, and identify which problems are recoverable at the analysis stage
    - Describe why the same statistical approach cannot be applied uniformly across omics platforms

## The problem every omics platform shares

Before looking at individual data types, it helps to state the problem they all have in common.

In most everyday measurements, numbers are absolute. A patient who weighs 80 kg weighs 80 kg regardless of who else is in the room or how many measurements were taken that day. The value stands on its own.

Omics measurements don't work like that. Every omics instrument operates under a finite technical budget, a total number of reads, a total ion signal, a total fluorescence intensity, and what you observe for any one feature is always a share of that total. 

!!! danger "The core problem"
    **An omics measurement is not an absolute quantity. It is a proportion of a technical total that varies between samples.**
    
    Because that total differs between samples — sometimes by chance, sometimes systematically, raw numbers cannot be compared directly across samples without first accounting for how they were generated.

TODO some diagram that communicates this 

Each platform has its own version of the same core problem, and its own specific failure modes on top of that. Summarised:

| Platform | Data type | Core problem | Key additional challenge |
|---|---|---|---|
| Bulk RNA-seq | Integer counts | Depth variation | Gene length bias; sampling zeros |
| Single-cell RNA-seq | UMI counts | Depth per cell | Cells ≠ replicates; dropout |
| Proteomics / metabolomics | Continuous intensity | Ion signal variation | MNAR missing values; detection bias |
| Microbiome (16S / shotgun) | Compositional counts | Compositionality | Contamination in low-biomass samples |
| Methylation arrays | Beta values [0–1] | Cell composition | Beta vs M-value; heteroscedasticity |

There is no universal normalisation or statistical method that works across all of these. Applying RNA-seq tools and algorithms to proteomics data, or standard differential tests to microbiome data produces systematically wrong results.

## Sequencing count data

### The biological reality

Consider the mechanism of gene expression: 

When a cell expresses a gene, it produces RNA molecules. Some genes are highly active and produce thousands of copies. Others are 
expressed at very low levels, producing only a handful. This variation in expression level is real biology, it is what makes  a liver cell different from a neuron, and a normal healthy cell different from a cancerous one.

The challenge we face in working with omics data is that our data generation platforms (e.g. sequencers, mass spectrometers) cannot count every RNA molecule in a sample. Instead it reads a subset of fragments and stops when it reaches a target depth, typically somewhere between 20 and 50 million reads for a bulk RNA-seq experiment. Each gene's count is therefore a share of whatever total happened to be generated for that sample.

### The statistical consequence

This produces counts that are:

**Discrete integers**: counts are whole numbers, and the statistical models appropriate for them (negative binomial, Poisson) are different from those appropriate for continuous measurements.

**Right-skewed and zero-inflated**: most genes are expressed at low levels. A typical count matrix has many small values and many zeros, with a long tail of highly expressed genes. This distribution is not normal, and treating it as though it were leads to incorrect 
inference.

**Dependent on sequencing depth**: a gene with a count of 100 in Sample A and 200 in Sample B may not have changed at all. If Sample B was sequenced twice as deeply, both observations represent exactly the same proportion of the library. The apparent difference is entirely technical.

**Affected by gene length**: longer genes produce more sequencing fragments than shorter genes at the same expression level, simply because there is more sequence to sample. A long gene and a short gene with identical biological expression will have very different raw counts. This is why methods like RPKM and TPM exist, and why length correction matters when comparing expression across genes rather than across samples.

!!! TIP "TODO exercise: link to webR module"

    Whats the webR module that demonstrates these principles?

### The zero problem

Zeros deserve special attention because they are common and easily misread. In a count matrix, a zero can mean one of two things:

- **Biological zero**: the gene is genuinely not expressed in this sample under these conditions
- **Sampling zero**: the gene was expressed, but no reads happened to be assigned to it under this sequencing budget

At shallow sequencing depth, low-abundance genes drop in and out of detection across samples not because their expression changed, 
but because the sampling was too sparse to capture them reliably. Increasing depth often makes these genes reappear. The biology hasn't changed — the measurement has simply improved.

TODO a diagram? 

!!! warning "Why this matters for interpretation"
    Treating sampling zeros as biological zeros inflates the apparent number of absent genes, distorts differential expression results, 
    and makes reproducibility across studies appear worse than it is. Depth is a design decision with direct consequences for the zeros 
    you will see in your data.

### When depth becomes a design problem

In principle, variation in sequencing depth between samples is a technical effect that normalisation can correct. In practice, it 
becomes a design problem when depth is systematically associated with the biological groups being compared.

If one tissue type consistently yields lower quality RNA and therefore lower sequencing depth, genes will appear systematically 
downregulated in that group even if nothing biologically different is happening. This looks like signal. It is noise.

TODO a diagram? 

!!! danger "Recoverable vs unrecoverable"
    Depth variation distributed randomly across conditions can largely be corrected by normalisation. Depth variation that tracks with biological groups cannot. It is confounded with the signal of interest and cannot be separated from it analytically. This is a design failure, not an analysis problem.

## Single-cell sequencing data

### The biological reality

Single-cell RNA-seq resolves what bulk RNA-seq averages away. Rather than measuring the mean expression across thousands of cells, it profiles each cell individually — revealing the heterogeneity within a tissue, identifying rare populations, and capturing cell-type-specific responses that bulk methods cannot see.

This resolution comes from a biological fact: individual cells differ. Even cells of the same type show natural variation in 
gene expression, cell cycle state, and activity level. Single-cell methods make this variation visible rather than averaging it out.

### The statistical consequences

**Sparsity is structural, not technical**: a typical single-cell count matrix has 80–95% zeros (TODO is this true?). This is not primarily a technical failure. It reflects the genuine biology of individual cells: **most genes are not actively transcribed in any given cell at any given moment.** This level of sparsity requires specialised analytical approaches. Standard bulk RNA-seq tools are not appropriate.

**UMIs reduce but do not eliminate amplification bias**: single-cell libraries use unique molecular identifiers (UMIs) attached to each molecule before amplification. Because each original molecule has a unique tag, PCR duplicates can be identified and collapsed. This substantially reduces the amplification bias described in the sequencing section, but does not eliminate variation in capture efficiency between cells.

**Cells are not independent replicates**: this is the most consequential statistical property of single-cell data and the most commonly violated assumption. Cells from the same individual share a common genetic background, environment, and sample processing history. They are subsamples of a donor, not independent biological observations.

!!! danger "The pseudoreplication problem"
    Treating 50,000 cells from 5 donors as n = 50,000 is pseudoreplication. The true biological n is 5. Statistical tests that treat cells as independent observations artificially inflate degrees of freedom, producing false positives at a rate far higher than the nominal significance threshold implies.

    The correct approach is aggregating cell-level counts to the donor level before differential testing, known as pseudobulk analysis (TODO add link: covered in Module 6). The important point here is that the unit of replication is determined by biology, not by the resolution of the technology.

!!! TIP "TODO exercise: link to webR module"
    This connects directly to Pitfall 2 from Module 1. The Alzheimer's disease re-analysis, where reported DEGs dropped from 1,031 to 26 when pseudobulk was applied correctly, is a published demonstration of what happens when this assumption is violated.

    make an exercise that links this pitfall with a webR module if possible? 
    Whats the webR module that demonstrates these principles?

## Proteomics and metabolomics abundance data

### The biological reality

Proteins and metabolites are the functional outputs of gene expression. They are what the cell actually uses to do things, catalysing reactions, sending signals, building structures. Measuring them directly captures a dimension of biology that RNA cannot: **post-translational modification, protein stability, and metabolic flux are invisible to transcriptomics but visible here**.

### The statistical consequences

Mass spectrometry does not count molecules, instead it measures signal intensity (i.e. how strongly a molecule's chemical signature was detected by the instrument). This produces continuous values rather than integers, and the statistical properties are fundamentally different from count data.

**Continuous, approximately log-normal**: after log2 transformation, proteomics and metabolomics intensities approximate a normal distribution. This means tools designed for normally distributed data, including limma, which was originally developed for microarrays, are appropriate here, where DESeq2 and edgeR are not.

**The budget is total ion signal**: just as sequencing counts reflect a share of total reads, MS intensities reflect a share of total ion signal loaded onto the instrument. Differences in sample loading, protein concentration, or ionisation efficiency between samples 
create the same relative measurement problem as depth variation in sequencing.

**Missing values are not random**: in sequencing data, zeros are common but distributed across all genes approximately proportionally to expression level. In mass spectrometry, missing values are structurally biased toward low-abundance features. A protein is absent from a sample not because it wasn't there, but because its signal fell below the instrument's detection threshold.

!!! warning "Missingness not at random?"

    See: https://stefvanbuuren.name/fimd/sec-MCAR.html 

    Missing not at random — has direct consequences for imputation. Standard imputation methods that assume values are missing randomly will systematically overestimate the abundance of low-signal proteins. Methods designed for MNAR data, or explicit modelling of the 
    detection threshold, are required. Choosing the wrong imputation approach introduces systematic bias that propagates through every downstream analysis.

**Detection depends on acquisition mode**: in data-dependent acquisition (DDA), the instrument selects the most abundant ions for fragmentation. Low-abundance proteins may never be selected and are therefore absent from the data entirely, not as missing values, but as features that were never measured. Data-independent acquisition (DIA) improves coverage but introduces different analytical challenges. The platform choice directly shapes which proteins appear in the data at all.

!!! TIP "TODO exercise: link to webR module"

    Whats the webR module that demonstrates these principles?

## Microbiome compositional data

### The biological reality

Microbial communities are inherently relative. In any given sample, the organisms present compete for the same niche and resources. Sequencing captures a snapshot of which organisms were detectable under the conditions of that sample, not a census of every microbe present.

### The statistical consequences

Microbiome count data looks superficially similar to RNA-seq count data: it is a matrix of integers, one row per taxon, one column per sample. But it has an additional mathematical constraint that makes standard statistical tests invalid.

**Compositional data violates independence**: because counts sum to the total reads sequenced, individual taxon counts are not independent of each other. If one taxon genuinely increases in abundance, its larger share of the library means all other taxa must appear smaller in relative terms: even if their absolute abundance is unchanged. A taxon can appear to decrease purely 
because something else increased.

!!! danger "Why standard tests fail"
    Standard differential abundance tests assume that features are measured independently. In compositional data, they are not. Applying a t-test, Wilcoxon test, or even DESeq2 directly to microbiome relative abundances will produce spurious results, not occasionally, but systematically. Methods designed for compositional data (ALDEx2, ANCOM-BC, log-ratio approaches) are required.

**Contamination is structurally invisible**: low-biomass samples (e.g., tissue biopsies, placental swabs, blood) contain very little  microbial DNA relative to host DNA or reagent contaminants. Contaminant sequences from extraction kits, water, and lab surfaces can 
dominate a library from a low-biomass sample, and their compositional signature is indistinguishable from true biology without negative extraction controls.

!!! TIP "TODO exercise: link to webR module"
    This connects directly to Pitfall 6 from Module 1 and the placental microbiome case study. An entire body of literature built 
    on reagent contamination because controls were absent.
    
    TODO make an exercise that links this pitfall with a webR module if possible? 
    Whats the webR module that demonstrates these principles?

## Methylation array data

### The biological reality

DNA methylation is a chemical modification in the form of the addition of a methyl group to cytosine, primarily at CpG sites, that regulates gene expression without changing the underlying DNA sequence. It is one of the primary mechanisms of epigenetic control, and it varies between cell types, developmental stages, environmental exposures, and disease states.

### The statistical consequences

Methylation arrays measure the proportion of methylated signal at each CpG site, producing a value between 0 (fully unmethylated) and 1 (fully methylated). These are called beta values.

**Beta values are intuitive but statistically problematic**: a beta value of 0.8 means 80% of cells carrying this CpG are methylated at 
this site. This is biologically interpretable. But beta values are bounded between 0 and 1 and follow a beta distribution, not a normal distribution. They are heteroscedastic: variance is highest near 0.5 and lowest near the extremes. Standard linear models that assume homogeneous variance are inappropriate.

**M-values are needed for testing**: the logit transformation of beta values produces M-values, which are approximately normally distributed and have more uniform variance across the range. M-values are appropriate for statistical testing. Beta values are appropriate for biological interpretation and visualisation. Using beta values for testing and M-values for interpretation are both common errors.

**Cell type composition is the dominant confounder**: different cell types have systematically different methylation profiles. 
Blood-based methylation studies are particularly vulnerable: a sample with more granulocytes will look globally different 
from a sample with more lymphocytes, regardless of disease status. Without accounting for cell type composition, statistically or by cell sorting, observed methylation differences may reflect cellular heterogeneity rather than biology.

!!! TIP "TODO exercise: link to webR module"

    Whats the webR module that demonstrates these principles?

!!! info "Coming up in Module 5"
    Normalisation strategies appropriate to each 
    platform — and how to choose between them based 
    on your data and experimental design — are 
    covered in **Module 5: Normalisation and Scaling**.

## Key takeaways

Every omics measurement is a relative signal captured under a finite technical budget. The budget differs by platform, reads for sequencing, ion signal for mass spectrometry, probe fluorescence for arrays, but the consequence is universal: raw numbers cannot be compared across samples without normalisation appropriate to that platform's statistical properties.

The most important things to carry forward from 
this module:

- A count of zero does not mean absent, it may mean undetected
- Cells are not biological replicates, individuals are
- Missing values in proteomics are not random they are biased toward low abundance
- Microbiome data is compositional, standard tests assume independence that doesn't exist
- Beta values look interpretable but require transformation before statistical testing
- No single method fits all platforms, the choice of analytical approach must follow from the data type