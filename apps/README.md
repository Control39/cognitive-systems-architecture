# Apps Directory - Microservices Architecture

This directory contains 10 microservices that compose the Cognitive Systems Architecture platform.

---

## 📦 Apps Overview

| App | Type | Purpose | Python Files | Status | Structure |
|-----|------|---------|--------------|--------|-----------|
| **it-compass** | FastAPI Service | IT landscape assessment & navigation | 21 | ✅ Production | 🟢 Compliant |
| **cloud-reason** | FastAPI Service | Cloud architecture reasoning & recommendations | 19 | ✅ Production | 🟢 Compliant |
| **ml-model-registry** | FastAPI Service | ML model versioning & management | 22 | ✅ Production | 🟢 Compliant |
| **career-development** | FastAPI Service | Career path analysis & recommendations | 12 | ✅ Production | 🟢 Compliant |
| **auth-service** | FastAPI Service | Authentication and authorization | 1 | 🟡 Minimal | 🟡 Needs expansion |
| **job-automation-agent** | Agent Service | Job automation & workflow orchestration | 8 | ✅ Production | 🟡 Docker-compose inline |
| **portfolio-organizer** | FastAPI Service | Portfolio organization & analytics | 3 | ✅ Stable | 🟡 Non-standard naming |
| **arch-compass-framework** | PowerShell Module | Architecture framework & patterns | 0 | ✅ Reference | ⚠️ Not Python |
| **thought-architecture** | Docs + Tools | Thought architecture framework & utilities | 0 | ✅ Reference | ⚠️ Documentation focused |
| **system-proof** | Prototype | System proof of concept | 1 | 🟡 Prototype | ⚠️ Minimal scope |

---

## 📂 Recommended Directory Structure

All Python microservices **should** follow this template (exceptions documented below):

```
apps/{APP_NAME}/
├── README.md                    # Service overview, API, quick start
├── requirements.txt             # Dependencies (pip freeze)
├── Dockerfile                   # Service container
├── docker-compose.override.yml  # Dev environment (local)
├── .env.example                 # Configuration template
│
├── src/                         # Main source code
│   ├── __init__.py
│   ├── main.py                  # FastAPI app or entry point
│   ├── config.py                # Configuration & environment
│   ├── models/                  # Data models, Pydantic schemas
│   ├── api/                     # Route handlers
│   ├── services/                # Business logic
│   ├── utils/                   # Helper functions
│   └── db/                      # Database models (if applicable)
│
├── tests/                       # Test suite (pytest)
│   ├── conftest.py              # Shared fixtures
│   ├── unit/                    # Unit tests
│   ├── integration/             # API integration tests
│   └── e2e/                     # End-to-end tests
│
├── docs/                        # App-specific documentation
│   ├── API.md                   # Endpoint documentation
│   ├── DEVELOPMENT.md           # Setup & contributing
│   └── ARCHITECTURE.md          # Internal design
│
└── scripts/                     # Utility scripts (optional)
```

---

## 🟢 Compliant Services (Follow as Model)

These services follow the standard template above:

- ✅ **career-development** - Complete structure, good documentation
- ✅ **cloud-reason** - Complete structure, excellent examples
- ✅ **ml-model-registry** - Complete structure, well-tested

**Use these as templates when creating new services.**

---

## 🟡 Needs Minor Improvements

### auth-service
**Current**: Only 3 files (main.py, requirements.txt, Dockerfile)  
**Issue**: No test suite, no proper source structure  
**Action**: Expand with src/, tests/, docs/ (low-risk refactor)  
**Timeline**: Phase 4.2  

### portfolio-organizer
**Current**: `portfolio-organizer/` directory instead of `src/`  
**Issue**: Non-standard naming confuses contributors  
**Action**: Rename to follow template  
**Timeline**: Phase 4.2  

### job-automation-agent
**Current**: `docker-compose.agent.yml` in app directory  
**Issue**: Docker configurations should be centralized  
**Action**: Move to `deployment/docker-compose.job-automation-agent.yml`  
**Timeline**: Phase 4.2  

---

## ⚠️ Special Cases (Keep as-is, Documented)

### arch-compass-framework
**Type**: PowerShell Module (not Python)  
**Structure**: `.psd1` (manifest), `.psm1` (module), tests, docs  
**Reason**: Legacy architecture component for Windows/PowerShell environments  
**Status**: ✅ Stable - Keep separate ecosystem  
**Contributing**: Use PowerShell standards, not Python patterns

### thought-architecture
**Type**: Documentation + Tools collection (not a service)  
**Structure**: `tools/`, `README.md`, no executable service  
**Reason**: Framework and reference materials  
**Status**: ✅ Reference - Consider moving to `docs/thought-architecture/` or keeping as collection  
**Contributing**: Add documentation, tools, examples

### system-proof
**Type**: Prototype / Proof of Concept  
**Structure**: Single `proof_schema.py` + README  
**Reason**: Experimental validation layer  
**Status**: 🟡 **Clarification needed** - Either expand with tests/docs or move to `utils/`  
**Contributing**: If expanding to production service, apply standard template

---

## 🚀 For New Services

When creating a new microservice:

1. **Copy skeleton** from any compliant service (cloud-reason, career-development, ml-model-registry)
2. **Follow the template** above
3. **Add tests** - minimum 70% coverage required
4. **Document** with README, API.md, DEVELOPMENT.md
5. **Containerize** - Create Dockerfile following platform patterns
6. **Update this file** - Add to overview table above

---

## 🔧 Development Setup

All services use the same development workflow:

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python src/main.py

# Or use Docker Compose from root
docker-compose up {SERVICE_NAME}

# Run tests
pytest tests/ -v

# Generate coverage
pytest --cov=src tests/
```

---

## 📊 Structure Conformance Checklist

Use this when developing or reviewing services:

```
For Python Microservices:
✅ README.md with description, quick start, API overview
✅ requirements.txt with pinned versions
✅ Dockerfile with multi-stage build
✅ .env.example with all config variables
✅ src/ directory with main.py, config.py, models/, api/, services/
✅ tests/ directory with unit/, integration/, conftest.py
✅ tests/ directory with minimum 70% code coverage
✅ docs/ directory with API.md, DEVELOPMENT.md, ARCHITECTURE.md
✅ docker-compose.override.yml for local development
✅ Dockerfile builds without errors
✅ Tests pass with pytest
⚠️ scripts/ directory for utilities (optional)

For Special Cases:
⚠️ PowerShell services: Use .psd1, .psm1, PowerShell conventions
⚠️ Documentation/Tools: Use docs/ conventions, clear README purpose
⚠️ Prototypes: Note as prototype in README, document scope
```

---

## 📚 See Also

- [APP_STANDARDIZATION_TEMPLATE.md](APP_STANDARDIZATION_TEMPLATE.md) - Detailed refactoring plan
- [STRUCTURE_DECISIONS.md](STRUCTURE_DECISIONS.md) - Rationale for design decisions
- [../docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md) - Platform architecture
- [../OPTIMIZATION_PLAN.md](../OPTIMIZATION_PLAN.md) - Repository optimization roadmap

