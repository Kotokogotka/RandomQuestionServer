Конечно, вот обновленный файл `README.md` с дополнительным описанием для `docker-compose.yml`, `Dockerfile` и `postgres.env`:

---

# My Python Project

Этот проект представляет собой простой веб-сервис для получения вопросов из внешнего API и сохранения их в базе данных PostgreSQL.

## Как использовать

### Сборка Docker-образа и настройка сервиса

1. Убедитесь, что Docker установлен на вашем компьютере.

2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/Kotokogotka/test_task.git
   cd my-python-project
   ```

3. Создайте файл `.env` в корневой директории проекта и укажите в нем следующие переменные окружения:
   ```env
   POSTGRES_USER=junior
   POSTGRES_PASSWORD=23102023
   POSTGRES_DB=bewise
   ```

4. Соберите Docker-образ:
   ```bash
   docker build -t my-python-project .
   ```

5. Запустите контейнеры с помощью Docker Compose:
   ```bash
   docker-compose up -d
   ```

### Пример запроса к API

Вы можете отправить POST запрос к сервису, чтобы получить случайные вопросы. Пример запроса с использованием `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 3}' http://localhost:5433/api/questions
```

Где:
- `questions_num` - количество вопросов, которые вы хотите получить.

## Структура проекта

- `app.py`: Основной файл приложения, содержит код Flask-приложения и его маршруты.
- `models.py`: Определение модели SQLAlchemy для взаимодействия с базой данных.
- `config.py`: Конфигурационный файл для настройки приложения.
- `docker-compose.yml`: Файл конфигурации Docker Compose для запуска сервиса и базы данных PostgreSQL.
- `Dockerfile`: Файл для сборки Docker-образа приложения.
- `postgres.env`: Файл с переменными окружения для базы данных PostgreSQL.

## Файлы конфигурации и переменные окружения

### `docker-compose.yml`

```yaml
version: '3.8'

services:
  postgres:
    image: my-python-project
    ports:
      - "543:5432"
    environment:
      POSTGRES_DB: bewise
      POSTGRES_USER: junior
      POSTGRES_PASSWORD: 23102023
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgresql://myuser:mypassword@postgres:5432/mydatabase

volumes:
  postgres_data:
```

### `Dockerfile`

```Dockerfile
# Версия python
FROM python:3.10-slim

# Рабочая директория
WORKDIR /app

# Копирование файлов из директории внутрь Docker
COPY . /app

# Установка всех необходимых пакетов
RUN pip install --no-cache-dir -r requirements.txt

# Определение команды при запуске контейнера
CMD ["python", "app.py"]
```

### `postgres.env`

```env
POSTGRES_USER=junior
POSTGRES_PASSWORD=23102023
POSTGRES_DB=bewise
```

