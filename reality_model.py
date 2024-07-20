from dataclasses import *
# import psutil
# import platform
# from datetime import datetime
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
    description: str|None = None
    about: str|None = None
    usage: str|None = None
    access: str|None = None # Waifu(specific waifu can do this)/Room(a waifu needs a furnish)/Global(anyone can do it)/Player(Only Player can do it)
    requirements: list|None = None  # For any dependencies

@dataclass
class Room: # A place where Waifu exist
    id: str = ""
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


# Unused for now
# @dataclass
# class HardwareInfo:
#     hostname: str = platform.node()
#     os: str = platform.system()
#     os_version: str = platform.version()
#     processor: str = platform.processor()
#     cpu_cores: int = psutil.cpu_count(logical=False)
#     cpu_threads: int = psutil.cpu_count(logical=True)
#     total_ram: int = psutil.virtual_memory().total
#     available_ram: int = psutil.virtual_memory().available
#     total_disk: int = psutil.disk_usage('/').total
#     free_disk: int = psutil.disk_usage('/').free
#     gpu_info: str = "N/A"  # You might need additional libraries for this
#     current_time: datetime = datetime.now()
#     uptime: float = psutil.boot_time()
#
#     def update_dynamic_info(self):
#         self.available_ram = psutil.virtual_memory().available
#         self.free_disk = psutil.disk_usage('/').free
#         self.current_time = datetime.now()
#
#     def get_cpu_usage(self) -> float:
#         return psutil.cpu_percent()
#
#     def get_ram_usage(self) -> float:
#         return psutil.virtual_memory().percent
#
#     def get_disk_usage(self) -> float:
#         return psutil.disk_usage('/').percent
#
#     def get_network_stats(self) -> dict:
#         net_io = psutil.net_io_counters()
#         return {
#             "bytes_sent": net_io.bytes_sent,
#             "bytes_recv": net_io.bytes_recv,
#             "packets_sent": net_io.packets_sent,
#             "packets_recv": net_io.packets_recv
#         }