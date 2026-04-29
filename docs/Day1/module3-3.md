## Sample Size and the Sequencing Depth Trap

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Apply the sample size sequencing depth trade off under a fixed budget
      constraint, and identify the limited cases where increased depth is
      biologically justified.

In most omics studies, sample size is not determined by statistical design but by practical constraints:- budget, sample availability, or sequencing capacity. This creates one of the most persistent failure modes in the field: studies that are technically well executed but statistically underpowered. The consequences are often invisible at the time of analysis and only become apparent later, when results fail to replicate across independent cohorts or platforms.

---

### Why classical power calculations do not translate to omics

Traditional power calculations were developed for single endpoint experiments, such as clinical trials. They assume a **known or estimable variance, a single hypothesis test, and a fixed effect size of interest**.

Omics experiments violate all three assumptions simultaneously:
- thousands to millions of features are tested in parallel,
- variance differs across features and is often unknown,
- and multiple testing correction imposes a substantially stricter significance threshold.

As a result, a design that is nominally “80% powered” for a single gene does not translate to 80% power across the transcriptome. For example, a study with n = 6 per group may detect a substantial fraction of truly differentially expressed genes before correction, but after FDR adjustment, the effective sensitivity drops sharply because the significance threshold is no longer α = 0.05 but a much smaller genome wide cutoff.

---

### Appropriate approaches to power estimation in omics

Because analytical solutions are limited in high dimensional settings, omics studies rely primarily on empirical and simulation based strategies:

- **Pilot-data simulation:**  
  Empirical count distributions are estimated from small pilot datasets, followed by simulation of the full analysis pipeline across increasing sample sizes. Packages such as `RNASeqPower` and `PROPER` implement this framework for RNA-seq.

- **Empirical benchmarks from large studies:**  
  Large scale replication experiments provide **data driven estimates of the sample sizes** required for stable inference under realistic biological and technical variability.

These approaches are fundamentally preferable to closed form calculations because they preserve the structure of real measurement noise and feature specific variability.

---

The figure below illustrates how statistical power depends jointly on effect size and within group variance. Even when the true effect size is identical, increases in biological variability substantially raise the required sample size to achieve a fixed power threshold. In omics contexts, this relationship is further amplified by multiple testing correction, which effectively raises the bar for detection across all features.

![Statistical power depends on both effect size and within group variance; minimum sample sizes from power analysis](Figures_module3/wagner2025_fig2_A.jpg){width=90%}

