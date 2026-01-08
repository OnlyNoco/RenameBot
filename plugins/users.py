from bot import Bot
from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from database.database import get_all_users
from config import OWNER_ID

# --- /users command --- #
@Client.on_message(filters.command("users") & filters.private & filters.user(OWNER_ID))
async def list_users(client: Bot, message: Message):
    users = await get_all_users()
    total_users = len(users)

    if total_users == 0:
        await message.reply_text("ɴᴏ ᴜꜱᴇʀꜱ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ.")
        return

    reply_text = f"<b>ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ:</b> {total_users}\n\n" 

    # Batch fetch users in chunks of 200 (Telegram limit for get_users)
    chunk_size = 200  # Number of users per message chunk
    for i in range(0, total_users, chunk_size):
        batch_ids = users[i:i + chunk_size] 
        try: 
            batch_user = await client.get_users(batch_ids) # returns list of User objects 
            if not isinstance(batch_user, list):
                batch_user = [batch_user] 
            
            for idx, user in enumerate(i + 1):
                reply_text += f"{idx}. <a href='tg://user?id={user.id}'>{user.first_name}</a> ɪᴅ: {user.id}\n"
        except Exception:
            for idx, user_id in enumerate(batch_ids, i + 1):
                reply_text += f"{idx}. ᴜꜱᴇʀ ɪᴅ: {user_id} !!\n"

    # Split message if too long
    if len(reply_text) > 4000:
        for i in range(0, len(reply_text), 4000):
            await message.reply_text(reply_text[i:i+4000], parse_mode=ParseMode.HTML)
    else:
        await message.reply_text(reply_text, parse_mode=ParseMode.HTML)


# --- /sendMessage <user_id> <message> --- #
@Client.on_message(filters.command("sendmessage") & filters.private & filters.user(OWNER_ID))
async def send_to_user(client: Bot, message: Message):
    if len(message.command) < 3:
        await message.reply_text("ᴜꜱᴀɢᴇ: /ꜱᴇɴᴅᴍᴇꜱꜱᴀɢᴇ <ᴜꜱᴇʀ_ɪᴅ> <ᴍᴇꜱꜱᴀɢᴇ>")
        return

    try:
        user_id = int(message.command[1])
    except ValueError:
        await message.reply_text("!! ɪɴᴠᴀʟɪᴅ ᴜꜱᴇʀ ɪᴅ ꜰᴏʀᴍᴀᴛ.")
        return

    msg_to_send = " ".join(message.command[2:])

    try:
        await client.send_message(chat_id=user_id, text=msg_to_send)
        await message.reply_text(f" ᴍᴇꜱꜱᴀɢᴇ ꜱᴇɴᴛ ᴛᴏ ᴜꜱᴇʀ ɪᴅ:<code>{user_id}</code>", parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply_text(f" ꜰᴀɪʟᴇᴅ ᴛᴏ ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ:\n<code>{e}</code>", parse_mode=ParseMode.HTML)