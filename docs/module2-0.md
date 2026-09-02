# Module 2: Designing Robust Omics Studies

!!! info "Learning objectives"
    - Select an appropriate platform to capture the biological signal of interest and describe the type of data it produces.
    - Evaluate a study design in terms of accuracy and interpretability, power and cost, and generalisability.


Module 1 ended by grouping study the pitfalls of study design into three buckets: recoverable,
limitable, and fatal. The fatal problems were:

- choosing the wrong omics platform
- fully confounding batch with biological groups
- missing or unrecorded metadata
- pooling samples when individual level inference was required

These problems cannot be fixed during analysis because they arise during study design or sample collection.  

Module 1 focused on what can go wrong; Module 2 focuses on what to decide before data collection begins.

Throughout this module, we will consider three aspects of study design:

- **Accuracy and interpretability**: Will the measurements accurately represent the biological feature of interest, and can the results be interpreted with confidence?
- **Power and cost**: Can the study detect the biological effect of interest within the available budget?
- **Generalisability**: Are the findings likely to apply beyond the study cohort?

These considerations are often connected and can involve trade-offs. A design choice that improves one aspect of a study may affect another, particularly when resources, sample availability, or experimental constraints are limited. The sections that follow examine these trade-offs through specific study-design decisions.

### How this module is organised

The module follows these three questions in sequence. 

- First, we consider what to measure and whether the study can produce interpretable results (Sections
2.1–2.3). 
- We then consider how much data are needed and how to allocate
resources (Sections 2.4–2.5). 
- Finally, we consider how broadly the findings
apply (Section 2.6). 
- Section 2.7 brings the three questions together in a
worked study design.

In practice, some decisions discussed later, such as who to recruit, are made before data collection
begins. They appear later here because they answer a different question.

The four fatal problems from Module 1 are revisited throughout the module: platform choice in 2.1, batch structure in 2.2, metadata in 2.3, and the unit of replication in 2.4.

!!! note "Design decisions often affect more than one question"

    Each section is labelled with the question it mainly addresses, but many
    decisions affect more than one. e.g. balanced batch allocation is covered under
    interpretability, but it also improves power; sample size affects both
    power and how far the findings extend. Each section flags these connections
    where they matter.