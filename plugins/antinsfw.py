nsfw_keywords = {
    "general": [
        "ahgagav"
    ],
    "hentai": [
        "eihwbwb"
    ],
    "abbreviations": [
        "djbeb"
    ],
    "offensive_slang": [
        "jsbsb"
    ]
}

exception_keywords = ["jshsv", "syhsb", "fjnr", "whvw"]

async def check_anti_nsfw(new_name, message):
    lower_name = new_name.lower()
    for keyword in exception_keywords:
        if keyword.lower() in lower_name:
            return False  # Allow the filename if it contains an exception keyword
    
    for category, keywords in nsfw_keywords.items():
        for keyword in keywords:
            if keyword.lower() in lower_name:
                await message.reply_text("You can't rename files with NSFW content.")
                return True
    return False
