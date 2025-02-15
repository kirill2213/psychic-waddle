import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Telegram Токен
TG_TOKEN = os.getenv("TG_BOT_TOKEN")
