# Contributing challenges

Each challenge belongs in `challenges/<number>_<slug>` and includes `challenge.yaml`, `README.md`, `app/`, `tests/`, `solution/`, and `solution/writeup.md`. Metadata must include three progressive hints, learning objectives, a synthetic `AICTF{...}` flag, and a unique Docker service name.

Challenge behavior must be deterministic. Never add outbound networking, system-command tools, real credentials, destructive actions, or access outside a challenge directory. Add engine tests and document both the vulnerable trust boundary and secure application-side remediation.
