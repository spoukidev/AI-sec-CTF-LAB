from pathlib import Path
import yaml

def test_metadata_contract():
    root = Path(__file__).parents[1]
    data = yaml.safe_load((root / "challenge.yaml").read_text(encoding="utf-8"))
    assert set(("id","name","category","difficulty","points","description","objective","flag","hints","learning_objectives","ports","docker_service")) <= data.keys()
    assert data["flag"].startswith("AICTF{") and data["flag"].endswith("}")
    assert len(data["hints"]) == 3
    assert (root / "solution" / "writeup.md").exists()
