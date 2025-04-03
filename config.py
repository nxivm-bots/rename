import re, os, time

id_pattern = re.compile(r'^.\d+$') 
ADMINS = [1110013191, 6698364560, 6663845789, 5126166591, 6618620897, 7445650518]
class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", 26634100)
    API_HASH  = os.environ.get("API_HASH", "9ea49405d5a93e784114c469f5ce4bbd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8052725016:AAEGHXgWtF13jP9xMjRBVpPjNC6ggVmLWBE")
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rename")
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://kratosnigger:GuH0qHewCzuynCE4@telegram.mhwll.mongodb.net/")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/_A8.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1110013191, 6698364560, 6663845789, 5126166591, 6618620897, 7445650518').split()]
    FORCE_SUB_1 = os.environ.get("FORCE_SUB_1", "-1002198818132")
    FORCE_SUB_2 = os.environ.get("FORCE_SUB_2", "-1002234935173")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002183841044"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002648752950"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """
<b>Hey {}! 𖤐</b>

Welcome to <b>Nxivm Rename Bot! ⨳</b>

✦ This bot helps you <b>rename files</b> with a custom caption and thumbnail.  
✦ You can also set a <b>prefix and suffix</b> for your files.  
✦ Simple, fast, and efficient! ⚡  

──────────────────  
⟡ <b>How to Use:</b> Click the button below to learn more about my commands.  
⟡ <b>Created by:</b> <a href="https://t.me/Nxivm_network">Nxivm Network</a>  

"""

    DONATE_TXT = """
<b>𖤐 Hey there, {}!</b>

Just wanted to drop a quick <b>thank you</b> your way! In our little corner of channels and bots, having your support feels like receiving a warm embrace.

No need to worry about donations – your small gestures and clicks mean the world to us. Every bit of support helps us keep things running smoothly.

A <b>huge thanks</b> for being the support <b>superstar</b> in our small but amazing space! ✦
"""

    HELP_TXT = """
<b>✦ Nxivm Rename Bot - Powerful Features ✦</b>

Nxivm Rename Bot is a <b>fast</b> and <b>efficient</b> tool to help you manage and rename files effortlessly.

<u>Key Features:</u>
➲ Rename any file with ease.  
➲ Manage file metadata seamlessly.  
➲ Upload in your preferred media type.  
➲ Set custom <b>prefix</b> and <b>suffix</b> for files.  
➲ Lightning-fast renaming process.  

Use the commands below to get started and make the most of the bot!
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @GeekLuffy🙏🥲
    ABOUT_TXT = """
<b>✦ Nxivm Rename Bot - About ✦</b>

» <b>Developer:</b> <a href=https://t.me/Nxivm_network>Nxivm Network</a>    
» <b>Library:</b> <a href=https://github.com/pyrogram>Pyrogram</a>  
» <b>Language:</b> <a href=https://www.python.org>Python</a>  
» <b>Network:</b> <a href=https://t.me/Nxivm_Network>Nxivm Network</a>  
» <b>Support:</b> <a href=https://t.me/Nxivm_support>Nxivm Support</a>  
"""

    META_TXT = """
✦ **ＭＥＴＡＤＡＴＡ  ＭＡＮＡＧＥＭＥＮＴ** ✦  

➤ **ᴠᴀʀɪᴏᴜꜱ ᴍᴇᴛᴀᴅᴀᴛᴀ**:  
╭───────────⍟  
┃ ⦿ **Ｔｉｔｌｅ** ⌁ Set a custom title.  
┃ ⦿ **Ａｕｔｈｏｒ** ⌁ Define the creator.  
┃ ⦿ **Ａｒｔｉｓｔ** ⌁ Specify the artist.  
┃ ⦿ **Ａｕｄｉｏ** ⌁ Assign an audio title.  
┃ ⦿ **Ｓｕｂｔｉｔｌｅ** ⌁ Set subtitle info.  
┃ ⦿ **Ｖｉｄｅｏ** ⌁ Name the video file.  
╰───────────⍟  

✦ **ＣＯＭＭＡＮＤＳ** ✦  

➤ **Ｔｏ Toggle Metadata**:  
◈ `/metadata` ⌁ Enable / Disable metadata.  

➤ **Ｔｏ Set Metadata**:  
◈ `/settitle` ⌁ 𝑺𝒆𝒕 𝒂 𝒄𝒖𝒔𝒕𝒐𝒎 𝒕𝒊𝒕𝒍𝒆.  
◈ `/setauthor` ⌁ 𝑺𝒆𝒕 𝒕𝒉𝒆 𝒂𝒖𝒕𝒉𝒐𝒓.  
◈ `/setartist` ⌁ 𝑺𝒆𝒕 𝒕𝒉𝒆 𝒂𝒓𝒕𝒊𝒔𝒕.  
◈ `/setaudio` ⌁ 𝑺𝒆𝒕 𝒂𝒖𝒅𝒊𝒐 𝒕𝒊𝒕𝒍𝒆.  
◈ `/setsubtitle` ⌁ 𝑺𝒆𝒕 𝒔𝒖𝒃𝒕𝒊𝒕𝒍𝒆 𝒕𝒊𝒕𝒍𝒆.  
◈ `/setvideo` ⌁ 𝑺𝒆𝒕 𝒗𝒊𝒅𝒆𝒐 𝒕𝒊𝒕𝒍𝒆.  

✦ **ＥＸＡＭＰＬＥ** ✦  
➜ `/settitle 𝑴𝒚 𝑨𝒘𝒆𝒔𝒐𝒎𝒆 𝑴𝒐𝒗𝒊𝒆`  

**⚡ Enhance Your Media with Custom Metadata! ⚡**
"""
