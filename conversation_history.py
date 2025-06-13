import json
from typing import List, Dict

class ConversationHistory:
    """Store and retrieve conversation exchanges on disk."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.history: List[Dict[str, str]] = self._load()

    def _load(self) -> List[Dict[str, str]]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_message(self, role: str, content: str) -> None:
        self.history.append({"role": role, "content": content})
        self._save()

    def get_recent(self, limit: int = 10) -> List[Dict[str, str]]:
        """Return the most recent conversation turns."""
        return self.history[-limit:]

    def prune_history(self, max_messages: int) -> None:
        """Keep only the latest `max_messages` turns."""
        if len(self.history) > max_messages:
            self.history = self.history[-max_messages:]
            self._save()

    def _save(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
