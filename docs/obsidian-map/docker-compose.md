# Docker Compose

- **Путь**: `docker-compose.yml`
- **Тип**: .YML
- **Размер**: 1,505 байт
- **Последнее изменение**: 2026-03-13 21:05:04

## Превью

```
services:
  it-compass:
    build: ./02_MODULES/it-compass
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    environment:
      - PYTHONPATH=/app
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8501/ || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3

  cloud-reason:
    build: ./02_MODULES/cloud-reason
    ports:
      - "8000:8000"
    volumes:
      - ./logs:/app/logs
      - ./02_MODULES/cloud-reason:/app
    environment:
      - P
... (файл продолжается)
```

