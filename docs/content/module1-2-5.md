## 🟠 Stage E: Reporting 

### Pitfall 9: Lost or incomplete metadata

High quality sequencing data is only as useful as the information
recorded alongside it. Missing or incomplete metadata, sample
processing dates, batch numbers, storage conditions, clinical
variables, tissue handling times, can render an otherwise technically
sound dataset uninterpretable.

Critically, **metadata that is not recorded cannot be recovered**.
Unlike batch effects that are documented, an unknown source of
variation cannot be tested, modelled, or corrected for in analysis.
Its only trace may be an unexplained axis in a PCA plot or a
pattern of QC outliers, suggestive of a problem, but impossible
to resolve without the original records.

!!! danger "The unrecoverable rule"
    Every metadata field not recorded at the time of sample collection
    is a potential confounder you can never remove.

**Real consequences of missing metadata:**

**No fasting status recorded (metabolomics)**
If fasting vs fed state is not documented, differences in circulating
metabolites between groups may simply reflect recent food intake
rather than disease biology, and there is no way to distinguish
the two after the fact.

**No ischaemia time recorded (tissue studies)**
If the delay between tissue collection and processing is unknown,
gene expression or protein abundance changes caused by sample
degradation can be mistaken for true disease effects. This is
particularly acute in surgical and post-mortem tissue studies.

**No batch or processing date recorded (any omics)**
Without knowing which samples were processed together, batch
effects cannot be identified or corrected, even with the most
sophisticated normalisation methods. The variation is present
in the data but invisible to the analyst.


??? example "Case study: When metadata saves the analysis, GTEx & Ischaemia Time" 
    ![](figs_m1/01_metadata_casestudy_v01.png){width=100%}  

!!! info "Coming up in Module 3"
    Designing a metadata collection plan, including a minimal
    metadata checklist for omics studies is covered in
    **Module 3: Experimental design fundamentals**.

#### Pitfall 10: Discovery without validation

Finding a statistically significant result in omics is not the
same as finding a generalisable biological truth. When thousands
of genes/proteins are tested simultaneously, some will reach significance
by chance and results derived from a single dataset may reflect
dataset specific effects (technical, cohort, or sampling variation) rather than true biology.

Not every omics study requires external validation, but the
requirement scales with the strength of the claim being made:

| Study type | Example claim | Validation required? |
|---|---|---|
| Exploratory / hypothesis generating | "We identify candidate DEGs associated with condition X" | Not strictly, if clearly labelled as exploratory |
| Confirmatory / mechanistic | "Gene X drives this pathway in disease Y" | Strongly recommended |
| Translational / clinical | "This 10 gene signature predicts patient outcome" | Essential |

Validation can take two forms: **independent cohort replication** (the same measurement platform applied to a new dataset) and **orthogonal validation** (a different measurement technology applied to the same finding. For example, confirming a proteomics finding with immunohistochemistry, an RNAseq hit with RT-qPCR or a variant call with Sanger sequencing). Orthogonal validation is particularly valuable when an independent cohort is not available, and is standard practice before functional follow up.

!!! info "The key principle"
    Any claim intended to generalise beyond the original dataset
    requires independent validation. Without it, results should
    be treated as exploratory candidates, not confirmed biology.

**Why omics is particularly vulnerable to above mentioned pitfalls**
Since omics measures high features (gene/proteins), sample size is often very small and biological variability between cohort sample is often high; so combination of all of them means that omics findings
are especially susceptible to dataset specific noise. 

- Differential expression analysis; gene signatures derived from small or heterogeneous cohorts often show limited reproducibility across independent datasets of the same disease
- Metabolomics biomarkers, as shown in Pitfall 2, 72% of
  reported significant metabolites were found in only one study
- **Proteomics:** a striking gap exists between biomarker discovery and clinical translation. Rifai et al. 
  described this validation gap in 2006 and nearly two decades 
  later, translating proteomics to clinical applications 
  has remained challenging despite significant technical progress,  
  with standardisation, regulatory compliance, and 
  the need for robust validation  continuing to be cited as 
  unresolved barriers at major proteomics symposia as recently as 2024.
  The problem Rifai described has not been solved, it has persisted 
  for two decades. <small>
    [Rifai et al. *Nature Biotechnology* 2006](https://doi.org/10.1038/nbt1235){target="_blank"}  
       [Proceedings of the 68th Benzon Foundation Symposium.
    *Journal of Proteome Research* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11652764/){target="_blank"}</small>
 
***The consequences are most severe when studies move from
discovery to claims of generalisable biomarkers, clinical
signatures, or mechanisms, without independent validation.***

??? example "Case study: Two decades of unreplicable genetics; The candidate gene era"

    From the 1990s through the mid 2000s, hundreds of candidate gene
    association studies were published linking specific genetic variants
    to psychiatric and complex diseases like depression, schizophrenia,
    addiction, personality traits. Most studies had n = 100–500.
    Results were statistically significant within each dataset.

    When adequately powered GWAS arrived (n > 10,000), the vast
    majority of these associations vanished. A landmark 2019 reanalysis
    of 18 candidate genes that had been studied for decades in
    relation to depression found that none replicated in a sample
    of over 620,000 individuals.

    The candidate gene literature was not fraudulent, it was
    underpowered discovery presented as confirmed biology, without
    independent validation in adequately sized cohorts.

    **The fix that was missing:**
    Independent replication in a larger cohort before claiming
    a generalisable genetic association. Modern GWAS pre register
    replication cohorts before publication precisely because of
    this history. <small> [Border et al. *American Journal of Psychiatry* 2019](https://psychiatryonline.org/doi/10.1176/appi.ajp.2018.18070881){target="_blank"} [Ioannidis et al. *Nature Genetics* 2009](https://doi.org/10.1038/ng.295){target="_blank"}
    </small>
---

!!! info "Can pitfalls be fixed?"
    
    !!! success "Recoverable :— fixable at analysis stage"
        - Normalisation method choice
        - Some batch effects (if not confounded with biology)
        - Outlier handling

    !!! warning "Limitable :— partially addressable with caveats"
        - Underpowered sample sizes
        - Platform mismatch
        - Suboptimal QC thresholds

    !!! danger "Fatal :— unrecoverable after data generation"
        - Batch fully confounded with biological groups
        - Missing or unrecorded metadata
        - Wrong omics platform chosen
        - Samples pooled where individual inference was needed

 