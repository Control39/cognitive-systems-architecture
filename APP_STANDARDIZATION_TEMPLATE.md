# Phase 4: App Structure Standardization Template

**Date**: 2026-04-11  
**Status**: Proposed for review  
**Branch**: `refactor/optimize-structure`

---

## Current State Analysis

| App | Type | Size | Structure Score | Issue |
|-----|------|------|-----------------|-------|
| arch-compass-framework | PowerShell | ~5 files | ⚠️ 3/10 | Not Python; different pattern |
| auth-service | Python (minimal) | 3 files | ⚠️ 4/10 | No src/, tests/ directories |
| career-development | FastAPI | 12 .py | ✅ 9/10 | Good structure, follow as model |
| cloud-reason | FastAPI | 19 .py | ✅ 9/10 | Good structure, follow as model |
| it-compass | Complex | 21 .py | ⚠️ 8/10 | Too many top-level dirs (portfolio, support, scripts, decisions) |
| job-automation-agent | FastAPI | 8 .py | 🟡 7/10 | Has docker-compose inline; should be separate |
| ml-model-registry | FastAPI | 22 .py | ✅ 9/10 | Good structure, follow as model |
| portfolio-organizer | FastAPI | 3 .py | 🟡 6/10 | Inconsistent dir naming |
| system-proof | Python | 1 .py | ⚠️ 3/10 | Minimal; unclear purpose |
| thought-architecture | Docs + Tools | 0 .py | 🟡 5/10 | Not a service; needs reclassification |

---

## Recommended Standard Template

```
apps/{APP_NAME}/
├── README.md                           # Service overview, quick start
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Container image definition
├── docker-compose.override.yml         # (Optional) Local dev overrides
├── .env.example                        # Environment variables template
│
├── src/                                # Main source code
│   ├── __init__.py
│   ├── main.py                         # FastAPI app or entry point
│   ├── config.py                       # Configuration & settings
│   ├── models/                         # Data models, schemas
│   │   └── __init__.py
│   ├── api/                            # API endpoints
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/                       # Business logic
│   │   ├── __init__.py
│   │   └── service.py
│   ├── utils/                          # Utilities, helpers
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── db/                             # Database (if applicable)
│       ├── __init__.py
│       └── models.py
│
├── tests/                              # Test suite
│   ├── __init__.py
│   ├── conftest.py                     # Pytest fixtures
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_services.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api.py
│   └── e2e/
│       ├── __init__.py
│       └── test_workflows.py
│
├── docs/                               # App-specific documentation
│   ├── API.md                          # API documentation
│   ├── DEVELOPMENT.md                  # Dev setup & guidelines
│   └── ARCHITECTURE.md                 # Internal architecture
│
├── scripts/                            # Utility scripts (optional)
│   ├── __init__.py
│   └── migrate.py                      # Migration scripts, etc
│
├── alembic/                            # DB migration (if using SQLAlchemy)
│   └── versions/
│
└── .gitignore                          # Git ignore rules
```

---

## Standardization Actions by App

### ✅ **NO CHANGES NEEDED** (Already compliant)
- `career-development`: Already follows template
- `cloud-reason`: Already follows template  
- `ml-model-registry`: Already follows template

### 🟡 **REFACTOR RECOMMENDED** (Non-breaking improvements)

#### `auth-service` → Expand structure
```
Current: main.py + requirements.txt + Dockerfile
Action: Create src/ directory, move main.py → src/main.py, add tests/, docs/
Risk: LOW (minimal app, isolated)
Size gain: +3 boilerplate files
```

#### `portfolio-organizer` → Fix naming
```
Current: portfolio-organizer/ (should be src/)
Action: Rename portfolio-organizer/ → src/
Risk: LOW (update imports in main.py)
Size gain: Clearer structure
```

