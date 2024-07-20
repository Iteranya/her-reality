from dataclasses import *


@dataclass
class Reminder:
    id: str | None = None
    name: str | None = None
    description: str|None = None
    content: str | None = None
    due_date: int| None = None
    remind_date : int | None = None
    repeat: bool | None = None  # Repeat
    priority: int | None = None  # 1-5, 5 being highest
    completed: bool | None = None
    tags: list | None = None

@dataclass
class Schedule:
    reminders: list | None = None