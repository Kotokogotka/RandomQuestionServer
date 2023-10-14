# Версия python
FROM python:3.10-slim

# Раабочая директория
WORKDIR /app

# Копирование файлов из директории внутрь Docker
COPY . /app

# Устновка всех необходимых пакетов
RUN pip install --no-cache-dir -r requirements.txt

# Определение команды при запуске контейнера
CMD ["python", "app.py"]