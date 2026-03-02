# Api Reference

- **Путь**: `components\career-development-system\docs\API_REFERENCE.md`
- **Тип**: .MD
- **Размер**: 1487 байт
- **Последнее изменение**: 1771483368.9913948

## Предпросмотр

```
# API Reference

## Базовый URL
```
http://localhost:5000/api
```

## Пользователи

### Получить список пользователей
```
GET /users
```

**Ответ:**
```json
[
  {
    "id": 1,
    "username": "ivan_petrov",
    "email": "ivan@example.com"
  }
]
```

### Создать пользователя
```
POST /users
```

**Тело запроса:**
```json
{
  "username": "ivan_petrov",
  "email": "ivan@example.com"
}
```

**Ответ:**
```json
{
  "id": 1,
  "username": "ivan_petrov",
  "email": "ivan@example.com"
}
```

### Получить
... (файл обрезан для предпросмотра)
```
