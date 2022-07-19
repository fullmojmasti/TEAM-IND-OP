# 𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫 // @𝑨𝒅𝒊𝒕𝒚𝒂𝑯𝒂𝒍𝒅𝒆𝒓
import os
import aiofiles
import aiohttp
import ffmpeg
import random
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import ASSISTANT_USERNAME, DURATION_LIMIT, que, OWNER_USERNAME, SUDO_USERS, SUPPORT_GROUP, UPDATES_CHANNEL, PROFILE_CHANNEL
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

# 𝑰𝒏𝒕𝒆𝒓𝒏𝒂𝒍 𝑴𝒐𝒅𝒖𝒍𝒆𝒔
chat_id = None
useer = "NaN"

themes = [
    "colourful",
    "cutedoll",
    "cutegirl",
    "cutepie",
    "love",
    "masti",
    "pink",
    "rabbit",
    "rose",
    "sky",
  
]

def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# 𝑪𝒐𝒏𝒗𝒆𝒓𝒕 𝑺𝒆𝒄𝒐𝒏𝒅𝒔 𝑻𝒐 𝒎𝒎:𝒔𝒔
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# 𝑪𝒐𝒏𝒗𝒆𝒓𝒕 𝒉𝒉:𝒎𝒎:𝒔𝒔 𝑻𝒐 𝑺𝒆𝒄𝒐𝒏𝒅𝒔
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# 𝑪𝒉𝒂𝒏𝒈𝒆 𝑻𝒉𝒖𝒎𝒃𝒏𝒂𝒊𝒍 𝑺𝒊𝒛𝒆
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))

# 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒆 𝑻𝒉𝒖𝒎𝒃𝒏𝒂𝒊𝒍
async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    theme = random.choice(themes)
    image1 = Image.open("./background.png")
    image2 = Image.open(f"resource/{theme}.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resource/font.otf", 32)
    draw.text((190, 550), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Powered By: Aditya Halder (@AdityaHalder)",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["/play", ".play", "!play", "play", "@", "#", "$"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    lel = await message.reply("**🔎Zoney Ki GF Dhund Rahi Hu...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Aditya_Player"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "**💥 𝐀𝐭🤞𝐅𝐢𝐫𝐬𝐭 🥀 𝐌𝐚𝐤𝐞 ♥️ 𝐌𝐞 ⭐ 𝐀𝐝𝐦𝐢𝐧 😎 ...**")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "** 😎 𝐈🤞𝐚𝐦 🥀 𝐑𝐞𝐚𝐝𝐲 ♥️ 𝐓𝐨 ⭐ 𝐏𝐥𝐚𝐲 😎 ...**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"**🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐌𝐚𝐧𝐮𝐚𝐥𝐥𝐲 🌺 𝐀𝐝𝐝 [𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭](https://t.me/FULL_ON_MOJ) 🎸 𝐢𝐧 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩 ♥️ 𝐎𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨 [𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫 ](https://t.me/{OWNER_USERNAME}) ✨ **")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"**🥀 𝐏𝐥𝐞𝐚𝐬𝐞 𝐌𝐚𝐧𝐮𝐚𝐥𝐥𝐲 🌺 𝐀𝐝𝐝 [𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭](https://t.me/FULL_ON_MOJ) 🎸 𝐢𝐧 𝐓𝐡𝐢𝐬 𝐆𝐫𝐨𝐮𝐩 ♥️ 𝐎𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨 [𝐁𝐨𝐭 𝐎𝐰𝐧𝐞𝐫 ](https://t.me/{OWNER_USERNAME}) ✨ **")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**💥 𝐏𝐥𝐚𝐲 🔊 𝐌𝐮𝐬𝐢𝐜 💿 𝐋𝐞𝐬𝐬 ⚡️\n🤟 𝐓𝐡𝐚𝐧⚡️ {DURATION_LIMIT} 💞 𝐌𝐢𝐧𝐮𝐭𝐞 ...**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://te.legra.ph/file/ed6920a2f0ab5af3fd55d.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="🥀 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 🕊️",
                            url=f"https://t.me/itszoney")
               ],
               [
                    InlineKeyboardButton(
                            text="𝐇𝐚𝐜𝐤𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                            url=f"https://t.me/TEAM_IND_OFFICIAL"),
                            
                    InlineKeyboardButton(
                            text="𝐌𝐚𝐬𝐭𝐢 𝐆𝐫𝐨𝐮𝐩 💬",
                            url=f"https://t.me/FULL_ON_MOJJ_MASTI")
               ],
               [
                        InlineKeyboardButton(
                            text="💖 𝐒𝐭𝐚𝐭𝐮𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🌺",
                            url=f"https://t.me/OP_STATUS")
                   
                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="🥀 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 🕊️",
                            url=f"https://t.me/itszoney")
               ],
               [
                    InlineKeyboardButton(
                            text="𝐇𝐚𝐜𝐤𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                            url=f"https://t.me/TEAM_IND_OFFICIAL"),
                            
                    InlineKeyboardButton(
                            text="𝐌𝐚𝐬𝐭𝐢 𝐆𝐫𝐨𝐮𝐩 💬",
                            url=f"https://t.me/FULL_ON_MOJJ_MASTI")
               ],
               [
                        InlineKeyboardButton(
                            text="💖 𝐒𝐭𝐚𝐭𝐮𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🌺",
                            url=f"https://t.me/OP_STATUS")
                   
                ]
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://te.legra.ph/file/ed6920a2f0ab5af3fd55d.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="🥀 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 🕊️",
                            url=f"https://t.me/itszoney")
               ],
               [
                    InlineKeyboardButton(
                            text="𝐇𝐚𝐜𝐤𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                            url=f"https://t.me/TEAM_IND_OFFICIAL"),
                            
                    InlineKeyboardButton(
                            text="𝐌𝐚𝐬𝐭𝐢 𝐆𝐫𝐨𝐮𝐩 💬",
                            url=f"https://t.me/FULL_ON_MOJJ_MASTI")
               ],
               [
                        InlineKeyboardButton(
                            text="💖 𝐒𝐭𝐚𝐭𝐮𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🌺",
                            url=f"https://t.me/OP_STATUS")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝐏𝐥𝐚𝐲 🔊 𝐌𝐮𝐬𝐢𝐜 💿 𝐋𝐞𝐬𝐬 ⚡️\n🤟 𝐓𝐡𝐚𝐧⚡️ {DURATION_LIMIT} 💞 𝐌𝐢𝐧𝐮𝐭𝐞 ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**🤖 𝐆𝐢𝐯𝐞 🙃 𝐌𝐮𝐬𝐢𝐜 💿 𝐍𝐚𝐦𝐞 😍\n💞 𝐓𝐨 🔊 𝐏𝐥𝐚𝐲 🥀 𝐒𝐨𝐧𝐠 🌷...**"
            )
        await lel.edit("**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🔊 𝐌𝐮𝐬𝐢𝐜 😕 𝐍𝐨𝐭 📵 𝐅𝐨𝐮𝐧𝐝❗️\n💞 𝐓𝐫𝐲 ♨️ 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 🌷...**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                            text="🥀 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 🕊️",
                            url=f"https://t.me/itszoney")
               ],
               [
                    InlineKeyboardButton(
                            text="𝐇𝐚𝐜𝐤𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",
                            url=f"https://t.me/TEAM_IND_OFFICIAL"),
                            
                    InlineKeyboardButton(
                            text="𝐌𝐚𝐬𝐭𝐢 𝐆𝐫𝐨𝐮𝐩 💬",
                            url=f"https://t.me/FULL_ON_MOJJ_MASTI")
               ],
               [
                        InlineKeyboardButton(
                            text="💖 𝐒𝐭𝐚𝐭𝐮𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🌺",
                            url=f"https://t.me/OP_STATUS")
                   
                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝐏𝐥𝐚𝐲 🔊 𝐌𝐮𝐬𝐢𝐜 💿 𝐋𝐞𝐬𝐬 ⚡️\n🤟 𝐓𝐡𝐚𝐧⚡️ {DURATION_LIMIT} 💞 𝐌𝐢𝐧𝐮𝐭𝐞 ...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="**💥 𝐘𝐨𝐮𝐫 🥀 𝐒𝐨𝐧𝐠 💿 𝐐𝐮𝐞𝐮𝐞𝐝❗️\n🔊 𝐀𝐭 💞 𝐏𝐨𝐬𝐢𝐭𝐢𝐨𝐧 » `{}` 🌷 ...**".format(position),
            reply_markup=keyboard,
        )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**💥 𝐓𝐞𝐚𝐦 𝐈𝐍𝐃 𝐌𝐮𝐬𝐢𝐜 🌺 𝐑𝐨𝐛𝐨𝐭 🎸 𝐍𝐨𝐰 💞\n🔊 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 😍 𝐎𝐏 🥀 ...**".format(),
           )

    os.remove("final.png")
    return await lel.delete()
    
    
