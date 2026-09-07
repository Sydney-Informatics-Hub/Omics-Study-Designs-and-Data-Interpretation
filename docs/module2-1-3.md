# 2.1.3 Measurement reliability and metadata

!!! info "Learning objectives"
    - Determine whether technical replication is warranted for a given platform and study design.
    - Explain how a shared reference sample enables batch effect estimation and correction.
    - Identify the biological, technical, and contextual variables that should be recorded for a given study.
    - Articulate why unrecorded variables cannot be recovered and how this constrains interpretation.

Section 2.1.1 addressed what to measure; Section 2.1.2 addressed how samples are allocated across processing conditions. This section covers two decisions that determine whether the resulting measurements can be interpreted: whether technical variation is characterised and controlled, and whether the contextual information needed to explain the data is recorded. Both share a critical property — neither can be addressed retrospectively. A reference sample that was never included and a variable that was never recorded leave identical traces in the data: an unexplained pattern that cannot be resolved.

??? tip "Consideration 8: Pseudoreplication and the unit of replication" 
    Only biological replicates (independent samples from the population) contribute to statistical power and n. Technical replicates are repeated measurements of the same sample; they characterise measurement consistency but do not represent additional independent observations. Conflating the two inflates the apparent sample size and can produce false confidence in the precision of an estimate.

??? tip "Consideration 9: Metadata completeness"
    Variables not recorded at the time of collection cannot be recovered afterwards. Recording a variable that turns out to be irrelevant costs almost nothing; but missing one that turns out to matter is a permanent gap.


## Technical replication: characterising the measurement

* A **biological replicate** is an independent sample from the population.
* A **technical replicate** is the same sample measured more than once. 

Technical replicates provide information about measurement consistency; they do not strengthen inference about biological variability. The choice of whether to include technical replicates is often a cost-based platform decision. Technical replicates are warranted when measurement noise is large enough to affect the scientific question. When measurement noise is small relative to the biological differences of interest, the same resources are generally better allocated to additional biological samples.

Platforms differ substantially in the ratio of technical to biological variance, and that ratio determines whether a technical replicate is measuring something that matters for the analysis. The table below summarises where technical variation is typically large enough to warrant dedicated replication, and where the same resources are better spent on additional biological samples.

| Layer | Technical vs biological variance | When technical replication may be useful |
|---|---|---|
| **Genome** | Technical much smaller than biological | Rarely; variant calling is highly reproducible across runs |
| **Epigenome** | Variable by assay; transposase and antibody efficiency can be substantial | Useful for ATAC-seq and ChIP-seq to characterise efficiency variation between batches |
| **Transcriptome** | Technical much smaller than biological | Rarely for power; useful for QC |
| **Proteome** | Often comparable, especially in discovery workflows | Often worthwhile; bridge channels in TMT designs serve this role |
| **Metabolome** | Often comparable | Yes; pooled QC injections are standard practice and expected by reviewers |

Sample quality modifies this picture across all layers. For degraded or low-input material (e.g. FFPE, archived tissue, needle biopsies) technical variance is elevated regardless of platform, and a reference sample or technical replicate becomes more informative than the table above would suggest.

### Technical replicates can remove noise

There is a second function of technical replication that is less commonly planned for. When the same sample is measured more than once, differences between those measurements cannot be attributed to biological differences. Instead, that signal can be used to estimate the structure of measurement variability and, with appropriate methods, subtract it from the dataset.

The most direct implementation is a **shared reference sample**, typically a pooled aliquot derived from all study samples, included in each batch and measured repeatedly through the run. Because its biology is fixed, any variation in its measurements is technical rather than biological. That signal provides both a direct measure of drift across batches and a common anchor for between-batch normalisation. 

How this is applied varies by platform:

| Layer | Common implementation | What it detects |
|---|---|---|
| **Genome** | Rarely needed | — |
| **Epigenome** | Input controls in ChIP-seq; spike-ins in ATAC-seq | Efficiency variation in IP or transposase activity |
| **Transcriptome** | Reference sample per library prep batch, particularly when input quality varies across samples | Between-batch drift; extraction quality differences |
| **Proteome** | Bridge or reference channel per TMT set; pooled reference across DIA batches | Between-batch intensity shifts; instrument drift |
| **Metabolome** | Pooled QC injections distributed across the run | Instrument drift over time; run-order effects |

Like blocking design explained in section 2.1.2, this only works prospectively. The reference material must be prepared and aliquoted before processing begins.

