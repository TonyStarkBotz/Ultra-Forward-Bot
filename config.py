# TonyStarkBotz 
# Don't Remove Credit 🥺
# Telegram Channel @TonyStark_Botz



import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "TonyStarkbotz")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '').split()]
    

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# TonyStarkBotz 
# Don't Remove Credit 🥺
# Telegram Channel @TonyStark_Botz