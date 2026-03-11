# Руководство для контрибьюторов

Спасибо за интерес к проекту `portfolio-system-architect`!

---

## Принципы проекта

1. **Системность** — все компоненты должны быть частью единой экосистемы
2. **Практичность** — каждый компонент должен решать реальную задачу
3. **Масштабируемость** — архитектура должна поддерживать расширение
4. **Документированность** — каждый компонент должен иметь полную документацию

---

## Как внести вклад

### 1. Форкните репозиторий

Создайте форк на GitHub.

### 2. Клонируйте

```bash
git clone https://github.com/ВАШ_ЛОГИН/portfolio-system-architect.git
cd portfolio-system-architect
```

### 3. Создайте ветку

```bash
git checkout -b feature/название-функции
```

### 4. Внесите изменения

- Исправьте ошибку в коде или документации
- Добавьте новый компонент в `components/`
- Создайте кейс в `cases/`
- Добавьте пример использования в `examples/`

### 5. Закоммитьте

```bash
git add .
git commit -m "feat: краткое описание изменения"
```

### 6. Отправьте и создайте PR

```bash
git push origin feature/название-функции
```

Создайте Pull Request с описанием изменений.

---

## Структура проекта

```
portfolio-system-architect/
├── components/     # Реализации компонентов (src, tests, docs)
├── cases/          # Практические кейсы
├── docs/          # Документация
├── examples/      # Примеры использования
├── scripts/       # Скрипты автоматизации
└── tests/         # Интеграционные тесты
```

---

## Требования к коду

### Python

- Следуйте PEP 8
- Используйте type hints
- Пишите docstrings

```python
def function(param: str) -> dict:
    """Краткое описание.
    
    Args:
        param: Описание параметра.
    
    Returns:
        Описание возвращаемого значения.
    """
    pass
```

### Тестирование

```bash
# Запустить все тесты
python -m pytest tests/

# Запустить тесты компонента
python -m pytest tests/components/it-compass/
```

### Проверка стиля

```bash
flake8 .
black .
```

---

## Документация

Каждый новый компонент должен включать:

- Описание в `README.md`
- Структуру `src/` с кодом
- Тесты в `tests/`
- Документацию в `docs/`

Используйте шаблон `docs/templates/COMPONENT.md`.

---

## Кейсы

Для добавления нового кейса:

1. Создайте папку в `cases/evolution-cases/` или `cases/thinking-cases/`
2. Добавьте `README.md` с описанием
3. Используйте шаблон `docs/templates/case-evolution.md`

---

## Вопросы?

- Создайте [Issue](https://github.com/leadarchitect-ai/portfolio-system-architect/issues)
- Напишите: leadarchitect@yandex.ru

