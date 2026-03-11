# План миграции структуры репозитория

> Переход от нарративной к модульной организации

## Цель

Переорганизовать репозиторий с нарративной структуры (01_JOURNEY...05_MANIFEST) на модульную структуру с чётким разделением компонентов, кейсов и документации.

## Этапы миграции

### Этап 1: Подготовка (выполнено)

- ✅ Созданы новые директории: `config/`, `examples/`, `cases/`, `docs/templates/`, `docs/history/`
- ✅ Созданы шаблоны документации
- ✅ Обновлён README.md

### Этап 2: Перенос компонентов

Переместить содержимое из старой структуры в новую:

| Старое расположение | Новое расположение |
|---------------------|-------------------|
| `cognitive-architect-manifesto/02_METHODOLOGY/it-compass/` | `components/it-compass/` |
| `cognitive-architect-manifesto/02_METHODOLOGY/arch-compass/` | `components/arch-compass-framework/` |
| `cognitive-architect-manifesto/03_EVIDENCE/rag-system/` | `components/cloud_reason/` |
| `cognitive-architect-manifesto/04_ARTIFACTS/career-development/` | `components/career-development-system/` |
| `cognitive-architect-manifesto/04_ARTIFACTS/case-studies/` | `cases/evolution-cases/` |
| `03_CASES/thinking-cases/` | `cases/thinking-cases/` |

### Этап 3: Обновление путей

Обновить ссылки в файлах:

- Markdown-ссылки (внутри файлов `.md`)
- Пути в скриптах (`scripts/*.py`)
- Импорты в Python-файлах
- Конфигурационные файлы (`*.yaml`, `*.json`)

### Этап 4: Удаление старых директорий

После успешного переноса:

```bash
git rm -r cognitive-architect-manifesto/
git rm -r 01_CONTEXT/
git rm -r 01_STRATEGY/
git rm -r 02_METHODOLOGY/
git rm -r 03_CASES/
git rm -r 04_CODE/
git rm -r 04_INTEGRATION/
git rm -r 05_PRESENTATIONS/
```

### Этап 5: Тестирование

- Проверить работу скриптов генерации
- Убедиться, что все ссылки работают
- Запустить тесты

## Команды Git для переноса

```bash
# Создать ветку для миграции
git checkout -b refactor/modular-structure

# Переместить файлы с сохранением истории
git mv cognitive-architect-manifesto/02_METHODOLOGY/it-compass components/
git mv cognitive-architect-manifesto/02_METHODOLOGY/arch-compass components/arch-compass-framework

# Закоммитить изменения
git add .
git commit -m "refactor: переход на модульную структуру"

# Слить с main
git checkout main
git merge refactor/modular-structure
```

## Проверка после миграции

1. Все компоненты в `components/` имеют структуру `src/`, `tests/`, `docs/`
2. Кейсы в `cases/` имеют README с описанием
3. Примеры в `examples/` для каждого компонента
4. Документация в `docs/` актуальна

## Откат при проблемах

```bash
git revert HEAD  # откатить последний коммит
git reset --hard HEAD~1  # полный откат
```

