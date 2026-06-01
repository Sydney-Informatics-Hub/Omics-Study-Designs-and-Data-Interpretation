# Module 2.3: Sparsity and zero inflation

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  

    - Distinguish between biological zeroes, technical zeroes, and sampling zeroes, and explain the mechanism behind each
    - Identify which type of zero or missing value is most likely given a platform, depth, and biological context 
    - Describe specific forms of zeros and missing values in different scenarios 
    - Explain what goes wrong analytically when zeros are misclassified 

## Sparsity is normal but not all sparsity is the same

The first thing most people notice when they take a look at their omics datasets is how many zero values it contains. In bulk RNA-seq 10-40% of gene-sample entries are zeros, in single-cell RNA-seq that number can exceed 90%, and in microbiome data it can exceed 95%. 

This often feels alarming at first but it is not necessarily a sign something is wrong. It is a direct consequence of trying to measure hundreds to millions of features simultaneously with a finite technical budget. Most features are not detectable in most samples under most conditions. The challenge we face in data analysis is not the presence of zeros, it’s understanding what they actually represent.

TODO add references to support these numbers and causes. 

| Platform | Missing rate | Primary cause |
|---|---|---|
| Bulk RNA-seq | 10–40% | Many genes genuinely not expressed |
| 10x scRNA-seq | >90% | Shallow depth per cell + capture inefficiency |
| SMART-seq2 | 60–80% | Better detection per cell, but still limited |
| 16S / metagenomics | 50–90% | True absence + undersampling of rare taxa |
| Proteomics (DDA) | 10–50% missing | Below detection limit |
| Metabolomics | 20–50% missing | Detection limits + ionisation variability |

## Not all zeros mean the same thing

A zero in any matrix arises from one of three causes. It means the feature was not detected but it does **not** tell you why.

TODO: diagram summarising these concepts

### 1. Biological zeros

These are the straightforward ones. The feature really is absent. 

- A gene is not expressed in a given cell type  
- A microbe is not present in a sample  
- A protein is not produced under certain conditions  

These zeros carry biological meaning and should be preserved as they are. Imputing values here (replacing a zero with an estimate) would be inventing biology that does not exist.  

### 2. Technical zeros

Here, the molecule exists, but it was lost before it could be detected. In single-cell RNA-seq, for example, only a fraction of transcripts are captured during library preparation. Capture efficiency can be as low as 10–15%, so most molecules are simply lost before sequencing.

Technical zeroes reflect a failure of the measurement process,n ot an absence of biology. They cannot be resolved by deeper sequencing, the molecule was lost before the detection process took place. 

### 3. Sampling zeros

These arise at the sequencing stage. By this point, the molecule has already been successfully extracted, converted, and amplified. It is in the library but the sequencer only reads a finite number of fragments. In complex samples containing tens of thousands to millions of sequences, low abundance molecules are less likely to be sampled by chance. 

!!! tip "Like eating jellybeans from a jar" 
    If you only pick out 20 jellybeans from a jar containing 10,000, you might miss any flavour thats only represented by less than 10 jellybeans. Not because the flavours don't exist, but because your sample size was too small to encounter them reliably. 

    Sequencing works in the same way. A gene expressed at low levels contributes only a tiny fraction of the fragments in the library. At 20 million reads, there may simply not be enough handfuls to guarantee a gene gets counted. Sequence the same library to 100 million reads and the same gene will appear more frequently.  

TODO make a diagram like this of our own 
![Sources of zeros in scRNAseq data: biological, technical, and sampling](module2Figs/01_zero_technical_Biological_v1.png){width=90%}