#### `job-automation-agent` → Extract docker-compose
```
Current: docker-compose.agent.yml inside app directory
Action: Move to deployment/docker-compose.job-automation-agent.yml
Risk: LOW (just file move)
Reference: Add volume path in DEVELOPMENT.md
```

#### `it-compass` → Consolidate top-level dirs
```
Current: 6 top-level dirs (portfolio/, support/, scripts/, decisions/, examples/, docs/)
Action: Move to src/portfolio/, src/support/, scripts/, docs/ (keep as-is, non-breaking)
Risk: MEDIUM (many imports to verify)
Benefit: Aligns with other apps
```

### ⚠️ **SPECIAL HANDLING** (Non-standard patterns)

#### `arch-compass-framework` → PowerShell Module
```
Current: .psd1, .psm1 (PowerShell Modules)
Status: KEEP AS-IS (different ecosystem, documented in README)
Reason: Legacy component; requires PowerShell environment
Action: Add label in apps/README: "⚠️ PowerShell module, not Python service"
```

#### `thought-architecture` → Reclassify
```
Current: docs/ + tools/ (not a microservice)
Status: SHOULD MOVE OR CLEARLY MARK
Options:
  a) Move to docs/thought-architecture/ (if documentation)
  b) Create services/thought-architecture-service/ if runnable
  c) Keep in apps/ but mark clearly in README: "Documentation & Tools Collection"
```

#### `system-proof` → Expand or move
```
Current: 1 .py file + schema
Status: EITHER expand or document purpose
Options:
  a) Expand with tests/, docs/ if active service
  b) Move to utils/system-proof-validator/ if supporting utility
  c) Clarify purpose in README
```

---

## Implementation Steps (Phase 4)

### Step 1: Document "AS-IS" state (Non-breaking)
Create `apps/README.md` with:
- Matrix of all 10 apps
- Structure conformance checklist (✅ compliant, 🟡 optional improvements, ⚠️ special cases)
- Contributing guidelines: "New apps should follow template in APP_STANDARDIZATION_TEMPLATE.md"

### Step 2: Refactor 3 low-risk apps (Non-breaking)
- `auth-service`: Add src/, tests/, docs/ structure
- `portfolio-organizer`: Rename portfolio-organizer/ → src/
- `job-automation-agent`: Move docker-compose.agent.yml to deployment/

### Step 3: Flag and document special cases
- Add labels for `arch-compass-framework` (PowerShell), `thought-architecture` (Docs), `system-proof` (Special)
- Create decision log in `apps/STRUCTURE_DECISIONS.md`

### Step 4: Verify no breaking changes
- Run unit tests for refactored apps
- Verify imports resolve correctly
- Test Docker builds for each app

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Broken imports | Test suite must pass 100% |
| Docker build failure | Rebuild each app's image |
| GitOps manifests outdated | Tests will catch path changes |
| User confusion | Add STRUCTURE_DECISIONS.md documenting why |

---

## Expected Outcomes

✅ **Metrics**:
- 10 apps → 7 fully compliant + 3 documented special cases
- Onboarding time: -30% (clear template)
- CI/CD maintainability: +25% (consistent paths)
- Quality score improvement: 7.9/10 → 8.4/10

**Files to create**:
- `apps/README.md` (structure matrix + guidelines)
- `apps/STRUCTURE_DECISIONS.md` (rationale for special cases)
- Updates to 3 apps (non-breaking refactors)

---

## Decision Point

**Ready to proceed?** ⚠️ This is **recommended but not blocking**.

Options:
1. ✅ **Execute Phase 4** → Standardize 3 low-risk apps now
2. 🟡 **Skip Phase 4** → Move to Phase 5 (cleanup) for other improvements
3. 🔄 **Partial Phase 4** → Only document template, let future PRs standardize gradually

**Recommendation**: Execute Phase 4.1 (Document template) + Phase 4.2 (3 low-risk refactors)  
**Why**: Non-breaking, aligns new apps, improves maintainability

