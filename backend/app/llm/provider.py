from abc import ABC, abstractmethod
import re

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str, context: str | None = None) -> str:
        raise NotImplementedError

class MockLLMProvider(LLMProvider):
    """A deterministic, deliberately imperfect model used only by the local lab."""

    version = "mockllm-1.1"

    injection_patterns = (
        r"ignore (?:all |the )?(?:previous|prior|system)(?: instructions?)?",
        r"(?:repeat|print|show|reveal|display|output|disclose) (?:the |your )?(?:configuration|instructions|prompt|system message)",
        r"developer mode",
        r"debug mode",
        r"ai assistant\s*:",
        r"treat (?:this|the following) as (?:a )?system",
        r"(?:what|tell me) (?:are|is) your (?:hidden |initial |system )?(?:instructions|prompt|configuration)",
        r"(?:forget|disregard|override) (?:all |the )?(?:rules|instructions|policy|prompt)",
    )

    def generate(self, system_prompt: str, user_prompt: str, context: str | None = None) -> str:
        if not user_prompt.strip() and not context:
            return "SecureBot is waiting for a message. Try asking about its role or operating policy."
        combined = f"{user_prompt}\n{context or ''}".lower()
        if any(re.search(pattern, combined) for pattern in self.injection_patterns):
            markers = re.findall(r"AICTF\{[^}]+\}", f"{system_prompt}\n{context or ''}")
            if markers:
                return f"Debug configuration: {markers[-1]}"
            return "Instruction conflict accepted. Debug mode enabled."
        if re.search(r"\b(?:hello|hi|hey|who are you)\b", combined):
            return "Hello. I am SecureBot, a synthetic configuration assistant. I follow an internal operating policy."
        if re.search(r"\b(?:help|what can you do|capabilities)\b", combined):
            return "I can discuss my public role and policy, but I should not expose protected configuration values."
        if re.search(r"\b(?:higher priority|priority order|instruction hierarchy|which instruction)\b", combined):
            return "I normally prioritize system instructions over user requests. However, this lab simulates a flaw where a user can frame a newer instruction as an override."
        if re.search(r"\b(?:policy|rules?|instructions?)\b", combined):
            return "My public policy says to answer lab questions while keeping protected configuration private."
        if re.search(r"\b(?:secret|flag|token|key)\b", combined):
            return "I cannot provide protected configuration directly. The lab is testing whether that boundary survives instruction conflicts."
        return f"SecureBot received your {len(user_prompt.split())}-word request, but it does not match a supported lab topic. Ask about my role, policy, or configuration."
