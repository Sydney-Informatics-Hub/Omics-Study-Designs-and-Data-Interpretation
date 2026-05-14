 ### Choosing a normalisation approach

There is no universal normalisation method. The correct choice depends
on the platform, the experimental design, and the downstream analysis.
Applying the wrong method introduces new artefacts rather than simply
failing to correct existing ones.

---

#### Bulk RNA-seq

Bulk RNA-seq has the most mature normalisation landscape and the most
common misunderstandings. The key distinction is between metrics
appropriate for visualisation and those appropriate for differential
expression testing.


| Method | Corrects for | Use | Not appropriate for |
|---|---|---|---|
| **CPM** (Counts Per Million) | Sequencing depth | Comparing same gene between replicates | Within-sample gene comparisons; DE testing |
| **TPM** (Transcripts Per Million) | Depth + gene length | Within-sample gene comparisons; same gene across samples | DE testing |
| **RPKM / FPKM** (Reads or Fragments Per Kilobase per Million) | Depth + gene length | Legacy reporting only | Between-sample comparisons; DE testing |
| **TMM** (Trimmed Mean of M-values) — edgeR | Depth + composition | DE analysis | Within-sample comparisons |
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

**TMM (Trimmed Mean of M-values)** calculates a scaling factor for
each sample by trimming the most extreme log-fold changes and computing
a weighted mean of the remainder, removing the genes most likely to be
compositionally dominant. TMM is the normalisation method built into
edgeR.

**DESeq2 size factors** achieve similar correction through a different
route: for each gene, the ratio of its count to the geometric mean
across all samples is calculated, and the median of those ratios becomes
the size factor for that sample. The median is robust to differentially
expressed genes. DESeq2 applies this normalisation internally — raw
counts are the correct input; providing CPM or TPM values to DESeq2
means normalising already-normalised data.