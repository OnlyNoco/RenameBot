from bot import Bot 
from pyrogram import filters, Client
from pyrogram.enums import ParseMode
from config import OWNER_ID

@Client.on_message(filters.command("report") & filters.private)
async def report_to_admin(client, message): 

    # save user id to mongodb
    await add_user(message.from_user.id)

    # Get the arguments after /report
    report_content = " ".join(message.command[1:])  # message.command[0] is 'report'

    if not report_content:
        await message.reply_text("Please write something after /report to send.")
        return

    report_text = (
        f"🚨 User Report\n"
        f"From: {message.from_user.mention} <code>({message.from_user.id})</code>\n\n"
        f"Message: {report_content}"
    )

    await client.send_message(
        chat_id=OWNER_ID,
        text=report_text,
        parse_mode=ParseMode.HTML
    )

    await message.reply_text("✅ Your report has been sent to the OWNER. Reply will be here.")