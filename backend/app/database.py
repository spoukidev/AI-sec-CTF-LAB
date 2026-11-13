from datetime import datetime
from sqlalchemy import DateTime, Integer, String, UniqueConstraint, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.pool import StaticPool
from .config import DATABASE_URL

class Base(DeclarativeBase):
    pass

class Solve(Base):
    __tablename__ = "solves"
    __table_args__ = (
        UniqueConstraint("player", "challenge_id", name="uq_solve_player_challenge"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player: Mapped[str] = mapped_column(String(40), index=True)
    challenge_id: Mapped[str] = mapped_column(String(80), index=True)
    solved_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

connect_args = {}
engine_kwargs = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False
    # :memory: databases are discarded when a connection closes. StaticPool
    # keeps one connection for the process so init_db() and later sessions
    # share the same tables (needed by the test suite).
    if ":memory:" in DATABASE_URL:
        engine_kwargs["poolclass"] = StaticPool
engine = create_engine(DATABASE_URL, connect_args=connect_args, **engine_kwargs)
SessionLocal = sessionmaker(bind=engine)

def init_db() -> None:
    Base.metadata.create_all(engine)
