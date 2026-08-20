# Sample size, power, and sequencing depth

## Why omics studies end up underpowered

Sample size in omics is rarely set by a power calculation. It is set by budget, sample availability, or sequencing capacity, and the number is often decided before anyone asks what it takes to detect the effect of interest. The result is a study that is well executed at the bench but ***underpowered*** on paper. This does not announce itself during analysis. It shows up later, when the findings fail to replicate in a second cohort or on a second platform.

### Why classical power calculations don't translate

Standard power calculations assume a single hypothesis, an approximately known variance, and a 0.05 threshold. None of those hold cleanly in omics.

Thousands to millions of features are tested at once. Variance differs from feature to feature and is usually not known in advance. Multiple-testing correction then lowers the effective significance threshold for every feature.

The practical consequence is that "powered for one feature" is not "powered for the dataset." A study may recover a reasonable number of signals before correction, and far fewer once false discovery rate (FDR) adjustment is applied.

---

## What determines the sample size you need

This is the power and cost axis of the three: can you detect the signal you
are looking for, within your budget? Three things decide it and the one most
people reach for first, "how many samples feels like enough," is not among them.


**Effect size: how big a difference you are trying to detect.** Larger
differences need fewer samples; subtle ones need many more. This is the part most
people do account for.

**Biological variability: how much your samples differ from each other for
reasons unrelated to the effect.** This is the one that quietly sinks small
studies. Even with the effect size fixed, more variable biology needs more
samples to reach the same power. Variability, not effect size alone, is usually
what decides whether a study succeeds.

**The multiple testing burden.** In omics this sits on top of everything else.
Because every feature is tested and corrected against every other (false
discovery rate control, usually the Benjamini–Hochberg method), each individual
feature has to clear a higher bar than it would in a single hypothesis study. The
more features you measure, the higher that bar.

![Statistical power depends on both effect size and within-group variance; minimum sample sizes from power analysis](figs_m2/wagner2025_fig2_A.jpg){width=90%}

