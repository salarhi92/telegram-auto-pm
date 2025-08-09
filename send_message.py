from telethon import TelegramClient
import random
import time
import traceback

# مشخصات حساب تلگرام
api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
phone_number = '+989203376965'

# گروه‌های هدف (ارسال توی چت اصلی گروه بر اساس اسم)
target_groups = [
    "Flash BTC Software Group.",
    "Flash Usdt Group",
    "BTC - FLASH ( Public Group)",
    "USDT PAKISTAN ONLINE"
]

# گروه‌هایی که باید پیام داخل یک Topic/Thread خاص ارسال شود
# مقدار 'thread_id' را برابر 32 گذاشتم همان‌طور که شما گفتی
target_groups_with_thread = [
    {
        'chat_id': -1002814308879,  # ← شناسه گروه/کانال
        'thread_id': 1037             # ← شناسه سکشن/Topic که شما گفتی
    }
]

# پیام‌ها
messages = [
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
    """🔥 Say Goodbye to Scams — Hello to Instant, Safe Flash USDT Transfers! 🔥
Tired of waiting? Sick of hidden fees? It’s time for a real upgrade:
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

# ساخت کلاینت
client = TelegramClient('flash_session', api_id, api_hash)

async def send_messages():
    await client.start(phone=phone_number)
    dialogs = await client.get_dialogs()

    # گروه‌هایی که قرار است پیام در تاپیک ارسال شود (برای جلوگیری از ارسال در ریشه)
    chat_ids_with_thread = {g['chat_id'] for g in target_groups_with_thread}

    # ارسال پیام به گروه‌های معمولی (بر اساس اسم یا در صورت نیاز بر اساس id)
    for dialog in dialogs:
        try:
            # اطمینان: فقط گروه‌ها
            if not dialog.is_group:
                continue

            # اگر نام گروه در لیست است و این گروه قرار نیست پیام داخل تاپیک بفرستیم
            if (dialog.name in target_groups or dialog.id in target_groups) and dialog.id not in chat_ids_with_thread:
                chosen_message = random.choice(messages)
                print(f"[+] ارسال پیام به (چت اصلی): {dialog.name}  (id: {dialog.id})")
                await client.send_message(dialog.id, chosen_message)

        except Exception as e:
            print(f"[!] خطا هنگام ارسال به {getattr(dialog, 'name', dialog.id)}:")
            traceback.print_exc()

    # ارسال پیام به گروه‌هایی که Topic دارند (با message_thread_id)
    for group in target_groups_with_thread:
        try:
            chosen_message = random.choice(messages)
            print(f"[+] ارسال پیام به تاپیک گروه {group['chat_id']} در thread {group['thread_id']}")
            await client.send_message(group['chat_id'], chosen_message, message_thread_id=group['thread_id'])
        except Exception as e:
            print(f"[!] خطا هنگام ارسال به تاپیک {group['chat_id']} (thread {group['thread_id']}):")
            traceback.print_exc()

# اجرای خودکار هر 5 دقیقه
with client:
    while True:
        try:
            client.loop.run_until_complete(send_messages())
            print("[*] پیام‌ها ارسال شدند، اجرای بعدی در 5 دقیقه...")
        except Exception:
            print("[!] یک خطای کلی رخ داد، ادامه داده می‌شود:")
            traceback.print_exc()
        time.sleep(300)  # 300 ثانیه = 5 دقیقه
