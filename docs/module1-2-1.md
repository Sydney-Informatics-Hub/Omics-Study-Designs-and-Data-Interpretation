## Module 1.2: Design</span>

**Thoughtful study design helps in saving cost across three dimensions:**

| Cost dimension | Examples |
|---|---|
| **Financial** | Sequencing runs, reagents, platform fees |
| **Time** | Sample processing, analysis pipelines, validation |
| **Irreplaceability** | Clinical biopsies, rare cohorts, longitudinal samples cannot simply be recollected |


Most poor study design decision are made during the **design stage** but only become visible at the **analysis stage** by which point they are often already compromised the study's results. This is why study design deserves as much rigour as the experiment itself.

### Pitfall 1: Sampling bias and inappropriate cohort design

Study design controls determine whether observed differences can reasonably be attributed to the biological question being studied rather than to systematic differences between groups.

Important considerations include age, sex, disease state, BMI, medication use, ethnicity, and recruitment source. 

Depending on the study, these factors may be addressed through matching, stratification, randomisation, balanced sampling, or careful collection of metadata.

Not all confounders can be controlled, particularly in retrospective studies where samples have already been collected. However, important sources of variation should be measured whenever possible and recorded in the study metadata so they can be evaluated during analysis.

*Example*: A transcriptomics study recruiting cancer cases from an oncology ward (median age 64) against controls from a university health check (median age 29) will find hundreds of "disease" genes that are really immune-ageing genes. Once the groups are recruited unmatched on age, no downstream analysis can separate the two signals.

??? example "Case study: The reference dataset has the same bias it's used to study"

    In 2011, a review of 2009 publications across 10 biological fields found male-only studies outnumbering female-only studies 5.5 to 1 in neuroscience and 5 to 1 in pharmacology, sex was often not even reported. The finding was influential enough that in 2016 the NIH made considering sex as a biological variable a formal requirement for federally funded research design, not just an analysis afterthought.

    Why the sampling choice matters mechanistically, not just ethically: a 2020 analysis of the GTEx project; 44 tissues, over 16,000 RNA-seq samples found that 37% of all genes show sex-biased expression in at least one tissue. A cohort imbalanced by sex isn't just missing half the population; it's silently confounding over a third of the transcriptome with a variable that was never built into the study design.

    The twist: GTEx itself, the reference dataset much of the field normalises against, is not immune. Its donor pool is roughly two-thirds male and skews toward older individuals, the same two variables named in this pitfall's confounder list. A study built on GTEx as a baseline quietly inherits GTEx's own sampling composition, whether or not that composition matches the population the study is actually about.

    <small>Beery & Zucker. *Neuroscience & Biobehavioral Reviews* 35, 565–572 (2011). [doi:10.1016/j.neubiorev.2010.07.002](https://doi.org/10.1016/j.neubiorev.2010.07.002){target="_blank"}</small>
    <small>Oliva et al. *Science* 369, eaba3066 (2020). [doi:10.1126/science.aba3066](https://doi.org/10.1126/science.aba3066){target="_blank"}</small>

!!! danger "Design principle"
    A confounder that was neither controlled nor recorded cannot be modelled directly. Once information is missing at the time of collection, there is usually no reliable way to recover it later. If a variable may influence the outcome, it is generally better to measure it than to assume it can be addressed retrospectively.


### Pitfall 2: Wrong platform for the biological question

Platform choice is a design decision, not a technical afterthought.
Selecting the wrong platform upstream cannot be compensated for by
better analysis downstream. The data simply does not contain the
information required to answer the question.

**Sequencing technology mismatch, short-read where long-read is needed**
Short-read sequencing cannot resolve structural variants, full length
isoforms, or repetitive regions, regardless of depth. This is a
read-length limitation, not a coverage problem.

*Example:* Short-read WES applied to structural variant detection
in repeat rich regions will produce false negatives that deeper
sequencing cannot recover.

**Proteomics acquisition mismatch**
In mass spectrometry proteomics, the instrument acquisition mode
determines which proteins get measured at all. Some modes
systematically miss low-abundance proteins by design, meaning
key targets may be absent from the data entirely, not just
under-quantified.

**Resolution mismatch, bulk where single-cell was needed**
Bulk RNAseq permanently averages signal across all cell types.
Rare populations and cell-type specific responses cannot be
recovered by deconvolution alone.

*Example:* Studying tumour infiltrating immune cells with bulk
RNA-seq produces a single averaged signal across cancer cells,
T cells, and macrophages, with no ability to identify which
population is driving the difference.

**Technology adopted for novelty rather than fit**
Single-cell omics adopted primarily because it is current, then
analysed as bulk, represents a significant waste of cost and
sample with no scientific gain over a cheaper bulk approach.

!!! danger "The unrecoverable rule"
    If the platform cannot capture the biological signal of interest,
    no analysis method can recover it. The choice must be made
    before data collection, not revisited after.

### Pitfall 3: Underpowered studies

In many omics studies, sample size is determined by budget or sample
availability rather than by statistical need. This is particularly
costly in omics, where thousands of molecular features are tested
simultaneously, multiple testing correction reduces the effective
power per feature dramatically, meaning that the sample size required to detect
true signal is far higher than most researchers expect.

The consequences are consistent across platforms:

- **Transcriptomics (RNAseq):** studies with n = 3 per condition,
  the field norm, typically detect only 20-40% of truly differentially
  expressed genes, with high rates of false positives among those reported. <small>[Schurch et al. *Rna* 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}</small>

- **Proteomics:** low sample size exacerbates the effects of missing values and technical variability, reducing statistical power and introducing bias, which can compromise reliable quantification across samples.<small>[Kong et al., *Proteomics* 2022](https://doi.org/10.1002/pmic.202200092){target="_blank"}</small>

- **Genomics (GWAS, variant calling):** underpowered cohorts produce
  associations that fail to replicate in independent datasets,
  driven by inflated effect size estimates in small discovery samples.<small>
    [Zou et al. *G3 Genes|Genomes|Genetics* 2022.](https://doi.org/10.1093/g3journal/jkac261){target="_blank"}. [Wray et al. *Nature Communications* 2018](https://www.nature.com/articles/s41467-018-07348-x){target="_blank"}
    </small>

- **Metabolomics:** Reproducibility crisis in metabolomics biomarker studies
A 2024 meta analysis study of 244 clinical metabolomics studies illustrates
  the scale of this problem: of 2,206 unique metabolites reported as
  statistically significant across these studies, 72% were identified by
  only a single study, with contradictory directions of change even
  for metabolites detected by more than one group. Small sample sizes
  were identified as a primary driver of this reproducibility failure. <small>[Cochran, Darcy, et al. *TrAC Trends in Analytical Chemistry* 2024](https://www.sciencedirect.com/science/article/pii/S0165993624004011){target="_blank"}</small>

- **Single cell omics:** pseudoreplication compounds the underpowering 
  problem, the true n is the number of donors, not cells.
  <small>[Murphy et al., *eLife* 2023](https://elifesciences.org/articles/90214){target="_blank"}</small>

In all cases, the result is the same: findings that look statistically
significant but do not replicate. This is one of the common
root causes of the omics reproducibility crisis. In practice, sample size requirements vary substantially by study type, e.g. discovery vs validation.

---