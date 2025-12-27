from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "14050586"))
API_HASH = getenv("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7473021518"))
SUPPORT_GRP = getenv("SUPPORT_GRP", "odsnetwork")
UPDATE_CHNL = getenv("UPDATE_CHNL", "iamvillain77")
START_LOGGER = int(getenv("START_LOGGER", "-1002029289902"))
EVENTS_LOGGER = int(getenv("EVENTS_LOGGER", "-1002029289902"))


IMG = [
    "https://files.catbox.moe/6qzh5y.jpg",
    "https://files.catbox.moe/9fqgen.jpg",
    "https://files.catbox.moe/et8fz6.jpg",
    "https://files.catbox.moe/ow4v71.jpg",
    "https://files.catbox.moe/nqzk5h.jpg"
]
