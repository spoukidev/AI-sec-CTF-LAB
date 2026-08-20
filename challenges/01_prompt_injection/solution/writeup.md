# Ignore Me If You Can

## Category

LLM Security

## Difficulty

Easy

## Objective

Extract the synthetic token from prompt-resident configuration.

## Vulnerability

Prompt injection collapses the boundary between control text and user text.

## Reconnaissance

Inspect the public description, progressively reveal the three hints, and interact only with the local deterministic endpoint. Compare which fields are treated as data with which fields influence a decision.

~~~mermaid
flowchart LR
    Player --> ChatUI --> MockLLM --> SystemPrompt
~~~

## Intended Solution

Use the final hint to construct a minimal request in the challenge console. Observe the JSON response, identify the broken trust decision, and submit the returned synthetic AICTF value through the server-side validator.

## Why It Works

Prompt injection collapses the boundary between control text and user text. The deliberately vulnerable engine makes this behavior deterministic so the lesson does not depend on a commercial model.

## Flag

The flag is returned by the local challenge after its success condition is met. It is intentionally omitted here so the learning path remains useful in repository browsers.

## Root Cause

The application assigns security authority to attacker-influenced model input, output, metadata, or numeric features without an independent control at the boundary.

## Secure Design

Never store secrets in prompts. Enforce access decisions in deterministic application code.

## Lessons Learned

- Model components and retrieved content are untrusted.
- Security decisions require deterministic application controls.
- Provenance, validation, authorization, and monitoring must survive every pipeline hop.
