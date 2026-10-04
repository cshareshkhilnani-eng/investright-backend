from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "InvestRight API"}

@app.get("/api/risk-profile/assess")
def assess(age: int, income_stability: int, emergency_fund: int, liabilities: int, crash_reaction: int, experience: int, checking_frequency: int):
    c = max(0, min(30, (60 - age) * 0.5)) + income_stability * 0.25 + emergency_fund * 0.25 + (100 - liabilities) * 0.2
    t = crash_reaction * 0.35 + experience * 0.30 + (100 - checking_frequency) * 0.30
    score = min(c, t)
    if score <= 40: level = "Conservative"
    elif score <= 70: level = "Balanced"
    else: level = "Aggressive"
    return {"risk_capacity": int(c), "risk_tolerance": int(t), "profile_level": level}