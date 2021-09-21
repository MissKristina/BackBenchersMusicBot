from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELUCJhGiacm9ro5nAJXr_GlzPrpV3UgAACNwIAAkGdiFW9ustLyOBHoiAE")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I'm Private music of @BACKBENCHERSXD For group's voice call. Developed by [who cares <3](https://t.me/PR4TIK_XD ).

If you want to add this Bot in your group Contact @PR4TIK_XD**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "who cares <3", url="https://t.me/PR4TIK_XD")
                  ],[ 
                    InlineKeyboardButton(
                        "🔥⌈ʙᴀᴄᴋ ʙᴇɴᴄʜᴇʀs⌋ ⚡️⛓", url="https://t.me/BACKBENCHERSXD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**BackBenchers Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "who cares <3", url="https://t.me/PR4TIK_XD")
                ]
            ]
        )
   )

