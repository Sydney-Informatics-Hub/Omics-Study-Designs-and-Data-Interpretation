# Module 1.2.3: Pre-processing

Once molecular data is translated into a digital form by a sequencer or mass spectrometer, it undergoes a series of computational processing steps to prepare it for analysis. We subject the data to a series of statistical methods that allow us to evaluate data quality, reliably identify features of interest, and reduce technical noise before we approach the biological question. Not every step will apply to every platform and the order of pre-processing steps and choice of methods matters.

Additionally, these decisions are not neutral. A filtering threshold that removes rare features cannot be undone later. A normalisation method built on an assumption that does not hold for the data will distort every downstream comparison. An imputation strategy that ignores why values are missing will introduce bias into the features it was meant to repair. The choice of genome assembly, gene annotation, or protein database a pipeline is run against determines what can be detected; a read that cannot be mapped to the reference is lost, and an outdated annotation will misassign or miss features that have since been characterised.

Across platforms, preprocessing typically follows four stages:

| Stage | Purpose | Genome | Transcriptome | Proteome | Metabolome | Epigenome | Microbiome |
|---|---|---|---|---|---|---|---|
| **Quality control** | Identify data quality issues before analysis | Sequence quality, read length distribution | Mapping rate, rRNA fraction | Signal-to-noise ratio, identification rates | TIC stability, QC pool reproducibility | Detection p-values, conversion rate | Read depth, primer removal |
| **Data cleaning** | Remove low-quality observations and noise | Low-quality read removal, adapter trimming | Adapter trimming, low-quality read removal | Peak picking, blank subtraction | Feature filtering, solvent blank removal | Failed probe removal | Chimera filtering, host read removal |
| **Reconstruction** | Infer the original biological sequence or structure | Read mapping to reference genome | Read mapping to transcriptome | Peptide-to-protein mapping | Feature annotation against spectral libraries | Read mapping to reference genome | OTU/ASV clustering |
| **Feature identification** | Annotate biologically relevant features | Variant calling | Gene quantification | Protein quantification | Metabolite identification | Methylation calling | Taxonomic assignment, abundance estimation |

??? note "Key terms"
    | Term | Definition |
    |---|---|
    | **Quality control (QC)** | Assessment of raw data to identify samples or features that fail technical thresholds — low sequencing depth, poor alignment rate, high duplicate rate, degraded signal |
    | **Filtering** | Removal of features (genes, proteins, taxa, metabolites) that do not meet a minimum threshold of detection or prevalence across samples |
    | **Missingness** | The absence of a measured value for a feature in one or more samples; can arise from true absence, signal below the detection threshold, or technical failure |
    | **Imputation** | Estimating a missing value from the values that are present, using statistical or data-driven methods |
    | **Normalisation** | Adjustment of measured values to remove systematic technical variation — differences in sequencing depth, total protein loaded, instrument sensitivity — that would otherwise obscure biological differences |

!!! tip "Always keep your raw files!" 
    Preprocessing errors can be corrected by rerunning the pipeline on the raw data, which is one reason raw data must always be retained and every preprocessing decision documented.

## Consideration 6: Data quality and cleaning

!!! danger "Design principle"
    QC thresholds should be defined before examining the data and applied consistently. Post-hoc threshold adjustment to retain or exclude specific samples introduces bias.

### Quality control 

Raw data always contains observations of variable quality. Quality control is the process of: 

- Systematically evaluating the data before analysis
- Identifying samples that have failed partially during collection or processing
- Assessing whether the instrument or sequencing run performed consistently
- Checking that individual features meet a minimum standard of detection. 

Each of these can introduce a different kind of problem: a failed sample adds noise or outliers to group comparisons; a drifting instrument introduces a run-wide trend that affects every measurement; features indistinguishable from background inflate the apparent size of the dataset without contributing signal. Addressing them requires different decisions, and all three should be assessed before any filtering or normalisation is applied.

