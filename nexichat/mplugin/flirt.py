import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

FLIRT = [
    "𝐃𝐨𝐜𝐭𝐨𝐫 𝐍𝐞 𝐀𝐝𝐯𝐢𝐜𝐞 𝐊𝐢𝐚 𝐇𝐚𝐢 𝐊𝐢 𝐒𝐨𝐧𝐞 𝐒𝐞 𝐏𝐚𝐡𝐥𝐞 𝐀𝐩𝐤𝐢 𝐏𝐢𝐜 𝐃𝐞𝐤𝐡 𝐊𝐚𝐫 𝐒𝐨𝐧𝐚 𝐉𝐚𝐫𝐨𝐨𝐫𝐢 𝐇𝐚𝐢, 𝐖𝐚𝐫𝐧𝐚 𝐇𝐞𝐚𝐫𝐭 𝐀𝐭𝐭𝐚𝐜𝐤 𝐀𝐚 𝐒𝐚𝐤𝐭𝐚 𝐇𝐚𝐢.",
    "𝐀𝐩 𝐈𝐭𝐧𝐞 𝐂𝐮𝐭𝐞 𝐇𝐨 𝐊𝐢 𝐀𝐠𝐚𝐫 𝐌𝐚𝐢 𝐌𝐬𝐠 𝐍𝐚 𝐁𝐡𝐢 𝐊𝐚𝐫𝐧𝐚 𝐂𝐡𝐚𝐡𝐮.𝐓𝐨 𝐁𝐡𝐢 𝐌𝐞𝐫𝐚 𝐇𝐚𝐭𝐡 𝐊𝐡𝐮𝐝 𝐊𝐞𝐲𝐩𝐚𝐝 𝐏𝐫 𝐂𝐡𝐚𝐥𝐧𝐞 𝐋𝐚𝐠𝐭𝐚 𝐇𝐚𝐢.",
    "𝐀𝐚𝐠 𝐣𝐨𝐡 𝐝𝐢𝐥 𝐦𝐞𝐢𝐧 𝐥𝐚𝐠𝐢 𝐡𝐚𝐢, 𝐮𝐬𝐬𝐞 𝐝𝐮𝐧𝐢𝐲𝐚 𝐦𝐞𝐢𝐧 𝐥𝐚𝐠𝐚 𝐝𝐨𝐨𝐧𝐠𝐚 𝐦𝐚𝐢𝐧 ... 𝐣𝐨𝐡 𝐭𝐞𝐫𝐢 𝐝𝐨𝐥𝐢 𝐮𝐭𝐡𝐢, 𝐳𝐚𝐦𝐚𝐚𝐧𝐞 𝐤𝐨 𝐣𝐚𝐥𝐚𝐚 𝐝𝐨𝐨𝐧𝐠𝐚 𝐦𝐚𝐢𝐧",
    "𝐉𝐚𝐥𝐝𝐢 𝐬𝐞 𝐤𝐨𝐢 𝐛𝐡𝐚𝐠𝐰𝐚𝐧 𝐤𝐨 𝐛𝐮𝐥𝐚𝐨 𝐤𝐲𝐮𝐤𝐢 𝐞𝐤 𝐩𝐚𝐫𝐢 𝐤𝐡𝐨 𝐠𝐚𝐲𝐢 𝐡𝐚𝐢𝐧 𝐚𝐮𝐫 𝐰𝐨 𝐩𝐚𝐫𝐢 𝐲𝐚𝐡𝐚 𝐦𝐮𝐣𝐡𝐬𝐞 𝐜𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐚𝐡𝐢 𝐡𝐚𝐢𝐧.",
    "𝐀𝐚𝐩 𝐞𝐤 𝐜𝐚𝐦𝐞𝐫𝐚 𝐤𝐢 𝐭𝐚𝐫𝐚𝐡 𝐡𝐨 𝐣𝐚𝐛 𝐛𝐡𝐢 𝐚𝐚𝐩𝐤𝐚 𝐩𝐡𝐨𝐭𝐨𝐬 𝐝𝐞𝐤𝐡𝐭𝐚 𝐡𝐮 𝐦𝐞𝐫𝐢 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜 𝐬𝐦𝐢𝐥𝐞 𝐚𝐚𝐚 𝐣𝐚𝐭𝐢 𝐡𝐚𝐢𝐧",
    "𝐀𝐚𝐩𝐤𝐢 𝐚𝐚𝐧𝐤𝐡𝐞 𝐨𝐜𝐞𝐚𝐧 𝐤𝐢 𝐭𝐚𝐫𝐚𝐡 𝐛𝐥𝐮𝐞 𝐡𝐞 𝐚𝐮𝐫 𝐦𝐞 𝐮𝐬𝐦𝐞 𝐡𝐚𝐫 𝐛𝐚𝐚𝐫 𝐝𝐮𝐛 𝐣𝐚𝐭𝐚 𝐡𝐮",
    "𝐀𝐚𝐩 𝐜𝐡𝐨𝐫𝐨 𝐤𝐞 𝐫𝐚𝐣𝐚 𝐥𝐚𝐠𝐭𝐞 𝐡𝐨 𝐤𝐲𝐮𝐤𝐢 𝐚𝐚𝐩𝐧𝐞 𝐦𝐞𝐫𝐚 𝐝𝐢𝐥 𝐜𝐡𝐮𝐫𝐚 𝐥𝐢𝐲𝐚 𝐡𝐚𝐢𝐧",
    "𝐌𝐞𝐫𝐢 𝐚𝐚𝐧𝐤𝐡𝐨 𝐤𝐨 𝐤𝐮𝐜𝐡 𝐡𝐨 𝐠𝐚𝐲𝐚 𝐡𝐚𝐢𝐧, 𝐚𝐚𝐩 𝐩𝐞𝐫 𝐬𝐞 𝐡𝐚𝐭 𝐡𝐢 𝐧𝐚𝐡𝐢 𝐫𝐚𝐡𝐢 𝐡𝐚𝐢𝐧",
    "𝐘𝐨𝐮𝐫 𝐡𝐚𝐧𝐝 𝐥𝐨𝐨𝐤𝐬 𝐡𝐞𝐚𝐯𝐲 𝐜𝐚𝐧 𝐢 𝐡𝐨𝐥𝐝 𝐢𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮?",
    "𝐘𝐨𝐮 𝐦𝐚𝐲 𝐟𝐚𝐥𝐥 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐬𝐤𝐲, 𝐲𝐨𝐮 𝐦𝐚𝐲 𝐟𝐚𝐥𝐥 𝐟𝐫𝐨𝐦 𝐚 𝐭𝐫𝐞𝐞, 𝐛𝐮𝐭 𝐭𝐡𝐞 𝐛𝐞𝐬𝐭 𝐰𝐚𝐲 𝐭𝐨 𝐟𝐚𝐥𝐥… 𝐢𝐬 𝐢𝐧 𝐥𝐨𝐯𝐞 𝐰𝐢𝐭𝐡 𝐦𝐞.",
    "𝐀𝐫𝐞 𝐲𝐨𝐮 𝐭𝐡𝐞 𝐬𝐮𝐧? 𝐁𝐞𝐜𝐚𝐮𝐬𝐞 𝐲𝐨𝐮’𝐫𝐞 𝐬𝐨 𝐛𝐞𝐚𝐮𝐭𝐢𝐟𝐮𝐥 𝐢𝐭’𝐬 𝐛𝐥𝐢𝐧𝐝𝐢𝐧𝐠 𝐦𝐞",
    "𝐈 𝐬𝐡𝐨𝐮𝐥𝐝 𝐜𝐚𝐥𝐥 𝐲𝐨𝐮 𝐆𝐨𝐨𝐠𝐥𝐞, 𝐛𝐞𝐜𝐚𝐮𝐬𝐞 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐞𝐯𝐞𝐫𝐲𝐭𝐡𝐢𝐧𝐠 𝐈’𝐦 𝐥𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫.",
    "𝐂𝐚𝐧 𝐲𝐨𝐮 𝐤𝐢𝐬𝐬 𝐦𝐞 𝐨𝐧 𝐭𝐡𝐞 𝐜𝐡𝐞𝐞𝐤 𝐬𝐨 𝐈 𝐜𝐚𝐧 𝐚𝐭 𝐥𝐞𝐚𝐬𝐭 𝐬𝐚𝐲 𝐚 𝐜𝐮𝐭𝐞 𝐠𝐢𝐫𝐥 𝐤𝐢𝐬𝐬𝐞𝐝 𝐦𝐞 𝐭𝐨𝐧𝐢𝐠𝐡𝐭?",
    "𝐈 𝐥𝐨𝐬𝐭 𝐦𝐲 𝐭𝐞𝐝𝐝𝐲 𝐛𝐞𝐚𝐫 𝐜𝐚𝐧 𝐢 𝐬𝐥𝐞𝐞𝐩 𝐰𝐢𝐭𝐡 𝐲𝐨𝐮 𝐭𝐨𝐧𝐢𝐠𝐡𝐭?",
    "𝐈’𝐦 𝐧𝐨 𝐨𝐫𝐠𝐚𝐧 𝐝𝐨𝐧𝐨𝐫 𝐛𝐮𝐭 𝐈’𝐝 𝐛𝐞 𝐡𝐚𝐩𝐩𝐲 𝐭𝐨 𝐠𝐢𝐯𝐞 𝐲𝐨𝐮 𝐦𝐲 𝐡𝐞𝐚𝐫𝐭.",
    "𝐈𝐟 𝐈 𝐡𝐚𝐝 𝐭𝐨 𝐫𝐚𝐭𝐞 𝐲𝐨𝐮 𝐨𝐮𝐭 𝐨𝐟 𝟏𝟎 𝐈’𝐝 𝐫𝐚𝐭𝐞 𝐲𝐨𝐮 𝐚 𝟗… 𝐛𝐞𝐜𝐚𝐮𝐬𝐞 𝐈 𝐚𝐦 𝐭𝐡𝐞 𝐨𝐧𝐞 𝐭𝐡𝐚𝐭 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐦𝐢𝐬𝐬𝐢𝐧𝐠",
    "𝐂𝐚𝐧 𝐈 𝐟𝐨𝐥𝐥𝐨𝐰 𝐲𝐨𝐮? 𝐂𝐚𝐮𝐬𝐞 𝐦𝐲 𝐦𝐨𝐦 𝐭𝐨𝐥𝐝 𝐦𝐞 𝐭𝐨 𝐟𝐨𝐥𝐥𝐨𝐰 𝐦𝐲 𝐝𝐫𝐞𝐚𝐦𝐬",
    "𝐘𝐨𝐮𝐫 𝐥𝐢𝐩𝐬 𝐥𝐨𝐨𝐤 𝐥𝐨𝐧𝐞𝐥𝐲 𝐰𝐨𝐮𝐥𝐝 𝐭𝐡𝐞𝐲 𝐥𝐢𝐤𝐞 𝐭𝐨 𝐦𝐞𝐞𝐭 𝐦𝐢𝐧𝐞?",
    "𝐓𝐡𝐞𝐫𝐞 𝐢𝐬𝐧’𝐭 𝐚 𝐰𝐨𝐫𝐝 𝐢𝐧 𝐭𝐡𝐞 𝐝𝐢𝐜𝐭𝐢𝐨𝐧𝐚𝐫𝐲 𝐭𝐨 𝐝𝐞𝐬𝐜𝐫𝐢𝐛𝐞 𝐡𝐨𝐰 𝐛𝐞𝐚𝐮𝐭𝐢𝐟𝐮𝐥 𝐲𝐨𝐮 𝐚𝐫𝐞",
    "𝐈 𝐡𝐚𝐯𝐞 𝐡𝐚𝐝 𝐚 𝐫𝐞𝐚𝐥𝐥𝐲 𝐛𝐚𝐝 𝐝𝐚𝐲 𝐚𝐧𝐝 𝐢𝐭 𝐚𝐥𝐰𝐚𝐲𝐬 𝐦𝐚𝐤𝐞𝐬 𝐦𝐞 𝐟𝐞𝐞𝐥 𝐛𝐞𝐭𝐭𝐞𝐫 𝐭𝐨 𝐬𝐞𝐞 𝐚 𝐩𝐫𝐞𝐭𝐭𝐲 𝐠𝐢𝐫𝐥 𝐬𝐦𝐢𝐥𝐞. 𝐒𝐨, 𝐰𝐨𝐮𝐥𝐝 𝐲𝐨𝐮 𝐬𝐦𝐢𝐥𝐞 𝐟𝐨𝐫 𝐦𝐞?",
]
# Command
FLIRT_COMMAND = ["flirt", "hflirt", "eflirt"]


@app.on_message(filters.command(FLIRT_COMMAND) & filters.group)
async def help(client: Client, message: Message):
    await message.reply_text(
        text=random.choice(FLIRT),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url=f"https://t.me/mlohvdryj"
                    ),
                    InlineKeyboardButton(
                        "𝙾𝙵𝙵𝙸𝙲𝙴", url=f"https://t.me/lolpagalokigc"
                    ),
                ]
            ]
        ),
    )


@app.on_message(filters.command(FLIRT_COMMAND) & filters.private)
async def help(client: Client, message: Message):
    await message.reply_text(
        text=random.choice(FLIRT),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url=f"https://t.me/mlohvdryj"
                    ),
                    InlineKeyboardButton(
                        "𝙾𝙵𝙵𝙸𝙲𝙴", url=f"https://t.me/lolpagalokigc"
                    ),
                ]
            ]
        ),
    )
