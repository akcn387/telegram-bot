"""
GitHub Actions tarafından zamanlanmış şekilde çalıştırılan basit script.
Çalıştığında tüm gruplara tek bir mesaj gönderir ve kapanır.
"""

import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = [c.strip() for c in os.environ["CHAT_ID"].split(",") if c.strip()]
MESSAGE_TEXT = os.environ.get("MESSAGE_TEXT", "Merhaba! Bu otomatik bir mesajdır.")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

for chat_id in CHAT_IDS:
    response = requests.post(
        url,
        data={"chat_id": chat_id, "text": MESSAGE_TEXT, "parse_mode": "HTML"},
    )
    if response.ok:
        print(f"Mesaj gönderildi (chat_id={chat_id})")
    else:
        print(f"HATA (chat_id={chat_id}):", response.status_code, response.text)
