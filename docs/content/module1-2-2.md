## 🟠 Stage B : Sample acquition 

### Path A: collect and sequrence your own 
### Path B: using Other people dataset

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