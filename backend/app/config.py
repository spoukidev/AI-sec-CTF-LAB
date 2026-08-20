from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[2]
CHALLENGES_DIR = Path(os.getenv("AICTF_CHALLENGES_DIR", ROOT / "challenges"))
DATABASE_URL = os.getenv("AICTF_DATABASE_URL", f"sqlite:///{ROOT / 'aictf.db'}")
