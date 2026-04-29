## Sample Size and the Sequencing Depth Trap

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Apply the sample size–sequencing depth trade off under a fixed budget
      constraint, and identify the limited cases where increased depth is
      biologically justified.

Most omics studies end up with the sample sizes they do not because someone ran a power calculation, but because of what was available, remaining biobank samples, a sequencing run that needed filling, or a grant budget that ran out. That is understandable, but it has consequences. Studies that are technically well executed can still be statistically underpowered in ways that are not obvious until the results fail to replicate, sometimes years later when another group tries to build on the work.

---

### Why classical power calculations do not translate to omics

The power formulas most researchers encountered in a statistics course were designed for experiments with a single primary endpoint, a clinical trial testing one outcome, or a lab experiment comparing two means. Those formulas assume you know roughly what the variance looks like, you are testing one hypothesis, and your significance threshold is 0.05.

None of that holds in omics. You are testing thousands to millions of features simultaneously, variance is feature specific and largely unknown before you collect the data, and multiple testing correction pushes the effective significance threshold well below 0.05. A study nominally "80% powered" for a single gene is not 80% powered across the transcriptome. In practice, n = 6 per group might detect a reasonable fraction of truly differentially expressed genes before correction, but after FDR adjustment that fraction can drop sharply, because you are no longer testing against α = 0.05, but against a much smaller genome-wide threshold.

---

### What actually works for power estimation in omics

Given these complications, the most useful approaches are empirical rather than analytical.

**Pilot-data simulation** uses count distributions estimated from small existing datasets to simulate the full analysis pipeline at increasing sample sizes. This preserves the structure of real measurement noise rather than replacing it with a textbook variance assumption. Tools like `RNASeqPower` and `PROPER` implement this for RNA-seq and are worth using when pilot data exist.

**Empirical benchmarks from large replication studies** provide a reality check that no formula can. When a well-powered study like Schurch et al. finds that n = 3 misses the majority of differentially expressed transcripts, that finding is more informative than any closed-form estimate.

Neither approach is perfect. Pilot datasets are often small and may not represent the full study population. Published benchmarks come from specific platforms and tissues. But both are more grounded than plugging numbers into a calculator and hoping the assumptions hold.

---

The figure below shows something worth sitting with: even when the true effect size is the same, higher biological variability forces you to recruit substantially more samples to achieve the same power. In bulk omics this is compounded further by multiple testing correction, which shifts the detection bar for every single feature tested.

![Statistical power depends on both effect size and within-group variance; minimum sample sizes from power analysis](Figures_module3/wagner2025_fig2_A.jpg){width=90%}

