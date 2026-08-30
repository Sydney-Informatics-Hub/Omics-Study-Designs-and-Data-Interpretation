# Module 1.2.5 Reporting

The reporting stage is where findings are communicated, in publications, preprints, data repositories, and supplementary materials. It is also where many studies fail to provide the information that would allow others to evaluate, reproduce, or build on the work. A technically sound study with poorly documented methods, incomplete metadata, or overclaimed conclusions contributes less to the scientific record than its data would otherwise allow.

Two problems are particularly common in omics reporting: 

1. **Incomplete metadata**: the contextual information about samples, processing conditions, and study design that makes a dataset interpretable
2. **Conflation of discovery with validated finding**: the presentation of results from a single dataset as generalisable biology when they remain candidates awaiting independent confirmation.

??? note "Key terms"
    | Term | Definition |
    |---|---|
    | **Metadata** | Information recorded alongside biological measurements that describes the sample, its collection, processing, and the conditions under which it was generated |
    | **Exploratory analysis** | Analysis intended to generate hypotheses or identify candidates; findings should be treated as provisional |
    | **Confirmatory analysis** | Analysis designed to test a pre-specified hypothesis in an independent dataset; findings support or refute a biological claim |
    | **Independent cohort replication** | Testing the same finding using the same measurement platform in a new, independent dataset |
    | **Orthogonal validation** | Confirming a finding using a different measurement technology — for example, validating an RNA-seq result with RT-qPCR, or a proteomics finding with immunohistochemistry |

## Consideration 9: Metadata completeness

!!! danger "Design principle"
    Metadata that is not recorded at the time of sample collection cannot be recovered later. Every field left undocumented is a potential source of variation that can never be identified, modelled, or corrected for.

High-quality omics data is only as interpretable as the information recorded alongside it. Metadata includes:

| Category | Examples |
|---|---|
| **Technical** | Processing date, batch identifier, reagent lot number, storage conditions, tissue handling time, operator, instrument ID |
| **Biological** | Age, sex, tissue type, cell type, developmental stage, organism strain |
| **Clinical** | Disease status, disease subtype, medication use, comorbidities, clinical scores, time of sample collection |

Metadata provides the context needed to distinguish biological signal from technical artefact. Without it, sources of variation that would otherwise be straightforward to account for become invisible.

Unlike batch effects that are documented, an unknown source of variation cannot be tested, modelled, or corrected. Its only trace may be unexplained structure in the data, suggestive of a problem, but impossible to resolve without the original records.

| Missing metadata | Platform | Consequence |
|---|---|---|
| Fasting status | Metabolomics | Group differences may reflect diet rather than biology |
| Ischaemia time | Any (tissue studies) | Degradation artefacts mistaken for disease effects |
| Processing date / batch | Any | Batch effects present but unidentifiable and uncorrectable |
| RNA integrity score | Transcriptomics | Degraded samples cannot be flagged or excluded retrospectively |
| Reagent lot number | Any | Lot-to-lot variation cannot be accounted for in analysis |

??? example "Case study: When metadata saves the analysis — GTEx and ischaemia time"
    ![](figs_m1/01_metadata_casestudy_v01.png){width=100%}

## Consideration 10: Discovery without validation

!!! danger "Design principle"
    A statistically significant result in a single dataset is a candidate finding, not a confirmed biological truth. The strength of the claim determines the level of validation required.

Finding a statistically significant result in omics is not the same as finding a generalisable biological truth. When thousands of features are tested simultaneously, some will reach significance by chance — this is why false discovery rate control is applied at all. But controlling the FDR within a dataset does not protect against findings that are real within that dataset but do not replicate elsewhere, driven by cohort-specific technical variation, sampling differences, or the particular composition of the study population.

Omics studies are especially vulnerable to this because the combination of high feature counts, small sample sizes, and high biological variability between cohorts creates conditions where dataset-specific noise can produce reproducible-looking signals that vanish in independent data. The problem is most severe when results from a discovery analysis are presented as confirmed biology — a generalisable biomarker, a mechanistic pathway, a clinical predictor — without having been tested in an independent cohort or on an independent platform.

