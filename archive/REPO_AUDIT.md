# REPO AUDIT — cognitive-systems-architecture

## 1. Текущее состояние (25 марта 2026)
- Основная ветка: `main` (содержит PR #29, #28, фиксы health-check, postgres 16)
- Deployed:
  - `github-pages` — успешно (latest: 11 минут)
  - `production` (Azure) — постоянно FAILED (при деплое из `main` #6..#1)
- Исправлены:
  - ссылки в `index.html` на корректный Github Pages / blob URL
  - контактный e-mail в футере на `leadarchitect@yandex.ru`
  - удалены устаревшие ветки `refactor/health-check-consolidation` и `blackboxai/job-automation-system`

## 2. Структура репозитория
- `apps/*` — 8 сервисов с разными FastAPI/Flask приложениями
- `docs/` (`mkdocs-site`) — статический сайт, генерируемый mkdocs
- `docker-compose.yml` — сборка для локальной инфраструктуры
- `.github/workflows` — CI/CD: `ci.yml`, `deploy.yml`, `deploy-pages.yml`, `code-quality.yml`, `sync-to-github.yml` и др.
- `src/common/` (рефакторинг health-check + async_helpers)

## 3. Проблемы в CI/CD
1. `production` деплой из main падает (Azure Deploy). Логи требуют анализа ошибок привязки (см. GitHub deployment job).  
2. В `pull_request` множество фейлов на security+test (20+), но для `push` main есть success. Проблема в различиях веток / окружений.
3. `gh-pages` работает, но ссылки перезаписываются некорректно при ручных правках `index.html`.

## 4. Основные улучшения
- Унификация `healthcheck` и `readiness` через один общий модуль (внедрено в `src/common/health_check.py`, но надо довести до всех сервисов, включая `apps/cloud-reason`, `apps/ml-model-registry`)
- Вынести конфигурацию версии Postgres в `.env` (`POSTGRES_IMAGE=postgres:16`)
- Разбить CI-сценарии: `test`, `lint`, `security`, `deploy-pages`, `deploy-production`.

## 5. Автоматизация (добавлено)
- Новой workflow `ci-full.yml` (полный pipeline с тестами, линтингом и security)
- `deploy-prod.yml` с проверкой `health` после деплоя и автоматическим rollback

## 6. Рекомендованные шаги
1. Настроить `azure-deploy` workflow на `main` с `healthcheck` endpoint.
2. Добавить `fail-fast` и `retry` для `deployment`.
3. Проверить и поправить `docs base_url` в mkdocs (`mkdocs.yml`).
4. В `GH Pages` указать `Source = gh-pages` и `folder = /`.
5. Снять метрики: `| git log --oneline | head` + `| git branch -a`.
6. При необходимости запустить локально:
   - `docker-compose up --build`,
   - `pytest -q`,
   - `pip install -r requirements-dev.txt && ruff check .`.

## 7. Контакты
- `leadarchitect@yandex.ru` (фиксированно)
- `LinkedIn`: `будет добавлен позже`.
