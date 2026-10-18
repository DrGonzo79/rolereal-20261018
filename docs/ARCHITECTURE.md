# Architecture

```text
demo_scenarios.json ──> Next.js static UI ──> local attempt state ──> debrief
          │                    │
          └──────────── contract mirror ─────┐
                                             v
                                  FastAPI /debrief (source only)
                                             │
                                      validation + scoring
```

GitHub Pages serves the static export under `/rolereal-20261018`. The demo never calls an unavailable backend; FastAPI proves the domain operation independently and is not deployed. Static data makes the experience reproducible and honest about simulation.

Failure paths: missing scenario renders no hidden fallback (build/type checks catch malformed imports); unavailable second scenario shows a clear review state; a choice locks after selection to prevent double scoring; restart clears all attempt state; API rejects empty decisions (422), duplicate scenes (409), unknown dimensions (422), and out-of-range impacts (422). Production requires authenticated authoring, immutable content versions, rate limits, audit logs, deletion policy, error metrics, completion funnel, and alerts on score/fixture version mismatch.

At 10×, CDN static delivery remains cheap and API scoring is stateless. At 100×, attempts/events move to queued analytics and partitioned storage; scenario reads remain cached by content version. Student identity is unnecessary for the first experiment and should not be collected.
