"""Thin challenge marker; behavior is implemented by the shared deterministic engine."""
CHALLENGE_DIRECTORY = "01_prompt_injection"

def safety_capabilities() -> dict[str, bool]:
    return {"network": False, "shell": False, "real_secrets": False, "synthetic_only": True}
