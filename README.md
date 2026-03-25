# Cognitive Systems Architecture

## О проекте
Экосистема для когнитивного управления ИИ в разработке. Создан архитектором, который не пишет код руками, а проектирует системы мышления и автоматизации. Проект — proof-of-concept новой роли "AI-Driven Architect".

### История создания
Два года назад я была "нулем в IT". Начала с Excel-таблички навыков, чтобы понять себя. Через диалоги с ИИ создала IT-Compass — методологию для новичков. Столкнулась с хаосом заметок и потерянными диалогами, что привело к RAG и Reasoning. Теперь — полная экосистема микросервисов.

### Архитектура
- **Микросервисы**: Auth, Cloud-Reason, Portfolio-Organizer и др.
- **Инструменты**: IT-Compass (навигация по навыкам), Portfolio-Organizer (авто-генерация резюме).
- **Технологии**: FastAPI, Docker, PostgreSQL, GitHub Actions.

## Структура проекта
- `apps/` - Микросервисы
- `src/` - Общий код (health-check, async_helpers)
- `docs/` - Документация и история
- `scripts/` - Сборщик наработок (collector.py)
- `tools/` - Инструменты (portfolio-organizer, it-compass)
- `tests/` - Тесты
- `deployment/` - Конфиги для K8s/Docker
- `archive/` - Старые версии и отчеты

## Проекты
| Проект | Описание | Статус |
|--------|----------|--------|
| **Arch-Compass-Framework** | Фреймворк для автоматизации архитектурных решений | Внутренний |
| **Cloud-Reason** | API для системного мышления с YandexGPT | Внутренний |
| **IT-Compass** | Система отслеживания навыков и предотвращения выгорания | Внутренний |
| **Career-Development** | AI-управляемое планирование карьеры | Внутренний |
| **ML-Model-Registry** | Реестр моделей с API и UI | Внутренний |
| **Portfolio-Organizer** | Автоматизированная организация портфолио | Внутренний |
| **System-Proof** | Формальная верификация архитектурных решений | Внутренний |
| **Thought-Architecture** | Коллекция когнитивных паттернов | Внутренний |

Подробная матрица: [Projects Matrix](docs/PROJECTS-MATRIX.md).

## Запуск
```bash
docker-compose up
```

## Сбор наработок
Используйте collector для интеграции локальных файлов и SourceCraft репо:
```bash
python scripts/collector.py --local-paths /path/to/notes --sourcecraft-repo https://github.com/user/repo
```

## Как внести вклад
Проект открыт для идей по когнитивной архитектуре. Issues welcome!

## Автор
[Ваше имя] — AI Systems Architect. Контакт: leadarchitect@yandex.ru
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
