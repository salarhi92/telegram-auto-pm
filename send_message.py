from telethon import TelegramClient
import random
import time

# مشخصات حساب تلگرام
api_id = 20072394
api_hash = '410a78f6ec28fa0d210af22989aef223'
phone_number = '+989203376965'

# گروه‌های هدف
target_groups = [
    "Flash BTC Software Group.",
    "Flash Usdt Group",
    "BTC - FLASH ( Public Group)",
    "USDT PAKISTAN ONLINE"
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

    for dialog in dialogs:
        if dialog.is_group and dialog.name in target_groups:
            chosen_message = random.choice(messages)
            print(f"[+] ارسال پیام به: {dialog.name}")
            await client.send_message(dialog.id, chosen_message)

# اجرای خودکار هر 2 دقیقه
with client:
    while True:
        client.loop.run_until_complete(send_messages())
        print("[*] پیام‌ها ارسال شدند، اجرای بعدی در 2 دقیقه...")
        time.sleep(300)  # ← اینجا تغییر کرد به 5 دقیقه
