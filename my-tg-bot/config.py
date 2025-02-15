import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Telegram Токен
TOKEN = os.getenv("TG_BOT_TOKEN")
