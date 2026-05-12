## Section 2 : Normalisation and Scaling

!!! info "Learning objectives"
    By the end of this section, participants will be able to:

    - Explain why raw counts cannot be compared across samples and
      identify the three sources of technical variation that
      normalisation addresses.
    - Distinguish normalisation from scaling, explain their different
      purposes, and describe the consequences of applying them in the
      wrong order.
    - Select an appropriate normalisation method for bulk RNA-seq,
      scRNA-seq, proteomics, metabolomics, and microbiome data and
      justify that choice.

---

### Why normalisation is required

Section 1 established that transformation makes data behave well enough
for visualisation. Normalisation is a different step with a different
purpose: it corrects for systematic technical differences *between*
samples so that values are directly comparable across the dataset.

Three distinct sources of technical variation require correction,
each operating differently across platforms.

**Library size variation**

In **sequencing based platforms**, samples routinely vary in total read
count by 2 fold or more within the same experiment, even with identical
input material and careful handling. A gene with 200 counts in a sample
sequenced to 40 million reads is not more expressed than the same gene
with 100 counts in a sample sequenced to 20 million reads; both
represent the same 0.0005% of their respective libraries. Without
normalisation, this depth difference appears as differential expression.

**Composition effects**

Library size correction alone is not sufficient. If a small number of
genes/proteins are extremely highly expressed, dominating the sequencing
budget, every other feature in that sample appears artificially lower
in relative terms, even if its true abundance has not changed. This is
the compositionality problem introduced in Module 2. A naive
per million scaling that treats total library size as comparable across
samples will be misled when the composition of that library differs.

![various Bias normalization](figures/04_Bias_normalization_v01.jpg){width=90%}

**Platform specific technical artefacts**

In **mass spectrometry based platforms**, the equivalent of library size
variation is run to run variability in total ion signal. Differences in
sample concentration, injection volume, and ionisation efficiency
introduce systematic shifts in measured abundance across runs. The
problem is **structurally identical to sequencing depth variation**; the
methods used to correct it differ because the data structure differs.

**Gene length bias (sequencing platforms)**

In RNA-seq, longer genes accumulate more reads simply because they 
offer more base pairs for sequencing fragments to map to, not because 
they are more highly expressed. A 10kb gene and a 1kb gene expressed 
at identical levels will produce roughly 10× more reads for the longer 
gene. This makes raw counts and count per million (CPM) values unsuitable for comparing 
expression levels between different genes within the same sample.

This bias is specific to sequencing platforms where reads distribute 
along the full transcript length. It does not apply to proteomics, 
metabolomics, or microbiome data. It also does not apply to most 
scRNA-seq protocols, 3' end capture methods (10x Chromium, Drop-seq) 
sequence only the end of transcripts, so reads do not accumulate 
proportionally with gene length. Applying length correction to 
3' scRNA-seq data is incorrect.

