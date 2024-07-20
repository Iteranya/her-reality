# This is where I define the Data Class for the Waifus
# This will contain the structure of all the things a waifu is
# This all exists above the reality_model, this will be handled by the "Front End", not the server.

from dataclasses import *

@dataclass
class Player:
    id:str = ""
    name: str|None =None
    desc: str|None =None
    materials:list|None =None
    creature:list|None =None # Owned Creatures NAME
    waifus:list|None =None  # Owned Waifus UUID

@dataclass
class Action:
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
    # Stage 2 Generation (The Randomly Generated Stuff, separated because might use tags)
    face: str | None = None
    body: str | None = None
    clothing: str | None = None
    ero: str | None = None
    # Stage 3 Generation (Even More Randomly Generated Stuff, separated because archetype)
    archetype:list[str]|None=None
    personality:str|None=None
    quirk:str|None=None
    fetish:str|None=None # I have a chance to turn this from my first game to my first eroge. Of course I'm doing it.
    # Stage 4 Generation (Planned Feature)
    avatar_picture: str|None = None
    full_picture:str|None = None
    # Misc Stuff
    gifts:list[str]|None=None # Stuff you've given to your waifu
    affection: int=0 # How much your waifu loves you
    lewd: int=0 # How lewd your waifu is (Again, this is an eroge, I don't care)

    # Also, I can slap this to RenPy if I want
    # That could be pretty interesting, Steam Worthy I say!