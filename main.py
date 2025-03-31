import logging
import sqlite3
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен бота, полученный от BotFather
API_TOKEN = 'YOUR_BOT_TOKEN'

# ID администратора (замените на ваш Telegram ID)
ADMIN_ID = 123456789

# Определение состояний для конечного автомата
class FeedbackStates(StatesGroup):
    waiting_for_feedback = State()  # Состояние ожидания отзыва от пользователя

# Функции для работы с базой данных
def init_db():
    """Инициализация базы данных SQLite"""
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    
    # Создаем таблицу, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedbacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        username TEXT,
        feedback TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    logging.info("База данных инициализирована")

def save_feedback(user_id, username, feedback_text):
    """Сохранение отзыва в базу данных"""
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO feedbacks (user_id, username, feedback) VALUES (?, ?, ?)',
        (user_id, username, feedback_text)
    )
    
    conn.commit()
    conn.close()
    logging.info(f"Отзыв пользователя {user_id} сохранен")

def get_all_feedbacks():
    """Получение всех отзывов из базы данных"""
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM feedbacks ORDER BY timestamp DESC')
    feedbacks = cursor.fetchall()
    
    conn.close()
    return feedbacks

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Инициализация базы данных
    init_db()
    
    # Обработчики команд
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        """
        Обработка команды /start - показать приветственное сообщение и инструкции
        """
        welcome_text = (
            "👋 Добро пожаловать в бота для сбора отзывов!\n\n"
            "Здесь вы можете поделиться своими впечатлениями, предложениями или сообщить о проблемах.\n\n"
            "Доступные команды:\n"
            "/feedback - Оставить отзыв\n"
            "/start - Показать это сообщение снова"
        )
        await message.answer(welcome_text)

    @dp.message(Command("feedback"))
    async def cmd_feedback(message: types.Message, state: FSMContext):
        """
        Обработка команды /feedback - начало процесса сбора отзыва
        """
        await state.set_state(FeedbackStates.waiting_for_feedback)
        await message.answer("Пожалуйста, поделитесь вашим отзывом. Напишите сообщение ниже:")

    @dp.message(FeedbackStates.waiting_for_feedback)
    async def process_feedback(message: types.Message, state: FSMContext):
        """
        Обработка полученного отзыва и сохранение его в базу данных
        """
        user_id = message.from_user.id
        # Получаем имя пользователя, если оно есть, иначе используем имя и фамилию
        username = message.from_user.username or f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        feedback_text = message.text
        
        # Сохраняем отзыв в базу данных
        save_feedback(user_id, username, feedback_text)
        
        # Благодарим пользователя
        await message.answer("Спасибо за ваш отзыв! 🙏 Он успешно записан.")
        
        # Сбрасываем состояние
        await state.clear()

    @dp.message(Command("all_feedbacks"))
    async def cmd_all_feedbacks(message: types.Message):
        """
        Обработка команды /all_feedbacks - показать все отзывы (только для админа)
        """
        user_id = message.from_user.id
        
        # Проверяем, является ли пользователь администратором
        if user_id != ADMIN_ID:
            await message.answer("Извините, эта команда доступна только для администраторов.")
            return
        
        # Получаем все отзывы из базы данных
        feedbacks = get_all_feedbacks()
        
        if not feedbacks:
            await message.answer("Пока нет отзывов.")
            return
        
        # Форматируем и отправляем все отзывы
        response = "📝 Все отзывы:\n\n"
        for feedback in feedbacks:
            id, user_id, username, text, timestamp = feedback
            response += f"ID: {id}\n"
            response += f"Пользователь: {username} ({user_id})\n"
            response += f"Дата: {timestamp}\n"
            response += f"Отзыв: {text}\n"
            response += "-" * 30 + "\n\n"
            
            # Telegram имеет ограничение на длину сообщения, поэтому может потребоваться разделение
            if len(response) > 3500:
                await message.answer(response)
                response = ""
        
        if response:
            await message.answer(response)
    
    # Обработка ошибок
    @dp.errors
    async def error_handler(exception):
        logging.exception(f"Произошла ошибка: {exception}")
        return True
    
    # Запуск бота
    logging.info("Бот для сбора отзывов запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())