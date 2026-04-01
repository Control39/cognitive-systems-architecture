# 04 Development Diagrams Interactive Data Flow Diagram

- **Путь**: `05_DOCUMENTATION\obsidian-map\04_DEVELOPMENT_diagrams_interactive_data-flow-diagram.md`
- **Тип**: .MD
- **Размер**: 1,001 байт
- **Последнее изменение**: 2026-03-13 20:21:49

## Превью

```
# Data Flow Diagram

- **Путь**: `04_DEVELOPMENT\diagrams\interactive\data-flow-diagram.md`
- **Тип**: .MD
- **Размер**: 1,463 байт
- **Последнее изменение**: 2026-03-05 05:17:34

## Превью

```
graph LR
    A[Пользователь] --> B(Веб-интерфейс)
    B --> C{API Gateway}
    C --> D[Сервис авторизации]
    D --> E[(БД пользователей)]
    C --> F[Сервис портфолио]
    F --> G[(БД портфолио)]
    C --> H[Сервис компетенций]
    H --> I[(БД компетенций)]
    C --> J[Сервис визуализации]
    J --> K[(
... (файл продолжается)
```