<small>Ref: Wagner & Kleiner. *Nature Communications* 16, 7263 (2025).
[doi:10.1038/s41467-025-62616-x](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"}
(CC BY-NC-ND 4.0)</small>

---

### Practical lower bounds across platforms

These are not hard rules — the right sample size depends on the specific question, the expected effect size, and the variability of the biological system. But there are rough floors below which most studies struggle to produce reproducible findings.

!!! info "Indicative sample size ranges across platforms"

    **Bulk RNA-seq (differential expression)**  
    The n = 3 per condition that appears in a large fraction of published studies is generally not enough for stable inference. It can detect large, consistent effects, but it misses a substantial proportion of real biology and produces feature lists that shift considerably between replications.  
    - n ≥ 6 per group: workable minimum for moderate to large effects  
    - n ≥ 12 per group: more appropriate when small fold changes are biologically meaningful  

    **Proteomics (label free MS)**  
    Missingness complicates everything here. Low-abundance proteins may be detected in only a subset of samples, so the effective sample size for any given protein is smaller than the nominal n. This needs to be factored into expectations.  
    - n ≥ 5–8 per group: minimum practical threshold  
    - higher n is needed for low-abundance or variable proteins  

    **Metabolomics**  
    Metabolite profiles are more sensitive to environmental and physiological context than most other omics readouts. Inter-individual variability tends to be high, and studies below a certain size routinely produce unstable feature sets.  
    - n < 20 per group: substantial risk of non-replicable findings  
    - larger cohorts are generally needed for robust biomarker work  

    <small>
    Schurch et al. *RNA* 2016.
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}

    Atwal et al. *Nature Communications* 2025.
    [doi:10.1038/s41467-025-65022-5](https://www.nature.com/articles/s41467-025-65022-5){target="_blank"}

    Cochran et al. *TrAC Trends in Analytical Chemistry* 2024.
    [doi:10.1016/j.trac.2024.117749](https://www.sciencedirect.com/science/article/pii/S0165993624004011){target="_blank"}
    </small>

The differences between platforms are not just a matter of convention — they reflect genuine differences in how the underlying measurements behave. Tarazona et al. (2020) compared omics platforms directly on reproducibility, dynamic range, and detection limits, and the variation in those properties maps fairly directly onto why the sample size floors differ.

![Figures of Merit across omic platforms — comparative summary of quality properties that drive sample size requirements](Figures_module3/tarazona2020_fig2_FoM.png){width=90%}

<small>Ref: Tarazona S, et al. *Nature Communications* 11, 3092 (2020).
[doi:10.1038/s41467-020-16937-8](https://www.nature.com/articles/s41467-020-16937-8){target="_blank"}
(CC BY 4.0)</small>

---

**Sample size in multi-omics settings**

The challenge becomes more constrained when multiple platforms are involved. Each omic has its own power curve, and you cannot optimise sample size independently for each one — you need a single n that works across all of them, which in practice means satisfying the platform with the worst power characteristics.

The figure below (Tarazona et al., 2020) makes this concrete. Using a conservative dispersion estimate (75th percentile of pooled standard deviation), the MultiPower tool identifies n = 16 per group as the jointly optimal sample size across platforms in a real multi-omics study. Panels D and E show both that this target is achievable and that the recommendation holds up across the range of variability observed in the data.

![MultiPower output: per-omic power curves and combined multi-omic optimisation for RNA-seq and metabolomics](Figures_module3/tarazona2020_fig4_MultiPower_v02.jpg){width=90%}


??? info "scRNA-seq: number of donors vs number of cells per sample"
    Statistical replication is defined at the level of donors, not cells. 
    Increasing the number of cells per donor improves resolution but does 
    not increase independent information.  
    - n = number of donors per condition  
    - cell numbers primarily affect resolution, not power  

    The figure below illustrates this asymmetry clearly. Moving from 5 to 20 donors produces a substantial gain in power because each donor adds genuinely independent biological information. Moving from 25 to 500 cells per donor barely moves the needle, because those extra cells are not independent — they are all coming from the same individual.

    ![Donors vs cells per donor in scRNA-seq power](Figures_module3/03_scRNAseq_cells_vs_samples_v01.png){width=90%}

    <small>[Ref: Zimmerman K, et al. *Nature Communications* (2021)](https://www.nature.com/articles/s41467-021-21038-1){target="_blank"}
    (CC BY 4.0)</small>

---

### The sequencing depth trap

When there is no realistic path to enrolling more samples, teams often ask whether increasing sequencing depth could compensate. It is an appealing idea — more data from the same samples, no additional recruitment required. In most cases, it does not work.

Liu et al. (2014) tested this directly. Given a fixed budget, redistributing money toward additional biological replicates rather than deeper sequencing of existing ones produced substantially greater improvements in differential expression power. The reason is that additional reads improve measurement precision within a sample — useful up to a point — but they do nothing to reduce uncertainty about population-level variability, which is constrained by the number of independent samples, full stop.

> **Practical rule:** When budget is fixed, prioritise biological replication over sequencing depth for discovery-oriented analyses.

<small>Liu Y, et al. *Bioinformatics* 2014; 30(3): 301–304.
[doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}</small>

---

### When depth does matter

That said, there are situations where depth is genuinely the limiting factor and more sequencing is the right answer.

- **Low-abundance transcript detection:**  
  Rare transcripts need sufficient coverage to be detected reliably across samples. No amount of replication helps if the transcript is invisible at the current depth.

- **Somatic variant detection in tumour samples:**  
  Subclonal variants present at low allele fractions (1–5%) require high coverage — typically 200–300× — to be distinguished from sequencing noise. This is not a replication problem; it is a signal-to-noise problem at the measurement level.

  ![Sequencing depth requirements for variant detection](Figures_module3/03_Sequencing_depth.jpg){width=90%}

- **Rare cell populations in single-cell studies:**  
  Detecting very rare cell types may require deeper sequencing per cell or targeted enrichment, depending on the platform and question.

In these cases the argument for depth is not about statistical power in the usual sense — it is about whether the feature of interest is observable at all. Targeted approaches (FACS sorting, targeted sequencing panels) often handle this more efficiently than simply increasing depth across the board.

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