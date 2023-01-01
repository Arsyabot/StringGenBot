import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = os.getenv("API_ID", "16179045").strip()
API_HASH = os.getenv("API_HASH", "dc99c86a0b38365fd6c8b35ae9c577b9").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "5102922761:AAHlV5I94TKE52ixf2vHrZ7W59lLcXyEMJw").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "ruangdiskusikami")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
