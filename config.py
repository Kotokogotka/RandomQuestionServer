import os
from dotenv import load_dotenv

# Загрузить переменные окружения из файла postgres.env
load_dotenv('postgres.env')

SECRET_KEY = os.urandom(24)  # Секретный ключ Flask
SQLALCHEMY_DATABASE_URI = 'postgresql://junior:23102023@postgres:5432/bewise'
