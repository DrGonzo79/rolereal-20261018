# RoleReal

A runnable prototype of an “honest week in the job”: students make pressure decisions inside a fictional nursing shift, see immediate trade-off feedback, and receive a transparent debrief. It is a product demo, not career or clinical advice.

## Run

```bash
npm ci
npm run typecheck && npm run test:e2e && npm run build
uv sync --project api --locked
uv run --project api pytest api/tests
uv run --project api uvicorn api.main:app --reload
```

The GitHub Pages deployment is frontend-only. The FastAPI service is tested source and is **not deployed**.

## What works

- Three-decision nursing-night-shift simulation with visible consequences
- Deterministic safety/pace/empathy debrief and restart flow
- Career switcher with honest unavailable state
- FastAPI scoring with validation, duplicate-scene conflict, and error tests
- Static export under repository base path, responsive mobile layout, CI/Pages workflow

## Evidence and limits

Fixtures are explicitly fictional composites. No claim is made that the scores predict career success. A production pilot requires named practitioner review, student safety review, consent/versioning, and observed sessions.

See [research](research/notes.md), [product plan](docs/PRODUCT.md), [architecture](docs/ARCHITECTURE.md), [review](docs/CEO_REVIEW.md), and [opportunity score](docs/OPPORTUNITY_SCORE.md).
