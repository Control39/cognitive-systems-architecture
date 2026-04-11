# Когнитивные системы архитектуры
> Экосистема для микросервисов, управляемых ИИ. Создана системным архитектором, который проектирует решения, а не пишет код. 

## 👋 Кто я?

**Я не разработчик, я архитектор.** Два года назад я была "нулём в IT". Сегодня я:
- Проектирую когнитивные системы (не пишу PHP в Sublime Text)
- Управляю ИИ через систематическое мышление и диалоги
- Преподаю новичкам, как ориентироваться в IT (IT-Compass)
- Автоматизирую управление портфолио, карьерой, архитектурой

**Результат**: приватный репо на SourceCraft с 10 микросервисами, 237 документами, используется для подготовки к грантам.

---

## 🎯 Выбери свой путь

### Для работодателей / HRы мне нужен специалист
**→ Открой [HIRE_ME.md](HIRE_ME.md)** (5 минут)
- Кто я (и почему я не разработчик)
- Что я построила (с метриками)
- Какие роли я ищу
- FAQ про мою позицию

### Для сообщества / я развиваюсь, помоги мне
**→ Открой [NAVIGATION.md](docs/NAVIGATION.md)** (10 минут)
- 5 путей для разных целей (новичок → архитектор)
- Микросервисы с примерами
- Как использовать IT-Compass

### Для грантов / я оцениваю projet
**→ Открой [MAIN_BRANCH_ANALYSIS.md](analysis/MAIN_BRANCH_ANALYSIS.md)** (20 минут)
- 53 MB, 8,716 файлов, 237 документов
- Методология разработки
- Open-source компоненты и интеграции

---

## 🏗️ Архитектура (кратко)

| Сервис | Назначение | Статус |
|--------|-----------|--------|
| **IT-Compass** | Система отслеживания навыков + метод для новичков | ✅ Активный |
| **Cloud-Reason** | API для системного мышления с YandexGPT | ✅ Активный |
| **Career-Development** | AI-управляемое планирование + карьерные решения | ✅ Активный |
| **Portfolio-Organizer** | Автоматическое резюме из архива | ✅ Активный |
| **ML-Model-Registry** | Реестр моделей + веб-UI | ✅ Активный |
| **Auth-Service** | OAuth2 + управление доступом | ✅ Активный |
| **Job-Automation-Agent** | Автоматизация трудозатрат и метрик | ✅ Активный |
| **System-Proof** | Верификация архитектурных решений | 🔄 Разработка |
| **Arch-Compass-Framework** | Фреймворк для архитектурных паттернов | 🔄 Разработка |
| **Thought-Architecture** | Коллекция когнитивных паттернов (RAG) | ✅ Активный |

Полная справка: [PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md)

---

## 🚀 Быстрый старт

### Локально (Docker)
```bash
git clone https://github.com/your-org/cognitive-systems-architecture.git
cd cognitive-systems-architecture
docker-compose up
```

Сервисы доступны на `localhost:800X` (см. `docker-compose.yml`).

### Kubernetes (с ArgoCD)
```bash
kubectl apply -f deployment/k8s/
# или используйте GitOps в ArgoCD
```

### Dev режим (Python)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
python -m pytest tests/
```

---

## 📊 Метрики проекта

- **8,716 файлов**, 53 MB кода + документации
- **237 документов** (методологии, логика, примеры)
- **10 микросервисов** (FastAPI, async, RAG)
- **68 Kubernetes манифестов** (production-ready)
- **181 файлов Python** (14K+ LOC, типизированный)
- **70+ checkpoints** в аудите репо (ENTERPRISE уровень)
- **5+ интеграций**: YandexGPT, ChromaDB, PostgreSQL, Prometheus, GitHub Actions

---

## 🔧 Инструменты и интеграции

**RAG система** (Chromadb + LangChain):
- Индексирует 237 документов из репо
- Ищет похожие решения при новых задачах
- Интегрирована в Cloud-Reason

**Мониторинг** (Prometheus + Grafana):
- Метрики всех микросервисов в реальном времени
- Дэшборды для Health, Requests, Errors, Latency
- Alerts в Slack для критических метрик

**CI/CD** (GitHub Actions):
- Автоматический Trivy-скан контейнеров
- Линтинг (pylint, black, isort)
- Unit тесты перед деплоем
- Автоматическое создание Docker образов

**Аудит репо** (собственный инструмент):
- Проверяет 70+ параметров качества кода
- Уровни: Base (нужна для стартапа), Professional (для компании), Enterprise (для критического ПО)
- Может автоматически создавать недостающие файлы

---

## 📚 Документация

| Документ | Для кого | Время |
|----------|---------|-------|
| [HIRE_ME.md](HIRE_ME.md) | Работодатели | 5 мин |
| [NAVIGATION.md](docs/NAVIGATION.md) | Новички + сообщество | 10 мин |
| [MAIN_BRANCH_ANALYSIS.md](analysis/MAIN_BRANCH_ANALYSIS.md) | Грант-ревьюэры | 20 мин |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Техлиды | 30 мин |
| [DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md) | DevOps инженеры | 45 мин |
| [PROJECTS-MATRIX.md](docs/PROJECTS-MATRIX.md) | Product менеджеры | 20 мин |

Все документы хранятся в `docs/` и обновляются с кодом.

---

## 🤝 Как внести вклад?

1. **Новичок в IT** — используй IT-Compass чтобы найти свой путь (в `apps/it-compass/`)
2. **Разработчик** — улучшай микросервисы, добавляй тесты в `tests/`
3. **Архитектор** — предлагай улучшения в `docs/` (Issues welcome)
4. **Грант-ревьюэр** — смотри [MAIN_BRANCH_ANALYSIS.md](analysis/MAIN_BRANCH_ANALYSIS.md)

---

## 📋 Лицензия и контакты

**Лицензия**: MIT (см. [LICENSE](LICENSE))

**Автор**: Системный архитектор (специализация: когнитивные системы, ИИ-управление)
- 📧 Email: [указано в HIRE_ME.md](HIRE_ME.md#контакты)
- 🔗 SourceCraft: https://sourcecraft.dev/[your-username]
- 💼 LinkedIn: [указано в HIRE_ME.md](HIRE_ME.md#контакты)

---

## ✨ Благодарности

Проект использует:
- **FastAPI** для микросервисов
- **PostgreSQL** для персистентности
- **ChromaDB** для RAG
- **Docker** и **Kubernetes** для оркестрации
- **YandexGPT** для системного мышления
- **GitHub Actions** для CI/CD

Спасибо сообществам этих проектов! 🙏
.env
.coverage
htmlcov/
.pytest_cache/
dist/
build/
*.egg-info/
```

