# Module 2: Designing Robust Omics Studies

!!! info "Learning objectives"
    By the end of this module, participants will be able to:  
    - Select an appropriate platform to capture the biological signal of interest and describe the type of data it produces. 
    - Evaluate a study design in terms of power and cost, accuracy and interpretability, and generalisability.

Module 1 ended by grouping study the pitfalls into three buckets: recoverable,
limitable, and fatal. The fatal problems were:

- choosing the wrong omics platform
- fully confounding batch with biological groups
- missing or unrecorded metadata
- pooling samples when individual level inference was required

These problems cannot be fixed during analysis because they arise during study design or sample collection.  
Module 1 focused on what can go wrong; Module 2 focuses on the decisions that can prevent these problems.

Throughout this module, we will consider three aspects of study design:

- **Power and cost**: Can the study detect the biological effect of interest within the available budget?
- **Accuracy and interpretability**: Will the measurements accurately represent the biological feature of interest, and can the results be interpreted with confidence?
- **Generalisability**: Are the findings likely to apply beyond the study cohort?

These considerations often involve trade-offs. For example, increasing the number of samples may improve statistical power but leave less budget for sequencing depth or other measurements. A highly matched cohort can reduce biological variability and make effects easier to interpret, but may also limit how widely the findings can be generalised.