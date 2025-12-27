from pymongo import MongoClient
import config

SonaOp = MongoClient(config.MONGO_URL)
Sonali = SonaOp["Sona"]["Raja"]

from .chats_db import *
from .users_db import *
from .admin import *
from .sonali import *
from .chat_toggle import *
