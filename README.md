# AI Security CTF Lab

A local-only, deliberately vulnerable training platform for prompt injection, RAG, agent security, adversarial ML, explainability, and AI SOC failure modes.

## Quick start

```bash
docker compose up --build
```

Open `http://localhost:5173`. The API is available at `http://localhost:8000/docs`.

No paid model or internet-facing target is used. The default provider is deterministic and all data, tools, users, alerts, and flags are synthetic.

## Local development

Backend:

```bash
cd backend
python -m venv .venv
.venv/Scripts/pip install -e ".[dev]"
.venv/Scripts/pytest
.venv/Scripts/uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Safety model

- Challenge services bind to localhost through Docker Compose.
- The agent has no shell, network, credential, persistence, or destructive tools.
- File-like content is held in an in-memory synthetic corpus.
- Flags are loaded server-side from challenge metadata and never shipped in frontend source.
- Resetting the backend deletes only the local SQLite progress database.

See [SECURITY.md](SECURITY.md) for boundaries and [CONTRIBUTING.md](CONTRIBUTING.md) for authoring guidance.