<small>Adapted from: [Jiang et al. *Genome Biology* 2022](https://link.springer.com/article/10.1186/s13059-022-02601-5){target="_blank"} (CC BY 4.0)</small>

### 4. Analytical zeros 

The three scenarios above arise from the measurement process itself, from biology, from capture failure, or sequencing budget. Analytical zeros are different, they are created by decisions made after the data is generated. 

Before data can be analysed, it undergoes pre-processing to convert raw sequence to a format that can be analysed. Preprocessing pipelines may apply filters and features that fall outside the permitted range are removed from the dataset. In some outputs, they are indistinguishable from features that were never detected at all. 

Common examples include: 

- **Variant calling**: a variant detected at 8x coverage is removed by a minimum depth filter of 10x. The site does not appear in the VCF
- **Bulk RNA-seq**: a gene with counts in two out of six samples is removed by a minimum prevalence filter before differential expression testing 
- **Single-cell RNA-seq**: a small quiecent cell type falls below the minimum UMI threshold and is removed during QC filtering 
- **Proteomics**: a low abundance protein detected in 40% of samples is excluded by a minimum 70% observation threshold. It is absent from the results 

!!! warning "Filters are directional and may leave no trace"
    Analytical filters are not neutral. They systematically remove low-signal features like rare variants, lowly expressed genes, small cell populations, low-abundance proteins, or rare taxa. These are often exactly the features a study is designed to find.

!!! tip "What this means in practice"
    Filters are often necessary. They reduce noise, improve statistical power, and make analyses more computationally tractable. The problem is not filtering itself but treating filtered output as though it represents the complete dataset.

    Two habits protect against this:

    - **Always report filter parameters alongside results**: how many features were removed, by which threshold, and in which direction
    - **Check what you lost**: before finalising a filter, examine what was removed and whether it clusters non-randomly by condition, sample quality, or biological group

## When data looks the same but means something different

In every omics platform, the same raw data value can arise from completely different causes. The correct interpretation and analytical response depends on which cause applies. This is a structural property of high-throughput measurements: when you are trying to detect thousands of features simultaneously, the boundary between not there and not detected is often blurred. What changes between platforms is where that boundary sits, what causes things to fall below it, and what you can reasonably infer when they do.

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

- If a gene known to be T-cell specific is zero across B cells, that’s almost certainly a biological zero
- If the same gene shows patchy detection across T cells, that pattern is more consistent with sampling or technical zeros  

Treating both situations the same leads to incorrect conclusions.

## Platform matters

What a zero *likely* means depends heavily on the technology.

- **Bulk RNA-seq:** most zeros are biological, since expression is averaged across many cells.  
- **Droplet-based scRNA-seq (e.g. 10x):** many zeros come from limited capture and shallow depth.  
- **SMART-seq2:** higher sensitivity per cell, but amplification noise plays a larger role.  
- **Microbiome data:** zeros can reflect both true absence and undersampling of rare taxa.  
- **Proteomics/metabolomics:** missing values often mean “below detection limit,” not absence.  

The same number (0) carries different implications depending on where it came from.

## What goes wrong when zeros are misclassified 

Treating all zeros as the same causes problems downstream.

TODO provide clear examples to explain this. Below I've added some extra information but its very janky. 

### **Differential expression** 

If one condition has systematically lower sequencing depth, sampling zeros will cluster in that condition. Genes will appear downregulated not because they are biologically downregulated but because they were not sampled. 

### **Correlation analysis**  

In matrices, multiple genes with low expression will all show zeros across most samples. This may look like correlated expression. In reality, it may reflect shared dropout probability.  

### **Imputation** 

If missing values in a dataset are imputed using random or mean-based methods, features that are systematically below detection in one condition will be assigned imputed values that are statistically indistinguishable from measured value. Downstream abdunance or expression analyses will compare real measurements in one group against imputed estimates in another without flagging that the comparison is not equivalent. 

### **False variant calls** 

In variant calling, a no-call silently converted to a reference genotype inflates apparent concordance with the reference genome. In clinical genomics, this means a pathogenic variant in a poorly converted region may not be reported, not because it was considered and excluded, but because the tools didn't see sufficient evidence to call it. 

## Questions to answer before handling zeros

Across all data modalities, the same reasoning process applies before any analytical decision about zeros or missing values:

### 1. What platform generated the data? 

Expected zero rates and likely causes differ substantially by technology. 

TODO find some comparison examples that connect with expected zero rates described above? 

### 2. What is the most likely cause of zeros in this dataset? 

Biological absence, capture failure, sampling change, detection threshold, or compositional compression? The sequencing depth, platform, and biology all inform this. 

### 3. Is the missingness random or structured?

If zeros cluster by samples, conditions, feature types, they are carrying information about the measurement process. Structured missingness is a signal, usually a technical one, not just noise to be removed. 

### 4. What do the applied analytical methods assume about zeros?

Different algorithms make different assumptions about where the zeros are coming from. Using a method with assumptions that do not match your data type will propagate the misclassification into your results. 

## What to take forward

**A zero is not a single thing. It’s an observation with multiple possible explanations.**

Before deciding how to handle zeros, you need to think about:  
- the platform  
- the depth  
- the biology you expect  

Zeros aren’t just missing data to “fix.” They’re part of the measurement process, and interpreting them correctly is essential for everything that follows.


