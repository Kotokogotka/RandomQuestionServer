import os

# Загружаем переменные окружения из файла .env
from dotenv import load_dotenv
load_dotenv()


SECRET_KEY = os.urandom(24)  # Секретный ключ Flask
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://junior:23102023@postgres:5000/bewise')