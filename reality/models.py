from dataclasses import *


@dataclass
class Reality: # Basically The Server The Waifu is Running On
    id: str = ""
    name: str|None = None
    description: str|None = None
    modules: list|None = None # Represents all the possible feature
    rooms: list|None = None # Represents All The Places a Waifu Can Exist
    rules: list|None = None  # For global settings

@dataclass
class Rule: # I'm really not sure how to implement this, I'll deal with it as time goes
    id: str = ""
    name: str|None = None
    description: str|None = None
    requirement: list|None = None

@dataclass
class Module: # A single feature that Waifu or a Furniture can help waifu to do.
    id: str = ""
    name : str = ""
    description: str|None = None
    about: str|None = None
    usage: str|None = None
    access: str|None = None # Waifu(specific waifu can do this)/Room(a waifu needs a furnish)/Global(anyone can do it)/Player(Only Player can do it)
    requirements: list|None = None  # For any dependencies

@dataclass
class Room: # A place where Waifu exist
    id: str = ""
    name : str = ""
    description: str|None = None
    detailed_description: str|None = None
    furnishings: list|None = None # List of items that can be interacted in 'room'
    render: str|None = None # An ID connected to something that will help with rendering everything
    capacity: int|None = None  # To limit number of waifus
    connected_rooms: list|None = None  # For navigation

@dataclass
class Furnish: # An item Waifu can interact
    id: str = ""
    name: str|None = None
    description: str|None = None
    detailed_description: str|None = None
    interaction: list|None = None
    render: str|None = None # An ID connected to something that will help with rendering everything
    status: str|None = None  # For on/off states

@dataclass
class Interaction:
    id: str = ""
    name: str|None = None
    description: str|None = None
    detailed_description: str|None = None
    module: str|None = None # Feature or something waifu can use to access thing, yknow, like in reality.
    requirements: list|None = None  # For preconditions