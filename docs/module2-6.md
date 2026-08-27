# 2.6 Generalisability: who and what the findings apply to

!!! abstract "Design question: How far do the findings extend beyond this study?"
    **Mainly affects:** Generalisability  
    **Also affects:** Accuracy and interpretability · Power and cost

Most of the decisions in this section are made at recruitment, before anything
in 2.1 to 2.5 happens. They appear last because they answer a different
question. The earlier sections asked whether the study can measure what it set
out to measure, and whether it has enough evidence to detect it. This one asks
what the answer is an answer *about*.

> A study can be internally flawless and still tell you very little about anyone who was not in it.

---

## Internal validity is not external validity

Take a two-group study where all cases come from Clinic A and all controls from
Clinic B. Section 2.2 dealt with why that fails: clinic and disease are the same
variable, and no analysis separates them.

Now suppose the design is fixed. Cases and controls are recruited from Clinic A
together, matched on age and sex, randomised through the lab, and the batch
structure is balanced. Everything 2.2 asked for has been done, and the disease
effect is cleanly estimable.

A second question remains, and nothing in the data answers it. **Do patients at
Clinic A resemble patients elsewhere?** If the clinic is a tertiary referral
centre, its patients are more severe than average. If it serves one
neighbourhood, they share diet, environment and ancestry. The effect you
measured is real, and it is an effect in that population.

The two questions are distinct. Fixing the confounding does not widen the
cohort, and widening the cohort does not fix confounding. A study can fail
either, both, or neither.

---

## Two things "generalisability" can mean

It is worth separating them, because they are set by different decisions.

**Population generalisability: who the findings apply to.** Set by recruitment.
Which individuals, from which places, at which point in the disease, under
which conditions.

**Biological scope: what the findings cover.** Set by the platform, the tissue,
and the timing. A targeted panel measures the features you named in advance and
is silent on the rest. A single tissue tells you about that tissue. A single
time point tells you about that moment.

Both are limits on the claim, and neither is a flaw. A study of one tissue in
one cohort is a perfectly good study. The failure is claiming more than the
design supports.

---

## Who is represented

Section 2.2 treated cohort composition as a source of confounding: sex skewed
between groups, each group recruited from a different place, cases collected in
one year and controls in another. Read the same variables again with the groups
balanced, and a second question appears.

**Sex.** As 2.2 put it, a sex-imbalanced two-group comparison is a confounder
you cannot fix afterwards. A single-sex study is different. The comparison is
estimable, the effect is real, and it is an effect in one sex. Module 1 showed
how much of the transcriptome differs by sex in at least one tissue, which is
the reason this matters rather than a formality. The limitation is statable,
and stating it is the whole obligation.

**Recruitment source.** Where people were recruited carries age, severity,
medication, comorbidity and socioeconomic position with it. Balanced across
groups, those characteristics need not confound the comparison. They still
describe who the answer is about.

**Disease spectrum.** Which patients have the condition matters as much as which
people were recruited. Late-stage, treatment-naive cases against healthy controls
will separate cleanly, and a marker that separates them may do nothing useful in
the patients it would actually be used on: early disease, mixed severity,
already on treatment. The easier the comparison, the narrower the population it
speaks for. Treatment works the same way. If nearly everyone in the cohort is on
one drug, part of what you measured is the drug.

**Site and season.** Multi-site studies broaden the cohort and add batch
structure at the same time, which is the trade-off in miniature: the design
choice that improves generalisability makes the analysis harder. Collection
season matters more than people expect for anything involving diet, infection
or daylight.

**Species, strain, and line.** Outside human studies the same logic holds. One
inbred mouse strain, one cell line, one cultivar, one field site. Inbred strains
reduce variability, which improves power (2.4) and narrows what the result
speaks to at the same time.

!!! danger "The trade-off named"
    A tightly matched cohort reduces biological variability, so effects are
    easier to detect and easier to interpret. The same matching narrows the
    population the finding describes. Power and interpretability often pull
    towards a narrower cohort; generalisability pulls towards broader
    representation. There is no setting
    that maximises all three.

---

