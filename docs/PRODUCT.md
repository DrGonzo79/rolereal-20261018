# Product plan

## ICP, JTBD, and MVP

Primary ICP: US adult career changers actively considering nursing school within 90 days. JTBD: “Before I spend tuition and rearrange my life, let me feel the job’s recurring trade-offs and know what to investigate in person.” Secondary buyer after proof: CTE coordinator needing scalable work-based exploration.

MVP is one RN-reviewed, signed nursing week; branching decisions; immediate consequence explanations; transparent debrief; accuracy/version note; $49 practitioner-debrief checkout test. Explicitly excluded: predictive fit, clinical instruction, 50-role library, school SSO, employer recruiting, and generative scenario publishing.

## Data and architecture

Entities: Practitioner, Scenario, Scene, Choice, Impact, Attempt, Decision, Debrief, ContentVersion, Consent, ValidationEvent. This demo uses shared JSON fixtures, deterministic TypeScript client scoring, and the same contract in a tested FastAPI `/debrief` operation. Production adds Postgres, signed content versions, anonymous attempt IDs, explicit consent, and event analytics. No model is needed for scoring. AI may draft scenes only behind practitioner approval, provenance, and safety review.

## Economics and validation

Start at $49 per kit; pay the practitioner $500 minimum plus 30% net kit revenue during validation. The report’s $5–$12/student school pricing becomes relevant only after learner completion and trust are proven. Track start→completion, decision dwell, debrief usefulness, RN accuracy rating, $49 checkout conversion, refund requests, and school-pilot LOIs. Pass: 30 observed prospects, ≥60% completion, ≥10% paid/deposit conversion, zero material accuracy objections after revision, and two counselor pilot conversations. Kill or reframe if fewer than three payments from 30 qualified prospects.

## Moat and roadmap

The only plausible moat is trusted supply: named practitioners, consented/versioned scenarios, observed outcome data, and school workflow—not branching UI. Days 0–30: one nursing simulation, 3 RN reviews, 30 observed users, price test. Days 31–60: revise, add debrief booking, author workflow prototype, one counselor pilot. Days 61–90: second nursing setting only if thresholds pass; export evidence for Perkins/work-based-learning reporting. Do not expand careers before the wedge clears.
