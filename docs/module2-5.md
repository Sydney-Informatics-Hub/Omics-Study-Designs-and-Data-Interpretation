# 2.5 Spending the budget: depth and allocation

!!! info "Learning objectives"
    - Identify the impacts of measurement depth vs. coverage to a study
    - Consider the trade-offs between measurement depth vs. coverage to an example study with a fixed budget
    - Assess how a more cost-effective platform or library-prep/sampling strategy can be applied to resolve a research goal

!!! abstract "Design question: How should we spend the budget to get that evidence?"
    **Mainly affects:** Power and cost  
    **Also affects:** Accuracy and interpretability · Generalisability

Section 2.4 dealt with how much independent evidence a study needs. This section
deals with the money. Budgets are fixed, and most of the decisions that follow
are about spending the same pool on competing things: more samples or more reads
per sample, more donors or more cells, better detection or wider coverage.

> The number of samples is only half the decision. The other half is what you spend on each one.

---

## Depth vs replication: two jobs, one budget

This is where the depth question usually gets answered wrong. Depth and
replication do **two different jobs**, and conflating them is the mistake.

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

### What replication does: power

Here is the part depth cannot do. Increasing depth improves precision *within* a
sample. It does nothing about the variability *between* samples, which is what
replication allows you to estimate.

As 2.4 established, power comes from the number of independent biological units.
Adding reads to the same libraries measures those same units more precisely; it
does not add units. So under a fixed budget, the lever for power is more
biological replicates, not more reads per sample.

> **Practical rule:** Reach adequate depth first, then spend what remains on
> biological replicates. Beyond the depth your question needs, extra reads
> usually buy less than extra samples.

<small>
Liu Y, et al. *Bioinformatics* 2014; 30(3): 301–304.
[doi:10.1093/bioinformatics/btt688](https://academic.oup.com/bioinformatics/article/30/3/301/228651){target="_blank"}
</small>

!!! note "Depth as a confounder is a different problem"
    Depth also matters when it lines up with your biological groups, for example
    when one condition is consistently sequenced shallower than the other. That
    is a confounding problem (2.2), not a sample-size one.

---

## When detection is the limit

The rule above is for discovery studies comparing groups. There are cases where
the question is not "is this feature different" but "can I see this feature at
all," and there more samples do not help. The measurement has to change.

- **Low-abundance transcript detection.** If a feature is never detected, more
  replicates don't help. It has to be measurable first. This is the direct
  continuation of the detection mechanism above.

- **Somatic variant detection in tumour samples.** Calling low-frequency variants
  (roughly 1–5% allele fraction) generally requires substantially higher coverage
  to separate signal from sequencing noise.

![Sequencing depth requirements for variant detection](figs_m2/VAF_Sequencing_depth.jpg){width=90%}

- **Rare cell populations in single-cell studies.** Seeing a rare population
  usually means profiling more cells or enriching for them; deeper sequencing
  helps when the limit is detecting transcripts within each cell.

In each case the issue is observability, not statistical power. Targeted
approaches such as enrichment or panel-based sequencing are often more efficient
than deepening the whole dataset.

!!! note "The same trade-off in proteomics"
    On mass spectrometry there is no depth dial to turn, but the choice has the
    same shape. When the proteins a question depends on are poorly detected
    (2.4), adding samples does not make them appear. Enrichment, fractionation,
    depletion of abundant proteins, or a targeted acquisition method can raise
    detection directly, each at a cost in instrument time and each with biases of
    its own. Acquisition mode is part of this too: as 2.1 set out, DDA favours
    abundant ions while DIA samples a broader set.

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

## One budget across several platforms

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

---

## What to carry forward

- **Depth buys detection; replication buys power.** Depth sets a practical floor
  on what can be detected reliably within a sample. Reducing between-sample
  uncertainty takes more biological replicates.
- Under a fixed budget, reach adequate depth first, then spend what remains on
  replication.
- The exception is when the question is observability itself: rare transcripts,
  low-frequency variants, rare cell types, poorly detected proteins. There the
  measurement has to change, not the sample count.
- In multi-omics, one *n* has to serve every platform, so the design is set by
  the most demanding one.

---

!!! question "Activity: what depth makes visible"

    Download the activities page
    <a href="../Activities-webR/module2/module2_design_activities.html" target="_blank">
    <button style="background-color: blue; color: white;">
        ⬇ Download HTML
      </button>
    </a>
    or take it from the repo folder `Activities-webR/module2/`, and open it in
    Chrome or Edge. Head to the tab **Detection Floor**.

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
