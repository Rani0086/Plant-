async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import random
import os
from config import OWNER_ID

SUDO_USERS = [7078181502, 6346273488, 7526369190, 5884969921]

GROUP = [-1002494871325, -1002119873436, -1001918533469, -1002009280180]

PORMS = [
        "https://telegra.ph/file/9bcc076fd81dfe3feb291.mp4",
        "https://telegra.ph/file/b7a1a42429a65f64e67af.mp4",
        "https://telegra.ph/file/dc3da5a3eb77ae20fa21d.mp4",
        "https://telegra.ph/file/22b89774a4ba9219d530b.mp4",
        "https://telegra.ph/file/7b15fbca08ae1e73e559c.mp4",
        "https://telegra.ph/file/a9c1dea3f34925bb60686.mp4",
        "https://telegra.ph/file/913b4e567b7f435b7f0db.mp4",
        "https://telegra.ph/file/5a5d1a919a97af2314955.mp4",
        "https://telegra.ph/file/0f8b903669600d304cbe4.mp4",
        "https://telegra.ph/file/f3816b54c9eb7617356b6.mp4",
        "https://telegra.ph/file/516dbaa03fde1aaa70633.mp4",
        "https://telegra.ph/file/07bba6ead0f1e381b1bd1.mp4",
        "https://telegra.ph/file/0a4f7935df9b4ab8d62ed.mp4",
        "https://telegra.ph/file/40966bf68c0e4dbe18058.mp4",
        "https://telegra.ph/file/50637aa9c04d136687523.mp4",
        "https://telegra.ph/file/b81c0b0e491da73e64260.mp4",
        "https://telegra.ph/file/4ddf5f29783d92ae03804.mp4",
        "https://telegra.ph/file/4037dc2517b702cc208b1.mp4",
        "https://telegra.ph/file/33cebe2798c15d52a2547.mp4",
        "https://telegra.ph/file/4dc3c8b03616da516104a.mp4",
        "https://telegra.ph/file/6b148dace4d987fae8f3e.mp4",
        "https://telegra.ph/file/8cb081db4eeed88767635.mp4",
        "https://telegra.ph/file/98d3eb94e6f00ed56ef91.mp4",
        "https://telegra.ph/file/1fb387cf99e057b62d75d.mp4",
        "https://telegra.ph/file/6e1161f63879c07a1f213.mp4",
        "https://telegra.ph/file/0bf4defb9540d2fa6d277.mp4",
        "https://telegra.ph/file/d5f8280754d9aa5dffa6a.mp4",
        "https://telegra.ph/file/0f23807ed1930704e2bef.jpg",
        "https://telegra.ph/file/c49280b8f1dcecaf86c00.jpg",
        "https://telegra.ph/file/f483400ff141de73767ca.jpg",
        "https://telegra.ph/file/1543bbea4e3c1abb6764a.jpg",
        "https://telegra.ph/file/a0d77be0d769c7cd334ab.jpg",
        "https://telegra.ph/file/6c6e93860527d2f577df8.jpg",
        "https://telegra.ph/file/d987b0e72eb3bb4801f01.jpg",
        "https://telegra.ph/file/b434999287d3580250960.jpg",
        "https://telegra.ph/file/0729cc082bf97347988f7.jpg",
        "https://telegra.ph/file/bb96d25df82178a2892e7.jpg",
        "https://telegra.ph/file/be73515791ea33be92a7d.jpg",
        "https://telegra.ph/file/fe234d6273093282d2dcc.jpg",
        "https://telegra.ph/file/66254bb72aa8094d38250.jpg",
        "https://telegra.ph/file/44bdaf37e5f7bdfc53ac6.jpg",
        "https://telegra.ph/file/e561ee1e1ca88db7e8038.jpg",
        "https://telegra.ph/file/f1960ccfc866b29ea5ad2.jpg",
        "https://telegra.ph/file/97622cad291472fb3c4aa.jpg",
        "https://telegra.ph/file/a46e316b413e9dc43e91b.jpg",
        "https://telegra.ph/file/497580fc3bddc21e0e162.jpg",
        "https://telegra.ph/file/3e86cc6cab06a6e2bde82.jpg",
        "https://telegra.ph/file/83140e2c57ddd95f310e6.jpg",
        "https://telegra.ph/file/2b20f8509d9437e94fed5.jpg",
        "https://telegra.ph/file/571960dcee4fce56698a4.jpg",
        "https://telegra.ph/file/25929a0b49452d8946c14.mp4",
        "https://telegra.ph/file/f5c9ceded3ee6e76a5931.jpg",
        "https://telegra.ph/file/a8bf6c6df8a48e4a306ca.jpg",
        "https://telegra.ph/file/af9e3f98da0bd937adf6e.jpg",
]

