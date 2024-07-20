# This is where I define the Data Class for the Waifus
# This will contain the structure of all the things a waifu is
# This all exists above the reality_model, this will be handled by the "Front End", not the server.

from dataclasses import *

@dataclass
class Action: # Used Either with AI or Coded Directly
    id:str = ""
    name: str|None=None
    trigger: str|None=None
    type: str|None=None
    arguments: str|None=None

@dataclass
class Waifu:
    id: str = ""
    name: str|None =None
    nickname: str|None =None
    desc: str | None = None
    appearance: str | None = None
    clothing: list | None = None
    face: str | None = None
    body: str | None = None
    erogenous_zones: str | None = None
    personality:str|None=None
    quirk:str|None=None
    fetish:str|None=None
    avatar_picture: str|None = None
    full_picture:str|None = None
    affection: int=0
    lewdness: int=0
    actions: list | None = None

    # Also, I can slap this to RenPy if I want
    # That could be pretty interesting, Steam Worthy I say!