# Module 1.1: The omics landscape

!!! info "Learning objectives"

    - Describe the molecular information captured by each of the five omics layers
    - Explain how the molecular layers relate through the central dogma and its regulatory steps
    - Select the most appropriate molecular layer for a given biological question
    - Evaluate the limitations of each layer and what a chosen layer cannot tell you

Modern biology has undergone a fundamental shift from measuring one 
biological molecule at a time to profiling entire classes of biological 
molecules simultaneously. This lets us ask questions not just about 
individual genes, proteins, or metabolites, but about the state of a 
whole biological system, a tumour, a leaf under drought, a gut 
microbial community, at the molecular level.

Every living system, whether a bacterium, a migratory bird, or a 
human, can be interrogated across multiple molecular layers, and each 
layer reveals a different dimension of how the system works. The 
choice of which layer to investigate, and often which combination
of layers, is one of the most consequential decisions a researcher 
makes before an experiment begins.


## From DNA to metabolite

Most biological questions can be investigated at multiple molecular layers. Each molecular layer captures a different aspect of cellular biology. A biological question may be addressed at one layer or several, depending on what is actually driving the phenotype of interest. 

The molecular layers follow a path described by the central dogma of molecular biology: DNA is transcribed to RNA, RNA is translated to protein, and protein actively drives metabolic reactions. Exceptions and regulatory mechanisms complicate this picture but the framework remains a useful starting point for understanding how information flows between layers and where omics technology intervenes. 