RAID = [ "𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐆𝐇𝐔𝐓𝐊𝐀 𝐊𝐇𝐀𝐀𝐊𝐄 𝐓𝐇𝐎𝐎𝐊 𝐃𝐔𝐍𝐆𝐀 🤣🤣", "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐍𝐇𝐈 𝐇𝐀𝐈 𝐊𝐘𝐀? 𝟗 𝐌𝐀𝐇𝐈𝐍𝐄 𝐑𝐔𝐊 𝐒𝐀𝐆𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐃𝐄𝐓𝐀 𝐇𝐔 🤣🤣🤩", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐄𝐑𝐎𝐏𝐋𝐀𝐍𝐄𝐏𝐀𝐑𝐊 𝐊𝐀𝐑𝐊𝐄 𝐔𝐃𝐀𝐀𝐍 𝐁𝐇𝐀𝐑 𝐃𝐔𝐆𝐀 ✈️🛫", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐔𝐓𝐋𝐈 𝐁𝐎𝐌𝐁 𝐅𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐉𝐇𝐀𝐀𝐓𝐄 𝐉𝐀𝐋 𝐊𝐄 𝐊𝐇𝐀𝐀𝐊 𝐇𝐎 𝐉𝐀𝐘𝐄𝐆𝐈💣", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐂𝐎𝐎𝐓𝐄𝐑 𝐃𝐀𝐀𝐋 𝐃𝐔𝐆𝐀👅", "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀", "𝐓𝐄𝐑𝐄 𝐁𝐄𝐇𝐄𝐍 𝐊 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐊𝐔 𝐃𝐀𝐀𝐋 𝐊𝐀𝐑 𝐂𝐇𝐔𝐓 𝐊𝐀 𝐊𝐇𝐎𝐎𝐍 𝐊𝐀𝐑 𝐃𝐔𝐆𝐀", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐀𝐊𝐓𝐄 🤱 𝐆𝐀𝐋𝐈 𝐊𝐄 𝐊𝐔𝐓𝐓𝐎 🦮 𝐌𝐄 𝐁𝐀𝐀𝐓 𝐃𝐔𝐍𝐆𝐀 𝐏𝐇𝐈𝐑 🍞 𝐁𝐑𝐄𝐀𝐃 𝐊𝐈 𝐓𝐀𝐑𝐇 𝐊𝐇𝐀𝐘𝐄𝐍𝐆𝐄 𝐖𝐎 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓", "𝐃𝐔𝐃𝐇 𝐇𝐈𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐄 𝐔𝐏𝐑 𝐍𝐈𝐂𝐇𝐄 🆙🆒😙", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 ✋ 𝐇𝐀𝐓𝐓𝐇 𝐃𝐀𝐋𝐊𝐄 👶 𝐁𝐀𝐂𝐂𝐇𝐄 𝐍𝐈𝐊𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 😍", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐊𝐄𝐋𝐄 𝐊𝐄 𝐂𝐇𝐈𝐋𝐊𝐄 🍌🍌😍", "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐋𝐀𝐆𝐀𝐀𝐔𝐍𝐆𝐀 𝐒𝐀𝐒𝐓𝐄 𝐒𝐏𝐀𝐌 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐃𝐇𝐀𝐍𝐃𝐇𝐄 𝐕𝐀𝐀𝐋𝐈 😋😛", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐂 𝐋𝐀𝐆𝐀 𝐃𝐔𝐍𝐆𝐀 𝐒𝐀𝐀𝐑𝐈 𝐆𝐀𝐑𝐌𝐈 𝐍𝐈𝐊𝐀𝐋 𝐉𝐀𝐀𝐘𝐄𝐆𝐈", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐇𝐎𝐑𝐋𝐈𝐂𝐊𝐒 𝐏𝐄𝐄𝐋𝐀𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😚", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐒𝐀𝐑𝐈𝐘𝐀 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐔𝐒𝐈 𝐒𝐀𝐑𝐈𝐘𝐄 𝐏𝐑 𝐓𝐀𝐍𝐆 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐇𝐎𝐍𝐆𝐄 😱😱", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐊𝐎𝐋𝐊𝐀𝐓𝐀 𝐕𝐀𝐀𝐋𝐄 𝐉𝐈𝐓𝐔 𝐁𝐇𝐀𝐈𝐘𝐀 𝐊𝐀 𝐋𝐔𝐍𝐃 𝐌𝐔𝐁𝐀𝐑𝐀𝐊 🤩🤩", "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐅𝐀𝐍𝐓𝐀𝐒𝐘 𝐇𝐔 𝐋𝐀𝐖𝐃𝐄, 𝐓𝐔 𝐀𝐏𝐍𝐈 𝐁𝐇𝐄𝐍 𝐊𝐎 𝐒𝐌𝐁𝐇𝐀𝐀𝐋 😈😈", "𝐓𝐄𝐑𝐀 𝐏𝐄𝐇𝐋𝐀 𝐁𝐀𝐀𝐏 𝐇𝐔 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 ", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐗𝐕𝐈𝐃𝐄𝐎𝐒.𝐂𝐎𝐌 𝐂𝐇𝐀𝐋𝐀 𝐊𝐄 𝐌𝐔𝐓𝐇 𝐌𝐀𝐀𝐑𝐔𝐍𝐆𝐀 🤡😹", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐆𝐑𝐎𝐔𝐏 𝐕𝐀𝐀𝐋𝐎𝐍 𝐒𝐀𝐀𝐓𝐇 𝐌𝐈𝐋𝐊𝐄 𝐆𝐀𝐍𝐆 𝐁𝐀𝐍𝐆 𝐊𝐑𝐔𝐍𝐆𝐀🙌🏻☠️ ", "𝐓𝐄𝐑𝐈 𝐈𝐓𝐄𝐌 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐋𝐔𝐍𝐃 𝐃𝐀𝐀𝐋𝐊𝐄,𝐓𝐄𝐑𝐄 𝐉𝐀𝐈𝐒𝐀 𝐄𝐊 𝐎𝐑 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃🤘🏻🙌🏻☠️ ", "𝐀𝐔𝐊𝐀𝐀𝐓 𝐌𝐄 𝐑𝐄𝐇 𝐕𝐑𝐍𝐀 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐃𝐀𝐍𝐃𝐀 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐌𝐔𝐇 𝐒𝐄 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐒𝐇𝐀𝐑𝐈𝐑 𝐁𝐇𝐈 𝐃𝐀𝐍𝐃𝐄 𝐉𝐄𝐒𝐀 𝐃𝐈𝐊𝐇𝐄𝐆𝐀 🙄🤭🤭", "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐄 𝐒𝐀𝐀𝐓𝐇 𝐋𝐔𝐃𝐎 𝐊𝐇𝐄𝐋𝐓𝐄 𝐊𝐇𝐄𝐋𝐓𝐄 𝐔𝐒𝐊𝐄 𝐌𝐔𝐇 𝐌𝐄 𝐀𝐏𝐍𝐀 𝐋𝐎𝐃𝐀 𝐃𝐄 𝐃𝐔𝐍𝐆𝐀☝🏻☝🏻😬", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐀𝐏𝐍𝐄 𝐋𝐔𝐍𝐃 𝐏𝐑 𝐈𝐓𝐍𝐀 𝐉𝐇𝐔𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐊𝐈 𝐉𝐇𝐔𝐋𝐓𝐄 𝐉𝐇𝐔𝐋𝐓𝐄 𝐇𝐈 𝐁𝐀𝐂𝐇𝐀 𝐏𝐀𝐈𝐃𝐀 𝐊𝐑 𝐃𝐄𝐆𝐈👀👯 ", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐁𝐀𝐓𝐓𝐄𝐑𝐘 𝐋𝐀𝐆𝐀 𝐊𝐄 𝐏𝐎𝐖𝐄𝐑𝐁𝐀𝐍𝐊 𝐁𝐀𝐍𝐀 𝐃𝐔𝐍𝐆𝐀 🔋 🔥🤩", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐂++ 𝐒𝐓𝐑𝐈𝐍𝐆 𝐄𝐍𝐂𝐑𝐘𝐏𝐓𝐈𝐎𝐍 𝐋𝐀𝐆𝐀 𝐃𝐔𝐍𝐆𝐀 𝐁𝐀𝐇𝐓𝐈 𝐇𝐔𝐘𝐈 𝐂𝐇𝐔𝐓 𝐑𝐔𝐊 𝐉𝐀𝐘𝐄𝐆𝐈𝐈𝐈𝐈😈🔥😍", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄𝐈 𝐉𝐇𝐀𝐀𝐃𝐔 𝐃𝐀𝐋 𝐊𝐄 𝐌𝐎𝐑 🦚 𝐁𝐀𝐍𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 🤩🥵😱", "𝐓𝐄𝐑𝐈 𝐂𝐇𝐔𝐓 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐇𝐎𝐔𝐋𝐃𝐄𝐑𝐈𝐍𝐆 𝐊𝐀𝐑 𝐃𝐔𝐍𝐆𝐀𝐀 𝐇𝐈𝐋𝐀𝐓𝐄 𝐇𝐔𝐘𝐄 𝐁𝐇𝐈 𝐃𝐀𝐑𝐃 𝐇𝐎𝐆𝐀𝐀𝐀😱🤮👺", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐑𝐄𝐃𝐈 𝐏𝐄 𝐁𝐀𝐈𝐓𝐇𝐀𝐋 𝐊𝐄 𝐔𝐒𝐒𝐄 𝐔𝐒𝐊𝐈 𝐂𝐇𝐔𝐓 𝐁𝐈𝐋𝐖𝐀𝐔𝐍𝐆𝐀𝐀 💰 😵🤩", "𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝟒 𝐇𝐎𝐋𝐄 𝐇𝐀𝐈 𝐔𝐍𝐌𝐄 𝐌𝐒𝐄𝐀𝐋 𝐋𝐀𝐆𝐀 𝐁𝐀𝐇𝐔𝐓 𝐁𝐀𝐇𝐄𝐓𝐈 𝐇𝐀𝐈 𝐁𝐇𝐎𝐅𝐃𝐈𝐊𝐄👊🤮🤢🤢", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐁𝐀𝐑𝐆𝐀𝐃 𝐊𝐀 𝐏𝐄𝐃 𝐔𝐆𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐂𝐎𝐑𝐎𝐍𝐀 𝐌𝐄𝐈 𝐒𝐀𝐁 𝐎𝐗𝐘𝐆𝐄𝐍 𝐋𝐄𝐊𝐀𝐑 𝐉𝐀𝐘𝐄𝐍𝐆𝐄🤢🤩🥳", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐔𝐃𝐎 𝐋𝐀𝐆𝐀 𝐊𝐄 𝐁𝐈𝐆𝐒𝐏𝐀𝐌 𝐋𝐀𝐆𝐀 𝐊𝐄 𝟗𝟗𝟗𝟗 𝐅𝐔𝐂𝐊 𝐋𝐀𝐆𝐀𝐀 𝐃𝐔 🤩🥳🔥", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐌𝐄𝐈 𝐁𝐄𝐒𝐀𝐍 𝐊𝐄 𝐋𝐀𝐃𝐃𝐔 𝐁𝐇𝐀𝐑 𝐃𝐔𝐍𝐆𝐀🤩🥳🔥😈", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐇𝐎𝐃 𝐊𝐄 𝐔𝐒𝐌𝐄 𝐂𝐘𝐋𝐈𝐍𝐃𝐄𝐑 ⛽️ 𝐅𝐈𝐓 𝐊𝐀𝐑𝐊𝐄 𝐔𝐒𝐌𝐄𝐄 𝐃𝐀𝐋 𝐌𝐀𝐊𝐇𝐀𝐍𝐈 𝐁𝐀𝐍𝐀𝐔𝐍𝐆𝐀𝐀𝐀🤩👊🔥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐒𝐇𝐄𝐄𝐒𝐇𝐀 𝐃𝐀𝐋 𝐃𝐔𝐍𝐆𝐀𝐀𝐀 𝐀𝐔𝐑 𝐂𝐇𝐀𝐔𝐑𝐀𝐇𝐄 𝐏𝐄 𝐓𝐀𝐀𝐍𝐆 𝐃𝐔𝐍𝐆𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄😈😱🤩", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐂𝐑𝐄𝐃𝐈𝐓 𝐂𝐀𝐑𝐃 𝐃𝐀𝐋 𝐊𝐄 𝐀𝐆𝐄 𝐒𝐄 𝟓𝟎𝟎 𝐊𝐄 𝐊𝐀𝐀𝐑𝐄 𝐊𝐀𝐀𝐑𝐄 𝐍𝐎𝐓𝐄 𝐍𝐈𝐊𝐀𝐋𝐔𝐍𝐆𝐀𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄💰💰🤩", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐒𝐀𝐓𝐇 𝐒𝐔𝐀𝐑 𝐊𝐀 𝐒𝐄𝐗 𝐊𝐀𝐑𝐖𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐄𝐊 𝐒𝐀𝐓𝐇 𝟔-𝟔 𝐁𝐀𝐂𝐇𝐄 𝐃𝐄𝐆𝐈💰🔥😱", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐀𝐏𝐏𝐋𝐄 𝐊𝐀 𝟏𝟖𝐖 𝐖𝐀𝐋𝐀 𝐂𝐇𝐀𝐑𝐆𝐄𝐑 🔥🤩", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄𝐈 𝐎𝐍𝐄𝐏𝐋𝐔𝐒 𝐊𝐀 𝐖𝐑𝐀𝐏 𝐂𝐇𝐀𝐑𝐆𝐄𝐑 𝟑𝟎𝐖 𝐇𝐈𝐆𝐇 𝐏𝐎𝐖𝐄𝐑 💥😂😎", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐎 𝐀𝐌𝐀𝐙𝐎𝐍 𝐒𝐄 𝐎𝐑𝐃𝐄𝐑 𝐊𝐀𝐑𝐔𝐍𝐆𝐀 𝟏𝟎 𝐫𝐬 𝐌𝐄𝐈 𝐀𝐔𝐑 𝐅𝐋𝐈𝐏𝐊𝐀𝐑𝐓 𝐏𝐄 𝟐𝟎 𝐑𝐒 𝐌𝐄𝐈 𝐁𝐄𝐂𝐇 𝐃𝐔𝐍𝐆𝐀🤮👿😈🤖", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐁𝐀𝐃𝐈 𝐁𝐇𝐔𝐍𝐃 𝐌𝐄 𝐙𝐎𝐌𝐀𝐓𝐎 𝐃𝐀𝐋 𝐊𝐄 𝐒𝐔𝐁𝐖𝐀𝐘 𝐊𝐀 𝐁𝐅𝐅 𝐕𝐄𝐆 𝐒𝐔𝐁 𝐂𝐎𝐌𝐁𝐎 [𝟏𝟓𝐜𝐦 , 𝟏𝟔 𝐢𝐧𝐜𝐡𝐞𝐬 ] 𝐎𝐑𝐃𝐄𝐑 𝐂𝐎𝐃 𝐊𝐑𝐕𝐀𝐔𝐍𝐆𝐀 𝐎𝐑 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐉𝐀𝐁 𝐃𝐈𝐋𝐈𝐕𝐄𝐑𝐘 𝐃𝐄𝐍𝐄 𝐀𝐘𝐄𝐆𝐈 𝐓𝐀𝐁 𝐔𝐒𝐏𝐄 𝐉𝐀𝐀𝐃𝐔 𝐊𝐑𝐔𝐍𝐆𝐀 𝐎𝐑 𝐅𝐈𝐑 𝟗 𝐌𝐎𝐍𝐓𝐇 𝐁𝐀𝐀𝐃 𝐕𝐎 𝐄𝐊 𝐎𝐑 𝐅𝐑𝐄𝐄 𝐃𝐈𝐋𝐈𝐕𝐄𝐑𝐘 𝐃𝐄𝐆𝐈🙀👍🥳🔥", "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐀𝐀𝐋𝐈🙁🤣💥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐂𝐇𝐀𝐍𝐆𝐄𝐒 𝐂𝐎𝐌𝐌𝐈𝐓 𝐊𝐑𝐔𝐆𝐀 𝐅𝐈𝐑 𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐀𝐔𝐓𝐎𝐌𝐀𝐓𝐈𝐂𝐀𝐋𝐋𝐘 𝐔𝐏𝐃𝐀𝐓𝐄 𝐇𝐎𝐉𝐀𝐀𝐘𝐄𝐆𝐈🤖🙏🤔", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐔𝐒𝐈 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐈𝐍𝐃𝐈𝐀𝐍 𝐑𝐀𝐈𝐋𝐖𝐀𝐘 🚂💥😂", "𝐓𝐔 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐓𝐄𝐑𝐀 𝐊𝐇𝐀𝐍𝐃𝐀𝐍 𝐒𝐀𝐁 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐖𝐃𝐄 𝐑𝐀𝐍𝐃𝐈 𝐇𝐀𝐈 𝐑𝐀𝐍𝐃𝐈 🤢✅🔥", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐈𝐎𝐍𝐈𝐂 𝐁𝐎𝐍𝐃 𝐁𝐀𝐍𝐀 𝐊𝐄 𝐕𝐈𝐑𝐆𝐈𝐍𝐈𝐓𝐘 𝐋𝐎𝐎𝐒𝐄 𝐊𝐀𝐑𝐖𝐀 𝐃𝐔𝐍𝐆𝐀 𝐔𝐒𝐊𝐈 📚 😎🤩", "𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇𝐍𝐀 𝐁𝐀𝐀𝐏 𝐊𝐀 𝐍𝐀𝐀𝐌 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄𝐄𝐄𝐄𝐄 🤩🥳😳", "𝐓𝐔 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐃𝐎𝐍𝐎 𝐊𝐈 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐌𝐄𝐓𝐑𝐎 𝐂𝐇𝐀𝐋𝐖𝐀 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐗𝐇𝐎𝐃 🚇🤩😱🥶", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐁𝐇𝐈 𝐔𝐒𝐊𝐎 𝐏𝐀𝐇𝐂𝐇𝐀𝐍𝐀𝐍𝐄 𝐒𝐄 𝐌𝐀𝐍𝐀 𝐊𝐀𝐑 𝐃𝐄𝐆𝐀😂👿🤩", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐇𝐀𝐈𝐑 𝐃𝐑𝐘𝐄𝐑 𝐂𝐇𝐀𝐋𝐀 𝐃𝐔𝐍𝐆𝐀𝐀💥🔥🔥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐊𝐈 𝐒𝐀𝐑𝐈 𝐑𝐀𝐍𝐃𝐈𝐘𝐎𝐍 𝐊𝐀 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐀 𝐊𝐇𝐎𝐋 𝐃𝐔𝐍𝐆𝐀𝐀👿🤮😎", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐀𝐋𝐄𝐗𝐀 𝐃𝐀𝐋 𝐊𝐄𝐄 𝐃𝐉 𝐁𝐀𝐉𝐀𝐔𝐍𝐆𝐀𝐀𝐀 🎶 ⬆️🤩💥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐆𝐈𝐓𝐇𝐔𝐁 𝐃𝐀𝐋 𝐊𝐄 𝐀𝐏𝐍𝐀 𝐁𝐎𝐓 𝐇𝐎𝐒𝐓 𝐊𝐀𝐑𝐔𝐍𝐆𝐀𝐀 🤩👊👤😍", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐕𝐏𝐒 𝐁𝐀𝐍𝐀 𝐊𝐄 𝟐𝟒*𝟕 𝐁𝐀𝐒𝐇 𝐂𝐇𝐔𝐃𝐀𝐈 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐃𝐄 𝐃𝐔𝐍𝐆𝐀𝐀 🤩💥🔥🔥", "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐓𝐄𝐑𝐄 𝐋𝐀𝐍𝐃 𝐊𝐎 𝐃𝐀𝐋 𝐊𝐄 𝐊𝐀𝐀𝐓 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 🔪😂🔥", "𝐒𝐔𝐍 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐈 𝐁𝐇𝐎𝐒𝐃𝐀 👿😎👊", "𝐓𝐔𝐉𝐇𝐄 𝐃𝐄𝐊𝐇 𝐊𝐄 𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐁𝐀𝐇𝐄𝐍 𝐏𝐄 𝐓𝐀𝐑𝐀𝐒 𝐀𝐓𝐀 𝐇𝐀𝐈 𝐌𝐔𝐉𝐇𝐄 𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄𝐄𝐄𝐄 👿💥🤩🔥", "𝐒𝐔𝐍 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐉𝐘𝐀𝐃𝐀 𝐍𝐀 𝐔𝐂𝐇𝐀𝐋 𝐌𝐀𝐀 𝐂𝐇𝐎𝐃 𝐃𝐄𝐍𝐆𝐄 𝐄𝐊 𝐌𝐈𝐍 𝐌𝐄𝐈 ✅🤣🔥🤩", "𝐀𝐏𝐍𝐈 𝐀𝐌𝐌𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇𝐍𝐀 𝐔𝐒𝐊𝐎 𝐔𝐒 𝐊𝐀𝐀𝐋𝐈 𝐑𝐀𝐀𝐓 𝐌𝐄𝐈 𝐊𝐀𝐔𝐍𝐂𝐇𝐎𝐃𝐍𝐄𝐄 𝐀𝐘𝐀 𝐓𝐇𝐀𝐀𝐀! 𝐓𝐄𝐑𝐄 𝐈𝐒 𝐏𝐀𝐏𝐀 𝐊𝐀 𝐍𝐀𝐀𝐌 𝐋𝐄𝐆𝐈 😂👿😳", "𝐓𝐎𝐇𝐀𝐑 𝐁𝐀𝐇𝐈𝐍 𝐂𝐇𝐎𝐃𝐔 𝐁𝐁𝐀𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐖𝐃𝐄 𝐔𝐒𝐌𝐄 𝐌𝐈𝐓𝐓𝐈 𝐃𝐀𝐋 𝐊𝐄 𝐂𝐄𝐌𝐄𝐍𝐓 𝐒𝐄 𝐁𝐇𝐀𝐑 𝐃𝐔 🏠🤢🤩💥", "𝐓𝐔𝐉𝐇𝐄 𝐀𝐁 𝐓𝐀𝐊 𝐍𝐀𝐇𝐈 𝐒𝐌𝐉𝐇 𝐀𝐘𝐀 𝐊𝐈 𝐌𝐀𝐈 𝐇𝐈 𝐇𝐔 𝐓𝐔𝐉𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐊𝐀𝐑𝐍𝐄 𝐖𝐀𝐋𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄𝐄 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀 𝐒𝐄 𝐏𝐔𝐂𝐇 𝐑𝐀𝐍𝐃𝐈 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄𝐄𝐄𝐄 🤩👊👤😍", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄𝐈 𝐒𝐏𝐎𝐓𝐈𝐅𝐘 𝐃𝐀𝐋 𝐊𝐄", "𝐋𝐎𝐅𝐈 𝐁𝐀𝐉𝐀𝐔𝐍𝐆𝐀 𝐃𝐈𝐍 𝐁𝐇𝐀𝐑 😍🎶🎶💥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐍𝐀𝐘𝐀 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐀 𝐊𝐇𝐎𝐋𝐔𝐍𝐆𝐀 𝐂𝐇𝐈𝐍𝐓𝐀 𝐌𝐀𝐓 𝐊𝐀𝐑 👊🤣🤣😳", "𝐓𝐄𝐑𝐀 𝐁𝐀𝐀𝐏 𝐇𝐔 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐑𝐀𝐍𝐃𝐈 𝐊𝐇𝐀𝐍𝐄 𝐏𝐄 𝐂𝐇𝐔𝐃𝐖𝐀 𝐊𝐄 𝐔𝐒 𝐏𝐀𝐈𝐒𝐄 𝐊𝐈 𝐃𝐀𝐀𝐑𝐔 𝐏𝐄𝐄𝐓𝐀 𝐇𝐔 🍷🤩🔥", "𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐀𝐏𝐍𝐀 𝐁𝐀𝐃𝐀 𝐒𝐀 𝐋𝐎𝐃𝐀 𝐆𝐇𝐔𝐒𝐒𝐀 𝐃𝐔𝐍𝐆𝐀𝐀 𝐊𝐀𝐋𝐋𝐀𝐀𝐏 𝐊𝐄 𝐌𝐀𝐑 𝐉𝐀𝐘𝐄𝐆𝐈 🤩😳😳🔥", "𝐓𝐎𝐇𝐀𝐑 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄𝐈 𝐏𝐔𝐑𝐈 𝐊𝐈 𝐏𝐔𝐑𝐈 𝐊𝐈𝐍𝐆𝐅𝐈𝐒𝐇𝐄𝐑 𝐊𝐈 𝐁𝐎𝐓𝐓𝐋𝐄 𝐃𝐀𝐋 𝐊𝐄 𝐓𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐀𝐍𝐃𝐄𝐑 𝐇𝐈 😱😂🤩", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐎 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐊𝐈 𝐒𝐀𝐏𝐍𝐄 𝐌𝐄𝐈 𝐁𝐇𝐈 𝐌𝐄𝐑𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐘𝐀𝐀𝐃 𝐊𝐀𝐑𝐄𝐆𝐈 𝐑𝐀𝐍𝐃𝐈 🥳😍👊💥", "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐀𝐔𝐑 𝐁𝐀𝐇𝐄𝐍 𝐊𝐎 𝐃𝐀𝐔𝐃𝐀 𝐃𝐀𝐔𝐃𝐀 𝐍𝐄 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐔𝐍𝐊𝐄 𝐍𝐎 𝐁𝐎𝐋𝐍𝐄 𝐏𝐄 𝐁𝐇𝐈 𝐋𝐀𝐍𝐃 𝐆𝐇𝐔𝐒𝐀 𝐃𝐔𝐍𝐆𝐀 𝐀𝐍𝐃𝐄𝐑 𝐓𝐀𝐊 😎😎🤣🔥", "𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐊𝐎 𝐎𝐍𝐋𝐈𝐍𝐄 𝐎𝐋𝐗 𝐏𝐄 𝐁𝐄𝐂𝐇𝐔𝐍𝐆𝐀 𝐀𝐔𝐑 𝐏𝐀𝐈𝐒𝐄 𝐒𝐄 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐊𝐎𝐓𝐇𝐀 𝐊𝐇𝐎𝐋 𝐃𝐔𝐍𝐆𝐀 😎🤩😝😍", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐀 𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐊𝐈 𝐓𝐔 𝐂𝐀𝐇 𝐊𝐄 𝐁𝐇𝐈 𝐖𝐎 𝐌𝐀𝐒𝐓 𝐂𝐇𝐔𝐃𝐀𝐈 𝐒𝐄 𝐃𝐔𝐑 𝐍𝐇𝐈 𝐉𝐀 𝐏𝐀𝐘𝐄𝐆𝐀𝐀 😏😏🤩😍", "𝐒𝐔𝐍 𝐁𝐄 𝐑𝐀𝐍𝐃𝐈 𝐊𝐈 𝐀𝐔𝐋𝐀𝐀𝐃 𝐓𝐔 𝐀𝐏𝐍𝐈 𝐁𝐀𝐇𝐄𝐍 𝐒𝐄 𝐒𝐄𝐄𝐊𝐇 𝐊𝐔𝐂𝐇 𝐊𝐀𝐈𝐒𝐄 𝐆𝐀𝐀𝐍𝐃 𝐌𝐀𝐑𝐖𝐀𝐓𝐄 𝐇𝐀𝐈😏🤬🔥💥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐀 𝐘𝐀𝐀𝐑 𝐇𝐔 𝐌𝐄𝐈 𝐀𝐔𝐑 𝐓𝐄𝐑𝐈 𝐁𝐀𝐇𝐄𝐍 𝐊𝐀 𝐏𝐘𝐀𝐀𝐑 𝐇𝐔 𝐌𝐄𝐈 𝐀𝐉𝐀 𝐌𝐄𝐑𝐀 𝐋𝐀𝐍𝐃 𝐂𝐇𝐎𝐎𝐒 𝐋𝐄 🤩🤣💥", "𝐓𝐄𝐑𝐈 𝐁𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐋𝐀𝐆𝐀𝐀𝐔𝐍𝐆𝐀 𝐒𝐀𝐒𝐓𝐄 𝐒𝐏𝐀𝐌 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐒𝐀𝐑𝐈𝐘𝐀 𝐃𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐔𝐒𝐈 𝐒𝐀𝐑𝐈𝐘𝐄 𝐏𝐑 𝐓𝐀𝐍𝐆 𝐊𝐄 𝐁𝐀𝐂𝐇𝐄 𝐏𝐀𝐈𝐃𝐀 𝐇𝐎𝐍𝐆𝐄 😱😱", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 ✋ 𝐇𝐀𝐓𝐓𝐇 𝐃𝐀𝐋𝐊𝐄 👶 𝐁𝐀𝐂𝐂𝐇𝐄 𝐍𝐈𝐊𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 😍", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐊𝐄𝐋𝐄 𝐊𝐄 𝐂𝐇𝐈𝐋𝐊𝐄 🤤🤤", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐂𝐇𝐔𝐓 𝐌𝐄 𝐒𝐔𝐓𝐋𝐈 𝐁𝐎𝐌𝐁 𝐅𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐊𝐈 𝐉𝐇𝐀𝐀𝐓𝐄 𝐉𝐀𝐋 𝐊𝐄 𝐊𝐇𝐀𝐀𝐊 𝐇𝐎 𝐉𝐀𝐘𝐄𝐆𝐈💣💋", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐇𝐎𝐑𝐋𝐈𝐂𝐊𝐒 𝐏𝐄𝐄𝐋𝐀𝐊𝐄 𝐂𝐇𝐎𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😚", "𝐓𝐄𝐑𝐈 𝐈𝐓𝐄𝐌 𝐊𝐈 𝐆𝐀𝐀𝐍𝐃 𝐌𝐄 𝐋𝐔𝐍𝐃 𝐃𝐀𝐀𝐋𝐊𝐄,𝐓𝐄𝐑𝐄 𝐉𝐀𝐈𝐒𝐀 𝐄𝐊 𝐎𝐑 𝐍𝐈𝐊𝐀𝐀𝐋 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃😆🤤💋", "𝐓𝐄𝐑𝐈 𝐕𝐀𝐇𝐄𝐄𝐍 𝐊𝐎 𝐀𝐏𝐍𝐄 𝐋𝐔𝐍𝐃 𝐏𝐑 𝐈𝐓𝐍𝐀 𝐉𝐇𝐔𝐋𝐀𝐀𝐔𝐍𝐆𝐀 𝐊𝐈 𝐉𝐇𝐔𝐋𝐓𝐄 𝐉𝐇𝐔𝐋𝐓𝐄 𝐇𝐈 𝐁𝐀𝐂𝐇𝐀 𝐏𝐀𝐈𝐃𝐀 𝐊𝐑 𝐃𝐄𝐆𝐈 💦💋", "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐒𝐀𝐃𝐀𝐊 𝐏𝐑 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 😂😆🤤", "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐑 𝐏𝐈𝐋𝐋𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔 😼😂🤤", "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐍𝐄 𝐒𝐇𝐎𝐑 𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 𝐑𝐀𝐍𝐃𝐈 𝐂𝐇𝐎𝐑 𝐇𝐄 💋💋💦", "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 😂👻🔥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐀𝐈𝐒𝐄 𝐂𝐇𝐎𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐃 𝐏𝐄𝐇𝐈 𝐌𝐔𝐓𝐇 𝐃𝐈𝐀 💦💦💦💦", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐁𝐇𝐎𝐒𝐃𝐄 𝐌𝐄 𝐀𝐀𝐀𝐆 𝐋𝐀𝐆𝐀𝐃𝐈𝐀 𝐌𝐄𝐑𝐀 𝐌𝐎𝐓𝐀 𝐋𝐔𝐍𝐃 𝐃𝐀𝐋𝐊𝐄 🔥🔥💦😆😆", "𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐂𝐇𝐀𝐋 𝐍𝐈𝐊𝐀𝐋", "𝐊𝐈𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐁𝐇𝐄𝐉 😆👻🤤", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎𝐓𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐏𝐔𝐑𝐀 𝐅𝐀𝐀𝐃 𝐃𝐈𝐀 𝐂𝐇𝐔𝐓𝐇 𝐀𝐁𝐁 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉 😆💦🤤", "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐊𝐎 𝐄𝐓𝐍𝐀 𝐂𝐇𝐎𝐃𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐆𝐅 𝐓𝐎 𝐌𝐄𝐑𝐈 𝐑𝐀𝐍𝐃𝐈 𝐁𝐀𝐍𝐆𝐀𝐘𝐈 𝐀𝐁𝐁 𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃𝐓𝐀 𝐅𝐈𝐑𝐒𝐄 ♥️💦😆😆😆😆", "𝐇𝐀𝐑𝐈 𝐇𝐀𝐑𝐈 𝐆𝐇𝐀𝐀𝐒 𝐌𝐄 𝐉𝐇𝐎𝐏𝐃𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 🤣🤣💋💦", "𝐂𝐇𝐀𝐋 𝐓𝐄𝐑𝐄 𝐁𝐀𝐀𝐏 𝐊𝐎 𝐁𝐇𝐄𝐉 𝐓𝐄𝐑𝐀 𝐁𝐀𝐒𝐊𝐀 𝐍𝐇𝐈 𝐇𝐄 𝐏𝐀𝐏𝐀 𝐒𝐄 𝐋𝐀𝐃𝐄𝐆𝐀 𝐓𝐔", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐁𝐎𝐌𝐁 𝐃𝐀𝐋𝐊𝐄 𝐔𝐃𝐀 𝐃𝐔𝐍𝐆𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐀𝐖𝐃𝐄", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐓𝐑𝐀𝐈𝐍 𝐌𝐄 𝐋𝐄𝐉𝐀𝐊𝐄 𝐓𝐎𝐏 𝐁𝐄𝐃 𝐏𝐄 𝐋𝐈𝐓𝐀𝐊𝐄 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 🤣🤣💋💋", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐄 𝐍𝐔𝐃𝐄𝐒 𝐆𝐎𝐎𝐆𝐋𝐄 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐋𝐀𝐄𝐖𝐃𝐄 👻🔥", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐕𝐈𝐃𝐄𝐎 𝐁𝐀𝐍𝐀𝐊𝐄 𝐗𝐍𝐗𝐗.𝐂𝐎𝐌 𝐏𝐄 𝐍𝐄𝐄𝐋𝐀𝐌 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐊𝐔𝐓𝐓𝐄 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦💋", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐊𝐎 𝐏𝐎𝐑𝐍𝐇𝐔𝐁.𝐂𝐎𝐌 𝐏𝐄 𝐔𝐏𝐋𝐎𝐀𝐃 𝐊𝐀𝐑𝐃𝐔𝐍𝐆𝐀 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐂𝐇𝐎𝐃𝐄 🤣💋💦", "𝐀𝐁𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐄𝐊𝐎 𝐂𝐇𝐀𝐊𝐊𝐎 𝐒𝐄 𝐏𝐈𝐋𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 🤣🤣", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐅𝐀𝐀𝐃𝐊𝐄 𝐑𝐀𝐊𝐃𝐈𝐀 𝐌𝐀𝐀𝐊𝐄 𝐋𝐎𝐃𝐄 𝐉𝐀𝐀 𝐀𝐁𝐁 𝐒𝐈𝐋𝐖𝐀𝐋𝐄 👄👄", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐔𝐍𝐃 𝐊𝐀𝐀𝐋𝐀", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐋𝐄𝐓𝐈 𝐌𝐄𝐑𝐈 𝐋𝐔𝐍𝐃 𝐁𝐀𝐃𝐄 𝐌𝐀𝐒𝐓𝐈 𝐒𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐎 𝐌𝐄𝐍𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐁𝐎𝐇𝐎𝐓 𝐒𝐀𝐒𝐓𝐄 𝐒𝐄", "𝐁𝐄𝐓𝐄 𝐓𝐔 𝐁𝐀𝐀𝐏 𝐒𝐄 𝐋𝐄𝐆𝐀 𝐏𝐀𝐍𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀 𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐔𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄 𝐍𝐀𝐍𝐆𝐀 💦💋", "𝐇𝐀𝐇𝐀𝐇𝐀𝐇 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐀𝐆𝐋𝐈 𝐁𝐀𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐓 𝐎𝐑 𝐌𝐄𝐑𝐄 𝐌𝐎𝐓𝐄 𝐋𝐔𝐍𝐃 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑", "𝐂𝐇𝐀𝐋 𝐁𝐄𝐓𝐀 𝐓𝐔𝐉𝐇𝐄 𝐌𝐀𝐀𝐅 𝐊𝐈𝐀 🤣 𝐀𝐁𝐁 𝐀𝐏𝐍𝐈 𝐆𝐅 𝐊𝐎 𝐁𝐇𝐄𝐉", "𝐒𝐇𝐀𝐑𝐀𝐌 𝐊𝐀𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐊𝐈𝐓𝐍𝐀 𝐆𝐀𝐀𝐋𝐈𝐀 𝐒𝐔𝐍𝐖𝐀𝐘𝐄𝐆𝐀 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐀 𝐁𝐄𝐇𝐄𝐍 𝐊𝐄 𝐔𝐏𝐄𝐑", "𝐀𝐁𝐄 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐁𝐀𝐂𝐇𝐇𝐄 𝐀𝐔𝐊𝐀𝐓 𝐍𝐇𝐈 𝐇𝐄𝐓𝐎 𝐀𝐏𝐍𝐈 𝐑𝐀𝐍𝐃𝐈 𝐌𝐀𝐀𝐊𝐎 𝐋𝐄𝐊𝐄 𝐀𝐀𝐘𝐀 𝐌𝐀𝐓𝐇 𝐊𝐀𝐑 𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀", "𝐊𝐈𝐃𝐙 𝐌𝐀𝐃𝐀𝐑𝐂𝐇𝐎𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐂𝐇𝐎𝐃𝐊𝐄 𝐓𝐄𝐑𝐑 𝐋𝐈𝐘𝐄 𝐁𝐇𝐀𝐈 𝐃𝐄𝐃𝐈𝐘𝐀", "𝐉𝐔𝐍𝐆𝐋𝐄 𝐌𝐄 𝐍𝐀𝐂𝐇𝐓𝐀 𝐇𝐄 𝐌𝐎𝐑𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐃𝐀𝐈 𝐃𝐄𝐊𝐊𝐄 𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 𝐎𝐍𝐂𝐄 𝐌𝐎𝐑𝐄 🤣🤣💦💋", "𝐆𝐀𝐋𝐈 𝐆𝐀𝐋𝐈 𝐌𝐄 𝐑𝐄𝐇𝐓𝐀 𝐇𝐄 𝐒𝐀𝐍𝐃 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 𝐎𝐑 𝐁𝐀𝐍𝐀 𝐃𝐈𝐀 𝐑𝐀𝐍𝐃 🤤🤣", "𝐒𝐀𝐁 𝐁𝐎𝐋𝐓𝐄 𝐌𝐔𝐉𝐇𝐊𝐎 𝐏𝐀𝐏𝐀 𝐊𝐘𝐎𝐔𝐍𝐊𝐈 𝐌𝐄𝐍𝐄 𝐁𝐀𝐍𝐀𝐃𝐈𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐏𝐑𝐄𝐆𝐍𝐄𝐍𝐓 🤣🤣", "𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐒𝐔𝐀𝐑 𝐊𝐀 𝐋𝐎𝐔𝐃𝐀 𝐎𝐑 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐄𝐑𝐀 𝐋𝐎𝐃𝐀", "𝐂𝐇𝐀𝐋 𝐂𝐇𝐀𝐋 𝐀𝐏𝐍𝐈 𝐌𝐀𝐀𝐊𝐈 𝐂𝐇𝐔𝐂𝐇𝐈𝐘𝐀 𝐃𝐈𝐊𝐀", "𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀 𝐁𝐀𝐂𝐇𝐇𝐄 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐀𝐊𝐎 𝐂𝐇𝐎𝐃 𝐃𝐈𝐀 𝐍𝐀𝐍𝐆𝐀 𝐊𝐀𝐑𝐊𝐄", "𝐓𝐄𝐑𝐈 𝐆𝐅 𝐇𝐄 𝐁𝐀𝐃𝐈 𝐒𝐄𝐗𝐘 𝐔𝐒𝐊𝐎 𝐏𝐈𝐋𝐀𝐊𝐄 𝐂𝐇𝐎𝐎𝐃𝐄𝐍𝐆𝐄 𝐏𝐄𝐏𝐒𝐈", "𝟐 𝐑𝐔𝐏𝐀𝐘 𝐊𝐈 𝐏𝐄𝐏𝐒𝐈 𝐓𝐄𝐑𝐈 𝐌𝐔𝐌𝐌𝐘 𝐒𝐀𝐁𝐒𝐄 𝐒𝐄𝐗𝐘 💋💦", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐂𝐇𝐄𝐄𝐌𝐒 𝐒𝐄 𝐂𝐇𝐔𝐃𝐖𝐀𝐕𝐔𝐍𝐆𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐎𝐃 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💦🤣", "𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐈 𝐂𝐇𝐔𝐓𝐇 𝐌𝐄 𝐌𝐔𝐓𝐇𝐊𝐄 𝐅𝐀𝐑𝐀𝐑 𝐇𝐎𝐉𝐀𝐕𝐔𝐍𝐆𝐀 𝐇𝐔𝐈 𝐇𝐔𝐈 𝐇𝐔𝐈", "𝐒𝐏𝐄𝐄𝐃 𝐋𝐀𝐀𝐀 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐂𝐇𝐎𝐃𝐔 𝐑𝐀𝐍𝐃𝐈𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 💋💦🤣", "𝐀𝐑𝐄 𝐑𝐄 𝐌𝐄𝐑𝐄 𝐁𝐄𝐓𝐄 𝐊𝐘𝐎𝐔𝐍 𝐒𝐏𝐄𝐄𝐃 𝐏𝐀𝐊𝐀𝐃 𝐍𝐀 𝐏𝐀𝐀𝐀 𝐑𝐀𝐇𝐀 𝐀𝐏𝐍𝐄 𝐁𝐀𝐀𝐏 𝐊𝐀 𝐇𝐀𝐇𝐀𝐇🤣🤣", "𝐒𝐔𝐍 𝐒𝐔𝐍 𝐒𝐔𝐀𝐑 𝐊𝐄 𝐏𝐈𝐋𝐋𝐄 𝐉𝐇𝐀𝐍𝐓𝐎 𝐊𝐄 𝐒𝐎𝐔𝐃𝐀𝐆𝐀𝐑 𝐀𝐏𝐍𝐈 𝐌𝐔𝐌𝐌𝐘 𝐊𝐈 𝐍𝐔𝐃𝐄𝐒 𝐁𝐇𝐄𝐉", "𝐀𝐁𝐄 𝐒𝐔𝐍 𝐋𝐎𝐃𝐄 𝐓𝐄𝐑𝐈 𝐁𝐄𝐇𝐄𝐍 𝐊𝐀 𝐁𝐇𝐎𝐒𝐃𝐀 𝐅𝐀𝐀𝐃 𝐃𝐔𝐍𝐆𝐀", "𝐓𝐄𝐑𝐈 𝐌𝐀𝐀𝐊𝐎 𝐊𝐇𝐔𝐋𝐄 𝐁𝐀𝐉𝐀𝐑 𝐌𝐄 𝐂𝐇𝐎𝐃 𝐃𝐀𝐋𝐀 🤣🤣💋", ]

RiZoeLX = [7526369190, 6346273488, 7078181502, 5884969921]

async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}spam <count> <message to spam>\n\n{hl}spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Rizoel) == 2:
            message = str(Rizoel[1])
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoel[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}bigspam <count> <message to spam>\n\n{hl}bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(rizoel) == 2:
            message = str(rizoel[1])
            counter = int(rizoel[0])
            for _ in range(counter):
                 async with e.client.action(e.chat_id, "typing"):
                     if e.reply_to_msg_id:
                          await smex.reply(message)
                     else:
                          await e.client.send_message(e.chat_id, message)
                 await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n{hl}delayspam <sleep time> <count> <message to spam>\n\n{hl}delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Rizoelsexy = Rizoel[1:]
        if len(Rizoelsexy) == 2:
            message = str(Rizoelsexy[1])
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Rizoelsexy[0])
            sleeptime = float(Rizoel[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)



async def pspam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(rizoel) == 1:
            counter = int(rizoel[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `{hl}pornspam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )

async def hang(e):
    usage = f"**MODULE NAME : HANG SPAM** \n\n Cmd : `{hl}hang <count>`"
    if e.sender_id in SUDO_USERS:
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(RiZoeL) == 1:
            counter = int(RiZoeL[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                hang = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟"
                await asyncio.wait([e.respond(hang, reply_to=e.reply_to_msg_id) for i in range(counter)])
        else:
            await e.reply(usage)


async def packspam(e):
    if e.sender_id in SUDO_USERS:
        try:
            x = await e.get_reply_message()
            if not (x and x.media and hasattr(x.media, "document")):
                return await e.reply("`Reply To Sticker Only.`")
            set = x.document.attributes[1]
            sset = await e.client(
                GetStickerSetRequest(
                InputStickerSetID(
                    id=set.stickerset.id,
                    access_hash=set.stickerset.access_hash,
                )
                )
            )
            pack = sset.set.short_name
            docs = [
                utils.get_input_document(x)
                for x in (
                await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
                ).documents
            ]
            for xx in docs:
                async with e.client.action(e.chat_id, "document"):
                    await e.client.send_file(e.chat_id, file=(xx))
                    await asyncio.sleep(0.3)
        except Exception as xy:
            print(str(xy))
            usage = f"**Module Name : Pack Spam** \n\n cmd: `{hl}packspam (replying to any sticker)`"
            await e.reply(usage)


HAN = [
   "**tere Maaki Chut Message Open Kar**"
   "**Bhen Ke Lode Message Kholle**",
   "**Dalle BhiKhari Message Bhi khol kar dekh**",
   "**Click Below Bitch**",
   "**Fuck You Kid**",
   "**Suar se Chudi hui olad message bhi kholle**",
   "**Tere Bhen Ko choud message khol",
   ]



async def spam(e):
    usage = f"**Module Name: Inline Spam** \n\nCommand:\n\n{hl}ispam <count> <Username Or reply to user>"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        RiZoeL = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(RiZoeL) == 2:
            user = str(RiZoeL[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is the owner Of these Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(RiZoeL[0])
                for _ in range(counter):
                    open_msg = random.choice(HAN)
                    prn = random.choice(PORMS)
                    caption = f"{username} {open_msg}"
                    await e.client.send_message(e.chat_id, 
                                                     caption, 
                                                     buttons=[
                                                     [
                                                      Button.inline("Click Here Bitch", data="dekhlo"),
                                                     ],
                                                     [
                                                      Button.url(f"{c}'s Mom's Porno", f"{prn}"),
                                                     ]
                                                     ]
                                                     )
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in RiZoeLX:
                text = f"I can't raid on @RiZoeLX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) == OWNER_ID:
                text = f"This guy is the owner Of these Bots."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(RiZoeL[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    open_msg = random.choice(HAN)
                    prn = random.choice(PORMS)
                    caption = f"{username} {open_msg}"
                    await e.client.send_message(e.chat_id, 
                                                     caption, 
                                                     buttons=[
                                                     [
                                                      Button.inline("Click Here Bitch", data="dekhlo"),
                                                     ],
                                                     [
                                                      Button.url(f"{c} Mom's Porno", f"{prn}"),
                                                     ]
                                                     ]
                                                     )
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        Alert = ("I Don't Want To Abuse You Master")
        await event.answer(Alert, cache_time=0, alert=True)
   else:
        textt = random.choice(RAID)
        await event.edit(textt)
