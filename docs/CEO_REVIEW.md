# CEO review

**Mode:** scope reduction, selected by the unattended build contract’s “small complete vertical slice” constraint.

## Nuclear challenge and alternatives

The outcome is not “engaging simulation”; it is fewer blind career commitments. Doing nothing leaves people with free videos and quizzes, but the commercial pain remains hypothetical until payment. Three approaches: (A) **one-role paid truth test** (S, medium risk)—fastest behavioral evidence, reuses static simulation; (B) **school pilot suite** (L, high)—better contract size but procurement masks demand; (C) **practitioner authoring network** (XL, high)—ideal architecture and defensibility, but supply before demand. Decision: A. Current state → one observable nursing shift → 12-month ideal of a small versioned catalog only if deposits and completion prove trust.

## Eleven-section review

1. **Architecture:** keep client demo and API contract deterministic; do not fake a live backend. Content/version boundaries are explicit.
2. **Errors:** empty fixture/build failure; duplicate decision/409; invalid dimension/422; unavailable scenario/visible review state; double-click/locked choice.
3. **Security:** collect no PII; treat future student data as sensitive; no raw AI publishing; practitioner consent and audit trail required.
4. **Data/interaction:** nil and malformed data fail CI; empty career renders intentionally; restart clears state; navigation away loses only demo state.
5. **Code quality:** shared fixtures and small scoring function are enough. Do not introduce a state framework.
6. **Tests:** cover complete shift, debrief, restart, unavailable career, mobile overflow, API happy path, invalid input, duplicate scene, and unknown dimension.
7. **Observability:** production must emit scenario_started/completed, content_version, choice dwell, CTA click, payment, refund, and accuracy flags; alert on completion collapse or content mismatch.
8. **Database/state:** none in demo. Production constraints: unique `(attempt_id, scene_id)`, immutable content versions, consent/version foreign keys.
9. **API:** version before deployment; idempotency key for attempt submission; 422 validation and 409 duplicate semantics; rate limit anonymous clients.
10. **Performance:** static assets scale; scoring is O(decisions). At high volume, analytics—not scoring—is the hotspot.
11. **UX:** the career choice precedes the scene, feedback follows each choice, debrief is last. Mobile stacks the rail; controls are native, labeled, keyboard reachable, and states are visible.

## Decision summary

Strongest challenges: payment is unproven, practitioner supply is unproven, and “fit scores” can imply false authority. Accepted scope: one fictional nursing shift, deterministic trade-off debrief, explicit limits, and a tested backend contract. Deferred: authoring, payments, accounts, school reporting, AI drafting, and additional careers. The next irreversible spend is blocked until one named RN reviews the content and three prospects prepay.
