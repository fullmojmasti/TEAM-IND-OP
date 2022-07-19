# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "4cf512e6f3274086dd6364a952b9a094")
API_ID = int(getenv("API_ID", "8334353"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "I LOVE MUSIC")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "FULL_ON_MOJ")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/a0a583cf8025c91141e99.png")
BOT_NAME = getenv("BOT_NAME", "𝐓𝐞𝐚𝐦 𝐈𝐍𝐃 𝐕𝐜 𝐏𝐥𝐚𝐲𝐞𝐫")
BOT_TOKEN = getenv("BOT_TOKEN", "5428318094:AAGUmTK4Df2KGrU_-aKkUFhU1kxGEqOCscA")
BOT_USERNAME = getenv("BOT_USERNAME", "FULL_MOJJ_MASTI_BOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "𝐌𝐀𝐒𝐎𝐎𝐌 𝐁𝐎𝐘")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MASOOM_B0Y")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/fullmojmasti/TEAM-IND-OP")
STRING_SESSION = getenv("STRING_SESSION", "BQCrqVsIWUPKuoTGbiCxiV1U392Qs2VgaiPYtGS41UTXmDpNsrr-fJb4hEcQHmZzfdi2e4l6lxKInLrU53Pv2557QLvlek_VzfYRRinj7755r0Xs7qhNeUJPJmJhnBpNJzexDtN57_1Mf9fDKQqtNOOcyYb9vuhYfFLAIVCg4P0EPEy7ApvHuPa-s8Z_THJV_3iw9tEO5GvUPQPqV0Dwj1ffAmVps6ipQExGmJ9FpIPxeUrvS6xhVWcYCD47GpxDY27ANh8u2wGDXnKN7vQixmuJByKOPHa5ftxQ4Kbo5j2Z-o6DQU-N1yXKnC8GotRnDzgKQdplKLDJZQmUYGcxceBHAAAAAHt4SIoA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5373329232 5450805606 5545626276 5533277204 5334643009").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/FULL_ON_MOJJ_MASTI")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/OP_STATUS")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝐀𝐝𝐢𝐭𝐲𝐚 𝐇𝐚𝐥𝐝𝐞𝐫) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/OP_STATUS")
