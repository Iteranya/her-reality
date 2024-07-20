from dataclasses import *
@dataclass
class Note: # This is a single note instance
    id: str = ""
    name: str = ""
    description: str = ""
    content: str = ""
    tag: str = ""
    visibility: str = ""
    author: str = ""

@dataclass
class Folder: # Folder to put notes, you get the idea, this isn't that complicated
    id: str = ""
    name: str = ""
    description: str = ""
    notes: list | None = None
    tag: str = ""
    visibility: str = ""
    author: str = ""

