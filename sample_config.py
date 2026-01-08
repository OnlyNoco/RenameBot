import os, random
import base64
import logging 
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "0")
API_ID = int(os.environ.get("API_ID", "26254064"))
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")
WORKER = int(os.environ.get("WORKER", "4"))
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067"))
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URL", "#db url here")
DB_NAME = os.environ.get("DB_NAME", "JOINREQ") 
DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
START_MSG = os.environ.get(
    "START_MSG",
    "<blockquote>Hello {mention}</blockquote>\n\n"
    "<b>I watch all that I am permitted to see. "
    "With the right access, I let anyone join private channels instantly. "
    "Add me as admin, and you can rely on me.</b>"
)
ABOUT_MSG = """
<b>›› ᴀʙᴏᴜᴛ ᴍᴇ:</b>
◧ ᴏᴡɴᴇʀ: <a href='https://t.me/OnlyNoco'>ᴏɴʟʏɴᴏᴄᴏ</a>
◧ ᴘᴏʀᴛғᴏʟɪᴏ: <a href='https://onlynoco.vercel.app'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>
◧ ʀᴇᴘᴏ: <a href='https://github.com/OnlyNoco/Auto-Request-Accept-Bot'>ɢɪᴛʜᴜʙ</a>
◧ ʟɪʙs ~ <a href='https://github.com/Mayuri-Chan/pyrofork'>ᴘʏʀᴏғᴏʀᴋ</a> • <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ</a> • <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏᴅʙ</a>

◧ ᴏᴜʀ sᴇʀᴠɪᴄᴇs ~
⊡ <a href='https://t.me/+O7PeEMZOAoMzYzVl'>ʜᴇɴᴛᴀɪ ᴄʀɪsᴘ</a>
⊡ <a href='https://t.me/HeavenlySubs'>ʙᴀᴛᴛʟᴇ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʜᴇᴀᴠᴇɴs</a>
⊡ <a href='https://t.me/CrispAnime'>ᴄʀɪsᴘ ᴀɴɪᴍᴇ</a>
"""
CMD_MSG = os.environ.get("CMD_MSG", "<blockquote>/start - to check bot alive or dead!\n/help - to get help from bot usuages\n/report - to report issue to admin\nSend or Forward anything i will broadcast it to all users.")
START_PIC = os.environ.get("START_PIC", "https://envs.sh/bjb.mp4 https://envs.sh/bjP.mp4 https://envs.sh/bjw.mp4 https://envs.sh/bj0.mp4 https://envs.sh/bjS.mp4 https://envs.sh/bjW.mp4 https://envs.sh/bjB.mp4 https://envs.sh/bjI.mp4 https://envs.sh/bjn.mp4 https://envs.sh/bjT.mp4 https://envs.sh/bjZ.mp4 https://envs.sh/bjL.mp4 https://envs.sh/bj5.mp4 https://envs.sh/bjY.mp4 https://envs.sh/bjC.mp4").split(" ")
#FLOOD_WAIT = int(os.environ.get("FLOOD_WAIT", "10")) # in seconds 
#BROADCAST_DELETE_TIME = int(os.environ.get("BROADCAST_DELETE_TIMED", "1800")) # IN SECONDS AND TRY NOT TO USE BIG TIME LIKE 1 YEAR OR MONTHS OR MANY DAYS (CURRENTLY SET TO 30 MINUTES)

# LOGGER SETUP
LOG_FILE_NAME = "onlynoco.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
loggiing = "LTEwMDIxOTcyNzk1NDI="
