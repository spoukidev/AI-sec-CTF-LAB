# Lab safety and responsible use

This repository is an intentionally vulnerable educational environment for AI-security and cybersecurity training. Run it only on systems you own or are explicitly authorized to test.

## Containment boundary

The challenge environment is designed around synthetic data and local services. Challenge implementations should:

- bind exposed Docker services to `127.0.0.1` by default;
- avoid scanning, probing, or contacting third-party systems;
- use synthetic flags, users, documents, alerts, credentials, and security events;
- avoid shell or operating-system command execution controlled by model output;
- keep challenge file access inside the challenge's own working directory;
- avoid requiring real API keys, cloud credentials, or production accounts;
- provide deterministic/mock AI behavior by default so exercises remain reproducible.

The main CTF platform must remain separated from intentionally vulnerable challenge services. A vulnerability that escapes a challenge container or compromises the platform itself is not an intended solution path.

## AI-specific trust boundaries

Challenges may intentionally demonstrate failures such as prompt injection, poisoned retrieval context, unsafe tool authorization, unvalidated model output, adversarial ML, or misleading explanations. These weaknesses must operate only on local synthetic resources.

The lab should reinforce that an LLM is not an authorization boundary: permissions, validation, file restrictions, and tool access must be enforced by deterministic application logic outside the model.

## Responsible use

Do not adapt the exercises, payloads, or challenge logic to attack third-party targets or systems without authorization. Do not place real secrets or personal data into challenge fixtures.

If you discover a defect that breaks the intended containment boundary—for example unintended external network access, host-file access, secret exposure, or arbitrary command execution—do not publish exploitation details in a public issue. Report the problem privately to the repository owner with the affected challenge, reproduction conditions, and expected containment behavior.

## Before adding a challenge

Challenge authors should verify that:

1. all targets and data are synthetic or locally controlled;
2. the intended solution is documented and testable;
3. reset behavior removes attacker-controlled challenge state;
4. external network access is unnecessary for solving the challenge;
5. flags are validated server-side and are not exposed in frontend bundles;
6. the challenge cannot access secrets belonging to the host or main platform;
7. tests cover both the intended exploit path and the expected containment boundary.
