

from os import environ

API_ID = int(environ.get("API_ID", "26271673"))
API_HASH = environ.get("API_HASH", "0e807111856890e4770b3e5a3324ec5f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8503412165:AAEQbSIzwTiHD1VYHfMXw2VUQI5rIag_l4w")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "FILE_STORE_2026_bot")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/FILE_STORE_2026_bot")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "820017857").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "820017857"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "6aqsMT1XqZVlgovU@cluster0.tihvbcy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")





