# Portfolio System Architect

[![CI](https://github.com/leadarchitect-ai/portfolio-system-architect/workflows/CI/badge.svg)](https://github.com/leadarchitect-ai/portfolio-system-architect/actions)
[![Coverage](coverage_html/index.html)](coverage_html/index.html)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](docker-compose.yml)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)


## 🚀 Elevator Pitch (30 сек)

[См. [[05_DOCUMENTATION/docs/ELEVATOR_PITCH.md](05_DOCUMENTATION/docs/ELEVATOR_PITCH.md)]](05_DOCUMENTATION/docs/ELEVATOR_PITCH.md)

**Запуск (10 сек):**
```bash
docker compose up -d
# Live UI: http://localhost:8501 (IT-Compass)
# API docs: http://localhost:8000/docs
# ML Registry: http://localhost:8001
open index.html  # Landing page
```

**[🎥 Demo Video](https://youtube.com/example)** *(Record: docker up → UI/API tour; 2min)*


## Modules
- **it-compass**: Streamlit career tracker (pytest 100%)
- **cloud-reason**: FastAPI reasoning API (pytest-cov)
- **ml-model-registry**: ML model versioning (pytest)
- **arch-compass-framework**: PowerShell arch patterns (Pester)

## CI/CD
- GH Actions: lint, test matrix, Docker build/push to GHCR
- Coverage: .coveragerc, pytest-cov, reports in Actions

## SourceCraft Grant
Project ready for submission:
- [Grant Proposal](cognitive-architect-manifesto/04_ARTIFACTS/grants/grant-proposal.md)
- Evidence: [Metrics](08_EVIDENCE/metrics/), Coverage badges above
- Architecture: [Ecosystem](diagrams/ecosystems.mmd)

\n\n## 📚 Документация и анализ\n\nПолный анализ экосистемы проекта доступен в:\n- [**PROJECT_ANALYSIS.md**](05_DOCUMENTATION/docs/PROJECT_ANALYSIS.md) - детальный разбор архитектуры, модулей и рекомендаций\n- [**05_DOCUMENTATION/docs/**](05_DOCUMENTATION/docs/) - вся техническая документация\n\n**Статус:** ✅ Все критические замечания нейроревью исправлены, PR #123 готов к слиянию.\n\nLicense: MIT | Author: Екатерина Куделя\n

