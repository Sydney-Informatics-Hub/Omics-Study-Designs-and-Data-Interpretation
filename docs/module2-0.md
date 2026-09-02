# Module 2: Designing Robust Omics Studies

!!! info "Learning objectives"
    - Select an appropriate platform to capture the biological signal of interest and describe the type of data it produces.
    - Evaluate a study design in terms of accuracy and interpretability, power and cost, and generalisability.

In module 1, we were introduced to the five molecular layers of omics datasets and the important design decisions made at each step of the experimental workflow. In module 2, we will explore these considerations more deeply. To evaluate these systematically, we have organised them around three questions that run through each section of this module:

| Aspect | Design question | What it means in practice |
|---|---|---|
| **Accuracy and interpretability** | Will the measurements accurately represent the biological feature of interest, and can the results be interpreted with confidence? | Selecting a platform that captures the right molecule and biological layer, and structuring the study so that observed differences can be attributed to biology rather than technical artefacts or unmeasured variables. |
| **Power and cost** | Can the study detect the biological effect of interest within the available budget? | Power is shaped by the size of the effect you expect, the number of independent samples you collect, and the technical variability of your measurements. An underpowered study may miss real effects entirely, or produce unstable estimates that do not replicate. |
| **Generalisability** | Are the findings likely to apply beyond the study cohort or experimental system? | A result that is accurate within one population or condition may not hold in another. Decisions about who or what is included — and what is controlled or excluded — all shape how broadly conclusions can be drawn. |

These considerations are often connected and can involve trade-offs. A design choice that improves one aspect of a study may affect another, particularly when resources, sample availability, or experimental constraints are limited. The sections that follow examine these trade-offs through specific study-design decisions.

!!! tip "Design decisions often affect more than one question"

    Each section is labelled with the question it mainly addresses, but many decisions affect more than one. For example, balanced batch allocation is covered under interpretability, but it also
    improves power; sample size affects both power and how broadly the findings apply. Each section
    flags these connections where they matter.