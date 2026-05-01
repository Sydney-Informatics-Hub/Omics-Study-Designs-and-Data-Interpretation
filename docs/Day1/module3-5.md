## Metadata: Putting Data in Context

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Draft a minimal metadata checklist for their own project and explain 
      why an unrecorded variable cannot be modelled, corrected for, or even 
      identified after data collection.

High quality sequencing or omics data is only useful, if meta information recorded alongside it. Metadata is a structured record of biological and technical variables associated with each sample. For many downstream analyses, meta data helps to explore the bias, and to discover new findings.

### Why unrecorded variables are permanent confounders

Every analysis that could be done on an omics dataset in the future depends 
on the metadata available today. A clinical variable which is not recorded at the time of sample 
collection cannot be retrieved later. For example: 

- Sample processing date not logged cannot be reconstructed. 
- A reagent lot number not noted cannot be recovered from the samples themselves.

Recording a variable that later proves irrelevant is inexpensive; failing to record a variable that turns out to be a confounder creates a permanent, unfixable problem. Its only trace may be an unexplained axis in a PCA plot which suggests a problem, but impossible to resolve without availability of original records.

###  Treatment choice creates confounding: a key pitfall in clinical omics studies

A common problem in clinical practice is that treatments are chosen because of a patient’s condition. If sicker patients tend to receive Drug A and less sick patients receive Drug B, any difference in omics measurements may reflect underlying severity as well as the drug and you can't separate those effects if severity wasn't recorded.

This problem is common in retrospective cohort (a study using previously collected records/samples) studies and is not detectable from the omics data alone. It requires knowledge of the clinical context and the metadata to record that context.

### A minimal metadata checklist

The following checklist is organised into three classes by the type of the variable, where not every item applies to every study. Deciding not to record a variable should be intentional and documented.

---

**Class 1 : Biological variables (required for every study)**

These describe the biological characteristics of the sample and determine the primary and secondary analyses.

| Variable | Why it matters |
|---|---|
| Age | Confounds gene expression, metabolite levels, microbiome composition across most disease comparisons |
| Sex | Systematic expression differences across thousands of genes; regulatory elements are sex specific |
| Diagnosis / condition | The primary biological grouping |
| Disease severity / stage | Determines whether comparison groups are biologically comparable |
| Treatment history | Current and recent medications alter expression, metabolite profiles, and microbiome |
| Collection site | Multi-site studies introduce site specific clinical and processing variation |
| Collection date / time | Circadian variation in metabolites and some transcripts; batch tracking |
| Fasting status | Critical for metabolomics; affects circulating metabolites substantially |
| Tissue type /anatomical location | Expression profiles differ across regions of the same organ |
| Sample preservation method | FFPE, fresh frozen, snap frozen, stabilisation reagent |

---

**Class 2: Technical variables (Mostly required for omics studies)**

These describe the handling of the sample from collection through sequencing and are essential for batch effect identification and correction.

| Variable | Why it matters |
|---|---|
| Sample extraction batch | Groups samples that share extraction conditions |
| Operator ID/Name | Operator specific technique variation is real and systematic |
| Extraction date | Day level batch tracking; reagent and equipment state |
| Library preparation batch | Identifies which samples share a library prep reaction |
| Sequencing run / flow cell ID | Identifies which samples share a sequencing run |
| Instrument ID | Systematic differences exist between instrument units of the same model |
| Sequencing lane | Lane level variation within a flow cell |
| RNA/DNA quality metrics | RIN, 260/280, DIN baseline quality for each sample |
| Input quantity | Amount of material used for library preparation |

---

**Class 3: Contextual variables (study specific)**

These apply to specific sample types, platforms, or study designs. The decision to record them should be made during study design, not after the first PCA plot shows some issues.

| Variable | Applies to |
|---|---|
| Ischaemia time (delay from collection to preservation) | Tissue biopsies, surgical and post mortem samples |
| Freeze thaw cycle count | Any frozen sample, protein and RNA integrity degrade with each cycle |
| Shipping conditions and duration | Samples transported between sites |
| Reagent lot numbers | Antibodies, extraction kits:- lot variation is documented across platforms |
| Cell passage number (the number of times a cell line has been subcultured) | Cell line experiments |
| Growth conditions / media batch | In vitro experiments |
| BMI / body composition | Metabolomics, immune profiling |
| Ethnicity / ancestry | GWAS, pharmacogenomics, biomarker studies |
| Time from symptom onset | Infectious disease, acute injury studies |



<small> Time from symptom onset means, the elapsed time between when a patient first noticed symptoms relevant to the study condition and when the sample was collected (or when the measurement was taken). </small>

---

!!! success "Practical recommendation"
    Assign someone to fill the sheet at the bench or during the clinical visit, responsibility matters. Do not rely on retrospective reconstruction from lab notebooks or electronic health records partial recovery is 
    possible but generally incomplete, and the variables most likely to be lost are the technical ones that are most useful for batch effect investigation.

---

## Module 3 Summary: Six questions to ask before any omics experiment

The design principles in this module can be distilled into six questions that should be answered *before* data generation begins. These questions apply to every omics platform, the specific answers will differ, but the need to answer them does not.

!!! info "Pre experiment checklist"

    **Q1 : Unit of replication:**
    What is the biological question, and what constitutes one independent replicate? Is the unit a patient, a mouse, a cell line passage, a microbiome donor? Ensure the n in your study design reflects this unit, not cells, wells, or technical measurements of the same sample.

    **Q2 : Batch design:**
    Are all biological groups present in every processing batch? If any batch contains only one biological group, batch correction is not possible and the study is at risk of an unrecoverable confound.

    **Q3 : Metadata:**
    What biological and technical variables will be recorded, by whom, and at what point in the workflow? Every variable not recorded could be a confounder that cannot be removed.

    **Q4 : Sample size:**
    Was n determined by a power estimate appropriate for omics, or by budget? If by budget, what are the consequences for the claims the study will make, and are those claims honest about the study's limitations?

    **Q5 : Platform fit:**
    Does the technology match the resolution and scale the biological question requires? Bulk where single cell is needed, short read where long read is needed, or DDA where DIA is needed? these mismatches cannot be corrected 
    downstream.

    **Q6 : Controls:**
    Are positive and negative controls included in the experimental design? Negative extraction controls for microbiome studies, ERCC spike-ins for RNAseq, ###pooled QC samples for metabolomics and proteomics##. Without them, 
    contamination and technical artefacts cannot be distinguished from biology.

    **If any answer is "I don't know" or "no", flag it before analysis begins.** Not to block the work, but to be honest about what the data can and cannot support.


??? abstract "Further Reading, experimental design in omics"

    Wagner & Kleiner. How thoughtful experimental design can empower 
    biologists in the omics era.
    *Nature Communications* 2025; 16: 7263.
    [doi:10.1038/s41467-025-62616-x](https://www.nature.com/articles/s41467-025-62616-x){target="_blank"} 

    Lafzi, Atefeh, et al. "Tutorial: guidelines for the experimental design of single-cell RNA sequencing studies." [Nature protocols 13.12 (2018): 2742-2757.](https://www.nature.com/articles/s41596-018-0073-y){target="_blank"} 

  