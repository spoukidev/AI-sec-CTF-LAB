"""Thin challenge marker; behavior is implemented by the shared deterministic engine."""
CHALLENGE_DIRECTORY = "09_tool_trust"

def safety_capabilities() -> dict[str, bool]:
    return {"network": False, "shell": False, "real_secrets": False, "synthetic_only": True}
