# Module 1.2: Stage 1 - Design

Every omics study begins with a scientific question: a clearly defined knowledge gap that the experiment is designed to address. The question must be specific enough to determine which molecular layer is relevant, what comparison to make, and what a meaningful result looks like. From the question, four interconnected elements follow: a testable hypothesis, a set of study variables, a cohort design, and a platform selection. Each constrains the next, and all must be resolved before data collection begins.

Omics studies also carry costs across three dimensions that make upfront design particularly important:

| Cost dimension | Examples |
|---|---|
| **Financial** | Sequencing runs, reagents, platform fees |
| **Time** | Sample processing, analysis pipelines, validation |
| **Irreplaceability** | Clinical biopsies, rare cohorts, and longitudinal samples cannot simply be recollected |

## Foundations of study design 

Omics studies rest on four interconnected elements that must be defined before data collection begins: the scientific question, a testable hypothesis, the study variables, and the platform. 

The question identifies the knowledge gap; the hypothesis specifies what is expected and at which molecular level; the variables define what is being compared and what needs to be controlled; and the platform determines what the experiment can actually measure. Each element constrains the next.

### Scientific question 

The scientific question defines the scope and purpose of the study. A well-formed question identifies:

1. The biological system of interest
2. The condition or comparison being investigated
3. The molecular level at which an answer is sought

!!! tip "A useful test"
    Vague or broad questions like "what is different between cases and controls?" do not constrain design decisions and make it difficult to evaluate whether your results are meaningful.

    If the question cannot specify which molecular layer would provide the most informative answer, it is not yet specific enough to design a study around.

### Hypothesis

A testable hypothesis specifies what is expected to differ, at which molecular level, and in which biological context. A hypothesis framed at the wrong molecular layer will produce a study that cannot address the underlying question regardless of execution quality. 

For example, expecting a genetic cause for a phenomenon that is primarily regulated at the level of chromatin accessibility or post-translational modification will generate data that is technically valid but biologically uninformative for the question being asked.

### Variables

Three categories of variable must be identified before a study begins:

| Type | Definition | Examples |
|---|---|---|
| **Independent** | The factor being compared across groups | Disease status, treatment, developmental stage, environmental exposure |
| **Dependent** | The molecular measurement being taken | Gene expression, protein abundance, methylation state, metabolite concentration |
| **Confounding** | Variables associated with both the independent variable and the outcome that can distort the apparent relationship between them | Age, sex, batch, tissue composition, collection site |

Identifying and planning for confounders is a design task. Variables that are neither controlled nor measured at the time of sample collection cannot be accounted for during analysis.

### Platform selection

Platform selection follows from the hypothesis. The question determines which molecular layer is relevant; the molecular layer determines which platform is appropriate; the platform constrains resolution, sensitivity, throughput, and cost per sample. These decisions interact with cohort size: a more expensive platform may require reducing sample numbers, which directly reduces statistical power. Platform selection is covered in detail in Key Consideration 2 below.

---

## Consideration 1: Cohort design and confounding

??? note "Key terms"
    | Term | Definition |
    |---|---|
    | **Confounder** | A variable associated with both the exposure and the outcome that can distort the apparent relationship between them |
    | **Matching** | Pairing cases and controls on one or more covariates (e.g. age, sex) so that differences between groups cannot be attributed to those variables |
    | **Stratification** | Dividing the study population into subgroups defined by a variable, then comparing within each subgroup |
    | **Randomisation** | Randomly allocating samples to experimental groups, which distributes known and unknown confounders approximately equally across groups |
    | **Metadata** | Structured information describing the samples and conditions in a study: demographics, collection site, processing batch, storage conditions, and any other variable that might influence the measurement |

Molecular profiles are sensitive to many biological and technical variables simultaneously. Age, sex, disease state, medication use, tissue composition, and sample handling conditions can all alter measured signal across every omics layer. A study that does not account for these variables risks attributing their effects to the biological question of interest.

Approaches for managing confounders, matching, stratification, randomisation, and balanced sampling, are covered in the Stage A workshop slides. Not all confounders can be controlled prospectively, particularly in retrospective studies where samples were collected before the study was designed. The minimum requirement is that important sources of variation are measured and recorded in study metadata so they can be evaluated during analysis.

*Example:* A study recruiting cases from a specialist hospital and controls from a community health screen will differ systematically in age, medication use, comorbidity burden, and health-seeking behaviour. These differences will appear in the molecular data across every omics layer measured, not just in the outcome of interest.

