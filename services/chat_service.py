from pathlib import Path

from llm.ollama_client import get_llm
from services.memory_service import get_session_history

_llm = get_llm()
_prompt_path = Path(__file__).resolve().parents[1] / "prompt.txt"
_instructions = _prompt_path.read_text(encoding="utf-8").strip()


def generate_reply(session_id: str, input_text: str) -> str:
    history = get_session_history(session_id)
    history.append({"role": "user", "content": input_text})

    messages = [
        {"role": "system", "content": _instructions},
    ] + history[-6:]

    response = _llm.invoke(messages)
    history.append({"role": "assistant", "content": response.content})
    return response.content
