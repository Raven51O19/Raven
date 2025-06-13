# Managing Conversation Context

To accurately recall previous exchanges while keeping memory use low, persist
conversation history to disk and load only the portions you need. The provided
`conversation_history.py` helper demonstrates one approach.

## Usage Example

```python
from conversation_history import ConversationHistory

history = ConversationHistory("history.json")
history.add_message("user", "Hello")
history.add_message("assistant", "Hi! How can I help?")
recent = history.get_recent()
```

Periodically prune the log to limit its size:

```python
history.prune_history(max_messages=100)
```

This keeps the most recent interactions while discarding older ones from memory.
