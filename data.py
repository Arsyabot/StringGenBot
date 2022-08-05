from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/ruangdiskusikami"),
         InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/punya_alby"),
        ],
    ]

    START = """
Hᴇʏ {},
━━━━━━━━━━━━━━━━━━━━━━━━
Saya adalah {},
di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━
Mᴀᴅᴇ ᴡɪᴛʜ ☕️ ʙʏ : [『ⒶⓁⒷⓎ』](https://t.me/punya_alby) !
    """
