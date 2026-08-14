# Module 2: Experimental Design Fundamentals for Omics

Module 1 ended by sorting the pitfalls into three buckets: recoverable,
limitable, and fatal. The fatal list was the short one:

- wrong omics platform chosen
- batch fully confounded with biological groups
- missing or unrecorded metadata
- samples pooled where individual inference was needed

Nothing on that list is an analysis mistake. Each one was settled before any
data existed, which is why no analysis recovers it. Module 1 asked what can go
wrong; **Module 2 asks what to decide, and when.**

Every decision in this module is scored three ways:

- **Power and cost** — can you detect the signal you are looking for, within
  your budget?
- **Accuracy and interpretability** — can you connect the effect you measure to
  the biological feature you care about?
- **Generalisability** — do the findings hold beyond your cohort?

Design is hard because these three compete. Money spent on more samples is not
spent on more depth; a tightly matched cohort is easier to interpret and harder
to generalise from. The sections that follow name the trade-off each time it
appears.

## Confounding: when a variable travels with your groups