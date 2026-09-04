# 2.7 Seeing the design as a whole

!!! info "Learning objectives"
    - Trace how a single design decision affects more than one of the module's three
questions
    - Apply the six-question pre-experiment checklist to identify unresolved risks 
    in a proposed design
    - Explain why none of these trade-offs should come at the cost of answering the
study's primary research question

The three questions have been asked one at a time so far. A real design has to
answer all of them at once, and the answers pull against each other. A tightly
matched cohort is easier to interpret and easier to power, and it speaks for
fewer people. Deeper sequencing buys detection and costs samples. Adding a
second site widens the claim and adds batch structure to manage.

Under a fixed budget, improving one of the three usually costs something on
another. The work is deciding which compromise you are making, and saying so.

---

## Where each decision lands

Every section of this module dealt with one decision. None of them affected only
one question.

| Decision | Accuracy and interpretability | Power and cost | Generalisability |
|---|---|---|---|
| **Platform and assay** (2.1) | Read length, acquisition mode and resolution set what can be measured at all | Cost per sample sets how many samples the budget buys | A targeted assay covers only the features named in advance |
| **Allocation to batches** (2.2) | A factor aligned with the groups is not estimable | Blocking removes a known source of variance, usually giving more power than randomising alone | Group composition is decided here; what it means for the claim is read in 2.6 |
| **Measurement and metadata** (2.3) | Reference samples separate drift from biology; unrecorded variables cannot be adjusted for | A recorded factor leaves less unexplained variance | Without recorded ancestry, site and conditions you cannot describe your own cohort |
| **Sample size** (2.4) | Usable observations per feature can be fewer than the nominal *n* | Effect size, variability and the multiple-testing burden set what you need | Small studies can give unstable estimates, which are less likely to replicate in another cohort |
| **Budget allocation** (2.5) | Depth sets what can be detected reliably | Depth buys detection, replication buys power; in multi-omics the most demanding platform sets the number | What the budget buys decides how many donors, sites or conditions can be included |
| **Cohort and scope** (2.6) | A relationship seen at one level need not hold at another | Broadening the cohort adds variability, which costs power | Who the findings apply to, and what they cover |

Read down a column to see what shapes one question. Read across a row to see
what a single decision costs elsewhere.

**The short version: every design choice changes what you can measure, what you
can detect, and who the findings apply to.**

---

## Six questions to ask before any omics experiment

Modules 1 and 2 can be distilled into six questions, all of which should be
answered *before* data generation begins. The unit of replication and controls
come from Module 1's pitfall framework; batch, sample size, and platform
questions come from Module 2's design decisions. They apply to every omics
platform. The specific answers will differ, but the need to answer them does
not.

!!! info "Pre-experiment checklist"

    **Q1: Unit of replication.**
    What is the biological question, and what constitutes one independent
    replicate? Is the unit a patient, a mouse, a cell line passage, a microbiome
    donor? Ensure the *n* in your study design reflects this unit, not cells,
    wells, or technical measurements of the same sample.

    **Q2: Batch design.**
    Are all biological groups present in every processing batch? If any batch
    contains only one biological group, batch and biology are not estimable from
    the data, and the study is at risk of an unrecoverable confound.

    **Q3: Metadata.**
    What biological and technical variables will be recorded, by whom, and at
    what point in the workflow? Every variable not recorded could be a
    confounder that cannot be removed.

    **Q4: Sample size.**
    Was *n* determined by a power estimate appropriate for omics, or by budget?
    If by budget, what are the consequences for the claims the study will make,
    and are those claims honest about the study's limitations?

    **Q5: Platform fit.**
    Does the technology match the resolution and scale the biological question
    requires? Bulk where single cell is needed, short read where long read is
    needed, or DDA where DIA is needed? These mismatches cannot be corrected
    downstream.

    **Q6: Controls.**
    What controls are appropriate for this experiment? Negative extraction
    controls for microbiome studies, spike-ins where relevant for RNA-seq,
    pooled QC samples for metabolomics and proteomics. Without appropriate
    controls, contamination and technical artefacts are much harder to
    distinguish from biology.

    **If any answer is "I don't know" or "no", flag it before analysis begins.**
    Not to block the work, but to be honest about what the data can and cannot
    support.

---

## What the module comes down to

Module 1 showed that some problems cannot be fixed after data collection. Module
2 dealt with the decisions that determine whether you meet them: what to
measure, how to allocate samples, what to record, how many to collect, how to
spend the budget, and who the study is about.

None of these decisions is made in isolation, and the most consequential ones
cannot be repaired once samples are collected or processed. A study that is
honest about which compromises it made is more useful than one that claims to
have avoided them all.

---

### Further reading

??? abstract "Experimental design in omics"

    Wagner MR, Kleiner M. How thoughtful experimental design can empower
    biologists in the omics era. *Nature Communications* 2025; 16: 7263.
    [doi:10.1038/s41467-025-62616-x](https://doi.org/10.1038/s41467-025-62616-x){target="_blank"}

    Lafzi A, Moutinho C, Picelli S, Heyn H. Tutorial: guidelines for the
    experimental design of single-cell RNA sequencing studies.
    *Nature Protocols* 2018; 13(12): 2742–2757.
    [doi:10.1038/s41596-018-0073-y](https://doi.org/10.1038/s41596-018-0073-y){target="_blank"}

    Tarazona S, Balzano-Nogueira L, Gómez-Cabrero D, et al. Harmonization of
    quality metrics and power calculation in multi-omic studies.
    *Nature Communications* 2020; 11: 3092.
    [doi:10.1038/s41467-020-16937-8](https://doi.org/10.1038/s41467-020-16937-8){target="_blank"}