from telethon import TelegramClient
from telethon.errors import FloodWaitError
import random
import asyncio
import os

api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
session_file = 'flash_session.session'  # فایل سشن باید وجود داشته باشه

group_message_map = {
    "crypto_groups": {
        "groups": [
            "flash_BTC_software_Group",
            "flashgroupTm",
            "shillgrow",
"GubbinLounge",
"jackpotgems",
"anbucryptotalk",
"wujishequ_cn",
"sgsbsc",
            "PLTcasino2",
"xifengshecc",
"Shillvillebsc",
"mememecoins",
"xiongmaoshequ_cn",
"cryptofinderandflasher",
"nanowhalesbsc",
"KTDoge",
"babyeloncoin_cn",
"SansanwuSQ",
"erc_shill",
"Bsc_Hidden_Gems",
"RobShillingGemOfficial",
"quontral_global",
"Crypt0h4nt3r",
"OldSaitamaETH",
"satoshimoonhot",
"cryptovist_Shill",
"Earlycallss",
"flashbtcpublicgroup",
"blockchainflashreflectgroup",
"fantom_BTC_market",
"cryptofinderandflasher",
"Flash_Crypto_Market",
"cryptoflash_group",
"Flashcrypto18",
"crypto_flasher_service",
"FlASH_BTC_USDT_USDC",
"flashcryptozone",
"cryptoflashsoft",
"sexybeastCHATbanned",
"MarketJualBeli",
"InstagramTrade",
"SwipeeNL",
"LukesMart",
"Swiperababies",
"Oriflame_aziza_market",
"Marketing_Tools_for_Telegram",
"VensDen",
"yeshinzuX2",
"slumdrunk",
"instaempiremarket",
"buyart4",
"caratmarket",
"laspaganmarket",
"market_place12",
"myvest4u",
"DarkEagleMarket",
"Referralshare2",
"sumting2",
"MoneyMakingMethodz",
"instaAccountbuying",
"EVERYBODYEATZZ",
"avatradercompany",
"yeshinzuOxh8e",
"igbst",
"engagementgroups",
"sfsgroup4u",
"sfsmarketss",
"ThePeachyMart",
"swiperzzss25",
"SocialMediasGames",
"sfsmarket2",
"socialsprint",
"phmartpremiums",
"pawxiemarket",
"MoneyTree89",
"blacklistedddd",
"viralsfsgains",
"rothshouse123",
"unholymarket",
"NsmIGGroup",
"SocialsMarkets",
"openmarket666",
"Renofficialgroup",
"yeshinzuX1",
"theehomee",
"Finesseuniverse",
"SpaceXGroup900",
"Cc4Btc",
"G4_to_the_world123",
"guccifersmarket",
"StopRippers",
"hammermarketplace",
"surgesocialmarket",
"vitorez",
"MJTrustedMarket",
"ourigmarket",
"chiddyxent",
"LasPrimasMercado",
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
            "usdtpaki",
            "safedegens_bsc"
        ],
        "messages": [
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
Telegram: https://t.me/flashusdtsafe_bot
🔗 https://youtu.be/EHmefIQZSBs""",
"""⚡Say NO to scams!
⚡ Instant Tether (USDT) delivery — zero gas fees, zero extra charges!
🔒 Secure payment with trusted gateway
💥 Works on Binance & all wallets
💨 Send crypto FAST, SAFE & EASY
Join thousands who trust Crypto Flash!
Get started now: https://cryptoflash.shop/
Telegram: https://t.me/flashusdtsafe_bot""",
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
🌐 https://www.youtube.com/watch?v=YB9D1woTfe0&feature=youtu.be"""
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
        print("[*] پیام‌ها ارسال شدند، 11.5 دقیقه صبر می‌کنم...")
        await asyncio.sleep(700)

if __name__ == '__main__':
    client.loop.run_until_complete(main_loop())
