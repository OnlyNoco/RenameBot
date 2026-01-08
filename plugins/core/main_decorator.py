import os
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ForceReply, CallbackQuery
from bot import Bot
from plugins.core.progressbar import progress_bar
from config import DOWNLOAD_DIR, LOGGER
from plugins.core.cleanup import cleanup_downloads 
from PIL import Image

user_data = {}



# --- 1. Main file handler ---
@Client.on_message(filters.video | filters.document)
async def main_decorator(client: Client, message: Message):
    try:

        thumb_path = f"thumbnails/{message.from_user.id}.jpg"
        if not os.path.exists(thumb_path):
            await message.reply_text(
                "ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ꜱᴇᴛ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ ʏᴇᴛ.\nSend an image in private and I will save it."
            )
            return

        # Store basic user state
        user_data[message.from_user.id] = {"file_msg_id": message.id}

        # Ask for filename
        reply_msg = await client.send_message(
            chat_id=message.chat.id,
            text="ᴘʟᴇᴀꜱᴇ ꜱᴇɴᴅ filename without extension as a reply",
            reply_markup=ForceReply(selective=True)
        )
        user_data[message.from_user.id]["reply_msg_id"] = reply_msg.id

    except Exception as e:
        await message.reply_text(f"ᴀɴ ᴇʀʀᴏʀ occurred: {e}")


# --- 2. Handle filename reply ---
@Client.on_message(filters.reply & filters.private)
async def handle_reply(client: Client, message: Message):

    uid = message.from_user.id
    user_state = user_data.get(uid)
    if not user_state:
        return

    if message.reply_to_message.id != user_state.get("reply_msg_id"):
        return

    user_state["file_name"] = message.text
    await message.reply_text(
        "Select upload type",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("📁 Document", callback_data="document"),
                InlineKeyboardButton("🎞 Video", callback_data="video"),
            ]]
        )
    )


# --- 3. Handle inline button click ---
@Client.on_callback_query(filters.regex("^(document|video)$"), group=-1)
async def upload_file_callback(client:Bot, query: CallbackQuery):    
    # ALWAYS ack first
    await query.answer()  # silent ack to stop Telegram spinner immediately

    user_id = query.from_user.id
    user_state = user_data.get(user_id)
    if not user_state:        return

    if "file_name" not in user_state:
        await query.message.edit_text("File name missing. Please restart the process.")
        return

    thumb_path = f"thumbnails/{user_id}.jpg"
    if not os.path.exists(thumb_path):
        await query.message.edit_text("Thumbnail missing. Please send one first.")
        return 
    

    max_dim = 320
    max_size_kb = 200 

    with Image.open(thumb_path) as im:
        im = im.convert("RGB")
        im.thumbnail((max_dim, max_dim))  # resize to max 320x320

        # save once at high quality
        im.save(thumb_path, format="JPEG")

        # check if file is too big
        if os.path.getsize(thumb_path) > max_size_kb * 1024:
            quality = 85
            step = 5
            while True:
                im.save(thumb_path, format="JPEG", quality=quality)
                if os.path.getsize(thumb_path) <= max_size_kb * 1024 or quality <= 20:
                    break
                quality -= step


    try:
        # status message
        pros_msg = await query.message.reply_text("Preparing download...")

        # download
        file_msg = await client.get_messages(query.message.chat.id, user_state["file_msg_id"])
        download_path = os.path.join(DOWNLOAD_DIR, user_state["file_name"])
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        start_time = time.time()

        downloaded_file = await client.download_media(
            message=file_msg,
            file_name=download_path,
            progress=progress_bar,
            progress_args=(start_time, pros_msg, "Downloading...")
        )
        ext = os.path.splitext(downloaded_file)[1]
        final_path = f"{download_path}{ext}"
        os.rename(downloaded_file, final_path)

        # upload
        upload_start = time.time()
        if query.data == "document":
            await client.send_document(
                chat_id=query.message.chat.id,
                document=final_path,
                thumb=thumb_path,
                caption=user_state.get("caption", user_state["file_name"]),
                progress=progress_bar,
                progress_args=(upload_start, pros_msg, "Uploading...")
            )
        elif query.data == "video":
            await client.send_video(
                chat_id=query.message.chat.id,
                video=final_path,
                thumb=thumb_path,
                caption=user_state.get("caption", user_state["file_name"]),
                progress=progress_bar,
                progress_args=(upload_start, pros_msg, "Uploading...")
            )


    except Exception as e:
        TRACE("callback EXCEPTION", error=str(e))
        await pros_msg.edit_text(f"Error occurred: {e}")
    finally:
        # cleanup
        await pros_msg.delete()
        user_data.pop(user_id, None)
        cleanup_downloads()




