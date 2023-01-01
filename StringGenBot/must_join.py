from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/a780d017b9d9a8d5d509a.jpg", caption=f"» Halo 👋🏻 Kamu harus bergabung [ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ](@ruangdiskusikami) terlebih dahulu untuk menggunakan bot ini. Setelah bergabung silahkan /start lagi! !",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 BERGABUNG 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
