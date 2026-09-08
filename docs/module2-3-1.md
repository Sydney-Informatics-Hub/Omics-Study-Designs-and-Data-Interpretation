# 2.3.1 Generalisability: who and what the findings apply to

!!! info "Learning objectives"
    - Use the metadata recorded about an example cohort to state who a study's findings do and do not apply to
    - Evaluate the trade-off between narrowing a cohort for power and broadening it for generalisability
    - Apply those trade-offs to recommend a follow-up design or a reallocation of resources between depth and coverage

The two previous sections of Module 2 asked whether the measurements were trustworthy and whether there were enough of them to detect an effect. This section asks a third question: **who and what does the finding apply to?**

**Generalisability** describes how far a study's findings extend beyond the specific samples and conditions in which they were produced. Every study is conducted on a defined group like particular individuals, a particular tissue, under particular conditions, at a particular time. The measurements describe that group. Whether they also describe other groups, other tissues, or other conditions is the generalisability question. 

Generalisability is sometimes called **external validity**: the extent to which findings hold outside the study. This is distinct from **internal validity**, which asks whether the comparison within the study is trustworthy: whether the observed difference between groups reflects the biology of interest rather than something else. A study can have strong internal validity and still have narrow generalisability. These are different questions and are addressed by different parts of the design.

The narrower a study's scope, the more precisely a comparison can be made — but the less that comparison describes beyond itself. This is not a flaw. A study designed and reported with clear limits is more useful than one that overclaims. The problem is not scope; it is claiming past the design.

---

## Components of generalisability

Before asking how generalisable a finding is, it helps to be precise about what generalising means. There are two distinct components:

1. **Population generalisability**: *who* the finding applies to. This is determined by who was recruited: which individuals, from which settings, at which point in their condition. 

2. **Biological scope**: *what* the finding covers. This is determined by the platform and sampling strategy: which molecular layer was measured, in which tissue or sample type, at which time point. A transcriptomic finding from liver tissue does not describe what is happening in kidney. 

