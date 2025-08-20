from telethon import TelegramClient
from telethon.errors import FloodWaitError
import random
import asyncio
import os

api_id = 20165233
api_hash = '5ef8e9dd2a3b609a055f24fd96b39c3f'
session_file = 'flash_session.session'  # فایل سشن باید وجود داشته باشه

group_message_map = {
    "crypto_groups": {
        "groups": [
            "CasacryptoLounge_353",
            "DoublyCommunityRU",
            "NeonMarketplace",
            "btcinvestment1111",
            "instabloog",
            "supersfs",
            "AdinathComodity1",
"DoublyCommunityBR",
"whitewookies",
"CYNMARKET",
"DoublyCommunityID",
"DoublyCommunityES",
"DoublyCommunityIR",
"usdtpaki",
"BEA_MALL_Pakistan",
"ShillNFT_Russia",
"Usdtmarket0",
"ghdqhghdqh1",
"Terra4860",
"lotusshill",
"CryptoPumpShillsgroup",
"aircoinchinese",
"bitfinescoins",
"cryptoprodsshills"
],
        "messages": [
            """💎 CryptoFlash.shop Affiliate Program – Earn 25% to 50% Commission! 💎
🚀 Turn Your Network into Real Earnings!
🌐 Sign up now: https://cryptoflash.shop
Do you want to earn 25%–50% commission for every Tether (USDT) Flash Sale you refer?
Join the CryptoFlash.shop Affiliate Program and start making money by promoting our high-demand crypto products!
💡 Why Join?
💰 High Commissions: 25% to 50% per successful sale.
⚡️ Fast & Easy: Share your unique referral link — we track every sale automatically.
🌍 Global Opportunity: Anyone can join and earn from anywhere in the world.
🎁 Ready-to-Use Marketing Materials: Banner ads, social posts, and links provided to boost your sales.
📈 How It Works:
Sign up and get your unique affiliate link.
Share it with your network via social media, Telegram, email, or websites.
Earn up to 50% commission on every successful transaction of Flash Tether!
🔥 Start earning today — turn every click into crypto rewards!"""
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
"""🔥 Say Goodbye to Scams — Hello to Instant, Safe Flash USDT shop! 🔥
Start Now at 👉 https://cryptoflash.shop/ It’s time for a real upgrade:
🚀 Instant Delivery — No Waiting, No Delays
💸 Zero Gas Fees & No Extra Charges — Keep 100% of Your Money
🔒 Rock-Solid Security — Pay via Trusted, Verified Gateway
💼 Compatible with Binance & All Wallets — Ultimate Flexibility
🌍 Send FLASH USDT Anywhere, Anytime — Fast, Easy, Reliable
💸Join the revolution of smart crypto users who refuse to get scammed!
Start Now at 👉 https://cryptoflash.shop/
💸Your funds deserve SPEED, SAFETY, and SIMPLICITY""",
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
🔗 https://youtu.be/EHmefIQZSBs""",
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
 https://youtu.be/rG8ksCwRWYE""",
"""🔥How to swap ETH/BNB/USDT to FLASH USDT 
✅NO REMIX , NO CODE
✅fast and secure
✅refund guarantee
🌐 https://cryptoflash.shop/swap/
💬 Whatsapp: +18603166184
🌐 https://www.youtube.com/watch?v=YB9D1woTfe0&feature=youtu.be""",
            """How to create your own flash usdt update August 2025 full tutorial. 
            Code: sites.google.com/view/telegramflashcrypto92/home
website : remix.ethereum.org/
Want to know how to create Flash USDT the easy and secure way? In this video, we break down the newest method (August 2025) to generate USDT flash transactions without complicated setups or risky steps. Whether you're a beginner or already familiar with blockchain tools, this guide walks you through everything step by step."""
        ]
    }
}

if not os.path.exists(session_file):
    print(f"[!] فایل سشن {session_file} پیدا نشد! باید قبلا ساخته باشی.")
    exit(1)

client = TelegramClient(session_file[:-8], api_id, api_hash)

async def send_messages():
    dialogs = await client.get_dialogs()
    for category in group_message_map.values():
        for dialog in dialogs:
            if dialog.is_group and dialog.entity.username in category['groups']:
                chosen_message = random.choice(category['messages'])
                try:
                    print(f"[+] ارسال پیام به گروه: {dialog.name}")
                    await client.send_message(dialog.id, chosen_message)
                    await asyncio.sleep(15)
                except FloodWaitError as e:
                    print(f"[!] محدودیت اسپم: صبر کن {e.seconds} ثانیه")
                    await asyncio.sleep(e.seconds + 15)
                except Exception as ex:
                    print(f"[!] خطا در ارسال پیام به {dialog.name}: {ex}")

async def main_loop():
    await client.connect()
    if not await client.is_user_authorized():
        print("[!] سشن معتبر نیست یا لاگین نشده.")
        return
    print("[*] اتصال موفق به تلگرام (با سشن ذخیره‌شده)")

    while True:
        await send_messages()
        print("[*] پیام‌ها ارسال شدند، 15 دقیقه صبر می‌کنم...")
        await asyncio.sleep(900)

if __name__ == '__main__':
    client.loop.run_until_complete(main_loop())
