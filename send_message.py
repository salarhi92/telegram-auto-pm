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
            "پیام ۱ ...",
            "پیام ۲ ...",
            "پیام ۳ ..."
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
