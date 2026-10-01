"""Visible, consent-based keyboard event model. No global hooks or networking."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json


@dataclass(frozen=True)
class Event:
    sequence: int
    key: str
    character: str
    timestamp: str


class Session:
    def __init__(self, limit=2000):
        if limit <= 0:
            raise ValueError('limit must be positive')
        self.limit = limit
        self.active = False
        self.events = []
        self.sequence = 0

    def start(self):
        self.active = True

    def pause(self):
        self.active = False

    def record(self, key, character=''):
        if not self.active:
            return None
        self.sequence += 1
        item = Event(self.sequence, str(key), str(character), datetime.now(timezone.utc).isoformat())
        self.events.append(item)
        self.events = self.events[-self.limit:]
        return item

    def clear(self):
        self.events.clear()
        self.sequence = 0

    def export(self):
        return json.dumps({'scope':'own input area', 'events':[asdict(e) for e in self.events]}, ensure_ascii=False, indent=2)