??? warning "The central dogma: exceptions to the rule"
    The central dogma is a useful framework, not a complete description of how biological information flows. Well-established exceptions include [reverse transcription](https://www.pnas.org/doi/10.1073/pnas.2604888123), RNA-based regulation of gene expression through [non-coding RNAs](https://www.cell.com/cell/fulltext/S0092-8674(24)01206-6), and [prion proteins](https://www.nature.com/articles/s41467-022-31460-8) that propagate heritable stats without any nucleic acid template. Our understanding of these exceptions continue to expand. 


The figure below maps these five molecular layers onto the central dogma, showing where each sits in the flow of biological information and what each layer captures.

![](figs/1-1_centraldogma.png){width=100%}

Each layer captures a different slice of biology, and no single layer gives the whole picture. To make that concrete, we will follow a single clinical question through all five layers.

!!! question "Research experiment scenario: unexplained heart failure"
    A population of patients present to hospital with heart failure and the underlying cause is unclear. We will ask the same question at each molecular layer: ***what is driving these patients' heart failure?***

??? note "Layers overlap: the choice is fit, not exclusivity" 
    Most questions can be approached from more than one layer. The lists below show what each layer is best suited to answer, not what it alone can answer.

    For example, if we want to know how closely two species are related, we can compare their DNA, RNA, or protein sequences. DNA is usually the best starting point because the same genome can be studied from any tissue, and it contains both coding and non-coding regions. 
    
    With RNA, we only capture genes that are expressed in the tissue we sampled. The general rule: **pick the layer where your signal is the dominant source of variation, not one where it competes with variation you are not studying.**

    The order of layers traces information from genomic
    variation through to its molecular consequences. It is a conceptual model,
    not a one way pathway, the layers feed back on each other throughout.
---

### Layer 1: DNA (the genome)

![](figs/1-1_dna.png){width=100%}

#### What is it?

DNA contains the instructions required to build and maintain cells. The genome is the complete set of DNA in an organism. 

Most of the genome does not encode proteins. Non-coding regions include regulatory elements like promoters, enhancers, and silencers, that control when, where, and how a gene is transcribed. Genes themselves are organised into exons (coding sequences) and introns (non-coding sequences removed during transcription). The structure of a gene determines which protein isoforms can be produced from it and therefore which downstream layers are affected. 

Understanding the genome is a prerequisite for interpreting the epigenome (which regions are regulated) and the transcriptome (which isoforms are expressed).

#### Role in biology

The genome is a stable repository of hereditary information. It determines which genes an organism possesses, how those genes are structured, and contains the regulatory elements that control gene activity across all downstream molecular layers. Unlike the layers beyond it, the genome changes relatively little across a lifetime. 

#### Insights this layer can provide

Genomics can reveal which genes an organism carries, how they are structured, and what variants are present. This includes single nucleotide variants or polymorphisms (SNV/SNP), small insertions and deletions (indels), structural variants, and copy number changes. Variants may be germline, inherited and present in every cell, or somatic, acquired in specific tissues as in cancer. The non-coding genome is equally informative: variants in promoters, enhancers, and silencers can alter when and where genes are active without changing the protein sequence itself, and are increasingly recognised as important drivers of phenotypic variation.

Beyond individual biology, the genome supports comparative questions. Genomic variation is the basis for reconstructing evolutionary relationships, characterising genetic diversity within and between populations, and identifying signatures of selection. These applications span species identification, population genetics, conservation biology, and the study of how genetic diversity shapes disease susceptibility across groups.

#### What it can't tell us 

The genome describes what an organism could do, not what it is doing. 

A gene's presence tells us nothing about whether it is transcribed, how much protein it produces, whether that protein is active, or what metabolic consequences follow. Two individuals can carry the same variant and present with completely different phenotypes, because gene expression, epigenetic regulation, environment, and chance all mediate the path from genotype to phenotype. The genome also cannot capture somatic changes that arise after development such as epigenetic alterations, transcriptional responses to stress, or acquired mutations in a subset of cells, unless those specific tissues are sampled and sequenced.

??? note "The genome in our research question"

    Blood-derived DNA from our heart failure patients can be screened for inherited variants in genes with established roles in cardiomyopathy. Whole genome or whole exome sequencing can identify rare pathogenic variants. For example, a truncating mutation in *TTN* (which encodes titin, the largest protein in the sarcomere and a major structural component of cardiac muscle) or a missense variant in *MYH7* (beta myosin heavy chain, the primary motor protein driving cardiac contraction). Variants in these genes are among the most common monogenic causes of dilated cardiomyopathy.

    Genomic analysis can also identify variants in non-coding regulatory regions that alter gene expression rather than protein sequence, and copy number variants that affect gene dosage. In a cohort study, comparing variant frequencies between patients and healthy controls can identify genomic loci associated with disease susceptibility or severity.

    - **What we learned:** a subset of patients carry pathogenic variants 
      in sarcomere genes, providing a potential molecular explanation for 
      their cardiac dysfunction.
    - **What we still don't know:** whether those variants are penetrant 
      in these individuals — not all carriers develop disease — and whether 
      patients without identified variants have a different underlying cause 
      that genomics alone cannot reveal.
---

### Layer 2: DNA modification (the epigenome) 

![](figs/1-1_epigenome.png){width=80%}

#### What is it?

The epigenome consists of chemical modifications to DNA and its associated histone proteins that determine how accessible different regions of the genome are. 

Two major mechanisms contribute to this: DNA methylation, which typically silences gene expression when it occurs at gene promoters, and histone modifications, which can either compact or open chromatin to restrict or permit transcription.

These modifications regulate gene activity without altering the underlying DNA sequence. The epigenome explains a fundamental puzzle in cell biology: how can a skin cell and a neuron contain identical DNA yet perform completely different functions? The answer lies in systematic epigenetic differences between cell types - which genes are accessible and which are locked away is established during development and maintained across cell divisions.

#### Role in biology

The epigenome acts as the regulatory interface between an organism's fixed genetic sequence and its dynamic environment. Developmental cues, ageing, and environmental exposures, including diet, stress, and toxins, can alter epigenetic marks, changing which genes are available for transcription without changing what those genes encode. The epigenome is therefore the layer at which genetic potential meets environmental context.

#### Insights this layer can provide

Epigenomics reveals the regulatory state of the genome in a given cell type at a given time. By mapping which regions are methylated or carry particular histone marks, we can determine which genes are accessible for transcription and which are silenced — information the DNA sequence alone cannot provide. This is particularly valuable for understanding how the same genome produces different cell types during development, how environmental exposures alter gene regulation over time, and how disease states involve changes in chromatin accessibility rather than changes in sequence. Epigenomic data also helps interpret non-coding variants identified by genomics: a SNP in a regulatory region only has functional relevance if that region is active in the tissue of interest, and the epigenome tells us whether it is.

#### What it can't tell us

Epigenetic changes indicate regulatory potential, not gene expression. An accessible chromatin region means a gene is available for transcription — not that it is being transcribed. Measuring DNA methylation or histone marks tells us nothing about whether accessible genes are actively producing RNA, how much, or in which isoforms. The epigenome also does not reveal the functional consequences of altered regulation — for that, we need to move to the transcriptome and beyond.

??? note "The epigenome in our research question"

    The epigenome can tell us which genes containing variants of interest are accessible for transcription in the failing heart. Profiling chromatin accessibility (ATAC-seq) or DNA methylation in cardiac tissue can reveal whether stress-response gene regions have opened up. This is a pattern associated with cardiac remodelling under sustained pressure or volume overload. Epigenetic changes reflect the cell's response to disease, not its inherited predisposition.

    - **What we learned:** stress-response and remodelling gene regions have become accessible in the patients' failing myocardium, consistent with active transcriptional reprogramming under sustained cardiac stress.
    - **What we still don't know:** whether those accessible regions are actually being transcribed, and whether the epigenetic changes are driving disease progression, compensating for it, or both.
---

### Layer 3: RNA (the transcriptome)

![](figs/1-1_rna.png){width=100%}

#### What is it?

The transcriptome is the complete set of RNA molecules a cell or tissue is producing at a given moment. 

Where the genome tells us which genes exist and the epigenome tells us which are accessible, the transcriptome tells us which are actually being used. It is the first layer that reflects the cell's current activity rather than its potential.

The transcriptome captures more than which genes are active. Alternative splicing, which is the process by which different combinations of exons are joined during RNA processing, means a single gene can produce multiple distinct transcripts, called isoforms. Each isoform potentially encodes a protein with a different structure or function. Two samples with identical gene-level expression can therefore differ substantially at the isoform level, with functional consequences that gene-level analysis would miss.

Beyond messenger RNA (mRNA), the transcriptome includes non-coding RNAs like microRNAs and long non-coding RNAs, that do not encode proteins but regulate gene expression, chromatin state, and RNA stability. Structural RNAs such as ribosomal and transfer RNAs are also transcribed constituents of the transcriptome, though they are typically removed in standard RNA-seq workflows. The regulatory non-coding RNA fraction is large, incompletely characterised, and increasingly recognised as central to the control of gene expression.

#### Role in biology

The transcriptome is the most dynamic of the molecular layers. Gene expression changes rapidly in response to developmental signals, environmental conditions, disease, and treatment. This responsiveness makes it a sensitive readout of cellular state. BUT it also means results depend heavily on when and from which tissue the sample was collected. A transcriptomic snapshot captures one moment in a continuous, context-dependent process.

#### Insights this layer can provide

Transcriptomics identifies which genes are active in a given cell or tissue, at what level, and in which isoforms. These are questions the genome and epigenome cannot answer directly. Differential expression analysis between conditions, for example disease versus healthy tissue or treated versus untreated cells, can reveal which pathways are engaged and how the cell has reorganised its transcriptional programme in response. Because expression changes rapidly, transcriptomics is also well suited to capturing dynamic processes like responses to acute stress, progression through a developmental stage, or the early effects of a drug.

At the isoform level, transcriptomics can detect alternative splicing events that produce functionally distinct protein variants from the same gene. This is relevant in conditions where splicing is disrupted. Transcriptomic profiling at single-cell resolution adds a further dimension, revealing how gene expression varies between individual cells within the same tissue and enabling the identification of rare cell populations or transitional states that bulk measurements would obscure.

#### What it can't tell us

RNA abundance does not reliably predict protein abundance. Post-transcriptional regulation, including RNA stability, translational efficiency, and protein degradation rates, means that transcript and protein levels can diverge substantially. A highly expressed gene is not necessarily producing abundant or active protein, and a gene with low transcript levels may still maintain significant protein levels due to slow protein turnover. 

??? note "The transcriptome in our research question"

    Moving from the epigenome to the transcriptome takes us from accessibility to observed activity. Measuring the transcriptome of failing cardiac tissue tells us which genes are up or downregulated relative to healthy myocardium, which signalling pathways, fibrosis, inflammation, hypertrophy, are engaged, and which isoforms are being produced from genes such as *TTN*, where isoform switching between the compliant fetal N2BA isoform and the adult N2B isoform has direct mechanical consequences for cardiac function.

    - **What we learned:** stress-response and remodelling genes are actively transcribed; fibrosis and hypertrophy pathways are upregulated; isoform shifts in structural genes are detectable and functionally relevant.
    - **What we still don't know:** whether those transcripts are being translated into functional protein at the expected levels, and whether the resulting proteins are correctly localised and active within the sarcomere.

---

### Layer 4: Proteins (the proteome)

![](figs/1-1_protein.png){width=100%}

#### What is it?

Proteins are the primary functional molecules of the cell. 

They catalyse the biochemical reactions that sustain life, form the structural scaffolds of cells and tissues, transmit signals, transport molecules, and regulate gene expression. The proteome is the complete set of proteins present in a cell, tissue, or organism at a given time.

Proteins rarely act in isolation. Many assemble into multi-protein complexes that are molecular machines whose activity depends on which subunits are present and in what stoichiometry. The composition of these complexes can determine substrate specificity, regulatory sensitivity, and subcellular localisation in ways that measuring individual protein abundance cannot capture. A protein can be present at normal levels while its binding partners are absent, leaving the complex non-functional.

The relationship between a protein's amino acid sequence and its three-dimensional structure, and therefore its function, is not always predictable from sequence alone. Small sequence differences can produce large structural and functional changes, and post-translational modifications further alter how a protein folds, where it localises, and what it binds. 

#### Role in biology

Proteins execute virtually every cellular function. Unlike RNA, which reflects transcriptional activity, the proteome reflects the cell's actual functional state: which enzymes are present and active, which signalling cascades are engaged, which structural components are intact. The proteome integrates the effects of post-translational modification by phosphorylation, ubiquitination, acetylation, and others, that rapidly alter protein activity, localisation, and stability in response to cellular signals without any change in transcript levels. This regulatory layer is invisible to transcriptomics and only partially visible to genomics, making the proteome essential for understanding how cells respond dynamically to their environment.

#### Insights this layer can provide

Proteomics directly measures the molecules that carry out cellular functions. It can quantify which proteins are present and in what abundance, identify changes in post-translational modification state that alter protein activity or interactions, and detect mislocalisation of proteins to the wrong cellular compartment. In clinical contexts, proteins measurable in accessible biofluids such as plasma or urine serve as biomarkers of tissue-level pathology, reflecting changes in distant tissues that cannot be directly sampled.

Proteomics also reveals discordance with the transcriptome. A transcript can be upregulated while its protein product is rapidly degraded, or a protein can accumulate without a corresponding increase in its mRNA due to changes in translation efficiency or protein stability. These mismatches are biologically meaningful and would be missed by transcriptomics alone. For questions about what the cell is actually doing, the proteome provides evidence that no upstream layer can substitute for.

#### What it can't tell us

Protein abundance alone does not capture activity. A protein can be present in abundance while sequestered in the wrong compartment, held in an inactive conformation by an inhibitor, or absent from its functional complex. Post-translational modifications modulate activity in ways that standard abundance measurements may not detect without modification-specific enrichment strategies. The proteome also does not directly reveal the downstream metabolic consequences of protein activity — for that, the metabolome is needed.

??? note "The proteome in our research question"

    Measuring the proteome of cardiac tissue or plasma brings us to the level of functional molecules. Clinically actionable signals emerge here that are invisible to transcriptomics: elevated BNP and troponin in plasma reflect cardiac stress and injury at the protein level; mislocalisation of sarcomeric proteins disrupts the mechanical function of the contractile apparatus; and abnormal phosphorylation of contractile proteins alters their calcium sensitivity and force generation. Proteomics can also expose mismatches with the transcriptomic picture, a transcript upregulated in the failing heart whose protein product is simultaneously being degraded, or a structural protein present at normal abundance but carrying modifications that impair its function.

    - **What we learned:** BNP and troponin are elevated in plasma; sarcomere proteins are mislocalised; phosphorylation patterns on contractile proteins are abnormal, with functional implications for myocardial force generation.
    - **What we still don't know:** what those protein-level changes mean for the heart's real-time metabolic and energetic state — the question the next layer is positioned to answer.

---

### Layer 5: Metabolites (the metabolome)

![](figs/1-1_metabolite.png){width=100%}

#### What is it?

Metabolites are small molecules produced, consumed, or modified during cellular metabolism. 

They include sugars, amino acids, lipids, nucleotides, and organic acids - the substrates and products of the enzymatic reactions that sustain cellular life. The metabolome is the complete set of these molecules present in a cell, tissue, or organism at a given time.

Metabolites occupy a distinctive position in the molecular hierarchy. Where upstream layers describe what the cell has the potential to do (genome), what is being regulated (epigenome), what is being expressed (transcriptome), and what machinery is present (proteome), the metabolome captures what is actually happening biochemically at the moment of measurement. It is the closest molecular readout of physiological state.

Beyond their role as metabolic intermediates, many metabolites function as signalling molecules, linking metabolic state back to gene regulation and completing a regulatory loop that runs in both directions through the molecular hierarchy.

#### Role in biology

The metabolome integrates information from all upstream molecular layers and from the external environment simultaneously. Nutritional state, oxygen availability, drug exposure, physical activity, microbial activity, and cellular stress all leave measurable signatures in the metabolome. This makes metabolomics a sensitive readout of whole-organism physiological state. It also means the metabolome reflects many influences at once, and attributing a metabolic change to a specific upstream cause requires supporting evidence from other layers.

#### Insights this layer can provide

Metabolomics directly measures the biochemical state of a cell or tissue at the time of sampling. It can identify which metabolic pathways are active, quantify the cell's energetic status through ratios such as ATP:ADP or NAD⁺:NADH, and detect the accumulation of pathway intermediates that indicates where a metabolic block has occurred. In disease contexts, characteristic metabolic signatures can serve as biomarkers of pathological state, and in pharmacology, metabolomics captures how a drug alters cellular biochemistry beyond its intended target.

Metabolomics is also the layer that closes the loop between molecular measurements and observable phenotype. The functional consequences of genetic variants, epigenetic changes, altered gene expression, and protein dysfunction ultimately manifest as changes in metabolic output. A metabolic shift observable in plasma or tissue is therefore often the most direct molecular correlate of a clinical phenotype — even when the upstream cause remains unclear.

#### What it can't tell us

The metabolome captures current state, not cause. A metabolic signature tells us what is happening now, not what initiated it. Establishing causality requires integrating evidence from upstream layers. Metabolites are also highly dynamic: concentrations can shift within minutes, and results are sensitive to pre-analytical variables including the time of sample collection, handling, freeze-thaw cycles, and the subject's nutritional state in the hours before sampling. Without rigorous standardisation of collection and processing, technical variation can obscure or mimic biological signal. Finally, the metabolome does not distinguish whether an observed metabolic change is a driver of
pathology, a consequence of it, or a compensatory response.

??? note "The metabolome in our research question"

    Measuring the metabolome gives us the failing heart's real-time biochemical state. A hallmark of heart failure is a substrate switch: the healthy adult heart derives approximately 70% of its ATP from fatty acid oxidation, but the failing heart shifts progressively toward glucose oxidation as mitochondrial function declines and energetic demand outstrips supply. 
    
    This fuel shift is directly detectable in tissue or plasma metabolite profiles. Reduced acylcarnitines reflecting decreased fatty acid oxidation, altered TCA cycle intermediates, and changes in lactate and ketone body concentrations, and represents the integrated physiological consequence of the changes identified across all previous layers: the inherited variant, the altered chromatin state, the dysregulated transcripts, and the dysfunctional protein complement, all converging on a measurable shift in cardiac fuel metabolism.

    - **What we learned:** the failing hearts have shifted from fatty acid to glucose oxidation, with metabolite profiles consistent with mitochondrial energetic impairment.
    - **What we still don't know:** whether the metabolic shift is driving disease progression or is a downstream consequence of structural and functional changes identified at earlier layers and which intervention point would be most effective to target.

---

## Summarising the layers 

No single layer answered the question of what is driving these patients' heart failure. Each layer captured a different aspect of the underlying biology, and each left questions that only the next layer could begin to address.

| Layer | What it tells us | What it misses | Phenotypic question addressed |
|---|---|---|---|
| **Genome** | Genetic predisposition | Whether genes are used | Why is this trait heritable? |
| **Epigenome** | Regulatory potential | Whether genes are expressed | Which environments alter trait expression? |
| **Transcriptome** | Gene expression and isoform diversity | Whether proteins are produced and active | Which genes are active in this phenotype? |
| **Proteome** | Functional molecules and their state | Physiological consequences | What is the cell doing to produce this phenotype? |
| **Metabolome** | Current physiological state | The underlying cause | What is the biochemical state associated with this phenotype? |

These layers are interconnected and feed back on each other. The table sets out where each layer is strongest, not a strict division of what each can address in isolation.

---

## Activity

Each of the five molecular layers described above is studied by its own scientific field. Collectively, these fields are called **omics**: genomics, epigenomics, transcriptomics, proteomics, metabolomics. The suffix denotes the comprehensive study of an entire class of molecules. 

The ambition is a global view of a biological layer, rather than the targeted measurement of selected molecules that characterised earlier approaches.

!!! question "Walk the layers"

    Pick the broad question closest to your field, or reinterpret the example using an organism or system you work with. These examples represent high-level biological questions rather than specific studies, and the same design principles apply across systems.

    Walk through the molecular layers and decide how you would approach the question.

    In your group, discuss:

    1. **Which molecular layer would you start with, and why?**
    2. **What would this layer tell you, and what would it miss?**
    3. **What comparisons or timing would be needed to 
       make this study meaningful?**
  
    <!-- 4. **Budget check:** you can measure only one molecular layer 
       initially. What evidence would convince you to add a second? -->

    **Report back:** your chosen layer, what another layer might 
    have revealed, and one assumption behind your choice.

    ??? example "Clinical / human disease"

        **What drives progression from a treatable tumour to one that 
        resists therapy?**

        Consider: where would you sample from, when in the disease 
        course, and what would each molecular layer contribute to 
        understanding progression?

    ??? example "Wildlife / infectious disease"

        **Why do some populations tolerate an infectious disease while 
        others suffer severe disease from the same pathogen?**

        Consider: is this a host question (immune response, genetic 
        resistance), a pathogen question (strain, virulence factors), 
        or both? Use any host–pathogen system relevant to your field.

    ??? example "Aquaculture / production biology"

        **Why do some farmed fish grow faster than others despite 
        receiving the same diet?**

        Consider: if diet is held constant, what could explain the 
        variation? Genetics, developmental history, physiology, gut 
        microbes? Which layer would you measure first, and how would 
        you sample to make the comparison meaningful?

    ??? example "Plant / environmental stress"

        **How does a crop plant respond to acute environmental stress, 
        and what makes some varieties more tolerant than others?**

        Consider: the stress could be drought, heat, or salinity, pick 
        whichever fits your system. The response happens fast, over 
        hours to days. Which layers capture that timescale, and which 
        are too slow or too stable to see it?


<!--

Module 1.1 Group Activity: Facilitator Guide

For facilitator use only. Do not display to participants.

The purpose of this activity is not to identify a single correct molecular layer. The aim is to help participants recognise that choosing an omics layer is a biological decision: each choice reflects a particular view of what is driving the phenotype, and each choice leaves some questions unanswered.

During report-back, the facilitator should focus on:

Why did the group choose this layer?
What biological process are they assuming is most important?
What information would another layer provide?

Every case has multiple defensible starting points.

Case 1: Clinical / human disease, treatment-resistant tumour

Question:
What drives progression from a treatable tumour to one that resists therapy?

Common defensible starting points

Genome

Appropriate when resistance may be driven by acquired mutations, such as resistance to targeted therapies (e.g. Trastuzumab blocks HER2 signalling). Useful for identifying genetic changes that may directly alter treatment response.

Transcriptome

Appropriate when resistance may involve pathway rewiring, altered cell states, or changes in gene regulation.
Useful when the biological question is broader than a single mutation.

Proteome

Appropriate when the important biology may occur at the level of protein abundance, activation, or signalling activity.
Useful because protein activity does not always directly match RNA abundance.
What another layer would have caught
Genome alone may miss resistance mechanisms driven by changes in gene regulation or cell state.
Transcriptome alone may not distinguish whether expression changes are causes of resistance or consequences of an underlying mutation.
Proteome alone may not reveal upstream genetic or regulatory drivers.

Hidden assumption
Genome choice implies a model where resistance is mainly driven by inherited or acquired genetic changes.
Transcriptome choice implies a model where resistance is mainly driven by changes in cellular regulation.
Proteome choice implies a model where functional activity at the protein level is the key driver.

Facilitation prompts
Genome: “Could two tumours with the same mutation respond differently to treatment? What else might explain that?”
Transcriptome: “How would you separate a cause of resistance from a downstream response?”
Proteome: “Would measuring protein abundance capture all changes in protein activity?”


Case 2: Wildlife / infectious disease, tolerance versus severe disease

Question:
Why do some populations tolerate an infectious disease while others suffer severe disease from the same pathogen?

Common defensible starting points

Pathogen genome

Appropriate if differences in pathogen strain or virulence may explain different outcomes.

Host transcriptome

Appropriate if differences in immune response or host physiology are expected to drive disease severity.

Host genome

Appropriate if population-level genetic differences may contribute to resistance or tolerance.

What another layer would have caught
Pathogen genomics alone may not explain why individuals exposed to the same strain have different outcomes.
Host transcriptomics alone may miss differences in the pathogen itself.
Host genomics alone may not explain how genetic differences influence actual immune responses.

Hidden assumption
Pathogen focused approaches assume variation in the pathogen is a major driver of outcome.
Host transcriptomics assumes differences in host response are central.
Host genomics assumes tolerance or resistance has a substantial inherited component.

Facilitation prompts
“Are we sure different populations are responding differently to the same pathogen?”
“Could environmental factors, co-infections, or nutrition also influence disease outcome?”
“What layer would help separate host effects from pathogen effects?”


Case 3: Aquaculture / production biology, growth variation

Question:
Why do some farmed fish grow faster than others despite receiving the same diet?

Common defensible starting points

Genome
- Appropriate when growth differences may be useful for breeding and selection.
- Assumes inherited variation contributes strongly to growth differences.

Transcriptome
- Appropriate when the goal is understanding biological mechanisms controlling growth.

Metagenome or metabolome
-Appropriate when differences may arise from nutrient utilisation, metabolism, or host–microbiome interactions.

What another layer would have caught
-Genome alone may miss environmental, metabolic, or microbiome effects.
-Transcriptome alone may show what pathways are active but not necessarily why they differ.
-Microbiome composition alone may not reveal microbial function or metabolic output.

Hidden assumption
-Genome choice assumes growth differences are largely explained by inherited variation.
-Transcriptome choice assumes differences arise mainly from regulatory changes in the fish.
-Microbiome/metabolome choice assumes differences arise mainly from biological efficiency and nutrient processing.

Facilitation prompts
-“If two fish have similar genetics but different growth rates, what else could explain the difference?”
-“Does seeing an active growth pathway tell us why it is active?”
-“Does measuring microbial composition tell us what the microbes are doing?”


Case 4: Plant / environmental stress — stress response and tolerance

Question:
How does a crop plant respond to acute environmental stress, and what makes some varieties more tolerant than others?

Common defensible starting points

Transcriptome
- Appropriate when the focus is rapid stress responses and changes in gene regulation.

Metabolome
- Appropriate when tolerance depends on protective compounds, energy balance, or biochemical adaptation.

Epigenome
- Appropriate when stress memory or longer-term adaptation is important.

Genome
-Appropriate when the goal is identifying genetic variation linked to tolerance for breeding.

What another layer would have caught
-Transcriptome alone may show stress responses without showing whether those responses successfully protect the plant.
-Metabolome alone may show protective compounds without identifying the regulatory pathways controlling them.
-Genome alone may miss environmental effects and regulatory responses.

Hidden assumption
Transcriptome choice assumes tolerance depends mainly on the ability to activate stress responses.
Metabolome choice assumes tolerance depends mainly on biochemical protection.
Epigenome choice assumes previous exposure and cellular memory contribute to tolerance.
Genome choice assumes tolerance has a stable inherited component.
Facilitation prompts
“Does a stronger stress response always mean a more tolerant plant?”
“If two plants have similar tolerance-associated genes but respond differently, what else could explain this?”
“Would your chosen layer explain the mechanism or only identify the phenotype?”
Closing facilitator note

A successful discussion is not one where groups select the same molecular layer. The goal is for participants to recognise that every choice represents a biological model and a trade off.

The strongest answers are those that:

justify why a layer was selected,
identify what information it cannot provide,
recognise what additional evidence would strengthen the conclusion.

The activity should reinforce the central message of the workshop: omics study design begins with defining the biological question, not choosing a technology.
-->