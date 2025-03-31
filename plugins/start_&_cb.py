import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt

@Client.on_message(filters.command("metadata"))
async def metadata(client, message):
    user_id = message.from_user.id

    current = await db.get_metadata(user_id)

    title = await db.get_title(user_id)
    author = await db.get_author(user_id)
    artist = await db.get_artist(user_id)
    video = await db.get_video(user_id)
    audio = await db.get_audio(user_id)
    subtitle = await db.get_subtitle(user_id)

    text = f"""
    **㊋ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ: {current}**

**◈ Tɪᴛʟᴇ ▹** `{title if title else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴛʜᴏʀ ▹** `{author if author else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aʀᴛɪꜱᴛ ▹** `{artist if artist else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴅɪᴏ ▹** `{audio if audio else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Sᴜʙᴛɪᴛʟᴇ ▹** `{subtitle if subtitle else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Vɪᴅᴇᴏ ▹** `{video if video else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
    """

    button = [[
        InlineKeyboardButton(f"On{' ✅' if current == 'On' else ''}", callback_data='on_metadata'),
        InlineKeyboardButton(f"Off{' ✅' if current == 'Off' else ''}", callback_data='off_metadata')
    ],
        [
            InlineKeyboardButton("How to Set Metadata", callback_data="metainfo")
        ]]
    keyboard = InlineKeyboardMarkup(button)

    await message.reply_text(text=text, reply_markup=keyboard, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("How to use", callback_data='help')
    ], [
        InlineKeyboardButton('Network', url='https://t.me/nxivm_network'),
        InlineKeyboardButton('Support', url='https://t.me/nxivm_support')
    ], [
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Donate', callback_data='donate')
    ]])
    if Config.START_PIC:
        await message.reply_video(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button,
                                 disable_web_page_preview=True)


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("How to use", callback_data='help')
            ], [
                InlineKeyboardButton('Network', url='https://t.me/nxivm_network'),
                InlineKeyboardButton('Support', url='https://t.me/nxivm_support')
            ], [
                InlineKeyboardButton('About', callback_data='about'),
                InlineKeyboardButton('Donate', callback_data='donate')
            ]])
        )
    elif data == "on_metadata":
        user_id = query.from_user.id
        await db.set_metadata(user_id, "On")

        current = await db.get_metadata(user_id)
        title = await db.get_title(user_id)
        author = await db.get_author(user_id)
        artist = await db.get_artist(user_id)
        video = await db.get_video(user_id)
        audio = await db.get_audio(user_id)
        subtitle = await db.get_subtitle(user_id)

        text = f"""
            **㊋ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ: {current}**

**◈ Tɪᴛʟᴇ ▹** `{title if title else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴛʜᴏʀ ▹** `{author if author else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aʀᴛɪꜱᴛ ▹** `{artist if artist else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴅɪᴏ ▹** `{audio if audio else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Sᴜʙᴛɪᴛʟᴇ ▹** `{subtitle if subtitle else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Vɪᴅᴇᴏ ▹** `{video if video else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
            """

        await query.message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(f"On{' ✅' if current == 'On' else ''}", callback_data='on_metadata'),
                InlineKeyboardButton(f"Off{' ✅' if current == 'Off' else ''}", callback_data='off_metadata')
            ],
                [
                    InlineKeyboardButton("How to Set Metadata", callback_data="metainfo")
                ]])
        )

    elif data == "off_metadata":
        user_id = query.from_user.id
        await db.set_metadata(user_id, "Off")
        current = await db.get_metadata(user_id)

        title = await db.get_title(user_id)
        author = await db.get_author(user_id)
        artist = await db.get_artist(user_id)
        video = await db.get_video(user_id)
        audio = await db.get_audio(user_id)
        subtitle = await db.get_subtitle(user_id)

        text = f"""
            **㊋ Yᴏᴜʀ Mᴇᴛᴀᴅᴀᴛᴀ ɪꜱ ᴄᴜʀʀᴇɴᴛʟʏ: {current}**

**◈ Tɪᴛʟᴇ ▹** `{title if title else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴛʜᴏʀ ▹** `{author if author else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aʀᴛɪꜱᴛ ▹** `{artist if artist else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Aᴜᴅɪᴏ ▹** `{audio if audio else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Sᴜʙᴛɪᴛʟᴇ ▹** `{subtitle if subtitle else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
**◈ Vɪᴅᴇᴏ ▹** `{video if video else 'Nᴏᴛ ꜰᴏᴜɴᴅ'}`
            """
        await query.message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(f"On{' ✅' if current == 'On' else ''}", callback_data='on_metadata'),
                InlineKeyboardButton(f"Off{' ✅' if current == 'Off' else ''}", callback_data='off_metadata')
            ],
                [
                    InlineKeyboardButton("How to Set Metadata", callback_data="metainfo")
                ]])
        )
    elif data == "metainfo":
        await query.message.edit_text(
            text=Txt.META_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Home", callback_data="start"),
                InlineKeyboardButton("Back", callback_data="commands")
            ]])
        )


    elif data == "donate":
        await query.message.edit_text(
            text=Txt.DONATE_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                # ⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT.format(client.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Metadata", callback_data="metainfo"),
                ],
                [
                    InlineKeyboardButton("Captions", callback_data="caption"),
                    InlineKeyboardButton("Thumbnails", callback_data="thumbnail")],
                [
                    InlineKeyboardButton("Suffix & Prefix", callback_data="suffix_prefix")],
                [
                    InlineKeyboardButton("Close", callback_data="close"),
                    InlineKeyboardButton("Back", callback_data="start")
                ]])
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                # ⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("Close", callback_data="close"),
                InlineKeyboardButton("Back", callback_data="start")
            ]])
        )

    elif data == "caption":
        await query.message.edit_text(
            text = """ 
<b><u>To Set Custom Caption and Media Type</u></b>

**Variables:**  
- Size: {filesize}  
- Duration: {duration}  
- Filename: {filename}  

**Commands:**  
➜ /set_caption - Set a custom caption.  
➜ /see_caption - View your custom caption.  
➜ /del_caption - Delete your custom caption.  

**Example:**  
/ setcaption File Name: {filename}  
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Home", callback_data="start"),
                InlineKeyboardButton("Back", callback_data="help")
            ]])
        )
    elif data == "thumbnail":
        await query.message.edit_text(
            text = """  
★ To Set Custom Thumbnail ★  

➜ /start: Send any photo to automatically set it as a thumbnail.  
➜ /del_thumb: Use this command to delete your old thumbnail.  
➜ /view_thumb: Use this command to view your current thumbnail.  

✦ Note: If no thumbnail is saved in the bot, it will use the thumbnail of the original file to set in the renamed file.  
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Home", callback_data="start"),
                InlineKeyboardButton("Back", callback_data="help")
            ]])
        )

    elif data == "suffix_prefix":
        await query.message.edit_text(
            text = """  
★ To Set Custom Suffix & Prefix ★  

➜ /set_prefix: To set a custom prefix.  
➜ /del_prefix: To delete your custom prefix.  
➜ /see_prefix: To view your custom prefix.  

➜ /set_suffix: To set a custom suffix.  
➜ /del_suffix: To delete your custom suffix.  
➜ /see_suffix: To view your custom suffix.  

✦ Example: /set_prefix [NA] | /set_suffix [NxivmAnime]  
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Home", callback_data="start"),
                InlineKeyboardButton("Back", callback_data="help")
            ]])
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()
