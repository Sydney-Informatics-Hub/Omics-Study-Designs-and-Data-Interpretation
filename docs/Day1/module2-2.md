## Section 2: Sparsity and zero inflation — not all zeros mean the same thing

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  

    - Distinguish between a biological zero (a feature genuinely absent)
      and a technical zero (a feature below detection), and explain why
      treating both identically leads to incorrect biological conclusions.   
      


In Section 1, we saw that counts reflect a limited sampling process rather than absolute quantities. A direct consequence of that is something you’ll notice immediately in real datasets:

**most entries in an omics count matrix are zero.**

This often feels alarming at first, especially if you’re coming from bulk measurements. In reality, it’s expected. The challenge is not the presence of zeros — it’s understanding what they actually represent.

## Sparsity is normal

Omics datasets are sparse because you’re trying to measure a very large number of features with a finite budget. How sparse things get depends on the platform:

| Platform | Typical zero rate | Main reason |
|---|---|---|
| Bulk RNA-seq | 10–40% | Many genes genuinely not expressed |
| 10x scRNA-seq | >90% | Shallow depth per cell + capture inefficiency |
| SMART-seq2 | 60–80% | Better detection per cell, but still limited |
| 16S / metagenomics | 50–90% | True absence + undersampling of rare taxa |
| Proteomics (DDA) | 10–50% missing | Below detection limit |
| Metabolomics | 20–50% missing | Detection limits + ionisation variability |

If you’re working with single-cell data, the numbers can look extreme. Seeing >90% zeros is completely normal for droplet-based platforms like 10x. It’s not a quality issue. It’s how the technology works.

## Not all zeros mean the same thing

A zero in the matrix just means “nothing was detected.” It does **not** tell you why. In practice, there are three main reasons a zero can appear:

### 1. Biological zeros

These are the straightforward ones. The feature really is absent.

- A gene is not expressed in a given cell type  
- A microbe is not present in a sample  
- A protein is not produced under certain conditions  

These zeros carry biological meaning and should be preserved.


### 2. Technical zeros

Here, the molecule exists, but it never makes it into the data. 
- In single-cell RNA-seq, for example, only a fraction of transcripts are captured during library preparation. Capture efficiency can be as low as 10–15%, so most molecules are simply lost before sequencing.

The result: zeros that reflect **failure to capture**, not true absence.

### 3. Sampling zeros

These arise later in the process. A molecule may be present and even successfully amplified, but still not get sequenced because:

- it was rare to begin with  
- amplification didn’t favour it  
- sequencing depth was limited  

This is essentially bad luck in the sampling step.


![Sources of zeros in scRNAseq data: biological, technical, and sampling](module2Figs/01_zero_technical_Biological_v1.png){width=90%}

<small>Adapted from: [Jiang et al. *Genome Biology* 2022](https://link.springer.com/article/10.1186/s13059-022-02601-5){target="_blank"} (CC BY 4.0)</small>

## The tricky part: they look identical

In the count matrix, all three cases are just zeros.

There’s no flag that tells you whether a zero is biological, technical, or due to sampling. Interpreting them requires context:   
- how highly the feature is expressed elsewhere  
- the sequencing depth  
- the platform you’re using  
- what you expect biologically  

This is why zero handling isn’t something you can fully automate.

## A simple example

Consider a gene measured across four single cells:

| Cell 1 | Cell 2 | Cell 3 | Cell 4 |
|---|---|---|---|
| 0 | 0 | 3 | 0 |

It’s tempting to say the gene is “off” in most cells.

But with typical single-cell capture rates, it’s just as plausible that the gene is expressed at low levels in all four cells, and only one of them happened to register counts.

You can’t resolve that ambiguity from this table alone.

## Same zero, different meaning

Context changes everything.

- If a gene known to be T-cell specific is zero across B cells, that’s almost certainly a biological zero.  
- If the same gene shows patchy detection across T cells, that pattern is more consistent with sampling or technical zeros.  

Treating both situations the same leads to incorrect conclusions.

## Platform matters

What a zero *likely* means depends heavily on the technology.

- **Bulk RNA-seq:** most zeros are biological, since expression is averaged across many cells.  
- **Droplet-based scRNA-seq (e.g. 10x):** many zeros come from limited capture and shallow depth.  
- **SMART-seq2:** higher sensitivity per cell, but amplification noise plays a larger role.  
- **Microbiome data:** zeros can reflect both true absence and undersampling of rare taxa.  
- **Proteomics/metabolomics:** missing values often mean “below detection limit,” not absence.  

The same number (0) carries different implications depending on where it came from.

## What goes wrong if you ignore this

Treating all zeros as the same causes problems downstream.

- **Differential expression:** differences in detection rates can look like biological changes  
- **Correlation analysis:** shared zeros can create artificial relationships between features  
- **Imputation:** filling in values can introduce signals that were never actually there  

These issues don’t show up immediately, but they can distort results in subtle ways.

## What to take forward

The key point is simple:

> **A zero is not a single thing. It’s an observation with multiple possible explanations.**

Before deciding how to handle zeros, you need to think about:  
- the platform  
- the depth  
- the biology you expect  

Zeros aren’t just missing data to “fix.” They’re part of the measurement process, and interpreting them correctly is essential for everything that follows.