@Client.on_message(commandpro(["pause", ".pause", "/pause", "!pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("**▶️ 𝐑𝐮𝐤 𝐆𝐚𝐲𝐚 🌷 ...**"
    )


@Client.on_message(commandpro(["resume", ".resume", "/resume", "!resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("**⏸ 𝐜𝐡𝐚𝐥𝐮 🌷 ...**"
    )



@Client.on_message(commandpro(["skip", ".skip", "/skip", "!skip"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**💥 𝐉𝐚𝐧𝐮 💞 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐍𝐚𝐡𝐢 𝐉𝐨 𝐑𝐚𝐡𝐚 ...**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await message.reply_text("**🥀 𝑸𝒖𝒆𝒖𝒆 𝑬𝒎𝒑𝒕𝒚, 𝑳𝒆𝒂𝒗𝒊𝒏𝒈 𝑽𝑪 ✨ ...**") 
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            await message.reply_text("**⏩ 𝐒𝐤𝐢𝐩 𝐐 𝐊𝐢𝐲𝐚 𝐍𝐨𝐨𝐛😒...**") 
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )



@Client.on_message(commandpro(["end", "/end", "!end", ".end", "stop", "/stop", ".stop", "stop", "x"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    await message.delete()
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("**𝐍𝐨𝐨𝐛𝐝𝐞 𝐄𝐧𝐝 𝐊𝐚𝐫 𝐃𝐢𝐲𝐚😒...**"
    )


@Client.on_message(commandpro(["reload", ".reload", "/reload", "!reload", "/admincache"]))
@errors
@authorized_users_only
async def update_admin(client, message):
    global a
    await message.delete()
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    a[message.chat.id] = new_admins
    await message.reply_text("**𝐓𝐚𝐩𝐚 𝐓𝐚𝐩...**")
