# Module 5 — Normalisation in omics


!!! info "Learning objectives"
    - By the end of this module, participants should be able to: 
        - Explain, in non-technical terms, why normalisation is necessary for omics data (e.g. to remove library size or technical intensity differences) and why “raw counts/intensities” are rarely interpretable across samples.
        - Distinguish normalisation from variance stabilisation (scaling), explain what each step achieves separately, and identify why applying them out of order (or applying scaling without prior normalisation) could be methodological error.
        - Recognise when an inappropriate normalisation choice may be driving apparent biological findings.
        - Match normalisation logic to data type — bulk RNA-seq, single-cell RNA-seq, proteomics, and compositional microbiome data — by explaining what makes each context distinct, not by implementing the methods computationally. 


## Good source of # Normalization of gene counts affects principal components-based exploratory analysis of RNA-sequencing data (https://www.sciencedirect.com/science/article/pii/S0165993606002329)