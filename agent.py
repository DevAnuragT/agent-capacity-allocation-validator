"""Validate assignment totals against named resource capacities."""
import math
def _n(v,n):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(float(v)) or float(v)<0 or float(v)>1e12: raise ValueError(n+" must be bounded and nonnegative")
    return float(v)
def analyze(payload:dict)->dict:
    if not isinstance(payload,dict) or not isinstance(payload.get("resources"),dict) or not isinstance(payload.get("assignments"),list): raise ValueError("resources and assignments are required")
    resources={}
    for name,cap in payload["resources"].items():
        if not isinstance(name,str) or not name.strip(): raise ValueError("resource names must be strings")
        resources[name]=_n(cap,"capacity")
    totals={k:0.0 for k in resources}; seen=set(); details=[]
    for a in payload["assignments"]:
        if not isinstance(a,dict) or set(a)!={"id","resource","amount"}: raise ValueError("invalid assignment shape")
        if not isinstance(a["id"],str) or not a["id"].strip() or a["id"] in seen: raise ValueError("assignment IDs must be unique")
        if a["resource"] not in resources: raise ValueError("assignment references unknown resource")
        seen.add(a["id"]); amount=_n(a["amount"],"amount"); totals[a["resource"]]+=amount
        details.append({"id":a["id"],"resource":a["resource"],"amount":amount})
    over=[k for k in resources if totals[k]>resources[k]]
    return {"status":"overallocated" if over else "within_capacity","overallocated_resources":over,"resources":[{"name":k,"capacity":resources[k],"allocated":totals[k],"remaining":resources[k]-totals[k],"over":k in over} for k in resources],"assignments":details,"basis":"sum assignment amounts by exact resource name"}