!!! question "Activity: where does the conclusion exceed the design?"

    Each scenario below describes a study and a conclusion drawn from it. For each one:

    1. Identify a **population generalisability** failure: who does the study actually describe, and who is the conclusion wrongly extended to?
    2. Identify a **biological scope** failure: what does the measurement actually capture, and what is the conclusion wrongly claiming it covers?

    Choose the scenario most relevant to your field, or work through all five.

    ??? question "**Scenario 1: Genome**"

        A GWAS of 480,000 individuals of European ancestry identifies 34 variants associated with type 2 diabetes risk. The authors conclude: *"These variants can be used to calculate polygenic risk scores to identify individuals at elevated risk of type 2 diabetes."*

        ??? example "Answers"

            *Population:* The cohort is European-ancestry only. Allele frequencies and linkage disequilibrium patterns differ between populations; polygenic risk scores built from European GWAS are substantially less accurate in people of other ancestries. The conclusion claims a general risk tool; the design produced one that works primarily in European-ancestry individuals.

            *Scope:* Identifying associated variants does not establish what those variants do biologically or in which tissue they act. A variant in a regulatory region may influence gene expression only in a specific cell type like pancreatic beta cells, adipocytes, or liver hepatocytes, that was never measured. The GWAS identifies statistical associations; the molecular mechanism and tissue of action require further experiments.

    ??? question "**Scenario 2: Epigenome**"

        ATAC-seq is performed on CD4+ T cells isolated from peripheral blood of 30 patients with active rheumatoid arthritis and 30 healthy controls. The authors report 1,240 differentially accessible chromatin regions and conclude: *"These regulatory elements control the gene expression changes that drive rheumatoid arthritis pathology."*

        ??? example "Answers"

             *Population:* The study uses CD4+ T cells from peripheral blood of patients with active disease. Whether the same chromatin changes are present in other immune cell types, in patients with early or remitting disease, or in other populations is not established.

            *Scope:* Chromatin state is established separately in each cell type. The accessible regions in circulating CD4+ T cells do not describe the regulatory state in synovial fibroblasts, tissue-resident macrophages, or other cell types at the site of joint inflammation — where much of RA pathology is driven. Blood is not a proxy for the epigenome of joint tissue.


    ??? question "**Scenario 3: Transcriptome**"

        Bulk RNA-seq is performed on liver tissue from male C57BL/6 mice fed a high-fat diet for 12 weeks versus standard chow controls. The authors report upregulation of lipid metabolism and inflammatory pathways and conclude: *"High-fat diet induces a conserved transcriptional programme in the liver that drives metabolic dysfunction."*

        ??? example "Answers"
            *Population:* The study uses one inbred mouse strain (C57BL/6), one sex (male), one diet duration (12 weeks), and one age. Transcriptional responses to high-fat diet differ between strains and sexes. "Conserved" implies generality across species and conditions; the design tests one narrow configuration.

            *Scope:* Bulk liver RNA-seq averages expression across all liver cell types — hepatocytes, Kupffer cells, stellate cells, endothelial cells. An upregulated lipid metabolism gene could reflect increased activity in hepatocytes, an expansion of a cell population that already expresses that gene at high levels, or both. The data cannot attribute the change to a specific cell type or process without single-cell or sorted-population data.

    ??? question "**Scenario 4: Proteome**"

        Plasma proteomics is performed on 45 individuals with early Alzheimer's disease and 45 age-matched cognitively normal controls. The authors identify 18 proteins at significantly different concentrations and conclude: *"These proteins are biomarkers of Alzheimer's disease pathology and reflect the molecular changes occurring in the brain."*

        ??? example "Answers"
            *Population:* The study is restricted to early Alzheimer's disease in one age group, likely from a memory clinic or specialist setting. Whether the same plasma proteins are altered in later-stage disease, in younger-onset cases, or in populations with different genetic backgrounds (e.g. APOE ε4 carriers versus non-carriers) is not established.

            *Scope:* Plasma proteins are secreted from many organs simultaneously. A difference in plasma protein concentration between groups reflects the net contribution of liver, kidney, immune cells, and other tissues — not specifically the brain. A plasma biomarker associated with Alzheimer's disease does not establish that the protein is elevated in brain tissue or that it reflects a brain-specific process. Establishing brain origin requires cerebrospinal fluid or brain tissue measurements.

    ??? question "**Scenario 5 — Metabolome**"

        Untargeted urine metabolomics is performed on samples from 60 adults with active inflammatory bowel disease and 55 healthy controls, collected at a single outpatient clinic between 9am and 12pm. The authors identify 47 differentially abundant metabolites and conclude: *"These urinary metabolites capture the metabolic signature of gut inflammation in IBD."*

        ??? example "Answers"
            *Population:* The study uses adults with active disease at a single outpatient clinic. People attending a specialist IBD clinic have disease requiring ongoing management — they may not represent the broader IBD population including those with mild or recently diagnosed disease. Whether the same metabolites are altered in paediatric IBD, in different disease subtypes (Crohn's versus ulcerative colitis), or at different disease stages is not answered.

            *Scope:* Urine metabolites reflect kidney filtration of circulating metabolites — not direct measurement of gut tissue metabolism. A difference in urinary metabolite concentrations is consistent with altered gut metabolism, but also with altered metabolism in liver, muscle, or other tissues that contribute to the circulating pool. Additionally, the collection window (9am–12pm) and any dietary differences between groups are not controlled; some differences may reflect collection timing or pre-collection diet rather than disease biology.

---

## Internal validity and external validity

Two different questions bear on whether a study's conclusions are trustworthy:

1. **Internal validity** asks: within this study, do the observed differences between groups reflect the biology of interest? A study has poor internal validity when something other than the comparison of interest differs between groups and influences the measurements. That other variable is called a **confounder**.

2. **External validity** asks a different question: does the finding hold beyond this specific study? Even when the internal comparison is clean — groups well-matched, confounders controlled — the study still represents a particular population studied under particular conditions. Whether the result extends to a different population, a different tissue, or a different set of conditions is not answered by the internal analysis.

Section 2.1.2 covered how to design for internal validity. Comparison groups should be matched on known confounders like age, sex, collection site, processing batch, so that differences between groups can be attributed to the biology being studied rather than to differences in who was recruited or how samples were handled. When this is done well, a difference in gene expression, protein abundance, or metabolite concentration between groups is more likely to reflect the biology of interest.

These two questions are independent:

- A study with good internal validity (well-controlled comparison) can have poor external validity (narrow population that does not represent others).
- A study with broad, diverse recruitment can still have poor internal validity if comparison groups are unbalanced on confounders.
- Fixing confounding does not broaden the population the finding describes. Broadening the population does not fix confounding.

---

## Biological scope: what each layer can and cannot generalise

[Module 1.1](module1-1.md) introduced the five molecular layers and what each one captures. The generalisation constraints for each layer follow directly from its biology.

**Genome.** DNA sequence is largely stable across all cells of an individual and does not change over time (germline mutations aside). A variant identified in blood DNA is present in liver, muscle, and brain. Genomic findings from one tissue can therefore inform questions about biology in other tissues, because the same variants are present everywhere. The exception is somatic mutations which differ between tissues and must be measured in the tissue of interest.

**Epigenome.** Chromatin state is established during cell differentiation and maintained differently in each cell type. The regulatory regions that are accessible in a blood cell are not the same as those accessible in a liver cell. An epigenomic result from one tissue describes the regulatory state in that tissue. It does not describe the regulatory state of the same genomic regions in another tissue, even though the underlying DNA sequence is identical.

**Transcriptome.** Gene expression is both tissue-specific and time-sensitive. The same gene may be expressed at very different levels in liver versus skeletal muscle. Expression in the same tissue changes in response to developmental stage, environmental conditions, disease, and treatment. A transcriptomic result is a snapshot: it describes which genes were active in that tissue, at that time point, under those conditions. A result from liver at one time point does not describe liver at a different time point, or what was happening in kidney at any time point.

**Proteome.** Protein abundance reflects not just transcription but also translation efficiency, post-translational modification, and protein degradation rates — none of which the transcriptome directly captures. Like the transcriptome, the proteome is tissue-specific. Plasma and liver proteomics from the same individual measure different things: plasma contains proteins secreted from multiple organs simultaneously, while a tissue proteome reflects what that tissue is actively producing. As covered in [Module 2.1.1](module2-1-1.md) and [Module 2.1.3](module2-1-3.md), proteomic measurements are also sensitive to how samples are handled: degradation, freeze-thaw, and storage conditions change what is detected and at what apparent abundance.

**Metabolome.** Metabolite concentrations change faster than any other layer. Concentrations in blood can shift within minutes in response to food intake, physical activity, time of day, and physiological stress. A metabolomic result is therefore particularly sensitive to the exact conditions under which samples were collected. A plasma sample taken after an overnight fast at 8am reflects a different metabolic state than one taken two hours after lunch. As covered in Section 2.1.3, pre-analytical standardisation — fasting protocol, collection time, handling after collection — is part of study design for metabolomics precisely because these variables directly affect the measurement.

A **targeted assay** is a targeted sequencing panel, a selected metabolite panel, a targeted proteomics method. These introduce a further constraint as they measure only the features that were specified in advance. No information is produced about features outside the panel, including features that might turn out to be more relevant than those selected.

---

## Two ways a conclusion can claim past the design

**Extrapolation** applies a result to a population, tissue, or set of conditions that the study did not include. A finding in one wheat variety is extrapolated when claimed to apply to all cereal crops. A finding in male mice is extrapolated when claimed to apply to female mice. A plasma biomarker result is extrapolated when claimed to describe what is happening inside liver cells. The gap may be small or large — that is an empirical question — but the original study does not close it.

**Drawing cell-level conclusions from bulk measurements.** Every bulk omics measurement is an average across all the cells in a sample. A bulk RNA-seq library from a liver biopsy averages gene expression across hepatocytes, endothelial cells, Kupffer cells, and stellate cells simultaneously. A mass spectrometry run on plasma averages protein contributions from the liver, kidney, and immune system at once. A metabolomics run on whole blood reflects the metabolism of red blood cells, white blood cells, and plasma components together.

When a bulk measurement is higher in one condition than another, there are at least two distinct biological mechanisms that could produce this result:

1. The same cell types are behaving differently in the two conditions — each hepatocyte, for example, is producing more of protein X.
2. The proportion of cell types has changed — there are more Kupffer cells, which produce a lot of protein X, while the hepatocytes themselves are unchanged.

These two mechanisms are biologically distinct. They point to different processes and potentially to different follow-up questions. Bulk measurement cannot tell them apart. This applies to all five layers, not just the transcriptome:

- A higher average methylation level at an epigenomic locus in diseased tissue could mean each cell is more methylated, or that a cell type with high methylation at that locus is more abundant.
- A higher plasma protein concentration could mean each contributing tissue is secreting more, or that a tissue that is a high secretor of that protein has increased in mass or activity.
- A higher metabolite concentration in whole blood could reflect altered metabolism across all blood cell types, or a shift in the proportions of those cell types.

Single-cell approaches (such as scRNA-seq, which Section 2.2.2 covered for sample size decisions) address this directly by measuring individual cells. Sorted-population approaches measure specific cell types after physical separation. Bulk measurement is not wrong — it is appropriate for many questions — but the interpretation must be constrained by what the measurement actually represents.

---

## Who is represented

Section 2.1.2 covered cohort composition as a source of confounding: when comparison groups differ on unmeasured variables, the measurement differences reflect those variables as well as the biology of interest. The question here is different. Assuming the groups are well-matched and internal validity is adequate, who do the findings describe?

| Characteristic | What it limits |
|---|---|
| **Sex composition** | Sex-associated differences in gene expression, chromatin state, protein abundance, and metabolite concentrations have been documented across all five molecular layers. A study conducted predominantly in one sex primarily describes that sex. Whether the same patterns hold in the other sex requires data from both. |
| **Recruitment setting** | A specialist referral clinic selects people with more severe or complex presentations than the general population with the same condition. A community health screen selects people who seek preventive care. Both are coherent and well-defined populations. Neither automatically represents all people with a condition. |
| **Disease stage and treatment** | Long-standing, heavily treated disease produces different molecular patterns than early or untreated disease. Treatment directly alters metabolic pathways, gene expression, and protein abundance. A finding in treated patients reflects the combination of the disease and the treatment. |
| **Collection conditions** | Time of day, fasting state, season, and prior physical activity influence the transcriptome, proteome, and metabolome. Samples collected under different conditions show measurement differences that may reflect collection context rather than biology. |
| **Species, strain, or variety** | An inbred mouse strain is genetically homogeneous, which reduces biological variability and improves statistical power (Section 2.2.1) while restricting what the finding applies to. Results from one strain may not hold in another strain, in outbred animals, or in humans. The same applies to plant varieties, microbial strains, and cultured cell lines. |

There is a genuine trade-off here. Narrowing recruitment — one strain, one sex, one disease stage, one site — reduces biological variability. Lower variability means effects are more detectable. Section 2.2.1 established that statistical power increases as within-group variability decreases: the required sample size is lower when groups are homogeneous. The cost is that the narrower the cohort, the fewer organisms or people the finding applies to. Broader recruitment improves generalisability and increases variability, which requires more samples to detect the same effect size (Section 2.2.1) and introduces more batch structure to manage (Section 2.1.2). These cannot all be optimised simultaneously under a fixed budget.

!!! example "Case study: polygenic risk scores and ancestry"

    Genome-wide association studies (GWAS) identify genetic variants associated with a trait or disease by comparing allele frequencies between affected and unaffected individuals across the genome. Most large GWAS have been conducted in people of European ancestry.

    Each individual study is internally valid: the cohorts are large, population structure is accounted for, and the analysis is correctly performed. The limitation appears when the results are applied. Polygenic risk scores — scores that aggregate the effect of many variants to estimate an individual's genetic risk — are substantially less accurate in people of non-European ancestry.

    Martin and colleagues quantified this across 17 quantitative traits. Taking prediction accuracy in European-ancestry individuals as 1.0, accuracy was approximately 0.6 in South Asian populations, roughly 0.5 in East Asian populations, and below 0.25 in individuals of African ancestry.

    ![Polygenic score prediction accuracy by ancestry, relative to European-ancestry individuals](figs_m2/PRS_ancestry_accuracy_v01.png){width=90%}

    <small>Redrawn from data reported in Martin AR, et al. *Nature Genetics* 51, 584–591 (2019). [doi:10.1038/s41588-019-0379-x](https://doi.org/10.1038/s41588-019-0379-x){target="_blank"}</small>

    The mechanism is in the recruitment, not the analysis. Allele frequencies and the patterns of correlation between nearby variants differ between populations; effect sizes estimated in one population do not transfer to another. No statistical method recovers ancestry that was never in the study. Closing the gap requires cohorts that include more populations.

    <small>Martin AR, et al. Clinical use of current polygenic risk scores may exacerbate health disparities. *Nature Genetics* 2019; 51(4): 584–591.</small>

---

## Underpowered studies produce unstable findings

A study can fail to replicate in an independent cohort for two different reasons: there is a genuine biological difference between the populations, or the original finding was not stable.

Section 2.2.1 established that underpowered studies — studies with too few independent biological samples relative to the effect size and variability in the data — do not only miss true effects. They also detect signals that depend on which specific samples happened to be in the study. At low sample sizes, the detected features are partly determined by which individuals showed the strongest signal in that particular run. A different set of samples from the same population would produce a partly different result.

In transcriptomics, studies have shown that *n* = 3 per group detects between 20% and 40% of truly differential genes. The genes that appear in any given small study are an incomplete and variable subset of the true differential set. A list generated from *n* = 3 will overlap only partially with a list generated from a different set of *n* = 3 samples from the same population.

In metabolomics, a meta-analysis of 244 clinical studies found that 72% of statistically significant metabolites were reported in only one study. Each individual study detected a signal. Almost none detected the same one.

This is why power and generalisability are not entirely independent. When a finding fails to replicate in an independent cohort, the explanation could be a genuine population difference — or it could be that the original result was driven by sampling variation in an underpowered study. Without adequate power in the original study, distinguishing these two explanations is not straightforward.

---

## Recommendations for follow-up

No single study can fully establish generalisability, and that is not the expectation. The table below describes three types of action. Each adds something, and they are not a checklist to complete before publication. The first costs nothing and can be done at the writing stage of any study. The second applies when design decisions are still open. The third is the most informative, but targeted approaches make it far more achievable than repeating the full study. Any one of these options strengthens a finding; none requires all three.

| Action | What to do | What it addresses | Effort |
|---|---|---|---|
| **State the limitation** | In the results and conclusions, name the population (sex, age, species or strain, disease stage, recruitment setting), the tissue or sample type, the molecular layer, the platform, and the collection conditions. Do not claim past them. This requires that metadata was recorded — the checklist in Section 2.1.3 is what makes an honest scope statement possible. | Makes the scope of the finding explicit. Prevents overclaiming. Helps readers assess whether the finding applies to their own context. | Low — done at the writing stage |
| **Broaden the design** | Recruit from additional sites, include both sexes, use multiple strains or varieties, or extend the time course. Each change widens the population the finding describes. | Directly expands who the finding applies to. | Medium to high — more biological variability means more samples needed (Section 2.2.1), more batch structure to manage (Section 2.1.2), and higher total cost (Section 2.2.2) |
| **Validate using public datasets** | Search existing reference repositories — TCGA (cancer genomics), UK Biobank (multi-omic population cohort), GTEx (multi-tissue transcriptomics), MetaboLights (metabolomics), PRIDE (proteomics) — for independent cohorts with different recruitment, protocols, and batch structure. A finding that replicates under different conditions is meaningful evidence of generalisability. | Tests whether the finding holds beyond the original study without collecting new samples. | Low to medium — computation and analysis time, no new sample collection |
| **Validate using targeted assays** | Use the discovery study to identify a shortlist of candidates. Test those candidates in an independent cohort using lower-cost targeted assays — qPCR, ELISA, targeted mass spectrometry, or a targeted sequencing panel. This is faster and cheaper than re-running the full discovery protocol, and more informative about generalisability than a larger discovery study in the original cohort. | Confirms that key findings replicate in a different population using an independent approach. | Lower than full replication; scales with the size of the candidate list |

??? question "Activity: reading a cohort for scope"

    A research team publishes a plasma metabolomics study comparing people with type 2 diabetes (T2D) to normoglycaemic controls. The recorded metadata is:

    | Variable | Cases (*n* = 48) | Controls (*n* = 52) |
    |---|---|---|
    | Age (mean ± SD) | 61 ± 8 years | 60 ± 9 years |
    | Sex | 79% male | 81% male |
    | BMI (mean ± SD) | 31.2 ± 4.1 | 28.6 ± 3.8 |
    | Recruitment | Single hospital diabetes outpatient clinic | Same hospital, GP referrals for metabolic screening |
    | Disease duration | 8–22 years (all established T2D) | — |
    | Treatment | 94% on metformin; 38% on additional glucose-lowering therapy | — |
    | Collection | 07:30–09:30, fasted ≥ 8 hours | Same |
    | Platform | Untargeted LC-MS, positive and negative ion mode | — |
    | Sample type | Plasma | Same |

    The study reports 34 metabolites significantly different between groups after FDR correction (the method for correcting for testing thousands of features simultaneously, covered in Section 2.2.1), including acylcarnitines, TCA cycle intermediates, and branched-chain amino acids.

    **Part 1: Who does this finding describe?**

    Using the metadata table above:

    1. Which sex does the finding primarily describe, and why does this matter for metabolomics?
    2. What disease stage and treatment context is described? Would you expect the same metabolite signature in newly diagnosed, untreated T2D?
    3. What does the recruitment source suggest about the severity of T2D in the case group?
    4. The collection protocol is tightly standardised (fasted, fixed time window). Is this a strength or a limitation for applying the result in other settings?

    **Part 2: What does the finding cover biologically?**

    5. The platform is untargeted LC-MS. Does this mean the study captured the complete metabolome?
    6. The sample type is plasma. Does a difference in plasma metabolite concentrations establish that the same metabolites are altered inside the tissues where T2D pathology is primarily driven — liver and skeletal muscle?

    **Part 3: Recommendation**

    7. A follow-up study has budget for one of two designs: (a) the same design with *n* = 150 per group at the same single site, or (b) the same *n* = 48/52 split across two recruitment sites, with targeted validation of the 34 reported metabolites in matched skeletal muscle biopsies from a subset. Which do you recommend, and what specific limitation does each address?

    ??? example "Answer"

        **Part 1**

        1. Approximately 80% of participants are male. Plasma metabolite concentrations differ systematically between sexes for acylcarnitines, amino acids, and lipid species — the classes reported in this study. The finding primarily describes T2D metabolite patterns in males. Whether the same signature appears in females is not answered by this study and cannot be inferred from it.

        2. Cases have established T2D of 8–22 years duration; 94% are on metformin. Metformin directly alters mitochondrial function and gut microbiome composition, both of which affect acylcarnitine and amino acid profiles. The metabolite signature reflects T2D in a long-established, predominantly treated state. Whether the same signature appears in newly diagnosed, untreated T2D is a separate question. Some of the reported differences may reflect drug effects rather than disease biology.

        3. A hospital diabetes outpatient clinic manages patients with more severe or complex T2D than those managed in primary care. The case group does not represent the full population of people with T2D — it represents those whose disease requires specialist management.

        4. Standardised fasted collection at a fixed time window is a strength for internal consistency: it removes dietary state and circadian variation as sources of noise within the study, which helps detect genuine metabolite differences between groups. It is a limitation for applying the result in settings where standardised fasted collection is not feasible — which includes most clinical and field settings. A biomarker that requires fasted morning collection is only useful where that is possible.

        **Part 2**

        5. No. Untargeted LC-MS with positive and negative ion modes provides broad but incomplete coverage. Which metabolites are detected depends on their ionisation efficiency, the chromatographic method, the mass range scanned, and the spectral reference library used for identification. Many metabolite classes are poorly covered by standard LC-MS methods. The study reports differences among detectable metabolites, not across all metabolites.

        6. No. Plasma metabolite concentrations reflect contributions from multiple organs simultaneously — liver, kidney, skeletal muscle, and others all secrete metabolites into circulation. An elevated plasma acylcarnitine concentration is consistent with reduced fatty acid oxidation but does not identify where in the body that reduction is occurring. Establishing that the same metabolites are altered within skeletal muscle tissue requires direct tissue measurement.

        **Part 3**

        Option (a) addresses the power and stability problem. At *n* ≈ 50 per group, the original study may have detected metabolites driven partly by sampling variation rather than a consistent biological signal. Increasing to *n* = 150 produces a more stable signature with fewer false positives and better coverage of smaller effects. It does not address sex imbalance, disease severity bias, treatment confounding, or the question of whether plasma differences reflect tissue-level changes.

        Option (b) addresses generalisability directly. A second recruitment site tests whether the plasma signature holds in a different clinical population under different institutional conditions. Targeted validation in skeletal muscle tissue tests whether the plasma result reflects tissue-level pathology in the organ most relevant to T2D. The constraint is that at the original *n*, the discovery signature being validated may itself be unstable.

        The right choice depends on the primary aim. If the goal is a stable, reliable plasma biomarker — something deployable in clinical practice — option (a) is the necessary first step: validating an unstable list in a second cohort provides limited information. If the goal is biological understanding of T2D pathology in muscle, option (b) addresses that directly. In either case, the reported findings should explicitly state who they describe and what they do not cover.

---

!!! info "Module 2.3.1 takeaways"
    - Generalisability has two components: population generalisability and biological scope.
    - Internal validity and external validity are independent. Controlling confounding does not widen the population the finding describes.
    - Each molecular layer has different scope constraints. 
    - Narrowing a cohort can improve power and interpretability. Broadening a cohort can improve generalisability. These trade-offs are governed by the same constraints as sample size and batch management.
    - Underpowered studies produce findings that may not replicate in independent cohorts even within the same population, because the detected features depend partly on which samples happened to be included.
    - Always state the scope of your finding explicitly: the population, tissue, molecular layer, platform, and collection conditions. 
    - External validation does not require repeating the full study. Public datasets and targeted low-cost assays in a second cohort both provide evidence of generalisability at lower cost than a full replication.
