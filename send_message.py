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
            """Flash usdt  Free App
🌐 https://cryptoflash.shop/app/
✅ Instant Auto Delivery
✅ No Demo / No Test Orders
✅ Trusted by Real Clients Worldwide
🔒We do not offer test transactions — our system is built for serious buyers only.
Once payment is confirmed, the Flash USDT hits your wallet 
automatically in just minutes.
💬 Have questions? Our support team is here 24/7 to help.
👉 Ready to experience true automation?
WhatsApp: +18603166184 
 Telegram: https://t.me/flashusdtsafe_bot
https://youtu.be/rG8ksCwRWYE""",
            """🔥How to swap ETH/BNB/USDT to FLASH USDT 
✅NO REMIX , NO CODE
✅fast and secure
✅refund guarantee
🌐 https://cryptoflash.shop/swap/
💬 Whatsapp: +18603166184
🌐 https://www.youtube.com/watch?v=YB9D1woTfe0&feature=youtu.be""",
            """🎯 Wallet Finder Pro – Advanced Crypto Wallet Scanner
Welcome to the next generation of blockchain wallet discovery technology.
🔍 Key Features:
Scans 750+ wallet patterns per session
Detects active wallets with BTC, ETH, or USDT balances
Identifies wallets from MetaMask, Trust Wallet, and hardware types
Shows full wallet details: Address + Private Key + Network
Real-time simulated logs with a sleek modern UI
Desktop compatible
https://cryptoflash.shop/app/
WhatsApp: https://wa.me/+18603166184
Telegram: https://t.me/flashusdtsafe_bot
https://youtu.be/2bFZ2F9ijfk""",
            """100% Automatic Delivery Flash usdt/ Free App 
✅ Instant Auto Delivery
✅ No Demo / No Test Orders
✅ Trusted by Real Clients Worldwide
🔒We do not offer test transactions — our system is built for serious buyers only.
Once payment is confirmed, the Flash USDT hits your wallet 
automatically in just minutes.
💬 Have questions? Our support team is here 24/7 to help.
👉 Ready to experience true automation?
WhatsApp:+18603166184
🌐 https://cryptoflash.shop/buy/""", 
            """🔥 Say Goodbye to Scams — Hello to Instant, Safe Flash USDT Transfers! 🔥
Start Now at 👉 https://cryptoflash.shop/ It’s time for a real upgrade:
🚀 Instant Delivery — No Waiting, No Delays
💸 Zero Gas Fees & No Extra Charges — Keep 100% of Your Money
🔒 Rock-Solid Security — Pay via Trusted, Verified Gateway
💼 Compatible with Binance & All Wallets — Ultimate Flexibility
🌍 Send FLASH USDT Anywhere, Anytime — Fast, Easy, Reliable
💸Join the revolution of smart crypto users who refuse to get scammed!
Start Now at 👉 https://cryptoflash.shop/
Telegram: https://t.me/flashusdtsafe_bot
💸Your funds deserve SPEED, SAFETY, and SIMPLICITY."""


        ]
    },

    # گروه‌های فروشگاه سنگ و جادو
    "stone_magic_groups": {
        "groups": [
            "racefiets"
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
            if dialog.is_group and dialog.entity.username in category['groups']:
                chosen_message = random.choice(category['messages'])
                print(f"[+] ارسال پیام به گروه: {dialog.name}")
                await client.send_message(dialog.id, chosen_message)

# اجرای خودکار هر 15 دقیقه
with client:
    while True:
        client.loop.run_until_complete(send_messages())
        print("[*] پیام‌ها ارسال شدند، اجرای بعدی در 15 دقیقه...")
        time.sleep(780)