!!! question "Activity: When is technical replication warranted?"

    A DIA proteomics study is measuring 80 plasma samples across four mass spectrometry injection batches over two weeks. Which of the following best describes the role of technical replication in this design?

    - A. Technical replicates are not needed because DIA is a highly reproducible platform
    - B. A subset of samples should be measured twice to increase the effective sample size
    - C. A pooled reference sample should be injected at regular intervals across all four batches to track instrument drift and anchor between-batch normalisation
    - D. Technical replicates should be added at the analysis stage if a batch effect is detected in the PCA plot

    ??? example "Answer"
        **C.** Because its composition does not change, variation in its measurements across the run reflects instrument drift rather than biology, and that signal can be used to normalise the study samples.

        A is incorrect because run-to-run variation in mass spectrometry is substantial enough that technical variance can rival biological effect sizes, particularly across multi-week acquisition. B confuses technical and biological replication — measuring the same sample twice does not add to *n*. D is the most common mistake: technical replication must be designed in from the start, and a PCA plot showing batch structure cannot be corrected without a reference sample that was never included.

---

## Metadata: putting measurements in context

Metadata is a structured record of the biological and technical variables associated with each sample. It serves two functions that operate at different timescales.

| | Role of metadata |
|---|---|
| **Within a study** | Allows observed patterns to be investigated — when structure in the data does not map to the biological grouping of interest, recorded variables are the only basis for identifying its origin |
| **Beyond a study** | Determines whether the data can be reused. Omics datasets are resource-intensive to generate but in principle reusable across secondary analyses, cross-study comparisons, and meta-analyses; adequate metadata is what makes that possible |

