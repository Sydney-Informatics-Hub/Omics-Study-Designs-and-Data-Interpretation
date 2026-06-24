TODO update as we go and simplify formatting. 

From module 1-1

??? abstract 

### Further Reading · Emerging Omics Technologies

    ** Spatial Transcriptomics**
    Entry-level overview, platform comparison, experimental design guidance 
    - [Williams CG et. al *Genome Medicine* 2022](https://link.springer.com/article/10.1186/s13073-022-01075-1){target="_blank"}
     
    spatial + single-cell integration, computational strategies
    - [Vandereyken K et. al *Nature Reviews Genetics* 2023](https://www.nature.com/articles/s41576-023-00580-2){target="_blank"}

    ---

    ** Long-Read Sequencing & Isoform Biology**
    
    Isoform resolution at single-cell level, library prep + bioinformatics
    - [Kumari P et.al 
      *Human Genetics* 2024.](https://link.springer.com/article/10.1007/s00439-024-02678-x){target="_blank"}
    
    Comprehensive guide: tools, applications, challenges
    - [Parker MT et. al *Nature Reviews Genetics* 2025](https://www.nature.com/articles/s41576-025-00828-z){target="_blank"}

    ---

  ### Further reading, Zero inflation and sparsity in omics

    **Conceptual framework, applies across all platforms**

    Jiang R, Sun T, Song D, Li JJ. Statistics or biology: the
    zero-inflation controversy about scRNA seq data. *Genome Biology*
    2022; 23: 31.
    [doi:10.1186/s13059-022-02601-5](https://doi.org/10.1186/s13059-022-02601-5){target="_blank"}

    Silverman JD, Roche K, Mukherjee S, David LA. Naught all zeros
    in sequence count data are the same. *Computational and Structural
    Biotechnology Journal* 2020; 18: 2789–2798.
    [doi:10.1016/j.csbj.2020.09.014](https://doi.org/10.1016/j.csbj.2020.09.014){target="_blank"}
   

    **Single cell RNAseq**

    Svensson V. Droplet scRNA-seq is not zero-inflated. *Nature
    Biotechnology* 2020; 38(2): 147–150.
    [doi:10.1038/s41587-019-0379-5](https://doi.org/10.1038/s41587-019-0379-5){target="_blank"}

    Wang X, He Y, Zhang Q, Ren X, Zhang Z. Direct comparative analyses
    of 10X Genomics Chromium and Smart-seq2. *Genomics Proteomics
    Bioinformatics* 2021; 19(2): 253–266.
    [doi:10.1016/j.gpb.2020.02.005](https://doi.org/10.1016/j.gpb.2020.02.005){target="_blank"}

    Ding J et al. Systematic comparison of single-cell and
    single-nucleus RNA-sequencing methods. *Nature Biotechnology*
    2020; 38: 737–746.
    [doi:10.1038/s41587-020-0465-8](https://doi.org/10.1038/s41587-020-0465-8){target="_blank"}

    Hou W et al. A systematic evaluation of single-cell RNA-sequencing
    imputation methods. *Genome Biology* 2020; 21: 218.
    [doi:10.1186/s13059-020-02132-x](https://doi.org/10.1186/s13059-020-02132-x){target="_blank"}


    **16S amplicon and metagenomics**

    Kaul A, Mandal S, Davidov O, Peddada SD. Analysis of microbiome
    data in the presence of excess zeros. *Frontiers in Microbiology*
    2017; 8: 2114.
    [doi:10.3389/fmicb.2017.02114](https://doi.org/10.3389/fmicb.2017.02114){target="_blank"}


    **Proteomics**

    Lazar C, Gatto L, Ferro M, Bruley C, Burger T. Accounting for the
    multiple natures of missing values in label-free quantitative
    proteomics data sets to compare imputation strategies.
    *Journal of Proteome Research* 2016; 15(4): 1116–1125.
    [doi:10.1021/acs.jproteome.5b00981](https://doi.org/10.1021/acs.jproteome.5b00981){target="_blank"}
    

    Kong W, Hui HWH, Peng H, Goh WWB. Dealing with missing values in
    proteomics data. *Proteomics* 2022; 22(23–24): e2200092.
    [doi:10.1002/pmic.202200092](https://doi.org/10.1002/pmic.202200092){target="_blank"}
  

    ---

    **Metabolomics**

    Do KT, Wahl S, Raffler J et al. Characterization of missing values
    in untargeted MS-based metabolomics data and evaluation of missing
    data handling strategies. *Metabolomics* 2018; 14: 128.
    [doi:10.1007/s11306-018-1420-2](https://doi.org/10.1007/s11306-018-1420-2){target="_blank"}

  ### Foundational framewor of Compositionality in Omics Data

    Gloor GB, Macklaim JM, Pawlowsky-Glahn V, Egozcue JJ.
    Microbiome datasets are compositional: and this is not optional.
    *Frontiers in Microbiology* 2017; 8: 2224.
    [doi:10.3389/fmicb.2017.02224](https://doi.org/10.3389/fmicb.2017.02224){target="_blank"}
  

    Quinn TP, Erb I, Richardson MF, Crowley TM. Understanding
    sequencing data as compositions: an outlook and review.
    *Bioinformatics* 2018; 34(16): 2870–2878.
    [doi:10.1093/bioinformatics/bty175](https://academic.oup.com/bioinformatics/article/34/16/2870/4956011){target="_blank"}
 

    ---

    **The microbiome case, most extensively studied**

    Weiss S et al. Normalization and microbial differential abundance
    strategies depend upon data characteristics.
    *Microbiome* 2017; 5: 27.
    [doi:10.1186/s40168-017-0237-y](https://doi.org/10.1186/s40168-017-0237-y){target="_blank"}
    
    ---

  ### Statistical models for omics count data

    Love MI, Huber W, Anders S. Moderated estimation of fold change
    and dispersion for RNA seq data with DESeq2. *Genome Biology*
    2014; 15: 550.
    [doi:10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8){target="_blank"}

    Robinson MD, McCarthy DJ, Smyth GK. edgeR: a Bioconductor package
    for differential expression analysis of digital gene expression data.
    *Bioinformatics* 2010; 26(1): 139–140.
    [doi:10.1093/bioinformatics/btp616](https://doi.org/10.1093/bioinformatics/btp616){target="_blank"}

    Ritchie ME, Phipson B, Wu D, Hu Y, Law CW, Shi W, Smyth GK.
    limma powers differential expression analyses for RNA sequencing
    and microarray studies. *Nucleic Acids Research* 2015; 43(7): e47.
    [doi:10.1093/nar/gkv007](https://doi.org/10.1093/nar/gkv007){target="_blank"}

    Schurch NJ et al. How many biological replicates are needed in an
    RNA seq experiment and which differential expression tool should
    you use? *RNA* 2016; 22(6): 839–851.
    [doi:10.1261/rna.053959.115](https://doi.org/10.1261/rna.053959.115){target="_blank"}

    Gierliński M et al. Statistical models for RNA-seq data derived
    from a two-condition 48-replicate experiment. *Bioinformatics*
    2015; 31(22): 3625–3630.
    [doi:10.1093/bioinformatics/btv425](https://doi.org/10.1093/bioinformatics/btv425){target="_blank"}

    Squair JW et al. Confronting false discoveries in single-cell
    differential expression. *Nature Communications* 2021; 12: 5692.
    [doi:10.1038/s41467-021-25960-2](https://doi.org/10.1038/s41467-021-25960-2){target="_blank"}
    ---
---
