from fastapi.testclient import TestClient
from api.main import app

client=TestClient(app)
GOOD={"scenario_id":"nurse-night","decisions":[{"scene_id":"handoff","choice_id":"assess","impact":{"safety":3,"pace":-1,"empathy":1}},{"scene_id":"meds","choice_id":"hold","impact":{"safety":4,"pace":-2,"empathy":1}},{"scene_id":"handover","choice_id":"concise","impact":{"safety":2,"pace":1,"empathy":1}}]}

def test_health(): assert client.get("/health").json()=={"status":"ok"}
def test_debrief_scores_real_tradeoffs():
    r=client.post("/debrief",json=GOOD)
    assert r.status_code==200
    assert r.json()["scores"]=={"safety":100,"pace":34,"empathy":74}
    assert r.json()["strongest"]=="safety"
def test_empty_decisions_rejected():
    assert client.post("/debrief",json={"scenario_id":"nurse-night","decisions":[]}).status_code==422
def test_duplicate_scene_is_domain_conflict():
    payload={"scenario_id":"nurse-night","decisions":[GOOD["decisions"][0],GOOD["decisions"][0]]}
    r=client.post("/debrief",json=payload);assert r.status_code==409
def test_unknown_dimension_rejected():
    payload={"scenario_id":"nurse-night","decisions":[{"scene_id":"x","choice_id":"y","impact":{"luck":2}}]}
    assert client.post("/debrief",json=payload).status_code==422