The consequences of metadata errors compound with reuse. A mislabelled sample in a dataset deposited to a public repository will be inherited by every secondary analysis that draws on that data. A 2016 analysis of 70 human transcriptomics studies found that 46% contained mislabelled samples, with sex annotation errors present in the original publications rather than introduced at deposition ([Toker et al., 2016](https://f1000research.com/articles/5-2103/v2)). Completeness is a separate problem from accuracy: an assessment of 29 transcriptomics studies found that on average only 65% of key metadata fields were shared publicly, with a further loss between what was reported in the publication and what was deposited in the repository ([Rajesh et al., 2021](https://doi.org/10.1186/s13059-021-02332-z)).

Some of these errors are detectable computationally (e.g. sex annotation, can be cross-referenced against read coverage and expression of XIST and Y-chromosome-specific genes in genomics and transcriptomics data). Most metadata errors, however, leave no internal signal and can only be found by cross-referencing external records that may no longer exist.

??? abstract "Learn more about the importance of metadata for FAIR research"

    These requirements are formalised in the [FAIR principles](https://www.go-fair.org/fair-principles/) (Findable, Accessible, Interoperable, Reusable), the standard framework for research data sharing. Metadata is the mechanism through which each principle is satisfied; a dataset without adequate metadata fails all four.
    
    Caliskan, Dangwal & Dandekar (2023) *Computational and Structural Biotechnology Journal* 21, 4895–4913. [doi:10.1016/j.csbj.2023.10.006](https://doi.org/10.1016/j.csbj.2023.10.006)

Treatment or condition assignment is rarely random. In each case, a variable correlated with the treatment drives omics differences that are indistinguishable from a treatment effect, unless that variable was recorded. Consider these example confounding factors in different experimental settings:

| Setting | Example confounder |
|---|---|
| Clinical | Disease severity correlated with treatment choice |
| Animal | Body weight or baseline phenotype correlated with group assignment |
| Agricultural | Soil type, altitude, or microclimate correlated with treatment plot |
| In vitro | Passage number or media batch correlated with condition |

Recognising these structures requires knowledge of how samples were collected and groups were formed. Consistency in how variables are recorded matters as much as whether they are recorded. Field names such as "tissue type", "tissue_type", and "TissueType" are not interchangeable when data is processed computationally or deposited to a repository. Where controlled vocabularies or ontologies exist for a variable (e.g. organism, tissue, disease, sex, ancestry) using them rather than free text improves the findability and interoperability of the data. The [FAIR Cookbook](https://faircookbook.elixir-europe.org) (ELIXIR) provides metadata profiles and controlled vocabulary recommendations for common omics data types.

### A minimal metadata checklist

The purpose of the checklist is to ensure that no variable capable of explaining structure in the data is left unrecorded. Variables are grouped by the phase at which they should be captured. The following variables should be recorded for any omics study where possible, regardless of platform or sample type.

| Phase | Variable | Why it matters |
|---|---|---|
| **Collection** | Sample type | Tissue, biofluid, cell line, and environmental samples produce fundamentally different profiles; required for any cross-sample interpretation. |
| | Experimental group or condition | The primary comparison variable; must be unambiguous and in a machine-readable form. |
| | Biological replicate identifier | Distinguishes independent biological units from repeated measurements of the same sample. |
| | Species, strain, or cell line | Defines the biological system; required for any cross-sample comparison. |
| | Sex | Systematic differences in expression, metabolite levels, and immune profiles across all molecular layers; a confounder when unbalanced between groups. |
| | Age or developmental stage | Correlated with molecular profiles across all layers; relevant whenever it differs between comparison groups. |
| | Genotype | Required when genetic variation is a study variable or a potential confounder. |
| | Collection date and time | Tracks when samples entered the workflow; can reveal temporal drift or confounding between collection period and comparison group. |
| | Operator | Operator-specific variation in technique is real and systematic. |
| **Handling** | Preservation method | FFPE, fresh frozen, snap frozen, and stabilisation reagents produce systematically different molecular profiles. |
| | Time from collection to preservation | RNA and protein integrity degrade at different rates; critical for tissue biopsies and post-mortem samples. |
| | Freeze–thaw cycle count | Updated at each thaw; each cycle degrades RNA and protein. |
| **Processing** | Extraction batch and date | Identifies which samples share extraction conditions; day-level tracking captures reagent and equipment state. |
| | Reagent lot numbers | Lot-to-lot variation in extraction kits, antibodies, and library preparation reagents is documented across platforms. |
| | Input quantity | Affects noise level and downstream interpretation. |
| | Sample quality metric | The metric appropriate to the platform and molecular layer (RIN for RNA, DIN for DNA, cell viability for single-cell, protein concentration for proteomics). |
| **Measurement** | Measurement or acquisition batch | Identifies which samples were processed or acquired together. |
| | Instrument identifier | Systematic differences exist between units of the same model. |
| | Run identifier | Identifies which samples share a sequencing run, mass spectrometry acquisition session, or equivalent. |

Beyond these, additional variables should be identified during study design based on what could systematically differ between samples in ways unrelated to the biological question. The relevant question is not "what variables are standard for this field" but "what conditions were not held constant across all samples." For clinical studies this typically includes diagnosis, disease severity, treatment history, and fasting status; for animal studies, housing conditions, diet, and circadian phase; for cell line work, passage number and media batch. The list above should be extended to cover anything that varied.

!!! question "Activity: metadata audit"
    Each activity presents a scenario describing a real study design problem. You are not expected to know the answer, the goal is to find it.

    1. Read the scenario.
    2. Open a web browser and your search engine of choice. 
    3. Use the provided search term as a starting point. You may need to follow links or refine the search.
    4. Write a short answer to the **Find** question in your own words.
    5. Open the collapsible block to check your answer.

    ??? question "Scenario: DNA extraction and preservation in whole-genome sequencing"

        A whole-genome sequencing study compares tumour tissue from two patient groups. Samples from Group A were collected prospectively and stored as fresh frozen; samples from Group B were retrieved from a hospital biobank where tissue had been archived as FFPE blocks. Preservation method was not recorded in the study metadata.

        **Search:** FFPE DNA sequencing artefacts

        **Find:** What type of chemical damage does FFPE fixation introduce into DNA, how does it appear in sequencing data, and why does it create a problem when FFPE and fresh-frozen samples are analysed together without a recorded preservation variable?

        ??? example "Answer"
            FFPE fixation causes cytosine deamination, which converts cytosine to uracil (read as thymine in sequencing). This produces a characteristic excess of C→T (and G→A) substitutions that appear as apparent single-nucleotide variants. Because the artefact is systematic and differs between FFPE and fresh-frozen samples, it introduces a technical signal that is confounded with any biological difference between the two groups. Without preservation method recorded, the source of the substitution pattern cannot be distinguished from true somatic variation.

    ??? question "Scenario: Input controls in ChIP-seq"

        A ChIP-seq experiment targets a histone modification associated with active transcription. Libraries were prepared for the immunoprecipitated (IP) fraction only; no input control library was generated. After sequencing, peaks are called and used to identify regions of differential modification between two conditions.

        **Search:** ChIP-seq input control purpose

        **Find:** What does an input control represent in a ChIP-seq experiment, what sources of signal does it capture, and what cannot be determined about a called peak when no input control is available?

        ??? example "Answer"
            An input control is a sequencing library prepared from chromatin that has not been immunoprecipitated — it represents the background distribution of reads across the genome before any enrichment step. It captures variation in chromatin accessibility, PCR amplification bias, and local sequence composition. When a peak is called in the IP library, comparison against the input establishes that the enrichment is above background. Without an input control, there is no reference for what background signal looks like at that locus, so it is not possible to determine whether a peak reflects genuine antibody enrichment or local biases in the chromatin preparation. IP efficiency also varies between samples; without an input, differences between conditions may reflect variation in pull-down efficiency rather than changes in the modification itself.

    ??? question "Scenario: Time of day and gene expression"

        A bulk RNA-seq study compares gene expression in peripheral blood between two disease subtypes. Samples were collected during routine clinical visits: subtype A patients were typically seen in morning clinics and subtype B patients in afternoon clinics. Collection time was not recorded in the study metadata.

        **Search:** circadian gene expression peripheral blood

        **Find:** What proportion of the expressed genome shows circadian rhythmicity in peripheral blood, and what does this imply for a study where collection time is systematically different between comparison groups?

        ??? example "Answer"
            Studies of peripheral blood transcriptomics estimate that a substantial proportion of expressed genes — figures from primary literature range from roughly 10% to over 20% depending on the tissue and study design — show time-of-day variation driven by circadian regulation. In peripheral blood, immune cell composition itself varies across the day, which affects bulk expression profiles independently of gene regulation within cells. When collection time is systematically confounded with the comparison groups (morning vs. afternoon mapping onto subtype A vs. subtype B), observed expression differences between subtypes cannot be separated from circadian effects. The direction and magnitude of the confounding depends on which genes are of interest and the amplitude of their circadian oscillation.

    ??? question "Scenario: Pre-analytical variation in label-free proteomics"

        A label-free quantitative proteomics study compares plasma samples from two clinical sites. Sample preparation, including depletion of high-abundance proteins, reduction, alkylation, and tryptic digestion, was performed by different operators at each site. Operator identity was not recorded in the metadata.

        **Search:** pre-analytical variation label-free proteomics sample preparation

        **Find:** Which steps in proteomics sample preparation are documented sources of inter-operator or inter-laboratory variation, and what is the magnitude of that variation relative to typical biological effect sizes?

        ??? example "Answer"
            Pre-analytical variation in label-free proteomics is introduced at multiple steps: protein depletion efficiency, reduction and alkylation completeness, digestion efficiency (enzyme-to-substrate ratio, incubation time and temperature), and peptide clean-up. Inter-laboratory and inter-operator studies report coefficients of variation in peptide or protein abundance that can reach 20–40% for some proteins, with systematic rather than random structure — meaning the variation is directional and reproducible within an operator or site. This is comparable to or larger than the fold-changes typically reported as biologically significant in plasma proteomics. When operator is perfectly confounded with site, the technical and biological sources of variation cannot be separated.

    ??? question "Scenario: Pooled QC samples in untargeted metabolomics"

        An untargeted metabolomics study analyses plasma samples from 120 participants using reverse-phase LC-MS. Samples were acquired in a single continuous run lasting approximately 14 hours. No pooled QC samples were included in the acquisition sequence.

        **Search:** pooled QC samples metabolomics instrument drift

        **Find:** What is the purpose of pooled QC samples in a metabolomics acquisition, what signal do they capture across a run, and what cannot be determined or corrected when they are absent?

        ??? example "Answer"
            A pooled QC sample is prepared by combining equal volumes of all study samples, producing a mixture that represents the average composition of the dataset. Injected at regular intervals throughout the acquisition sequence, it provides repeated measurements of the same material under changing instrument conditions. Over a long LC-MS run, instrument response drifts due to changes in ionisation efficiency, source contamination, and column performance. The QC injections track this drift: because the material is constant, any change in measured abundance across QC injections is attributable to the instrument rather than biology. This signal is used to fit and apply a correction to the study samples. Without QC injections, there is no within-run reference for instrument state, and drift cannot be distinguished from a genuine biological gradient — for example, one that correlates with sample acquisition order if groups were not randomised across the run.

---

!!! info "Module 2.1.3 takeaways"
    - Technical replicates characterise measurement consistency but do not add to biological replicates.
    - Whether technical replication is warranted depends on the ratio of technical to biological variance for the molecular layer and sample type. 
    - A shared reference sample measured in every processing batch provides a direct estimate of technical drift that can be used for between-batch correction. 
    - Metadata serves two distinct functions: within a study it provides the basis for investigating unexpected structure in the data; beyond a study it determines whether the data can be reused. 