??? example "Case study: Reference datasets carry their own sampling biases"

    The GTEx project profiled gene expression across 44 tissues in over 16,000 samples, making it one of the most widely used references in transcriptomics for normalisation and comparison. A 2020 analysis found that 37% of all genes show sex-biased expression in at least one tissue. GTEx itself is approximately two-thirds male and skews toward older donors. Studies that use GTEx as a normalisation reference inherit its sampling composition, whether or not that composition matches the population the study is designed to represent.

    This is not specific to GTEx or to gene expression data. Any reference dataset — a reference proteome, a methylation atlas, a metabolite database — reflects the population from which it was built. A 2011 review across ten biological fields found that male-only studies outnumbered female-only studies by more than 5:1 in multiple disciplines, and sex was frequently not reported at all. The NIH responded in 2016 by mandating that sex be considered as a biological variable in federally funded research design.

    <small>Beery & Zucker. *Neuroscience & Biobehavioral Reviews* (2011). [doi:10.1016/j.neubiorev.2010.07.002](https://doi.org/10.1016/j.neubiorev.2010.07.002){target="_blank"}</small>
    <small>Oliva et al. *Science* (2020). [doi:10.1126/science.aba3066](https://doi.org/10.1126/science.aba3066){target="_blank"}</small>

!!! danger "Design principle"
    A confounder that was neither controlled nor recorded cannot be modelled during analysis. If a variable may influence the outcome, measure it at the time of collection.

---

## Consideration 2: Platform selection

The platform determines what biological information the experiment can capture. A platform that cannot measure the signal of interest at the required resolution or sensitivity will produce data that cannot answer the question, regardless of downstream analysis.

| Mismatch type | Description | Example |
|---|---|---|
| **Scope** | The platform measures the wrong molecular layer for the question | A question about gene regulatory state is not answered by sequencing the genome |
| **Resolution** | The platform aggregates signal at a level that obscures the relevant biology | Bulk approaches average across heterogeneous cell populations; cell-type-specific responses cannot be recovered |
| **Sensitivity** | The platform cannot detect molecules at the abundance levels relevant to the question | In proteomics, acquisition mode determines which proteins are measured at all; key targets may be absent rather than under-quantified |
| **Technical scope** | The platform cannot capture the structural feature of interest | Short-read sequencing cannot resolve structural variants or full-length isoforms regardless of sequencing depth |
| **Novelty over fit** | A more sophisticated platform than the question requires is used, then analysed as though a simpler platform had been used | Single-cell omics applied to a bulk-level question, with no cell-type-level analysis performed |

!!! danger "Design principle"
    Platform selection is a biological decision driven by the question. It must be made before data collection and cannot be revised after.

---

## Consideration 3: Statistical power

??? note "Key terms"
    | Term | Definition |
    |---|---|
    | **p-value** | The probability of observing a result at least as extreme as the one obtained, assuming no true effect exists. A small p-value indicates the result is unlikely under the null hypothesis; it does not indicate the effect is large or biologically meaningful |
    | **Statistical power** | The probability that a study will detect a true effect of a given size, given the sample size and significance threshold used. Power increases with sample size and effect size, and decreases with stringent multiple testing correction |
    | **Effect size** | The magnitude of a difference or relationship between groups, independent of sample size |
    | **Multiple testing** | When many hypotheses are tested simultaneously, the expected number of false positives increases proportionally. At p < 0.05 with 20,000 features tested, approximately 1,000 false positives are expected by chance alone |
    | **False discovery rate (FDR)** | The expected proportion of statistically significant results that are false positives. Commonly controlled at 5–10% using the Benjamini-Hochberg procedure |
    | **Pseudoreplication** | Treating non-independent observations as independent. In single-cell and spatial omics, measurements from the same biological donor are not independent; the true sample size is the number of donors, not cells or spots |

In a standard single-outcome experiment, a significance threshold of p < 0.05 is widely used. In omics, thousands to millions of features are tested simultaneously. Multiple testing corrections reduce the effective per-feature significance threshold, which substantially increases the sample size required to maintain adequate power to detect true effects.

An underpowered omics study has two characteristic failure modes: it misses true effects (low sensitivity), and among the effects it does detect, it overestimates their magnitude. Inflated effect size estimates in small discovery samples are a primary reason that omics findings fail to replicate in independent cohorts. This pattern is consistent across genomics, transcriptomics, proteomics, metabolomics, and epigenomics, and is one of the main structural contributors to the omics reproducibility problem.

A 2024 meta-analysis of 244 clinical metabolomics studies illustrates the scale: of 2,206 metabolites reported as statistically significant, 72% were identified by only a single study, with contradictory directions of change even among those appearing in more than one. Small sample sizes were identified as a primary driver. <small>[Cochran et al. *TrAC* 2024](https://www.sciencedirect.com/science/article/pii/S0165993624004011){target="_blank"}</small>

Power calculations should be performed before data collection using realistic estimates of expected effect size, biological variability, and the significance correction that will be applied. The required sample size varies substantially by study type, platform, and whether the study is intended for discovery or validation.

!!! danger "Design principle"
    Statistical significance in an underpowered study does not indicate a robust finding. Power analysis is part of study design.

---