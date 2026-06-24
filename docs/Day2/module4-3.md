### Choosing a normalisation approach

There is no universal normalisation method. The correct choice depends
on the platform, the experimental design, and the downstream analysis.
Applying the wrong method introduces new artefacts rather than simply
failing to correct existing ones.

---

#### Bulk RNA-seqa.      

Bulk RNA-seq has the most mature normalisation landscape and the most
common misunderstandings. The key distinction is between metrics
appropriate for visualisation and those appropriate for differential
expression testing.


| Method | Corrects for | Use | Not appropriate for |
|---|---|---|---|
| **CPM** (Counts Per Million) | Sequencing depth | Comparing same gene between replicates | Within-sample gene comparisons; DE testing |
| **TPM** (Transcripts Per Million) | Depth + gene length | Within-sample gene comparisons; same gene across samples | DE testing |
| **RPKM / FPKM** (Reads or Fragments Per Kilobase per Million) | Depth + gene length | Legacy reporting only | Between-sample comparisons; DE testing |
| **TMM** (Trimmed Mean of M-values) edgeR | Depth + composition | DE analysis | Within-sample comparisons |
| **DESeq2 size factors** | Depth + composition | DE analysis | Within-sample comparisons |

<small>Ref: [Dillies et.al. *Briefings in bioinformatics (2013)* ](https://academic.oup.com/bib/article/14/6/671/189645?login=false){target="_blank"}</small>
<small>Ref: [Lingen et.al.*Biochimica et Biophysica Acta (BBA)-Gene Regulatory Mechanisms (2024)*]( https://www.sciencedirect.com/science/article/pii/S1874939924000543){target="_blank"}</small>


**CPM** and **TPM** are widely used for reporting and visualisation but
neither corrects for composition effects. If a small set of highly
expressed genes dominates one sample's library, CPM will suppress the
apparent expression of everything else in that sample. CPM and TPM
should not be used as input to differential expression testing.

The distinction between CPM and TPM follows directly from gene length 
bias: CPM corrects for depth only, making it valid for comparing the 
same gene across samples (where length is constant and cancels out); 
TPM additionally divides by gene length, making it valid for comparing 
different genes within the same sample.

**RPKM/FPKM** are not recommended for new analyses. Unlike TPM, RPKM
totals differ between samples, making direct between-sample comparisons
unreliable. TPM is the preferred alternative when length correction is
needed.

**TMM (Trimmed Mean of M-values)** is the normalisation method
built into edgeR, which correct for both depth
and composition. In edgeR workflows, normalisation is applied by
calling `calcNormFactors()` before differential expression (DE) testing,
a single function that calculates and stores the TMM scaling
factors for use in all downstream steps.

**DESeq2 size factors** achieve the same correction fully
internally, DESeq2 calculates them automatically as part of the
analysis pipeline, with no separate normalisation function to call.
The only practical requirement is that you provide **raw counts**
as input. Providing CPM, TPM, or any pre-normalised values will
cause DESeq2 to normalise already normalised data, invalidating
the model assumptions and producing unreliable results.  

**For visualisation**, after depth and composition normalisation,
count data still exhibit strong mean–variance dependence (which is not appropreiate input for PCA, as discussed in section 1). Apply a
variance-stabilising transformation before PCA or heatmaps: rlog
or VST for DESeq2 workflows, log-CPM for edgeR. 


!!! info "TMM vs DESeq2 size factors"
    Both correct for depth and composition and perform similarly in
    practice. The choice is usually determined by which DE tool you
    are using: TMM with edgeR, size factors with DESeq2. Applying
    TMM factors before running DESeq2 is double normalising and
    should not be used.

??? abstract "How DESeq2 and edgeR handle composition bias: conceptual summary"
    
    Both methods solve the same problem from different angles: when a
    small number of genes dominate a library, simple per million scaling
    makes everything else appear artificially lower. The question is how
    to identify the stable genes and use them as the anchor for
    normalisation.

    ---

    **DESeq2: median of ratios**

    For each gene, DESeq2 calculates its geometric mean across all
    samples, this becomes the reference value for that gene. For each
    sample, every gene's count is divided by that gene's geometric
    mean, producing one ratio per gene. 

    For a dataset with 20,000 genes, each sample therefore has up to
    20,000 gene-wise ratios. The **median of those ratios** is the size
    factor for that sample, one number, derived from the middle of the
    gene-wise ratio distribution for that sample, and repeated
    independently for every sample in the dataset.

    The median is robust to a small number of extreme ratios. A handful
    of massively upregulated genes will produce very large ratios, but
    their influence on the size factor is minimised rather than
    explicitly removed, the size factor remains anchored by the stably
    expressed genes that form the bulk of the distribution.

    Counts are normalised by dividing each sample's raw counts by its
    size factor. The adjustment reduces the artificial compression of
    other genes caused by composition bias, making normalised counts
    across samples more directly comparable.

    ---

    **edgeR: TMM (Trimmed Mean of M-values)**

    TMM starts by selecting one reference sample. By default, edgeR
    selects as reference the sample whose upper-quartile expression is
    closest to the mean upper quartile across samples. This makes it
    the most neutral, representative sample available. The reference
    sample gets a scaling factor of 1 by definition; it is the anchor,
    not the thing being corrected.

    Every other sample is then compared to this reference
    independently, one at a time. For each pairwise comparison,
    TMM calculates:

    - the M value (log2 fold change) for each gene between the
      test sample and the reference; how much that gene appears
      to have changed
    - the A value (average log CPM across the two samples being
      compared); how abundantly the gene is expressed

    It then trims by default:

    - the top and bottom 30% of genes by M value: genes with
      extreme fold-changes that are unlikely to represent the
      stable majority needed for normalisation
    - the top and bottom 5% by A value: genes with extremely
      high or extremely low expression

    Of the remaining genes, a weighted average of their M values
    becomes the scaling factor for that test sample. Each gene is
    weighted approximately by the **inverse variance of its
    log fold-change estimate**, which depends on its count in both
    the test and reference samples. Genes with higher counts have
    lower variance and therefore receive higher weight, contributing
    more to the average. Genes with low counts have high variance
    and contribute less. This prevents noisy low-count genes from
    pulling the scaling factor away from a robust scaling estimate.

    This process repeats independently for every non-reference
    sample. Each gets its own scaling factor derived from its own
    comparison to the same reference. The scaling factor is then
    applied as an effective library size correction, adjusting the
    denominator used for normalisation rather than the raw counts
    themselves.

    ---

    **The shared logic and its limit**

    Both methods rest on the same biological assumption: the majority
    of genes are not differentially expressed between conditions. Under
    that assumption, the median ratio (DESeq2) and the trimmed mean
    fold-change (edgeR) **produce similar results in practice**, the
    stable genes dominate the calculation while extreme genes
    contribute little to the final scaling estimate.

    Neither method changes the raw counts, the composition 
    imbalance remains in the data. What changes is the scaling 
    factor used for comparison, **which accounts for the bias so 
    that it no longer substantially distorts relative abundance 
    estimates**:- provided that the majority of genes are not 
    truly differentially expressed between conditions.

    <small>
    Robinson MD, Oshlack A. *Genome Biology* 2010.
    [doi:10.1186/gb-2010-11-3-r25](https://link.springer.com/article/10.1186/gb-2010-11-3-r25){target="_blank"}
    *(TMM — original paper)*

    Love MI, Huber W, Anders S. *Genome Biology* 2014.
    [doi:10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8){target="_blank"}
    *(DESeq2 — original paper)*
    </small>
---

!!! warning "When default normalisation breaks down"
    DESeq2 and edgeR both assume that the majority of genes are 
    not differentially expressed between conditions. This assumption 
    breaks down in some situations:

    **Global perturbations**, experiments where a treatment causes 
    widespread transcriptional activation or shutdown across the 
    genome. The stable gene anchor no longer exists, and the scaling 
    factor reflects biology rather than technical bias.

    **Targeted gene panels**, such as NanoString nCounter or custom 
    amplicon approaches, where genes are deliberately selected because 
    they are expected to change. Most genes on the panel may genuinely 
    be differentially expressed by design.

    In both cases, use **spike-in** normalisation, adding known quantities 
    of external RNA to each sample before sequencing, or housekeeping 
    genes as the normalisation reference instead of relying on the 
    default method.