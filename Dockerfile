# Официальный образ Python в качестве родительского образа
FROM python:3.9-slim

# Установить зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установить рабочую директорию
WORKDIR /app

# Скопировать файл зависимостей в контейнер
COPY requirements.txt .

# Установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать оставшуюся часть приложения в контейнер
COPY . .

# Открыть порт
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]