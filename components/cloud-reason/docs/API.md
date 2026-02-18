# Cloud Reason API Документация

## Обзор

Cloud Reason API предоставляет RESTful интерфейс для управления решениями, их анализа и получения рекомендаций. API следует принципам REST и возвращает данные в формате JSON.

## Базовый URL

```
http://localhost:5000/api/v1
```

## Аутентификация

API не требует аутентификации в текущей версии.

## Форматы данных

Все данные передаются в формате JSON. Убедитесь, что вы устанавливаете заголовок `Content-Type: application/json` при отправке данных.

## Ошибки

API использует стандартные HTTP коды состояния для указания успеха или неудачи запроса:

- `200 OK` - Запрос успешно выполнен
- `201 Created` - Ресурс успешно создан
- `400 Bad Request` - Некорректный запрос
- `404 Not Found` - Ресурс не найден
- `429 Too Many Requests` - Превышено ограничение частоты запросов
- `500 Internal Server Error` - Внутренняя ошибка сервера

## Эндпоинты

### Решения

#### Создание решения

```
POST /decisions
```

**Тело запроса:**
```json
{
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"]
}
```

**Ответ:**
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"],
  "status": "string",
  "created_at": "string",
  "updated_at": "string"
}
```

#### Получение списка решений

```
GET /decisions
```

**Параметры запроса:**
- `status` (string, optional) - Фильтр по статусу
- `owner` (string, optional) - Фильтр по владельцу
- `tag` (string, optional) - Фильтр по тегу

**Ответ:**
```json
[
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "context": "string",
    "owner": "string",
    "tags": ["string"],
    "status": "string",
    "created_at": "string",
    "updated_at": "string"
  }
]
```

#### Получение решения

```
GET /decisions/{id}
```

**Ответ:**
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"],
  "status": "string",
  "created_at": "string",
  "updated_at": "string"
}
```

#### Обновление решения

```
PUT /decisions/{id}
```

**Тело запроса:**
```json
{
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"],
  "status": "string"
}
```

**Ответ:**
```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"],
  "status": "string",
  "created_at": "string",
  "updated_at": "string"
}
```

#### Удаление решения

```
DELETE /decisions/{id}
```

**Ответ:**
```json
{
  "message": "string"
}
```

### Анализ

#### Анализ решения

```
POST /decisions/{id}/analyze
```

**Тело запроса:**
```json
{
  "analysis_type": "string",
  "additional_data": {}
}
```

**Ответ:**
```json
{
  "decision_id": "string",
  "recommendations": ["string"],
  "insights": ["string"],
  "confidence": 0.0,
  "explanation": "string"
}
```

### Рекомендации

#### Получение рекомендаций

```
GET /decisions/{id}/recommendations
```

**Ответ:**
```json
[
  {
    "id": "string",
    "decision_id": "string",
    "text": "string",
    "confidence": 0.0,
    "insight": "string",
    "created_at": "string"
  }
]
```

#### Добавление рекомендации

```
POST /decisions/{id}/recommendations
```

**Тело запроса:**
```json
{
  "text": "string",
  "confidence": 0.0,
  "insight": "string"
}
```

**Ответ:**
```json
{
  "id": "string",
  "decision_id": "string",
  "text": "string",
  "confidence": 0.0,
  "insight": "string",
  "created_at": "string"
}
```

### Мониторинг

#### Получение метрик

```
GET /metrics
```

**Ответ:**
```json
{
  "total_decisions": 0,
  "total_recommendations": 0,
  "analyzed_decisions": 0,
  "requests_total": 0,
  "decisions_created_total": 0,
  "decisions_analyzed_total": 0
}
```

#### Проверка состояния

```
GET /health
```

**Ответ:**
```json
{
  "status": "string",
  "timestamp": "string",
  "components": {
    "api": "string",
    "gigachat_assistant": "string",
    "storage": "string"
  }
}