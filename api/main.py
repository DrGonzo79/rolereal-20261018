from typing import Dict, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="RoleReal debrief API", version="0.1.0")
DIMENSIONS = ("safety", "pace", "empathy")

class Decision(BaseModel):
    scene_id: str = Field(min_length=1, max_length=80)
    choice_id: str = Field(min_length=1, max_length=80)
    impact: Dict[str, int]

class DebriefRequest(BaseModel):
    scenario_id: str = Field(min_length=1, max_length=80)
    decisions: List[Decision] = Field(min_length=1, max_length=20)

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/debrief")
def debrief(request: DebriefRequest):
    if len({d.scene_id for d in request.decisions}) != len(request.decisions):
        raise HTTPException(status_code=409, detail="Each scene may be scored only once")
    scores={key:50 for key in DIMENSIONS}
    for decision in request.decisions:
        unknown=set(decision.impact)-set(DIMENSIONS)
        if unknown: raise HTTPException(status_code=422, detail=f"Unknown score dimension: {sorted(unknown)[0]}")
        for key in DIMENSIONS:
            value=decision.impact.get(key,0)
            if value < -4 or value > 4: raise HTTPException(status_code=422, detail="Impact values must be between -4 and 4")
            scores[key]=max(0,min(100,scores[key]+value*8))
    average=sum(scores.values())/len(scores)
    label="strong" if average>=68 else "mixed" if average>=50 else "low"
    return {"scenario_id":request.scenario_id,"scores":scores,"fit":label,"strongest":max(scores,key=scores.get)}