<small>Ref: Wagner & Kleiner. *Nature Communications* 16, 7263 (2025).
[doi:10.1038/s41467-025-62616-x](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"}
(CC BY-NC-ND 4.0)</small>

---

### Practical lower bounds across omics platforms

!!! info "Indicative sample size ranges across platforms"

    **Bulk RNA-seq (differential expression)**  
    The field norm of n = 3 per condition is widely recognised as insufficient for stable inference. While it may detect strong signals, it typically captures only a subset of truly differentially expressed genes, with reduced reproducibility across studies.  
    - n ≥ 6 per group: minimum for moderate to large effect sizes  
    - n ≥ 12 per group: recommended when small changes (fold change) are biologically relevant  

    **Proteomics (label free MS)**  
    Missingness is a defining feature of MS based proteomics, particularly for low abundance proteins. This induces feature specific effective sample sizes that are often smaller than the nominal n.  
    - n ≥ 5–8 per group: minimum practical threshold  
    - higher n required for low abundance or highly variable proteins  

    **Metabolomics**  
    Inter individual variability is typically high, and metabolite profiles are strongly influenced by environmental and physiological context. Small studies frequently produce unstable feature sets.  
    - n < 20 per group: high risk of non replicable findings  
    - larger cohorts needed for robust biomarker discovery  

    <small>
    Schurch et al. *RNA* 2016.
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}

    Atwal et al. *Nature Communications* 2025.
    [doi:10.1038/s41467-025-65022-5](https://www.nature.com/articles/s41467-025-65022-5){target="_blank"}

    Cochran et al. *TrAC Trends in Analytical Chemistry* 2024.
    [doi:10.1016/j.trac.2024.117749](https://www.sciencedirect.com/science/article/pii/S0165993624004011){target="_blank"}
    </small>

The variation in these recommended ranges is not arbitrary; it reflects fundamental differences in measurement technology. As shown in Tarazona et al. (2020), omics platforms differ substantially in reproducibility, dynamic range, and detection limits. These properties directly influence effect size detectability and therefore the number of samples required for reliable inference.

![Figures of Merit across omic platforms — comparative summary of quality properties that drive sample size requirements](Figures_module3/tarazona2020_fig2_FoM.png){width=90%}

<small>Ref: Tarazona S, et al. *Nature Communications* 11, 3092 (2020).
[doi:10.1038/s41467-020-16937-8](https://www.nature.com/articles/s41467-020-16937-8){target="_blank"}
(CC BY 4.0)</small>

---

**Sample size calculations across multi Omics**

The figure below (Tarazona et al., 2020) illustrates differences in sample size requirements across omic platforms in a real multi omics setting. This highlights a core challenge of multi omics design: sample size cannot be optimised independently for each platform:- a common n must be found that satisfies the least powered omic. Using a conservative dispersion estimate (75th percentile of pooled standard deviation), the MultiPower tool identifies n = 16 per group as the jointly optimal sample size across all platforms. Panels D and E together show both that this target is achievable and that the recommendation is robust to variability in biological signal across features and platforms.

![MultiPower output: per-omic power curves (panels a–c) and combined multi-omic optimisation (panel d) for RNA-seq and metabolomics](Figures_module3/tarazona2020_fig4_MultiPower_v02.jpg){width=90%}

 
??? info "scRNA-seq: number of donors vs number of cells per sample"
    Statistical replication is defined at the level of donors, not cells. 
    Increasing the number of cells per donor improves resolution but does 
    not increase independent information.  
    - n = number of donors per condition  
    - cell numbers primarily affect resolution, not power  

    The figure shows a clear asymmetry in how power is gained in single cell RNAseq studies. Increasing the number of subjects from 5 to 20 leads to a substantial improvement in statistical power, reflecting the added independent biological information. In contrast, increasing the number of cells per individual from 25 to 500 has minimal impact on power, as these additional cells do not represent independent observations. 

    ![Paper on scRNA-seq](Figures_module3/03_scRNAseq_cells_vs_samples_v01.png){width=90%}

    <small>[Ref: Zimmerman K, et al. *Nature Communications* (2021): https://www.nature.com/articles/s41467-021-21038-1]( https://www.nature.com/articles/s41467-021-21038-1){target="_blank"}
    (CC BY 4.0)</small> 


### The sequencing depth trap

When additional biological samples are not feasible, a common but misleading strategy is to increase sequencing depth instead. While intuitively appealing, this substitution rarely recovers the statistical information lost by low sample size.

Liu et al. (2014) explicitly evaluated this trade off and showed that reallocating budget toward additional biological replicates yields substantially greater gains in differential expression power than increasing read depth for a fixed number of samples. The key limitation is that variance estimation remains constrained by the number of independent samples. Additional reads improve precision within samples but do not meaningfully reduce uncertainty about population level variability.

> **Practical rule:** When budget is fixed, prioritise biological replication over sequencing depth for discovery-oriented analyses.

<small>Liu Y, et al. *Bioinformatics* 2014; 30(3): 301–304.
[doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}</small>

---

### Legitimate exceptions where depth is essential

The sequencing depth rule is not universal. There are specific contexts where depth is the limiting factor rather than replication:

- **Low-abundance transcript detection:**  
  Rare transcripts require sufficient depth to achieve stable detection across samples.

- **Somatic variant detection in heterogeneous tumours:**  
  Subclonal variants at low allele fractions (1–5%) require high coverage (200–300×) to distinguish signal from noise.
  
  ![Figures of Merit across omic platforms — comparative summary of quality properties that drive sample size requirements](Figures_module3/03_Sequencing_depth.jpg){width=90%}


- **Rare cell populations in single-cell studies:**  
  Detecting extremely rare cell types may require deeper sequencing or targeted enrichment strategies.

In these cases, increasing depth is not a substitute for replication but a requirement for observability of the biological signal itself.

Modern experimental strategies and platforms often address these constraints more effectively through targeted enrichment approaches (e.g. FACS sorting or targeted sequencing), rather than indiscriminate increases in sequencing depth.

---

### Further reading

??? abstract "Power estimation in omics"

    Schurch NJ et al. *RNA* 2016.  
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}

    Tarazona S et al. *Nature Communications* 2020.  
    [doi:10.1038/s41467-020-16937-8](https://www.nature.com/articles/s41467-020-16937-8){target="_blank"}

    Atwal S et al. *Nature Communications* 2025.  
    [doi:10.1038/s41467-025-65022-5](https://www.nature.com/articles/s41467-025-65022-5){target="_blank"}

    Liu Y et al. *Bioinformatics* 2014.  
    [doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}