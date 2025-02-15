import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

# Загружаем токен из переменной окружения Railway
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")

# Проверяем, что токен загружен
if not BOT_TOKEN:
    raise ValueError("❌ Ошибка: Переменная окружения VK_TOKEN не найдена!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📷 Как работает фотостудия?")],
        [KeyboardButton(text="🕒 Забронировать время")],
        [KeyboardButton(text="📍 Где находится студия?")],
        [KeyboardButton(text="❓ Задать вопрос")],
    ],
    resize_keyboard=True
)

@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer(
            "Привет! Добро пожаловать в студию автопортрета «Отражения»! 📷✨\n\nЧем могу помочь?",
            reply_markup=keyboard
        )
    elif message.text == "📷 Как работает фотостудия?":
        await message.answer("📷 Наша студия полностью автоматизирована! Вы управляете камерой с помощью пульта.")
    elif message.text == "🕒 Забронировать время":
        await message.answer("🕒 Чтобы забронировать время, перейдите по ссылке: https://n1331728.yclients.com/")
    elif message.text == "📍 Где находится студия?":
        await message.answer("📍 Студия находится в Колпино, адрес: улица Труда, 7/5, этаж 3, офис 12. Подробности и карту смотрите здесь: https://otrazheniya-kolpino.ru/")
    elif message.text == "❓ Задать вопрос":
        await message.answer("❓ Напишите ваш вопрос, и мы ответим вам как можно быстрее!")
    else:
        await message.answer("Я пока не понимаю этот запрос 😕 Попробуйте выбрать один из вариантов.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
