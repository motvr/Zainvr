import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اصدار"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e1afd8ed6c94fe4b3a270.jpg",
        caption=f"""**⋖━━❲• ᯓ𓆩˹ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥 ˼𓆪𓆃❳━━⋗**\nمرحبا بك عزيزي {message.from_user.mention}\n
♡♕᚜ اسم سورس:-الصياد
♡♕᚜ نوعه:-ميوزك
♡♕᚜ للغه برمجه:- بايثون
♡♕᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
♡♕᚜ مجال تشغيل :- تشغيل بوتات الميوزك
♡♕᚜ نظام تشغيل:-المرتجل بوت ميوزك
♡♕᚜ الاصدار 4.0.1 pyrogram 
♡♕᚜ تاريخ تاسيس:-10-4-2020

**⋖━━❲• ᯓ𓆩˹ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥 ˼𓆪𓆃❳━━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "●━◉⟞⟦ • ᯓ𓆩˹ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗩𝗥 ˼𓆪𓆃 ⟧⟝◉━●", url=f"https://t.me/Jaithon"), 
               ],
          ]
        ),
    )


