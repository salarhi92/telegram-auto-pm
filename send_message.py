from telethon import TelegramClient
import random
import time
from telethon.errors import FloodWaitError
import asyncio

# مشخصات حساب تلگرام
api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
phone_number = '+989203376965'

# تعریف گروه‌ها و پیام‌ها به صورت دیکشنری
group_message_map = {
    # گروه‌های کریپتو و USDT
    "crypto_groups": {
        "groups": [
            "flash_BTC_software_Group",
            "flashgroupTm",
            "flashbtcpublicgroup",
            "CasacryptoLounge",
            "nano_caps",
            "yrbcioo2",
            "cryptoflash_group",
            "xingkongshequ2022",
            "latinosBSC",
            "gemsroombsc",
            "moneyshiill",
            "ShillNFT_Russia",
            "Usdtmarket0",
            "ghdqhghdqh1",
            "Terra4860",
            "lotusshill",
            "CryptoPumpShillsgroup",
            "AirCoinChineseTraditional",
            "cryptoprodsshills",
            "Shitcoinmoonshotss",
            "qihangCN",
            "uniswaptalk",
            "chuletashill",
            "Spartatgm",
            "hard_shill",
            "Hiddengemsearly",
            "SatoshiNakamoto1478",
            "blockchainflashreflectgroup",
            "safedegens_bsc"
        ],
        "messages": [
            # پیام‌ها بدون تغییر
            """🔥 24-Hour Exclusive Deal! 🔥
Buy Flash usdt today and get flash usdt software absolutely FREE!
⏳ Only for the next 24 hours – don’t miss out!

✅ Instant & Automated: Your Flash USDT is delivered instantly, with no manual steps.

✅ Secure Payments: Fully verified payment processing ensures your peace of mind.

✅ Money-Back Guarantee: Not satisfied? Get a full refund—no questions asked.

✅ Registered & Trustworthy: A legit company, VAT-registered, with 24/7 live support.

💬 WhatsApp: +18603166184

Telegram: https://t.me/flashusdtsafe_bot

👉 Grab yours now: https://cryptoflash.shop/buy/""",
            # ... بقیه پیام‌ها هم مثل قبلی باشند ...
        ]
    },

    # گروه‌های فروشگاه سنگ و جادو
    "stone_magic_groups": {
        "groups": [
            "racefiets"
        ],
        "messages": [
            # پیام‌ها بدون تغییر
            """💫✨ Awaken Your Inner Magic! ✨💫
🔮 Unique Magic & Enchanted Stones, Crafted Just for You 🔮
At UniBazaar, each stone is ritual-charged with powerful intention to amplify your personal energy.
💰 Attract lasting wealth, ❤️ invite genuine love, and 🛡️ shield yourself with potent protection — all in one mystical collection designed to transform your life.

🌐 https://unibazaar.shop
📩 DM now to begin your magical journey and unlock your true potential!""",
            # ... بقیه پیام‌ها هم مثل قبلی باشند ...
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
            # چک با یوزرنیم گروه
            if dialog.is_group and dialog.entity.username in category['groups']:
                chosen_message = random.choice(category['messages'])
                try:
                    print(f"[+] ارسال پیام به گروه: {dialog.name}")
                    await client.send_message(dialog.id, chosen_message)
                    await asyncio.sleep(5)  # فاصله کوتاه بین پیام‌ها برای جلوگیری از اسپم
                except FloodWaitError as e:
                    print(f"[!] تلگرام به دلیل اسپم محدودیت گذاشت، باید {e.seconds} ثانیه صبر کنی...")
                    await asyncio.sleep(e.seconds + 15)
                except Exception as ex:
                    print(f"[!] خطا در ارسال پیام به {dialog.name}: {ex}")

# اجرای خودکار هر 11.5 دقیقه
with client:
    while True:
        client.loop.run_until_complete(send_messages())
        print("[*] پیام‌ها ارسال شدند، اجرای بعدی در 11.5 دقیقه...")
        time.sleep(700)