<small>
Ref: Wagner & Kleiner. *Nature Communications* 16, 7263 (2025).
[doi:10.1038/s41467-025-62616-x](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"}
(CC BY-NC-ND 4.0)
</small>

---

## Estimating it in practice

Because the classical formulas don't fit omics, sample size is best estimated
**empirically** rather than calculated, and the honest expectation is that the
number will come out higher than intuition suggests.

??? info "Two ways to estimate it empirically"
    **Pilot-data simulation.** Estimate the variability from a small pilot
    dataset, then simulate the full analysis across a range of sample sizes. This
    carries realistic measurement noise into the estimate, instead of assuming a
    variance you don't actually have.

    **Learning from large benchmarking studies.** Big replication studies give
    direct evidence of how sample size affects detection and reproducibility.
    Several have shown that *n* = 3 per group misses a large fraction of true
    differential expression.

    Neither is perfect, a pilot may not represent the full population, and
    published benchmarks are often specific to one platform or tissue. Both are
    still more informative than a formula applied to a variance you had to guess.


---

## Practical lower bounds

These are **indicative ranges, not universal cut-offs.** The right sample size
depends on biological variability, effect size, study design, and whether the
goal is discovery or validation not on the platform alone.

!!! info "Indicative sample size ranges across platforms"    

    **Bulk RNA-seq (differential expression)**  
    *n* = 3 per condition is common but rarely sufficient for stable inference:
    it detects large, consistent effects, but feature lists vary substantially
    between analyses. Two large benchmarking studies, one in yeast (48
    replicates), one in mouse (N = 30) independently land on the same range:  

    - *n* ≈ 6 per group: workable minimum for ***moderate to large effects***
    - *n* ≈ 12 per group: more appropriate when ***smaller*** changes matter  

    **Proteomics (label free MS)**  
    There is no universal proteomics minimum. Missing values are the
    complication: many proteins are not measured in every sample, so the
    *usable information for a given protein* is often lower than the number of
    samples run even though your biological *n* is unchanged.  
    - Plan *n* around expected variability and missingness rather than a fixed
      floor; low-abundance and highly variable proteins need more.  

    **Metabolomics**   
    Metabolite profiles are highly sensitive to biological and pre analytical
    variation, fasting state, time of day, diet, medication. Two people with
    similar genetics can show very different profiles if one has fasted and the
    other has just eaten. Between sample variability is correspondingly high.  
    - Discovery: ~5–10 per group is a common starting range, but reproduces
      poorly at the low end.  
    - Biomarker/clinical validation: many tens to hundreds per group.  
    - A meta-analysis of 244 clinical metabolomics studies found 72% of
      reported metabolites appeared in only one study and ~85% were
      statistically indistinguishable from noise, direct evidence that small,
      single cohort metabolomics findings often fail to reproduce.  

    <small>
    Schurch et al. *RNA* 2016.
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"} ·
    Halasz et al. *Nature Communications* 16 (2025).
    [doi:10.1038/s41467-025-65022-5](https://www.nature.com/articles/s41467-025-65022-5){target="_blank"} ·
    Cochran et al. *TrAC* 180, 117918 (2024).
    [doi:10.1016/j.trac.2024.117918](https://www.sciencedirect.com/science/article/abs/pii/S0165993624004011){target="_blank"}
    </small>

!!! warning "These are not magic numbers"
    *n* = 6 is not automatically a good design, and *n* = 20 is not automatically
    a safe one. Sample size should follow from the biological question, the
    expected effect size, the variability, and the power you need not from the
    platform. Standardising collection conditions can matter as much as adding
    samples.

---
## Depth vs replication: two jobs, one budget

This is the pivot of the whole section, and where the depth question usually gets
answered wrong. Depth and replication do **two different jobs**, and conflating
them is the mistake.

### What depth does: detection

Depth is a measurement budget spent *within* a sample. A sequencer cannot count
every molecule; it reads a subset of fragments and stops at a target depth. Each
feature's count is therefore a share of whatever total was generated for that
sample.

At shallow depth, low-abundance features drop in and out of detection across
samples, not because their expression changed, but because the sampling was too
sparse to catch them reliably. Increase the depth and they reappear. The biology
didn't change; the measurement improved.

![Shallow vs deep sequencing: how depth affects gene detection](figs_m2/02_shallow_vs_deep_sequencing_v2.jpg){width=100%}

<small>At a total of 10 reads, a gene at 1% true abundance receives no reads here and is invisible. Another at 5% receives a single read, technically detected but statistically unreliable; a replicate might return zero. At 1,000 reads, the same proportions produce reliable counts for both. **The biology did not change between the two panels. The budget did.**</small>

So depth sets a practical floor on what can be detected reliably. That floor is
set by the least-abundant feature your question depends on, not chosen
arbitrarily, and detecting that a feature is present takes less depth than
detecting a change in it.

!!! tip "Activity"
    Head to the webR page, tab **Count & Depth** → *Multigene Detection*.

### What replication does: power

Here is the part depth cannot do. Increasing depth improves precision *within* a
sample. It does nothing about the variability *between* samples, which is what
replication allows you to estimate.

As the replication section established, power comes from the number of
independent biological units. Adding reads to the same libraries measures those same units more precisely; it does not add units. So under a fixed budget, the
lever for power is more biological replicates, not more reads per sample.

> **Practical rule:** Reach adequate depth first, then spend what remains on
> biological replicates. Beyond the depth your question needs, extra reads
> usually buy less than extra samples.

<small>
Liu Y, et al. *Bioinformatics* 2014; 30(3): 301–304.
[doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}
</small>

!!! note "Depth as a confounder is a different problem"
    Depth also matters when it lines up with your biological groups e.g. one
    condition consistently sequenced shallower than the other. That is a
    confounding problem, not a sample-size one.

---
## When depth genuinely is the limit

The rule above is for discovery studies comparing groups. There are cases where
the question is not "is this feature different" but "can I see this feature at
all," and there depth is exactly the right lever.

- **Low-abundance transcript detection.** If a feature is never detected, more
  replicates don't help. It has to be measurable first. This is the direct
  continuation of the detection mechanism.

- **Somatic variant detection in tumour samples.** Calling low-frequency variants
  (roughly 1–5% allele fraction) generally requires substantially higher coverage
  to separate signal from sequencing noise.

![Sequencing depth requirements for variant detection](figs_m2/VAF_Sequencing_depth.jpg){width=90%}

- **Rare cell populations in single-cell studies.** Seeing a rare population
  usually means profiling more cells or enriching for them; deeper sequencing
  helps when the limit is detecting transcripts within each cell.

In each case the issue is observability, not statistical power. Targeted
approaches (enrichment, panel-based sequencing) are often more efficient than
deepening the whole dataset.

??? info "scRNA-seq: splitting a fixed budget between donors and cells"
    In single-cell RNA-seq the budget splits two ways: how many donors you
    profile, and how many cells you profile per donor. The two do different
    things: donors provide biological replication, cells provide deeper sampling
    within each donor.

    - *n* = number of donors per condition
    - More cells per donor improve resolution within that donor; they do not add
      biological replicates

    Moving from 5 to 100 donors substantially increases power, because each donor
    is new biological information. Going from 100 to 1000 cells per donor
    characterises each donor far better, but does not add biological replicates.

    ![Donors vs cells per donor in scRNA-seq power](figs_m2/03_scRNAseq_cells_vs_samples_v01.png){width=90%}

    <small>
    Zimmerman K, et al. *Nature Communications* (2021)
    [doi:10.1038/s41467-021-21038-1](https://www.nature.com/articles/s41467-021-21038-1){target="_blank"}
    </small>

---

### Sample size in multi-omics studies

In multi-omics studies, sample size cannot be optimised independently for each
platform. One *n* has to serve every dataset. You cannot "borrow" extra samples
for one platform without affecting the others, so in practice the design has to
satisfy the platform with the greatest sample-size requirement.

The figure below (Tarazona et al., 2020) makes this concrete: across six omics
platforms in a real multi-omics study, n = 16 per group was the sample size
required to meet the specified power criterion across all six platforms. That
number was set by the most demanding platform, not by the average one.

![MultiPower output: per-omic power curves and combined multi-omic sample-size optimisation across six omics platforms in the STATegra dataset](figs_m2/tarazona2020_fig4_MultiPower_v02.jpg){width=90%}

<small>
Tarazona S, et al. *Nature Communications* 2020; 11: 3092.
[doi:10.1038/s41467-020-16937-8](https://www.nature.com/articles/s41467-020-16937-8){target="_blank"}
</small>

## Key takeaways

- In omics studies, sample size is often constrained by budget rather than determined by the desired power. Underpowering is invisible until findings fail to replicate.
- What you need is driven by **effect size, biological variability, and the multiple-testing burden**, not by intuition about "enough" samples.
- Empirical estimates (pilot simulation, replication benchmarks) can provide more realistic power assessments than simple formula-based calculations for complex omics designs.
- **Depth buys detection; replication buys power.** Depth sets a practical floor on what can be detected reliably within a sample. Reducing between-sample uncertainty takes more biological replicates.
- Under a fixed budget, reach adequate depth first, then spend what remains on replication, unless the question is observability itself (rare transcripts, low-frequency variants, rare cell types), where depth is the correct lever.
- In multi-omics, one *n* has to serve every platform, so the design is set by the most demanding one.

---

### Further reading

??? abstract "Power estimation in omics"

    Schurch NJ et al. *RNA* 2016
    [PMC4878611](https://pmc.ncbi.nlm.nih.gov/articles/PMC4878611/){target="_blank"}

    Liu Y et al. *Bioinformatics* 2014
    [doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}

    Zimmerman K et al. *Nature Communications* 2021
    [doi:10.1038/s41467-021-21038-1](https://www.nature.com/articles/s41467-021-21038-1){target="_blank"}

    Tarazona S et al. *Nature Communications* 2020
    [doi:10.1038/s41467-020-16937-8](https://www.nature.com/articles/s41467-020-16937-8){target="_blank"}