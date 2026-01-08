from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
from bot import Bot
import os

@Client.on_message(filters.photo & filters.private)
async def set_thumbnail(client: Client, message: Message):
    try:
        os.makedirs("thumbnails", exist_ok=True)
        thumb_path = f"thumbnails/{message.from_user.id}.jpg"
        await message.download(file_name=thumb_path)
        if os.path.exists(thumb_path):
            await message.reply_text("ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ :)",)
        else:
            await message.reply_text("ꜱᴏʀʀʏ, ғᴀɪʟᴇᴅ ᴛᴏ ꜱᴀᴠᴇ ᴛʜᴜᴍʙɴᴀɪʟ. ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ.")
    except Exception as e:
        await message.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ: {e}")