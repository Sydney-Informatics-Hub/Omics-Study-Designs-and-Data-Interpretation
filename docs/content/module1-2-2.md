## 🟠 Stage B : Sample acquition 

Samples and data reach a study one of two ways: you generate them yourself, or
you use what someone else generated. Both bring technical structure with them,
what differs is how much of that structure you still control.

**Path A: collect and sequence your own.** In most cases, samples are never all processed at once. Recruitment runs over months or years, extractions happen on different days, libraries are prepared in kit-sized sets, and sequencing happens run by run. Each of those groupings is a **batch**, and batches are unavoidable, they're a property of doing the work. The problem is only when a batch lines up with your comparison (Groups): cases recruited in year one and controls in year three, or one person running the treated samples while someone else runs the controls. Then "batch" and "biology" are the same variable. The good news is that on this path *you* decide which sample goes in which batch, day and run, so the fix is available to you before anything is processed.

**Path B: using someone else's data.** Here the batch structure already exists and you didn't choose it and the batch is now the entire **study**, which bundles cohort, collection protocol, extraction kit, instrument and analysis pipeline into one label you can't take apart. The common fatal version is generating your own cases and taking controls from a public dataset: every case shares one study and every control shares another, so disease and study are perfectly confounded. The PCA will separate beautifully, but nothing in the data tells you whether you're seeing disease or the difference between two laboratories. Public data is excellent as an independent validation cohort, or when every dataset you include contributes *both* of your comparison groups. It is dangerous the moment it supplies one arm of the comparison.

The two pitfalls below apply on both paths.

### Pitfall 4: Batch effects

A **batch effect** is a systematic technical bias introduced when samples are processed under different experimental conditions, such as different sequencing runs, reagent lots, operators, instruments, or processing dates. Unlike random noise, batch effects produce consistent patterns in the data that can either resemble true biological variation or mask it, making technical artifacts difficult to distinguish from genuine biological signal.

*Example*: Batch effect fully confounded with biology.  
Study A processed all cases in Batch 1 (2023) and all controls in Batch 2 (2026). The PCA shows a clean separation. But it is driven almost entirely by batch, not biology. Cases and controls cluster by processing year, not by disease. There is no way to know whether any observed difference is biological or technical, because the two are perfectly aligned. **This design is unrecoverable**, becuase no downstream computational pipeline can reliably recover signal from a fully confounded dataset. 

Study B distributed cases and controls across both batches. The PCA still shows a batch structure circles (Batch 1) and triangles (Batch 2) separate within each group. But cases and controls remain distinguishable within each batch. The batch effect is now estimable and correctable. **The biology is recoverable**.


![Batch effect fully confounded with Biology](figs_m1/01_batch_Effect_v02.png){width=90%}

??? example "Case Study: When batch effects reach the clinic"

    Between 2006 and 2011, Anil Potti and colleagues at Duke published a 
    series of high profile papers claiming to have developed genomic 
    predictors of chemotherapy response in cancer patients using gene 
    expression microarrays. Three clinical trials were opened using these 
    predictors to assign patients to treatment arms.

    Keith Baggerly and Kevin Coombes at MD Anderson had been trying and 
    failing to replicate the research methods, finding systematic errors 
    in how the data had been processed; including off by one errors in 
    the assignment of drug sensitivity labels to cell lines and undisclosed 
    batch effects in the training data.

    ![Duke clinical trial retraction timeline](figs_m1/01_duke_case_study_01.png){width=90%}

    **Outcome:** The trials were halted. The case 
    became a landmark example of how undetected batch effects, combined 
    with lack of reproducibility, can cause direct patient harm.
    <small>Ref: [Baggerly & Coombes, *Ann. Appl. Stat.* 2009](https://doi.org/10.1214/09-AOAS291){target="_blank"}</small>

---
### Pitfall 5: Experimental controls 

Experimental controls determine whether measurements are technically reliable.

Examples include negative extraction controls, positive controls, spike-ins, process blanks, and technical replicates. These controls help identify contamination, assay failure, reagent problems, sample handling artefacts, and other sources of technical variation before data enter the analysis pipeline.

Without appropriate controls, technical artefacts may be difficult or impossible to distinguish from genuine biological signal. The resulting bias is carried forward into every downstream analysis.

| Platform	| Commonly overlooked control|
|---|---|
| 16S sequencing / metagenomics	| Negative extraction control |
| Bulk RNA-seq | RNA integrity assessment and balanced batch design|
| Single-cell RNA-seq |	Empty droplet controls, ambient RNA assessment|
| Proteomics (MS)	| Blank injections, digestion controls|
| Metabolomics	| Pooled QC samples, solvent blanks|
| DNA methylation assays	| Conversion efficiency controls|

---