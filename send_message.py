from telethon import TelegramClient
import random
import time

# مشخصات حساب تلگرام
api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
phone_number = '+989203376965'

# تعریف گروه‌ها و پیام‌ها به صورت دیکشنری
group_message_map = {
    # گروه‌های کریپتو و USDT
    "crypto_groups": {
        "groups": [
            "Flash BTC Software Group.",
            "Flash Usdt Group",
            "BTC - FLASH ( Public Group)",
            "USDT PAKISTAN ONLINE"
        ],
        "messages": [
            """⚡Say NO to scams!
⚡ Instant Tether (USDT) delivery — zero gas fees, zero extra charges!
🔒 Secure payment with trusted gateway
💥 Works on Binance & all wallets
💨 Send crypto FAST, SAFE & EASY
Join thousands who trust Crypto Flash!
Get started now: https://cryptoflash.shop/
Telegram: https://t.me/flashusdtsafe_bot""",
            """🚀 Flash Crypto sender Pro – Tired of slow, clunky crypto apps?
Experience lightning-fast, secure FLASH USDT transactions
✅ TRC20, ERC20, BEP20, and BTC 
✅ Clean, modern interface
✅ Instant visual feedback with real-time logs
✅ No login. No wallet connection. 100% Safe to try
🔐 Built for speed. Designed for trust.
🎁 Now available for FREE download – limited time only!
👉 Click below to experience the next level of transfer Flash USDT.
WhatsApp:+18603166184
🔗 https://cryptoflash.shop/app/
Telegram: https://t.me/flashusdtsafe_bot""",
        ]
    },

    # گروه‌های فروشگاه سنگ و جادو
    "stone_magic_groups": {
        "groups": [
            "Racefiets Marktplaats NL🚲🇾🇪",
            "Flash BTC Software Group.",
            "Flash Usdt Group",
            "BTC - FLASH ( Public Group)",
            "USDT PAKISTAN ONLINE"
        ],
        "messages": [
            """💫✨ Awaken Your Inner Magic! ✨💫
🔮 Unique Magic & Enchanted Stones, Crafted Just for You 🔮
At UniBazaar, each stone is ritual-charged with powerful intention to amplify your personal energy.
💰 Attract lasting wealth, ❤️ invite genuine love, and 🛡️ shield yourself with potent protection — all in one mystical collection designed to transform your life.

🌐 https://unibazaar.shop
📩 DM now to begin your magical journey and unlock your true potential!""",
           """🔥💎 Touch the Magic, Transform Your Life 💎🔥
✨ Rare Crystals & Custom Spells, Infused with Sacred Energy ✨
Discover Citrine, Golden Pyrite, Hexed Amethyst, and more — each stone hand-selected and empowered to help you manifest your deepest desires.
🌙 Personalized spells crafted with pure, focused intent, designed to bring clarity, power, and breakthrough results.

🎁 Luxurious packaging and fast worldwide shipping.
🚀 Step boldly into the world of magic today!

👉 https://unibazaar.shop""",
          """⚡️🔥 The Key to True Magic is in Your Hands! 🔥⚡️
✨ Unlock abundance, love, and protection with our sacred stones and potent spells — all ritual-charged with your personal intention.
💎 Every product is carefully prepared to empower and elevate your life’s journey.

🌍 Worldwide secure shipping
🎁 Beautiful, gift-ready packaging

Take the first step now 👉 https://unibazaar.shop

"""
        ]
    }
}

# ساخت کلاینت
client = TelegramClient('flash_session', api_id, api_hash)

async def send_messages():
    await client.start(phone=phone_number)
    dialogs = await client.get_dialogs()

    for category in group_message_map.values():
        for dialog in dialogs:
            if dialog.is_group and dialog.name in category['groups']:
                chosen_message = random.choice(category['messages'])
                print(f"[+] ارسال پیام به گروه: {dialog.name}")
                await client.send_message(dialog.id, chosen_message)

# اجرای خودکار هر 5 دقیقه
with client:
    while True:
        client.loop.run_until_complete(send_messages())
        print("[*] پیام‌ها ارسال شدند، اجرای بعدی در 5 دقیقه...")
        time.sleep(300)
