import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/43ef267b4ffb3cc9f5c38.png",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🐯 Hҽʅʅσ, I αɱ Sυρҽɾϝαʂƚ Hιɠԋ Qυαʅιƚყ 
Nσ Lαɠ Vƈ Mυʂιƈ Pʅαყҽɾ Bσƚ.

┏━━━━━━━━━━━━━━━━━━━━┓
┣★ Cɾҽαƚσɾ 🛠️  [𝐌𝐀𝐒𝐎𝐎𝐌 𝐁𝐎𝐘](https://t.me/MASOOM_B0Y)
┣★ Cɾҽαƚσɾ 🛠️ [𝐙𝐎𝐍𝐄𝐘 𝐎𝐏](https://t.me/itszoney)
┣★ Uρԃαƚҽʂ 📢 [𝐓𝐄𝐀𝐌 𝐈𝐍𝐃](https://t.me/TEAM_IND_OFFICIAL)
┣★ Sυρρσɾƚ ☣️ [𝐅𝐔𝐋𝐋 𝐎𝐍 𝐌𝐎𝐉 𝐌𝐀𝐒𝐓𝐈](https://t.me/FULL_ON_MOJJ_MASTI)
┣★ Cԋαƚƚιɳɠ ©️ [𝐅𝐔𝐋𝐋 𝐎𝐍 𝐌𝐎𝐉 𝐌𝐀𝐒𝐓𝐈](https://t.me/FULL_ON_MOJJ_MASTI)
┗━━━━━━━━━━━━━━━━━━━━┛

🗽 Jυʂƚ Aԃԃ Mҽ » Tσ Yσυɾ Gɾσυρ Aɳԃ
Eɳʝσყ Bҽʂƚ Qυαʅιƚყ ❥︎ Mυʂιƈ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Aԃԃ Mҽ Tσ Yσυɾ Gɾσυρ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"/start@{BOT_USERNAME}", "/alive", "/BGT",  ".Kaal"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo()
       photo=f"https://te.legra.ph/file/c6e1041c6c9a12913f57a.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝐂𝐥𝐢𝐜𝐤 𝐌𝐞 𝐓𝐨 𝐆𝐞𝐭 𝐑𝐞𝐩𝐨 💞", url=f"{SOURCE_CODE}")
                ]
            ]
        ),
    )


