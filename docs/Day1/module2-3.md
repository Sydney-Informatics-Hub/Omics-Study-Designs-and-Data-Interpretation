## Section 3: Compositionality — you are always looking at a pie chart

!!! info "Learning objectives" 

    By the end of this module, participants will be able to:  
    
    - Explain compositionality and relative abundance in intuitive terms
      and describe why naive fold change and correlation analyses can be
      misleading in compositional data.  


In Section 1, we established that counts depend on sequencing depth. In Section 2, we saw that many entries are zero, and that those zeros are not all the same.

There’s a third property that follows directly from how the data is generated, but it’s easy to overlook:  **counts are compositional.**

## The fixed total problem

When you sequence a sample, you generate a fixed number of reads. Every read assigned to one feature is a read that cannot go to another.

So the counts are not independent. They are all competing for the same total.

In practical terms, this means that if one gene takes up a larger share of the reads, the relative share of other genes must decrease, even if their actual expression hasn’t changed.

A useful way to think about it:

> You are always looking at a pie chart, not a bar chart.

A bar chart shows absolute quantities. A pie chart shows proportions. Sequencing data gives you proportions.

## A simple example

Imagine a sample with three genes:

| Gene | Sample 1 | Sample 2 |
|---|---|---|
| A | 100 | 200 |
| B | 100 | 100 |
| C | 100 | 100 |
| **Total reads** | 300 | 400 |

Gene A doubled in absolute counts. Genes B and C stayed the same.

Now look at proportions:

| Gene | Sample 1 | Sample 2 |
|---|---|---|
| A | 33% | 50% |
| B | 33% | 25% |
| C | 33% | 25% |

Genes B and C appear to decrease, even though nothing about them actually changed.

This isn’t a measurement error. It’s just arithmetic.

## Why this matters in practice

Once you start looking at proportions, it becomes easy to misinterpret what’s changing.

### Apparent increases may not be real

A gene can appear to increase simply because other genes decreased.

You’ll see this often in microbiome data. If most species drop after a treatment, the remaining ones automatically take up a larger fraction of the total, even if their absolute abundance stayed the same.


### Apparent decreases may not be real

The reverse also happens.

A gene can genuinely increase in absolute terms, but still look flat or even decreased if other features increased more strongly. This can make real biological signals harder to detect.

## Correlation becomes tricky

Compositional data also affects how features relate to each other.

Because everything shares the same total, features are constrained. If one goes up, others must go down in relative terms.

This creates artificial negative correlations.

Two genes with no biological relationship can appear negatively correlated simply because they are competing for the same pool of reads. If you build networks directly from these correlations, you can end up with edges that reflect this constraint rather than real biology.

## Normalisation doesn’t remove this

It’s important to be clear about what normalisation does and does not do.

Normalisation methods (CPM, TPM, size factors, etc.) adjust for differences in total library size between samples. They make samples comparable. But after normalisation, the data is still compositional. You still have proportions of a total, and the same constraints apply.

## Where this shows up most strongly

Compositional effects are most obvious in:

- **Microbiome data (16S, metagenomics):** proportions are often the primary output  
- **Low biomass samples:** where a few features dominate the signal  
- **Single-cell data:** where shallow depth exaggerates competition between features  

But the same principle applies to bulk RNA-seq and other sequencing-based assays as well. It’s just sometimes less visible.

## What to take forward

The key point here is subtle but important:

> **A change in proportion is not the same as a change in absolute abundance.**

When working with count data, you are always dealing with relative measurements. That shapes how differences and relationships should be interpreted.

If this isn’t taken into account, it’s easy to:
- overstate increases  
- misinterpret decreases  
- infer relationships that aren’t actually there  


> **You are always looking at a pie chart, not a bar chart.**
> A bar chart shows you absolute quantities. A pie chart shows you
> proportions. Sequencing gives you a pie chart, and a larger slice
> for one gene automatically means smaller slices for all the others,
> regardless of what the biology actually did.

### A worked example: when proportions mislead

??? example "Case study: The antibiotic experiment that wasn't what it looked like"

    A researcher is studying the gut microbiome of mice before and after
    a heavy dose of antibiotics. They sequence stool samples from both
    time points.

    ![ anitbiotic_example](module2Figs/02_compositionality_v01.jpg){width=98%}
    ## Species Composition Summary

    | Species    | Before | After  | Reality                                                   |
    |------------|--------|--------|------------------------------------------------------------|
    | Species A  | 20%    | 80% ↑  | Unchanged, same absolute numbers                          |
    | Species B  | 30%    | 0%     | Below detection, not necessarily absent                   |
    | Species C  | 50%    | 20% ↓  | Reduced, but proportions distorted by biomass loss         |

    The researcher runs a standard statistical test on these percentages.
    Species A shows a dramatic and highly significant increase.

    **The published conclusion:** *"Antibiotic X acts as a growth booster
    for Species A."*

    ---

    **What actually happened:**

    The antibiotics killed 99% of all bacteria in the gut. Species A did
    not grow, its absolute numbers stayed the same. But because everything
    else was wiped out, Species A now represents 80% of what remains. The
    pie shrank dramatically; Species A's slice simply got bigger by
    default.

## Looking ahead

So far, we’ve seen three structural properties of omics data:

- counts depend on sequencing depth  
- zeros have multiple causes  
- features are compositionally constrained  

The next step is to bring these together and ask a practical question:

**what does this mean for statistical testing?**

That’s where standard approaches start to break down, and where specialised methods come in.