Not every omics study requires external validation, but the requirement scales with the strength of the claim:

| Study type | Example claim | Validation required? |
|---|---|---|
| Exploratory / hypothesis generating | "We identify candidate features associated with condition X" | Not strictly, if clearly labelled as exploratory |
| Confirmatory / mechanistic | "Gene X drives this pathway in disease Y" | Strongly recommended |
| Translational / clinical | "This signature predicts patient outcome" | Essential |

Validation takes two forms. Independent cohort replication applies the same measurement platform to a new, independent dataset. Orthogonal validation confirms the finding using a different measurement technology — a proteomics result confirmed by immunohistochemistry, an RNA-seq result confirmed by RT-qPCR, a variant call confirmed by Sanger sequencing. Orthogonal validation is particularly important when an independent cohort is not available, and is standard practice before functional follow-up is initiated.

The consequences of skipping this step are documented across platforms. In transcriptomics, gene signatures derived from small or heterogeneous cohorts frequently show limited reproducibility across independent datasets of the same disease. In metabolomics, 72% of reported significant metabolites in one systematic review were identified in only a single study. In proteomics, the gap between biomarker discovery and clinical translation has remained largely unchanged since Rifai and colleagues described it in 2006 — standardisation, validation burden, and regulatory compliance continue to be cited as unresolved barriers nearly two decades later. <small>[Rifai et al. *Nature Biotechnology* 2006](https://doi.org/10.1038/nbt1235){target="_blank"} · [Proceedings of the 68th Benzon Foundation Symposium. *Journal of Proteome Research* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11652764/){target="_blank"}</small>

??? example "Case study: Two decades of unreplicable genetics — the candidate gene era"
    From the 1990s through the mid-2000s, hundreds of candidate gene association studies were published linking specific genetic variants to psychiatric and complex diseases. Most had sample sizes of 100–500. Results were statistically significant within each dataset.

    When adequately powered genome-wide association studies arrived (n > 10,000), the vast majority of these associations vanished. A landmark 2019 reanalysis of 18 candidate genes studied for decades in relation to depression found that none replicated in a sample of over 620,000 individuals.

    The candidate gene literature was not fraudulent — it was underpowered discovery presented as confirmed biology, without independent replication in adequately sized cohorts. Modern GWAS pre-register replication cohorts before publication precisely because of this history.

    <small>[Border et al. *American Journal of Psychiatry* 2019](https://psychiatryonline.org/doi/10.1176/appi.ajp.2018.18070881){target="_blank"} · [Ioannidis et al. *Nature Genetics* 2009](https://doi.org/10.1038/ng.295){target="_blank"}</small>

---

!!! info "Can errors be fixed?"

    !!! success "Recoverable: fixable at the analysis stage"
        Normalisation method choice; some batch effects if not confounded with biology; outlier handling.

    !!! warning "Limitable: partially addressable with caveats"
        Underpowered sample sizes; platform mismatch; suboptimal QC thresholds.

    !!! danger "Unrecoverable: cannot be fixed after data generation"
        Batch fully confounded with biological groups; missing or unrecorded metadata; wrong platform chosen for the question; samples pooled where individual-level inference was needed.

---

!!! info "Module 1.2.5 takeaways"
    - Metadata that is not recorded at collection cannot be recovered. Undocumented sources of variation cannot be modelled, corrected, or even identified — they become permanent ambiguities in the dataset.
    - A significant result in a single dataset is a candidate finding. Whether it requires validation, and what form that validation should take, depends on the strength of the claim being made.
    - Independent cohort replication and orthogonal validation are complementary strategies; orthogonal validation is particularly important when a second cohort is not available.
    - Omics studies are structurally prone to non-replicable findings: high feature counts, small samples, and cohort-specific variation combine to produce signals that appear robust within a dataset but do not generalise.
    - The move from exploratory candidate to confirmed biological finding requires independent evidence. Studies that skip this step should label their results as hypothesis-generating, not as established biology.