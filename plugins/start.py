import os, random
from config import START_PIC, START_MSG, ABOUT_MSG, CMD_MSG
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.enums import ParseMode, ChatAction
from bot import Bot
from database.database import add_user


#-- 🫆 start command --#
@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
  # chat action
  await client.send_chat_action(message.chat.id, ChatAction.PLAYING)
  
  # save user id to mongodb
  await add_user(message.from_user.id) 
  
  bot = await client.get_me() # obj
  bot_username = bot.username # username
  # buttons 
  reply_btns = InlineKeyboardMarkup(
    [
      [
        InlineKeyboardButton("Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ", url=f"https://t.me/{bot_username}?startgroup=botstart")
      ],
      [
        InlineKeyboardButton("✏️ Aʙᴏᴜᴛ", callback_data="about"),
        InlineKeyboardButton("💨 Cᴏᴍᴍᴀɴᴅs", callback_data="cmd")
      ]
    ]
  )

  photo = random.choice(START_PIC)
  
  # send a photo with msg 
  await message.reply_photo(
    photo = photo,
    caption = START_MSG.format(
      mention = message.from_user.mention),
    reply_markup = reply_btns
  )
  

#-- Callback Queries --#
@Client.on_callback_query()
async def callback_queries(client: Bot, query: CallbackQuery):
    #-- About --#
    if query.data == "about":
        await query.message.edit_text(
            text = ABOUT_MSG.format(mention=query.from_user.mention),
            disable_web_page_preview = True, 
            parse_mode = ParseMode.HTML,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🖇️ ʙᴀᴄᴋ", callback_data="back"),
                        InlineKeyboardButton("💨 Cᴏᴍᴍᴀɴᴅs", callback_data="cmd")
                    ]
                ]
            )
        )
    
    #-- Commands --#
    elif query.data == "cmd":
        await query.message.edit_text(
            text = CMD_MSG.format(mention=query.from_user.mention),
            disable_web_page_preview = True, 
            parse_mode = ParseMode.HTML,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✏️ Aʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("🖇️ ʙᴀᴄᴋ", callback_data="back")
                    ]
                ]
            )
        )
    
    #-- Back Callback --#
    elif query.data == "back":
        await query.message.edit_text(
            text = START_MSG.format(mention=query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("✏️ Aʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("💨 Cᴏᴍᴍᴀɴᴅs", callback_data="cmd")
                    ]
                ]
            )
        )