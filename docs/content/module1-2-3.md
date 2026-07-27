module## 🟠 Stage C :  Preprocessing
 
### Pitfall 6: Missingness & normalisation

#### Missingness
**Imputation choice depends on why data is missing, not how much is missing.** Whether a gap should be filled (imputed) and how, depends on the platform, the proportion missing, and whether the pattern is random or structured. Treating every missing value the same way carries whichever assumption is wrong straight into the results.

*Example:* Filling a protein's missing values with the **sample mean** assumes they're missing at random. But in label-free mass spectrometry, missing usually means the signal fell below the detection threshold the true value is more likely low, not average. Mean-imputation systematically inflates exactly the low-abundance proteins a discovery study is trying to find.

Sample mean approach can:

- underestimate differences between groups,
- bias fold-change estimates,
- and lead to misleading statistical results.

**Filtering can quietly remove exactly the features a study cares about most.** Rare taxa, lowly-expressed genes, and low-abundance proteins are the first to be dropped by a standard threshold and could be of biological interest.

*Example*: A microbiome study removes all taxa present in less than 20% of samples before analysis.
One pathogen associated with disease is present in only 15% of cases and absent from controls.

The filtering threshold removed the very organism driving the biological effect.

Potential consequence
Loss of biologically relevant features
False conclusion that no disease-associated taxa exist

#### Normalisation 

Some normalisation methods only work if a reference sample, spike-in, or technical replicate was included at the wet-lab stage. Pooled QC injections and shared batch references have to be planned and prepared before data collection starts. If they were never included, that normalisation strategy isn't available later, no analysis choice can substitute for it.
