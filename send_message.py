from telethon import TelegramClient
from telethon.errors import FloodWaitError, SessionPasswordNeededError
import random
import time
import os
import asyncio

api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
phone_number = '+989203376965'
session_file = 'flash_session.session'

# حذف فایل سشن قدیمی برای جلوگیری از خطای AuthKeyDuplicatedError
if os.path.exists(session_file):
    print("[*] فایل سشن قدیمی حذف شد.")
    os.remove(session_file)

group_message_map = {
    # (همون داده‌های گروه‌ها و پیام‌ها مثل قبل...)
}

client = TelegramClient(session_file[:-8], api_id, api_hash)  # حذف '.session' از نام فایل

async def start_client():
    print("[*] شروع اتصال به تلگرام...")
    await client.connect()

    if not await client.is_user_authorized():
        try:
            print("[*] ارسال کد تایید ...")
            await client.send_code_request(phone_number)
            code = input('کد تایید را وارد کنید: ')
            try:
                await client.sign_in(phone_number, code)
            except SessionPasswordNeededError:
                password = input('لطفا پسورد دو مرحله‌ای را وارد کنید: ')
                await client.sign_in(password=password)
        except Exception as e:
            print(f"[!] خطا در ورود: {e}")
            return False
    print("[*] اتصال موفق!")
    return True

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
    connected = await start_client()
    if not connected:
        print("[!] اتصال انجام نشد، برنامه متوقف شد.")
        return

    while True:
        try:
            await send_messages()
            print("[*] پیام‌ها ارسال شدند، 11.5 دقیقه صبر می‌کنم...")
            await asyncio.sleep(700)
        except Exception as e:
            print(f"[!] خطای کلی در حلقه ارسال: {e}")
            print("[*] 60 ثانیه صبر میکنم و دوباره تلاش میکنم...")
            await asyncio.sleep(60)

if __name__ == '__main__':
    try:
        client.loop.run_until_complete(main_loop())
    except KeyboardInterrupt:
        print("\n[*] برنامه با دستور کاربر متوقف شد.")
