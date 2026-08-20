from datetime import datetime
from sqlalchemy import DateTime, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from .config import DATABASE_URL

class Base(DeclarativeBase):
    pass

class Solve(Base):
    __tablename__ = "solves"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player: Mapped[str] = mapped_column(String(40), index=True)
    challenge_id: Mapped[str] = mapped_column(String(80), index=True)
    solved_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine)

def init_db() -> None:
    Base.metadata.create_all(engine)
