#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""෴❤️ආයුබෝවන්❤️෴\n\n 🔥/ytdl: This command should be used as reply to a supported link\n\n 

🔥/leech: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [this command will SPAM the chat and send the downloads a seperate files, if there is more than one file, in the specified torrent]\n\n 

🔥/leech archive: This command should be used as reply to a magnetic link, a torrent link, or a direct link. [This command will create a .tar.gz file of the output directory, and send the files in the chat, splited into PARTS of 1024MiB each, due to Telegram limitations]\n\n 

🔥/gleech: This command should be used as reply to a magnetic link, a torrent link, or a direct link.\n\n 

🔥/leech unzip: This will unzip the .zip file and dupload to telegram.\n\n 

🔥/gleech unzip: This will unzip the .zip file and upload to drive.\n\n 

🔥/leech unrar: This will unrar the .rar file and dupload to telegram.\n\n 

🔥/gleech unrar: This will unrar the .rar file and upload to drive.\n\n 

🔥/leech untar: This will untar the .tar file and upload to telegram.\n\n 

🔥/gleech untar: This will untar the .tar file and upload to drive.\n\n 

🔥/tleech: This will mirror the telegram files to ur respective cloud drive.\n\n 

🔥/tleech unzip: This will unzip the .zip telegram file and upload to drive.\n\n 

🔥/tleech unrar: This will unrar the .rar telegram file and upload to drive.\n\n 

🔥/tleech untar: This will untar the .tar telegram file and upload to drive\n\n """, disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
