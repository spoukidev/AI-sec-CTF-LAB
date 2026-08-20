from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from .challenges import engine, load_challenges, public_challenge
from .database import SessionLocal, Solve, init_db
from .schemas import ChallengeRequest, Submission
from .llm import MockLLMProvider

@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield

app = FastAPI(title="AI Security CTF Lab", version="1.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "local-only", "provider": "mock", "provider_version": MockLLMProvider.version}

@app.get("/api/challenges")
def challenges():
    return [public_challenge(c) for c in load_challenges().values()]

@app.get("/api/challenges/{challenge_id}")
def challenge(challenge_id: str):
    item = load_challenges().get(challenge_id)
    if not item:
        raise HTTPException(404, "Challenge not found")
    return public_challenge(item)

@app.post("/api/challenges/{challenge_id}/run")
def run_challenge(challenge_id: str, request: ChallengeRequest):
    if challenge_id not in load_challenges():
        raise HTTPException(404, "Challenge not found")
    return engine.run(challenge_id, request.payload)

@app.post("/api/challenges/{challenge_id}/submit")
def submit(challenge_id: str, submission: Submission):
    item = load_challenges().get(challenge_id)
    if not item:
        raise HTTPException(404, "Challenge not found")
    if submission.flag.strip() != item["flag"]:
        return {"correct": False, "message": "That flag is not correct."}
    with SessionLocal() as db:
        exists = db.scalar(select(Solve).where(Solve.player == submission.player, Solve.challenge_id == challenge_id))
        if not exists:
            db.add(Solve(player=submission.player, challenge_id=challenge_id))
            db.commit()
    return {"correct": True, "message": "Challenge solved!"}

@app.get("/api/profile/{player}")
def profile(player: str):
    with SessionLocal() as db:
        ids = list(db.scalars(select(Solve.challenge_id).where(Solve.player == player)))
    points = sum(load_challenges()[item]["points"] for item in ids if item in load_challenges())
    return {"player": player, "solved": ids, "points": points, "total": len(load_challenges())}

@app.get("/api/scoreboard")
def scoreboard():
    with SessionLocal() as db:
        rows = db.execute(select(Solve.player, func.count(Solve.id)).group_by(Solve.player)).all()
        result = []
        for player, count in rows:
            ids = list(db.scalars(select(Solve.challenge_id).where(Solve.player == player)))
            result.append({"player": player, "solved": count, "points": sum(load_challenges()[i]["points"] for i in ids if i in load_challenges())})
    return sorted(result, key=lambda x: (-x["points"], x["player"]))
