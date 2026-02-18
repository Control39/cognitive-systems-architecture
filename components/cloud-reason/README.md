# Cloud Reason

Система облачных рассуждений для принятия решений с использованием ИИ.

## Описание

Cloud Reason - это система, которая помогает в принятии решений с помощью искусственного интеллекта. Она предоставляет REST API для управления решениями, их анализа и получения рекомендаций.

## Основные возможности

- Создание и управление решениями
- Анализ решений с помощью GigaChat
- Генерация рекомендаций на основе анализа
- Мониторинг и логирование
- Ограничение частоты запросов
- Управление сессиями пользователей

## Структура проекта

```
cloud-reason/
├── src/
│   ├── api/
│   │   └── reasoning_api.py     # Основной API сервер
│   ├── utils/
│   │   ├── logger.py              # Логирование
│   │   ├── validation.py          # Валидация данных
│   │   ├── rate_limiter.py        # Ограничение частоты запросов
│   │   ├── session_store.py        # Хранение сессий
│   │   ├── monitoring.py          # Мониторинг
│   │   └── error_handler.py      # Обработка ошибок
│   └── gigachat_assistant.py       # Ассистент GigaChat
├── tests/                         # Тесты
├── docs/                          # Документация
├── requirements.txt                # Зависимости
└── README.md                     # Этот файл
```

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <repository-url>
   cd cloud-reason
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Установите переменные окружения:
   ```bash
   export GIGACHAT_API_KEY="ваш_api_ключ"
   export LOG_LEVEL="INFO"
   ```

## Запуск

Запустите сервер:
```bash
python src/api/reasoning_api.py
```

Сервер будет доступен по адресу `http://localhost:5000`.

## API

### Основные эндпоинты

- `POST /api/v1/decisions` - Создание нового решения
- `GET /api/v1/decisions` - Получение списка решений
- `GET /api/v1/decisions/{id}` - Получение решения по ID
- `PUT /api/v1/decisions/{id}` - Обновление решения
- `DELETE /api/v1/decisions/{id}` - Удаление решения
- `POST /api/v1/decisions/{id}/analyze` - Анализ решения с помощью GigaChat
- `GET /api/v1/decisions/{id}/recommendations` - Получение рекомендаций для решения
- `POST /api/v1/decisions/{id}/recommendations` - Добавление рекомендации к решению

### Мониторинг

- `GET /api/v1/metrics` - Получение метрик системы
- `GET /api/v1/health` - Проверка состояния системы

## Документация

Документация API доступна по адресу `http://localhost:5000/api/docs`.

## Тестирование

Запустите тесты:
```bash
python -m pytest tests/
```

## Лицензия

MIT