!!! example "Case study: when the cohort decides who benefits"

    Genome-wide association studies have been conducted overwhelmingly in people
    of European ancestry. Each individual study can be internally sound: well
    powered, properly controlled for population structure, correctly analysed.
    Nothing inside any one of them flags a problem.

    The consequence appears only when the results are used. Polygenic risk
    scores built from those studies are substantially less accurate in everyone
    else. Martin and colleagues quantified this across 17 quantitative traits.
    Taking prediction accuracy in European-ancestry individuals as 1, accuracy
    was around 0.6 in American and South Asian populations, roughly half in East
    Asian populations, and under a quarter in individuals of African ancestry.

    ![Polygenic score prediction accuracy by ancestry, relative to European-ancestry individuals](figs_m2//PRS_ancestry_accuracy_v01.png){width=90%}

    <small>Redrawn from data reported in Martin AR, et al. *Nature Genetics* 51,584–591 (2019).
    [doi:10.1038/s41588-019-0379-x](https://doi.org/10.1038/s41588-019-0379-x){target="_blank"}
    Figure created independently for this module. Points show mean relative
    accuracy across 17 quantitative traits; bars show standard error.</small>

    The mechanism is design, not analysis. Allele frequencies and linkage
    disequilibrium patterns differ between populations, so effect sizes
    estimated in one do not transfer cleanly to another. Trans-ancestry methods can
    narrow the gap, but no reanalysis recovers ancestry that was never in the
    study. Closing it takes more diverse cohorts.

    **Why it belongs here rather than in 2.2.** Nothing was confounded. The
    studies measured what they intended to measure, in the people they recruited.
    The limitation is entirely in who was recruited, and it was invisible from
    inside any single study.

    <small>
    Martin AR, Kanai M, Kamatani Y, Okada Y, Neale BM, Daly MJ. Clinical use of
    current polygenic risk scores may exacerbate health disparities.
    *Nature Genetics* 2019; 51(4): 584–591.
    [doi:10.1038/s41588-019-0379-x](https://doi.org/10.1038/s41588-019-0379-x){target="_blank"}
    </small>

---

## The evidence that this is not hypothetical

Two numbers from 2.4 are generalisability findings, not power findings.

At *n* = 3 per group, RNA-seq feature lists vary substantially between
analyses. That is not only a detection problem. It means the gene list from one
small study is a poor guide to what the next one will find.

In the meta-analysis of 244 clinical metabolomics studies, 72% of reported
metabolites appeared in only a single study. Each of those studies found
something. Almost none of them found the same thing.

Underpowered studies do not simply miss effects. They can also produce unstable
findings that are less likely to replicate in another cohort, which is why power
and generalisability are harder to separate than the three-question framing
suggests.

---

## What the sample can and cannot speak for

The lake and sea activity in 2.4 makes the same point at the level of the
sampling unit. Three vials from one lake give a precise answer about that lake.
They cannot tell you how much freshwater bodies differ from each other, because
the study contains only one freshwater body.

Precision and scope are different quantities. More measurements within one unit
buy precision. Only more units buy scope, and which one you need depends
entirely on what the conclusion is meant to cover.

---

## What to do about it

Three honest options, in increasing order of cost.

**State the limitation.** Name the population, the tissue, the platform and the
time point in the conclusions, and do not claim past them. This costs nothing
and is the most commonly skipped step. Section 2.3's metadata checklist is what
makes it possible: without recorded ancestry, site, age and collection
conditions, you cannot describe your own cohort accurately.

**Broaden the design.** More sites, more strains, more time points, both sexes.
This widens the claim and adds variability, which costs power (2.4) and adds
batch structure to manage (2.2). It is a real trade, not a free improvement.

**Validate externally.** Test the finding in a cohort that was not used to
derive it. Module 1's Pitfall 10 set out when this is optional and when it is
essential. It is the only one of the three that produces evidence rather than
caveats.

??? example "Case study: what demonstrating generalisability looks like"

    Most case studies in this workshop are failures. This one is not.

    Wirbel and colleagues asked whether gut microbiome signatures of colorectal
    cancer hold up across populations. Rather than a single cohort, they
    meta-analysed eight fecal shotgun metagenomic studies spanning three
    continents (*n* = 768), which differed in sampling procedure, storage and
    DNA extraction protocol. The technical heterogeneity was the point: a
    signature that survives it is not an artefact of one laboratory's workflow.

    They identified a core set of 29 species enriched in colorectal cancer
    metagenomes, and found that signatures derived from single studies retained
    their accuracy when applied to the others. Models trained across multiple
    studies performed better still.

    **The design lesson.** Generalisability was not asserted in a discussion
    section. It was tested, by holding out cohorts the model had never seen. That
    is the difference between a claim and a demonstration, and it was only
    possible because the individual studies had recorded enough about their
    cohorts and protocols to be combined.

    <small>
    Wirbel J, Pyl PT, Kartal E, et al. Meta-analysis of fecal metagenomes reveals
    global microbial signatures that are specific for colorectal cancer.
    *Nature Medicine* 2019; 25(4): 679–689.
    [doi:10.1038/s41591-019-0406-6](https://doi.org/10.1038/s41591-019-0406-6){target="_blank"}
    </small>

---

## What to carry forward

- Internal validity and external validity are separate. Fixing confounding does
  not widen the cohort.
- Generalisability has two halves: **who** the findings apply to, set at
  recruitment, and **what** they cover, set by platform, tissue and timing.
- A narrow cohort is a limitation, not an error. Claiming past it is the error.
- Matching and inbred lines buy power and interpretability by narrowing scope.
  That trade should be made deliberately.
- You cannot describe your own cohort without the metadata to describe it (2.3).
- Stating a limitation is free. Testing it in an independent cohort is the only
  thing that turns the claim into evidence.