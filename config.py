import os
from dotenv import load_dotenv

# Загрузить переменные окружения из файла postgres.env
load_dotenv('postgres.env')

SECRET_KEY = os.urandom(24)  # Секретный ключ Flask
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://' +
                                   os.getenv('POSTGRES_USER') + ':' +
                                   os.getenv('POSTGRES_PASSWORD') + '@' +
                                   'postgres:5432/' + os.getenv('POSTGRES_DB'))

