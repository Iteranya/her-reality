import tinydb
from tinydb import TinyDB
from dataclasses import asdict

# Initialize the database
db = TinyDB('waifu_world.json')

# Create tables for each class
reality_table = db.table('reality')
rule_table = db.table('rules')
module_table = db.table('modules')
room_table = db.table('rooms')
furnish_table = db.table('furnishings')
interaction_table = db.table('interactions')

def save_to_db(item, table):
    """Generic function to save an item to a specified table"""
    table.insert(asdict(item))

def get_from_db(item_id, table):
    """Generic function to retrieve an item from a specified table"""
    Query = tinydb.Query()
    return table.get(Query.id == item_id)

def update_in_db(item, table):
    """Generic function to update an item in a specified table"""
    Query = tinydb.Query()
    table.update(asdict(item), Query.id == item.id)

def delete_from_db(item_id, table):
    """Generic function to delete an item from a specified table"""
    Query = tinydb.Query()
    table.remove(Query.id == item_id)

# Specific functions for each class
def save_reality(reality):
    save_to_db(reality, reality_table)

def get_reality(reality_id):
    return get_from_db(reality_id, reality_table)

def update_reality(reality):
    return update_in_db(reality, reality_table)

def save_rule(rule):
    save_to_db(rule, rule_table)

def get_rule(rule_id):
    return get_from_db(rule_id, rule_table)

def save_module(module):
    save_to_db(module, module_table)

def get_module(module_id):
    return get_from_db(module_id, module_table)

def save_room(room):
    save_to_db(room, room_table)

def get_room(room_id):
    return get_from_db(room_id, room_table)

def update_room(room):
    return update_in_db(room, room_table)

def save_furnish(furnish):
    save_to_db(furnish, furnish_table)

def get_furnish(furnish_id):
    return get_from_db(furnish_id, furnish_table)

def save_interaction(interaction):
    save_to_db(interaction, interaction_table)

def get_interaction(interaction_id):
    return get_from_db(interaction_id, interaction_table)
