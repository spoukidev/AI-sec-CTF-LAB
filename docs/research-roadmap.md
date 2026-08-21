# AI Security CTF Research Roadmap

This roadmap evolves the platform from a training lab into a reproducible AI-security research portfolio project.

## Phase 1 — Deterministic Challenge Baseline

- Keep every core challenge reproducible without paid APIs.
- Document the threat model, expected attacker capability, and trust boundary for each challenge.
- Add tests that confirm both the intended vulnerable behavior and the secure remediation path.
- Ensure all flags, data, identities, and services are synthetic and local-only.

## Phase 2 — Prompt Injection Evaluation

- Add a benchmark set for direct and indirect prompt-injection attempts.
- Record success/failure outcomes under multiple prompt templates.
- Separate instruction-following failures from authorization failures.
- Compare simple mitigations such as delimiters, content labeling, output schemas, and deterministic policy checks.

## Phase 3 — RAG Security

- Measure retrieval poisoning success under different ranking strategies.
- Track trusted-source weighting and provenance metadata.
- Compare naive retrieval against source-aware retrieval filters.
- Add citation-integrity tests so displayed provenance is tied to trusted metadata rather than filenames.

## Phase 4 — Agent and Tool Security

- Model the confused-deputy problem with local synthetic roles and tools.
- Add deterministic authorization checks outside the LLM layer.
- Compare vulnerable tool-routing logic with secure allowlisted execution.
- Document how untrusted retrieved content can influence tool decisions.

## Phase 5 — Adversarial Machine Learning

- Keep evasion and poisoning challenges limited to synthetic numeric feature spaces.
- Measure model performance before and after controlled perturbations.
- Document mutable versus immutable features.
- Compare baseline models with defensive approaches such as robust feature selection or adversarial training.

## Phase 6 — Explainability Security

- Test whether small allowed feature changes can significantly alter SHAP explanations while preserving predictions.
- Track explanation stability separately from prediction accuracy.
- Add examples showing why explanation confidence and model confidence are not the same concept.

## Phase 7 — AI SOC Security

- Expand the final challenge around alert triage, RAG context, local tools, ATT&CK-style mappings, and incident correlation.
- Make every inferred security conclusion traceable to stored evidence.
- Add failure cases for alert correlation, severity scoring, and AI-generated analyst summaries.

## Phase 8 — Research Reporting

For each challenge family, report:

- threat model,
- attack preconditions,
- success criteria,
- mitigation,
- limitations,
- reproducibility notes,
- and test coverage.

Never invent benchmark results. If an experiment has not been run, mark the result as unavailable.

## Long-Term Goal

The platform should demonstrate practical understanding of:

- LLM security,
- prompt injection,
- RAG security,
- agent authorization,
- adversarial ML,
- explainable AI limitations,
- AI SOC security,
- and secure AI application design.
