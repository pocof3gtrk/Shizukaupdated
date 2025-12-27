from config import OWNER_ID
from PurviBots import PurviBots
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


HELP_BACK = [

    [
        InlineKeyboardButton(text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", url=f"https://t.me/iamvillain77"),
        InlineKeyboardButton(text="⌯ вᴧᴄᴋ ⌯", callback_data="back"),
    ],
]


ALPHA_BACK = [
    [
        InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"ALPHA_MAIN")
    ]
]

ALPHA_BTNS = [
    [
        InlineKeyboardButton("• ʙᴀsɪᴄ •", callback_data="ALPHA_BASIC"),
        InlineKeyboardButton("• ᴄʜᴀᴛ-ʙᴏᴛ •", callback_data="ALPHA_CHAT"),
    ],
    [
        InlineKeyboardButton("• ɪɴғᴏ •", callback_data="ALPHA_INFO"),
        InlineKeyboardButton("• ᴛᴀɢs •", callback_data="ALPHA_TAG"),
    ],
    [
        InlineKeyboardButton("• ʀᴀɴᴋ •", callback_data="ALPHA_RANK"),
        InlineKeyboardButton("• ᴡᴇʟᴄᴏᴍᴇ •", callback_data="ALPHA_WEL"),
    ],
    [InlineKeyboardButton("⌯ вᴧᴄᴋ ⌯", callback_data="back")]
]



HELP_BUTTON = [

    [
        InlineKeyboardButton(text="✙ ᴀᴅᴅ ᴍᴇ ✙", url=f"https://t.me/{PurviBots.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"),
        InlineKeyboardButton(text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", url=f"https://t.me/iamvillain77"),
    ],
]

ABOUT_BUTTON = [
    [
        InlineKeyboardButton("⌯ 𝛅ᴜᴘᴘσʀᴛ ⌯", url="https://t.me/iamvillain77"),
        InlineKeyboardButton("⌯ ᴜᴘᴅᴧᴛє ⌯", url="https://t.me/iamvillain77")
    ],
    [
        InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"back")
    ]
]


STBUTTON = [
  [
       InlineKeyboardButton(
    text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
    url=f"https://t.me/{PurviBots.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users",
        ),
  ],
  [
    InlineKeyboardButton(
      text="⌯ ❍ᴡɴᴇʀ ⌯",
      user_id=OWNER_ID,
    ),
      InlineKeyboardButton(
      text="⌯ ᴧʙσᴜᴛ ⌯",
      callback_data="ABOUT",
    ),
  ],
    [
        InlineKeyboardButton(text="⌯ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ⌯", callback_data="ALPHA_MAIN"),
    ],
]


