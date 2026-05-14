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

    For a dataset with 20,000 genes, each sample therefore has 20,000
    gene-wise ratios. The **median of those 20,000 ratios** is the size
    factor for that sample, one number, derived from the middle of the
    gene-wise ratio distribution for that sample, and repeated
    independently for every sample in the dataset.

    The median is the key step. A handful of massively upregulated genes
    will produce very large ratios, outliers that the median ignores by
    definition. The size factor is anchored by the stably expressed genes
    that form the bulk of the distribution. The dominant genes are
    effectively excluded from the calculation without being explicitly
    identified.

    The size factor is then used to calculate an effective library size:

    `effective library size = actual library size × size factor`

    Normalised counts are computed by dividing raw counts by this
    effective library size, not the actual one. The adjustment
    compensates for the reads consumed by dominant genes, and the
    apparent downregulation of everything else disappears.

    ---

   
---