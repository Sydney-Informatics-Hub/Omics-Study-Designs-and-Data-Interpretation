# 2.4.1 Design decisions in practice

!!! info "Learning objectives"
    - Trace how a single design decision propagates across more than one of the module's three organising questions
    - Use the six-question pre-experiment checklist to identify unresolved design risks before data collection begins
    - State a study's trade-offs explicitly as part of the design, rather than treating them as omissions

The three questions this module has worked through include:

1. Are the measurements trustworthy?
2. Is the study adequately powered?
3. Who does the finding apply to?

Choosing a more specific cohort makes confounding easier to control and power easier to achieve, and narrows the population the finding represents. Increasing measurement depth per sample raises per-sample cost, which reduces how many biological samples the budget can support. Recruiting across multiple sites broadens representativeness and introduces batch structure that must be managed. Every choice affects more than one question simultaneously, and the goal is to make those effects explicit rather than leave them implicit.

# 2.4.1 Putting the design together

!!! info "Learning objectives"
    - Explain why most design decisions in omics studies are irreversible once samples have been processed
    - Identify, for a proposed design, which decisions are still open and which have already been locked in
    - Describe how the methods section of a study should report design choices, trade-offs, and their rationale

Most design problems in omics studies are not discovered during analysis. They are discovered when a finding fails to replicate, when a reviewer asks why cases and controls were processed on different dates, or when a second study in the same tissue produces incompatible results. By the time any of these questions arise, the samples have been collected, processed, and sequenced. The decisions that caused the problem were made — or not made — months earlier.

This section works through those decisions in the order they actually occur, identifies the point at which each one becomes unrecoverable, and provides a planning tool for checking that none remain unresolved when data collection begins.

---

## The decision timeline

Design decisions in omics do not all occur at the same point. Some must be made before a single sample is collected. Others must be made before processing begins. A decision deferred past its window does not become available again; it becomes a constraint the analysis must work around, or a limitation that must be reported.

| Decision | Covered in | Must be made before | Why it cannot be made later |
|---|---|---|---|
| Which platform, library strategy, and acquisition mode | 2.1.1 | Library preparation | The library determines which analytes are in the data. Fractions excluded at preparation are absent permanently; acquisition mode determines which ions are sampled and whether coverage is consistent across runs. |
| How samples are allocated across batches, operators, and runs | 2.1.2 | Any sample is processed | Once processing begins, the allocation is fixed. A technical factor that ends up aligned with biological groups cannot be disentangled from those groups in the analysis, regardless of statistical method. |
| Which variables to record and what controls to include | 2.1.3 | Sample collection | A variable not recorded at the time of collection cannot be recovered. Controls not prepared before the run cannot be added afterwards. |
| How many independent biological samples | 2.2.1 | Samples are purchased or collected | Sample number is set by the time the study begins. Running a power estimate after the fact describes what the study was powered to detect, not what the study needs. |
| How much measurement depth per sample, and on how many platforms | 2.2.2 | Samples are processed | Depth is set at the point of measurement. Adding replicates after the fact, or switching platforms, requires re-processing samples that may no longer exist. |
| Which population was recruited and what the platform can resolve | 2.3.1 | Study design is finalised | Who was recruited and what the platform can measure at the depth used determine the scope of any claim the study can make. These cannot be expanded after data exists. |

Read the table top to bottom: it is also the chronological sequence. Each row's window closes before the next row's decision matters.

---

## Before data collection: an open-question inventory

The questions below are organised by the point in the workflow where they close. A question that cannot be answered is a decision still open.

**Before cohort assembly**

- What is the biological unit of replication for this question — a participant, an animal, an environmental sample, a cell line passage? Is the planned *n* a count of this unit, not a count of wells, subsamples, or technical measurements?
- Which groups are being compared, and are the individuals in each group comparable on the variables that are not the subject of the comparison — age, sex, collection site, housing conditions, collection date?
- What is the population the study is designed to speak for, and does the recruitment strategy reflect that population?

**Before processing begins**

- Is there a written allocation plan distributing all biological groups across all processing batches, operators, extraction days, and sequencing or acquisition runs?
- Does the platform choice match the analyte class, abundance range, and resolution the question requires? Has the library preparation strategy, acquisition mode, or enrichment approach been confirmed against the biological features of interest?
- Are the required controls identified and costed into the design: extraction blanks, pooled QC samples, spike-in standards, or shared reference samples, depending on platform? Have they been prepared before the first sample is processed?

**Before data collection is finalised**

- Has the sample size been estimated using effect size and biological variability from domain knowledge, published data, or pilot data, with the multiple-testing burden of this platform included? If the sample number was set by budget, has the study been reframed around what that *n* can actually detect?
- Is measurement depth set at the minimum needed to consistently detect the features the question depends on, not above it? Is depth matched across all comparison groups?
- Which biological and technical variables will be recorded, and at which points in the workflow? Are pre-analytical conditions — freeze-thaw cycles, processing intervals, storage temperature — standardised and documented across groups?

---

## What to report in the methods section

A design decision that is not reported cannot be evaluated. The methods section of an omics study should allow a reader to reconstruct the design choices made, the trade-offs they involved, and the conditions under which the findings hold.

For each decision area above, the methods section should state what was done and, where a trade-off was made, what it means for the scope of the finding:

- **Platform**: which platform, library preparation strategy, and acquisition mode; what the choice captures and what it does not (e.g. bulk measurements that do not resolve cell-type composition; targeted panels that cover a pre-specified analyte list)
- **Batch design**: how samples were allocated across processing runs and whether any technical factors were balanced or blocked; if randomisation was used, how
- **Controls**: which controls were included, how many, and at what intervals
- **Sample size**: how *n* was determined; if a power estimate was run, what inputs were used; if not, what the study is appropriately scoped to claim
- **Depth**: what depth was used per platform and why; whether it was set against a detection floor or by convention
- **Population and scope**: who was recruited, what was excluded, and what biological layer and resolution the measurement captures

A trade-off reported is a defined condition. A reader who knows that a study used a bulk measurement in a heterogeneous tissue, or that *n* was constrained by sample availability, can place the finding in context. A trade-off not reported becomes a limitation the reader cannot see.

!!! info "Module 2.4 takeaways"
    - Most design decisions in omics become unrecoverable at a specific point in the workflow. The majority close before data collection begins.
    - An open-question inventory is more useful than a checklist of criteria to satisfy: the goal is to identify which decisions are still available, not which standards have been met.
    - The methods section should report what was decided, why, and what the trade-off means for the scope of the finding — not only the protocol steps.
    - A stated trade-off defines the conditions under which a finding holds. An unstated one limits the finding in ways no reader can account for.
