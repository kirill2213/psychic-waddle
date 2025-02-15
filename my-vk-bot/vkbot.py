import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from dotenv import load_dotenv

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    load_dotenv()

# Загружаем токен из переменной окружения Railway
TOKEN = os.getenv("VK_BOT_TOKEN")

# Проверяем, что токен загружен
if not TOKEN:
    raise ValueError("❌ Ошибка: Переменная окружения VK_TOKEN не найдена!")

# Подключение к API
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Функция для отправки сообщений
def send_message(user_id, text, keyboard=None):
    vk.messages.send(
        user_id=user_id,
        message=text,
        random_id=0,
        keyboard=keyboard.get_keyboard() if keyboard else None
    )

# Функция для создания клавиатуры
def get_main_keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("📷 Как работает фотостудия без фотографа?", color=VkKeyboardColor.PRIMARY)
    keyboard.add_button("🕒 Забронировать время", color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("📍 Где мы находимся?", color=VkKeyboardColor.SECONDARY)
    keyboard.add_button("❓ Задать вопрос", color=VkKeyboardColor.NEGATIVE)
    return keyboard

# Основной цикл обработки событий
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id

        if user_message in ["начать", "привет", "здравствуйте"]:
            welcome_text = (
                "Привет! Добро пожаловать в первую студию автопортрета в Колпино – «Отражения»! 📷✨\n\n"
                "Чем могу помочь?"
            )
            send_message(user_id, welcome_text, get_main_keyboard())

        elif "как работает" in user_message:
            send_message(
                user_id, 
                "📷 Наша студия полностью автоматизирована! Вы сами управляете камерой с помощью пульта, а профессиональный свет помогает создать идеальные снимки."
            )

        elif "забронировать" in user_message:
            send_message(
                user_id, 
                "🕒 Чтобы забронировать время, перейдите по ссылке: https://n1331728.yclients.com/"
            )

        elif "где мы находимся" in user_message:
            send_message(
                user_id, 
                "📍 Мы находимся в Колпино, адрес: улица Труда, 7/5, этаж 3, офис 12. Подробности и карту смотрите здесь: https://otrazheniya-kolpino.ru/"
            )

        elif "вопрос" in user_message:
            send_message(
                user_id, 
                "❓ Напишите ваш вопрос, и мы постараемся ответить как можно быстрее!"
            )

        else:
            send_message(
                user_id, 
                "Я пока не понимаю этот запрос 😕 Попробуйте выбрать один из вариантов ниже.", 
                get_main_keyboard()
            )