| Molecular layer | Platform | QC metric | What a failing value suggests |
|---|---|---|---|
| Transcriptome | Bulk RNA-seq | Number of mapped reads | Insufficient input RNA or failed library preparation |
| Transcriptome | Bulk RNA-seq | Proportion of reads mapping to rRNA | Incomplete rRNA depletion |
| Transcriptome | Single-cell RNA-seq | Proportion of mitochondrial reads per cell | Damaged or dying cells |
| Proteome | LC-MS/MS | Number of proteins identified per sample | Failed injection or blocked column |
| Proteome | LC-MS/MS | Total ion current (TIC) | Instrument sensitivity problem or sample loss |
| Metabolome | LC-MS / GC-MS | Reproducibility of pooled QC injections | Extraction failure or instrument instability |
| Metabolome | LC-MS / GC-MS | Signal-to-blank ratio | Feature indistinguishable from background noise |
| Microbiome | 16S / metagenomics | Read count per sample | Insufficient sequencing depth to represent community composition |
| Microbiome | 16S / metagenomics | Chimeric sequence rate | PCR amplification artefacts inflating diversity estimates |
| Epigenome | DNA methylation arrays | Detection p-value per probe | Probe failed to hybridise reliably |

### Filtering 

Filtering is a related but distinct step. Where QC removes low-quality samples or runs, filtering removes features — genes, proteins, taxa, metabolites — that are detected in too few samples or at too low a level to carry reliable information. A protein quantified in two samples out of eighty, or a metabolite whose signal is indistinguishable from the solvent blank, contributes noise rather than signal. In microbiome studies, taxa detected at a single read across the entire dataset are routinely removed on the same basis.

The risk in filtering is that low-prevalence or low-abundance features are not necessarily biologically unimportant. A taxon present in 15% of cases and absent from all controls would be removed by a standard 20% prevalence threshold — and with it, the only organism differentiating the two groups. A protein consistently detected at low abundance in one condition and absent in another carries exactly the kind of differential signal the study is trying to find. The appropriate threshold depends on the platform, the sample size, and what the study is designed to detect. It should be chosen with the biological question in mind, not inherited from a pipeline default.

### Missingness

Missingness is the absence of a measured value for a feature in one or more samples. A value can be absent because the feature was genuinely not present in the sample, because it was present but fell below the instrument's detection threshold, or because of a technical failure during processing. These situations are not equivalent and should not be handled the same way.

The key question is whether missingness is random or structured. When it is random, (unrelated to the true value of the feature or to sample group membership) imputation based on the distribution of observed values is defensible. When it is structured, (concentrated in particular samples, batches, or biological groups) it carries information that imputation can destroy. A feature consistently absent from one condition and present in another is not missing at random; that pattern is itself a potential biological finding, and imputing the absent values erases it before analysis begins.

The proportion of missingness also matters. A feature missing in the majority of samples in one group cannot be reliably estimated from the few values that exist. Whether it should be imputed, treated as absent, or excluded from the analysis depends on the platform and the question being asked, but the decision should be explicit, not left to a pipeline default.

### Normalisation

Measured values in omics data reflect both biological signal and technical variation. Two samples may produce different read counts, protein intensities, or metabolite peak areas not because the biology differs, but because one sample had more input material, was processed on a different day, or was run on the instrument at a different position in the queue. Normalisation adjusts for these technical sources of variation so that measurements are comparable across samples.

The appropriate method depends on the platform and the assumptions that hold for a given dataset. In RNA-seq, normalisation for sequencing depth is standard; the choice of method depends on assumptions about the distribution of counts across genes. In proteomics, median centering or total ion current normalisation correct for differences in the amount of protein loaded. In metabolomics, normalisation to an internal standard (a known compound added at a fixed concentration before extraction) corrects for variation introduced during sample handling, which is why spike-ins must be planned before data collection begins.

Some normalisation strategies assume that most features are unchanged between conditions. This assumption is violated when the biological effect is global — for example, a transcriptional shutdown affecting the majority of genes, or a metabolic phenotype characterised by broad shifts in abundance across many metabolites. In such cases, normalisation to a stable reference set or to spike-ins is more appropriate than methods that anchor to the dataset's own central tendency.

--- 

!!! info "Stage C takeaways"
    - Preprocessing transforms raw instrument output into a form suitable for analysis. The steps involved vary by platform, and the order and choice of methods affect what information enters the analysis.
    - QC should assess sample quality, run or instrument performance, and feature-level detection. Thresholds should be defined before examining the data.
    - Filtering removes low-quality or low-prevalence features, but low abundance does not mean biologically unimportant. Thresholds should reflect the biological question, not pipeline defaults.
    - Missing values arise for different reasons and the appropriate response differs in each case. Structured missingness may itself be a biological finding.
    - Normalisation corrects for technical variation but rests on assumptions about the data. Methods that require reference material must be planned before data collection begins.
    - The choice of reference database or genome assembly determines what can be detected. Outdated or mismatched references will silently exclude features from the analysis.
