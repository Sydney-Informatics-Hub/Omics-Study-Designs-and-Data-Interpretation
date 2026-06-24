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

In standard bulk RNA-seq, longer transcripts generate more reads 
because sequencing fragments are sampled across the transcript body, 
read count is approximately proportional to both transcript abundance 
and transcript length. A 10kb gene and a 1kb gene expressed at 
identical levels will produce roughly 10× more reads for the longer 
gene under uniform coverage. This makes raw counts and CPM values 
unsuitable for comparing expression levels between different genes 
within the same sample.

This bias applies to assays/platform where reads are distributed across 
transcript length. It does not apply to proteomics, metabolomics, 
or microbiome data.

For scRNA-seq, the picture depends on the protocol:

- **Full-length protocols** (e.g. Smart-seq2) exhibit gene length 
  bias similar to bulk RNA-seq, length correction is appropriate.
- **UMI-based 3′/5′ capture protocols** (e.g. 10x Chromium, 
  Drop-seq) show substantially reduced length bias because 
  sequencing is concentrated near transcript ends rather than 
  distributed across the full transcript. Length correction is 
  generally not recommended for standard gene level analyses 
  with these protocols, though some residual bias can still exist.

### Normalisation, transformation, and scaling : what each one does

### Three terms, three different jobs

These terms appear throughout omics methods sections and are frequently
used interchangeably. They should not be, each addresses a different
problem.

**Normalisation** makes samples technically comparable by correcting
for the depth, compositional, and platform-specific differences
described above. It operates between samples.

**Transformation: is the data the right shape?**

This was introduced in Section 1 but worth stating precisely here
in relation to scaling. Raw count data is heavily skewed: a handful
of highly expressed genes have counts in the tens of thousands, while
most genes sit near zero. This extreme range causes problems for
statistical models and visualisation, the few dominant genes
overwhelm everything else.

Log2 transformation compresses this range. A gene with 50,000 counts
becomes ~15.6; a gene with 50 counts becomes ~5.6. The 1000 fold
difference in raw counts becomes a 3 unit difference on the log2
scale. The distribution becomes more symmetric, and both genes are
now visible in the same plot.

Log2 transformation partially reduces the dominance of highly
expressed genes, but it does not eliminate it. After log2, a highly
variable gene still has higher variance than a stable one. That is
where scaling comes in.

**Scaling: does every feature get a fair hearing in PCA?**

PCA finds the directions of greatest variation in the data and uses
them as axes. This means it is driven by whichever features vary the
most, not necessarily the most biologically important ones.

In metabolomics, glucose measured in **micromolar** concentrations will
have much larger absolute variance than leucine measured in **nanomolar**
concentrations; not because glucose is more biologically interesting,
but simply because its values are larger. Without scaling, glucose
dominates every PCA axis while leucine barely contributes, regardless
of what the biology is actually doing.

**Pareto scaling** divides each feature by the square root of its standard
deviation. **Auto-scaling** divides by the full standard deviation. Both
reduce the dominance of high-abundance genes/proteins, so that PCA is less
driven by absolute measurement scale.

| Step | Fixes | Does not fix |
|---|---|---|
| **Normalise** | Between sample depth and technical differences | Distribution shape; unequal feature variance  |
| **Transform** | Skewed distribution; compresses extreme values | Between sample technical differences; unequal feature variance |
| **Scale** | Unequal feature variance for multivariate analysis | Between sample technical differences; distribution shape |

In many exploratory omics workflows this sequence follows from the
logic of each step. Some tools collapse steps, DESeq2 normalises
internally on raw counts, rlog and VST combine normalisation and
transformation, CLR in microbiome data integrates compositional
correction into the transformation itself. Always check what the
tool expects before processing.

!!! warning "Order matters, and not every workflow needs all three steps"
    Scaling before normalising does not remove depth differences, it
    standardises them, locking in the technical variation that
    normalisation was meant to remove.

    RNA-seq differential expression tools (DESeq2, edgeR) normalise
    internally, providing pre-normalised values will invalidate the
    model assumptions and produce unreliable results. Feature level
    scaling is generally not applied in RNA-seq because the statistical
    models account for the mean-variance relationship directly, and
    rlog/VST already stabilise variance across the expression range
    for visualisation.

    In metabolomics, features are chemically heterogeneous molecules
    measured across vastly different concentration ranges, scaling is
    often needed so that PCA is less dominated by variables with the
    largest absolute variance or measurement scale. Always check what
    the tool expects as input.

!!! info "The word 'scaling' means different things depending on the platform"
    In metabolomics, scaling means adjusting each feature by its
    variability (Pareto or auto-scaling) before PCA, to stop
    high-variance metabolites dominating the analysis.

    In scRNA-seq, scaling usually means z-scoring each gene across
    cells, centering and standardising gene expression so that all
    genes contribute equally to clustering, regardless of their
    expression level.

    Same word, different operation, different purpose. When reading
    a methods section, always check what is actually being divided
    by what.
---

