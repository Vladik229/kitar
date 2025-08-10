import os, re
from telethon.sync import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

client = TelegramClient("render_session", os.getenv("API_ID"), os.getenv("API_HASH"))

async def send_alert(text):
    await client.send_message("me", f"🔔 {text}")

@client.on(events.NewMessage(chats=[int(id) for id in os.getenv("CHANNEL_IDS").split(",")]))
async def handler(event):
    text = event.text
    if "LONG" in text or "SHORT" in text:
        await send_alert(f"Новий сигнал: {text[:60]}...")

async def main():
    await client.start(os.getenv("PHONE"))
    print("🟢 Бот активний")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())