## Documentation for Employers

For a quick overview of the project's value and capabilities, see the [One-Pager](docs/EMPLOYER_ONE_PAGER.md) designed for technical leads and hiring managers. It highlights systemic thinking, AI orchestration, and **relevance for the Russian corporate sector** (Yandex, banks, IT integrators).

## GitOps & CI/CD

The project implements a modern GitOps workflow with automated security gates, container scanning, and Kubernetes deployment.

- **CI Pipeline**: Security scanning (detect‑secrets, safety, pip‑audit, Trivy), linting, testing, Docker builds, and GitOps deployment.
- **GitOps**: Kubernetes manifests are managed with Kustomize and automatically applied via Argo CD or GitHub Actions.
- **Secrets Management**: Encrypted secrets using Sealed Secrets / SOPS.

For detailed instructions, see [GitOps Guide](docs/DEVOPS_GITOPS_GUIDE.md).

## Repository Audit Tool

This repository includes an **automated audit tool** that evaluates the maturity of the codebase against three levels (Base, Professional, Enterprise) with 70+ checkpoints.

### Features

- **Python CLI** (`tools/repo_audit/audit.py`) – run manually or in CI.
- **GitHub Actions workflow** – automatically audits on push/PR and posts results.
- **AI Skill for SourceCraft** – interact via chat: `@repo-audit проверить репозиторий`.
- **Customizable checklists** – YAML‑based, easy to extend.
- **Auto‑fix** – can automatically create missing files, fix formatting, etc.

### Usage

```bash
# Run audit for 'base' level
python -m tools.repo_audit.audit --level base --output markdown

# Run for all levels with auto‑fix
python -m tools.repo_audit.audit --level base,professional,enterprise --auto-fix
```

### Integration

- **CI/CD**: The audit runs in GitHub Actions; see `.github/workflows/repo-audit.yml`.
- **AI Skill**: Configured in `.sourcecraft/skills/repo-audit.yml`.
- **Configuration**: Settings are in `pyproject.toml` under `[tool.repo-audit]`.

For full documentation, see [Repo Audit Guide](docs/repo-audit-guide.md).

## Relevance for Russian Corporate Sector

This portfolio is designed to meet the specific needs of **Yandex**, **Russian banks (Sberbank, Tinkoff, VTB)**, and **IT integrators (Krok, IBS, Lanit)**:

- **Yandex Cloud** – uses Kubernetes, Docker, cloud‑native patterns directly applicable to Yandex Cloud’s container services.
- **Yandex GPT** – integration with Yandex’s LLM for AI skills (see `.sourcecraft/skills/`).
- **Security & compliance** – network policies, PodSecurityPolicies, secrets management, SAST/DAST that meet strict financial sector standards.
- **Legacy modernization** – shows how to incrementally migrate monolithic systems to microservices with AI‑assisted refactoring.

The **systemic thinking** and **AI orchestration** demonstrated here are exactly what Russian enterprises need to accelerate digital transformation while maintaining reliability and security.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

See: https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

**Documentation:**
- API Docs: https://Control39.github.io/cognitive-systems-architecture/
- Scaling Plan: [docs/scaling-plan.md](docs/scaling-plan.md)
- GitOps Guide: [docs/DEVOPS_GITOPS_GUIDE.md](docs/DEVOPS_GITOPS_GUIDE.md)
- Security: [docs/security/SECRETS-MANAGEMENT.md](docs/security/SECRETS-MANAGEMENT.md)
- Repo Audit: [docs/repo-audit-guide.md](docs/repo-audit-guide.md)

**Monitoring (Grafana/Prometheus):**
```
docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d prometheus grafana
```
Grafana: http://localhost:3000 (admin/admin)
Prometheus: http://localhost:9090
