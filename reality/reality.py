from models import *
import data_manager
import uuid


def create_reality(name, description):
    try:
        init = Reality(
            id=str(uuid.uuid4()),
            name = name,
            description = description,
        )
        data_manager.save_reality(init)
        return "Created A New Reality!"
    except Exception as e:
        return f"Error: {e}"

def create_room(name, description, reality_id):
    try:
        init = Room(
            id = str(uuid.uuid4()),
            name = name,
            description = description
        )
        data_manager.save_room(init)
        reality = data_manager.get_reality(reality_id)

        if not isinstance(reality.rooms,list):
            reality.rooms = [init.id]
        else:
            reality.rooms.append(init.id)
        data_manager.update_reality(reality)
        return f"{init.name} have been constructed inside {reality.name}"
    except Exception as e:
        return f"Error: {e}"


def add_furnishing(furnish:Furnish, room_id:str):
    try:
        furnish.id = str(uuid.uuid4())
        data_manager.save_furnish(furnish)
        room = data_manager.get_room(room_id)
        if not isinstance(room.furnishings, list):
            room.furnishings = [furnish.id]
        else:
            room.furnishings.append(furnish.id)
        data_manager.update_room(room)
        return f"Added {furnish.name} into {room.name}"
    except Exception as e:
        return f"Error: {e}"


