## Metadata: putting data in context

High-quality omics data is only as useful as the metadata needed to interpret
it. Metadata is a structured record of the biological and technical
variables attached to each sample, and it is what allows bias to be investigated
rather than merely suspected.

### Why unrecorded variables can become permanent confounders

Module 1 (Pitfall 9) established the rule: a variable not recorded at the time of
collection cannot be recovered afterwards. A processing date not logged cannot be
reconstructed; a reagent lot number not noted cannot be read back off the samples.

What follows from that rule is an asymmetry worth designing around. Recording a
variable that later proves irrelevant costs almost nothing. Failing to record one
that turns out to be a confounder is permanent. That asymmetry is the argument
for the checklist below.

### When the confounder is the reason for the treatment

Treatments are chosen because of a patient's condition. If sicker patients tend
to receive Drug A and less sick patients Drug B, any difference in the omics
measurements may reflect severity as much as drug, and the two cannot be
separated if severity was never recorded.

This is the confounding structure from the confounding and batch section, with
one difference that matters here: it is invisible in the omics data. Nothing in
the measurements flags it. It is especially common in retrospective cohorts,
where samples and records were assembled for another purpose, and recognising it
requires clinical context rather than analysis.

### A minimal metadata checklist

The following checklist is organised into three classes by the type of the variable, where not every item applies to every study. Deciding not to record a variable should be intentional and documented.

---

**Class 1: Biological variables**

These describe the biological characteristics of the sample and determine the primary and secondary analyses.

| Variable | Why it matters |
|---|---|
| Age | Varies systematically with gene expression, metabolite levels and microbiome composition; matters whenever it differs between comparison groups |
| Sex | Systematic expression differences across thousands of genes; regulatory elements are sex specific |
| Diagnosis / condition | The primary biological grouping |
| Disease severity / stage | Determines whether comparison groups are biologically comparable |
| Treatment history | Current and recent medications alter expression, metabolite profiles, and microbiome |
| Collection site | Captures site-specific clinical, environmental and processing variation in multi-site studies |
| Collection time of day | Circadian variation in metabolites and some transcripts |
| Fasting status | Critical for metabolomics; affects circulating metabolites substantially |
| Tissue type /anatomical location | Expression profiles differ across regions of the same organ |

---

**Class 2: Technical variables**

These describe the handling of the sample from collection through sequencing and are essential for batch effect identification and correction.

| Variable | Why it matters |
|---|---|
| Collection date | Tracks when samples entered the workflow; can reveal temporal and collection-site effects |
| Sample preservation method | FFPE, fresh frozen, snap frozen, stabilisation reagent |
| Sample extraction batch | Groups samples that share extraction conditions |
| Operator ID | Operator-specific technique variation is real and systematic |
| Extraction date | Day level batch tracking; reagent and equipment state |
| Library preparation batch | Identifies which samples share a library prep reaction |
| Sequencing run / flow cell ID | Identifies which samples share a sequencing run |
| Instrument ID | Systematic differences exist between instrument units of the same model |
| Sequencing lane | Lane level variation within a flow cell |
| RNA/DNA quality metrics | RIN for RNA, DIN for DNA, 260/280 where applicable; baseline quality for each sample |
| Input quantity | Amount of material used for library preparation |

---

**Class 3: Contextual variables (study specific)**

These apply to specific sample types, platforms, or study designs. The decision to record them should be made during study design, not after the first PCA plot reveals unexpected variation.

| Variable | Applies to |
|---|---|
| Ischaemia time (delay from collection to preservation) | Tissue biopsies, surgical and post mortem samples |
| Freeze thaw cycle count | Any frozen sample, protein and RNA integrity degrade with each cycle |
| Shipping conditions and duration | Samples transported between sites |
| Reagent lot number | Lot-to-lot variation in antibodies, extraction kits and library-prep reagents is documented across platforms |
| Cell passage number (the number of times a cell line has been subcultured) | Cell line experiments |
| Growth conditions / media batch | In vitro experiments |
| BMI / body composition | Metabolomics, immune profiling |
| Genetic ancestry / population structure | GWAS, pharmacogenomics; record self-identified ethnicity separately if used, it captures social and environmental exposure that ancestry does not |
| Time from symptom onset | Infectious disease, acute injury studies |



<small> Time from symptom onset means, the elapsed time between when a patient first noticed symptoms relevant to the study condition and when the sample was collected (or when the measurement was taken). </small>

---

!!! success "Practical recommendation"
    Assign someone to maintain the metadata sheet at the bench or during the clinical visit. Responsibility matters. Do not rely on retrospective reconstruction from lab notebooks or electronic health records. Partial recovery is possible but generally incomplete, and the variables most likely to be lost are the technical ones that are most useful for batch-effect investigation.

---

## Module 2 summary: six questions to ask before any omics experiment

Modules 1 and 2 can be distilled into six questions, all of which should be
answered *before* data generation begins. The unit of replication and controls
come from Module 1's pitfall framework; batch, sample size, and platform
questions come from Module 2's design decisions. They apply to every omics
platform, the specific answers will differ, but the need to answer them does
not.

!!! info "Pre-experiment checklist"

    **Q1 : Unit of replication:**
    What is the biological question, and what constitutes one independent replicate? Is the unit a patient, a mouse, a cell line passage, a microbiome donor? Ensure the n in your study design reflects this unit, not cells, wells, or technical measurements of the same sample.

    **Q2 : Batch design:**
    Are all biological groups present in every processing batch? If any batch contains only one biological group, batch and biology are not estimable from the data, and the study is at risk of an unrecoverable confound.

    **Q3 : Metadata:**
    What biological and technical variables will be recorded, by whom, and at what point in the workflow? Every variable not recorded could be a confounder that cannot be removed.

    **Q4 : Sample size:**
    Was n determined by a power estimate appropriate for omics, or by budget? If by budget, what are the consequences for the claims the study will make, and are those claims honest about the study's limitations?

    **Q5 : Platform fit:**
    Does the technology match the resolution and scale the biological question requires? Bulk where single cell is needed, short read where long read is needed, or DDA where DIA is needed? These mismatches cannot be corrected downstream.

    **Q6 : Controls:**
    Are positive and negative controls included in the experimental design? Negative extraction controls for microbiome studies, ERCC spike-ins for RNA-seq, pooled QC samples for metabolomics and proteomics. Without appropriate controls, contamination and technical artefacts are much harder to distinguish from biology.

    **If any answer is "I don't know" or "no", flag it before analysis begins.** Not to block the work, but to be honest about what the data can and cannot support.


??? abstract "Further Reading, experimental design in omics"

    Wagner & Kleiner. How thoughtful experimental design can empower 
    biologists in the omics era.
    *Nature Communications* 2025; 16: 7263.
    [doi:10.1038/s41467-025-62616-x](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"} 

    Lafzi, Atefeh, et al. "Tutorial: guidelines for the experimental design of single-cell RNA sequencing studies." [Nature protocols 13.12 (2018): 2742-2757.](https://www.nature.com/articles/s41596-018-0073-y){target="_blank"}