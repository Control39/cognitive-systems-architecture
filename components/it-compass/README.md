# IT-Compass

Объединённая версия методологии и приложения IT-Compass.

## Назначение компонента

IT Compass - это комплексная система для отслеживания профессиональных компетенций в IT, объединяющая методологию объективных маркеров компетенций с практической реализацией веб-интерфейса и API-интеграций.

## Структура компонента (после объединения)

```
it-compass/
├── decisions/                    # Архитектурные решения (ADR)
├── docs/                        # Документация
│   ├── ARCHITECTURE.md          # Архитектура компонента
│   ├── METHODOLOGY.md           # Методология
│   ├── PSYCHOLOGICAL_SUPPORT.md # Психологическая поддержка
│   ├── PROJECT_ANALYSIS.md      # Анализ проекта
│   ├── SUPPORT_GUIDE.md         # Руководство по поддержке
│   └── context_for_ai_analysis.md # Контекст для анализа ИИ
├── src/                         # Исходный код
│   ├── __init__.py
│   ├── main.py                  # Основной файл приложения
│   ├── core/                    # Основная логика
│   │   ├── __init__.py
│   │   ├── tracker.py           # Основная система отслеживания
│   │   ├── api_integration.py   # Интеграция с внешними API
│   │   └── mental-support.py    # Психологическая поддержка
│   ├── data/                    # Данные и маркеры
│   │   ├── __init__.py
│   │   ├── markers/             # Маркеры технологий
│   │   │   ├── ai_applications.json
│   │   │   ├── cloud_computing.json
│   │   │   ├── cybersecurity.json
│   │   │   ├── data_analysis.json
│   │   │   ├── database.json
│   │   │   ├── devops.json
│   │   │   ├── frontend.json
│   │   │   ├── mobile_development.json
│   │   │   ├── python.json
│   │   │   └── system_design.json
│   │   └── user_progress.json   # Прогресс пользователя
│   ├── ui/                      # Пользовательский интерфейс
│   │   └── app.py               # Веб-интерфейс (упрощенный)
│   └── utils/                   # Вспомогательные утилиты
│       ├── __init__.py
│       └── portfolio_gen.py     # Генератор портфолио
├── examples/                    # Примеры использования
│   └── usage_example.py
├── config/                      # Конфигурация
│   └── settings.json
├── scripts/                     # Скрипты
│   └── reasoning_integration.py
├── support/                     # Поддержка
│   ├── community_guide.md       # Руководство сообщества
│   ├── low_energy_mode.py       # Режим низкой энергии
│   └── resources/               # Ресурсы поддержки
│       ├── crisis_contacts.json
│       └── motivational_quotes.json
├── tests/                       # Тесты
│   └── test_tracker.py
├── ARCHITECTURE.md              # Архитектура проекта в экосистеме
├── Dockerfile                   # Docker конфигурация
├── requirements.txt             # Зависимости Python
└── README.md                    # Этот файл
```

## Ключевые особенности

### 1. Методология объективных маркеров
- Система отслеживания компетенций на основе объективных критериев
- 5-уровневая модель развития компетенций
- Интеграция с профессиональными платформами

### 2. Психологическая поддержка
- Комплексная система поддержки IT-специалистов
- Профилактика выгорания и импостерского синдрома
- Практики самопомощи и управления стрессом

### 3. Техническая реализация
- Модульная архитектура с четким разделением ответственности
- Веб-интерфейс для взаимодействия с пользователем
- API для интеграции с внешними системами
- Генератор профессионального портфолио

### 4. Интеграция с экосистемой
- Связь с Portfolio-Organizer для автоматической генерации материалов
- Интеграция с Cloud-Reason для анализа контекста
- Использование в Career Development System

## Начало работы

### Установка
```bash
# Клонирование репозитория
git clone <repository-url>

# Установка зависимостей
pip install -r requirements.txt
```

### Запуск
```bash
# Запуск веб-интерфейса
python src/main.py
```

### Использование
```python
# Пример использования
from src.core.tracker import CompetencyTracker
from src.data.markers import load_markers

# Загрузка маркеров технологий
markers = load_markers()

# Создание трекера компетенций
tracker = CompetencyTracker()

# Добавление маркеров и отслеживание прогресса
for marker in markers:
    tracker.add_marker(marker)
```

## Документация

### Основные документы
- [ARCHITECTURE.md](ARCHITECTURE.md) - Архитектура проекта в экосистеме
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - Архитектура компонента
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md) - Методология IT Compass
- [docs/PSYCHOLOGICAL_SUPPORT.md](docs/PSYCHOLOGICAL_SUPPORT.md) - Психологическая поддержка

### Дополнительные материалы
- [docs/PROJECT_ANALYSIS.md](docs/PROJECT_ANALYSIS.md) - Анализ проекта
- [docs/SUPPORT_GUIDE.md](docs/SUPPORT_GUIDE.md) - Руководство по поддержке
- [docs/context_for_ai_analysis.md](docs/context_for_ai_analysis.md) - Контекст для анализа ИИ

## Развитие проекта

### Планы по развитию
- Добавление архитектурных решений (ADR) в папку decisions/
- Подключение к Cloud-Reason для расширенного анализа
- Расширение набора маркеров компетенций
- Интеграция с системами автоматической оценки навыков
- Развитие веб-интерфейса и API

### Участие в разработке
Для участия в разработке ознакомьтесь с:
- [CONTRIBUTING.md](../../CONTRIBUTING.md) - Руководство по внесению вклада
- [CODE_OF_CONDUCT.md](../../CODE_OF_CONDUCT.md) - Кодекс поведения

## Лицензия

Проект распространяется под соответствующей лицензией. Подробности в файле LICENSE (будет добавлен при необходимости).

---

*Это объединенная версия, созданная на основе оригинальной методологии и архивной реализации IT Compass.*