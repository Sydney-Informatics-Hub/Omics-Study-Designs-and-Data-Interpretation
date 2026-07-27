!!! question "Part 1: Activity, Analyse this study design"

    A 2012 gut microbiome study collected microbiota from five pregnant women 
    per condition, pooled them into a single inoculum, and inoculated 
    six germ-free mice per condition. Statistics were performed on n = 6 mice.

    ![](figs_m1/01_pseudoreplication_activity01_v01.png){width=90%}

    <small>Ref: Koren et al., *Cell* 150, 470–480 (2012)</small>

    Discuss in your group:

    1. What is the true experimental unit, the mouse or the human donor?
    2. What is the actual n per condition?
    3. Are the six mice independent biological replicates? Why or why not?
    4. What does this mean for the p-values reported?
    5. What information would you need to determine if this is recoverable?
    6. Is this error recoverable after data collection?

<!--
??? success "Answers: reveal after group discussion"

    **Q1. True experimental unit?**  
    The human donor, not the mouse.

    **Q2. Actual n per condition?**  
    n = 1. There was only one pooled inoculum per condition.

    **Q3. Are the six mice independent biological replicates?**  
    No, all six received the same inoculum. They are technical 
    replicates, not biological replicates.

    **Q4. What does this mean for the p-values?**  
    They are uninterpretable. Degrees of freedom are artificially 
    inflated, producing false precision and invalid inference.

**Q5. What information would you need to determine if this
    is recoverable?**
    You would need to know whether individual donor samples were
    kept separate before pooling. Specifically:

    - Were aliquots from each donor preserved individually
      before pooling into the shared inoculum?
    - Is DNA or 16S sequence data available per donor that
      could distinguish their microbial contributions?
    - Were any mice inoculated with single-donor material
      rather than the pool?

        If all donor material was irreversibly pooled and no
        individual aliquots were retained, this is **unrecoverable**.
        The biological contributions of individual donors cannot
        be separated from a mixed inoculum after the fact.
        The experiment would need to be repeated with one
        inoculum per donor.

    **Q6. Is this recoverable?**  
    No: unrecoverable. Pooling happened at sample collection. 
    Donor contributions cannot be separated retrospectively.

    <small>Ref: Wagner & Kleiner, *Nat Commun* 16, 7263 (2025)</small>

    ![](figs_m1/02_pseudoreplication_activity01_v02.png){width=100%}

-->

!!! question "Part 2: Apply to your own study"

    Briefly describe a study you are planning or have
    been involved in. In small groups:

    1. Identify which one of the pitfalls your study
       is most vulnerable to
    2. Classify the risk: fatal, limitable,
       or recoverable?
    3. What one change at the design stage would
       reduce that risk?
