# Apps Structure Design Decisions

**Date**: 2026-04-11  
**Decision Board**: Phase 4 Standardization Review  
**Status**: Approved for Phase 4.2-4.4 implementation

---

## Decision 1: Standard Template for Python Microservices

**Question**: Should all Python microservices follow the same directory structure?

**Decision**: ✅ **YES** - Adopt standard template for all FastAPI services  
**Rationale**:
- Reduces onboarding time for contributors
- Enables automated tooling (CI/CD pipelines, linters, test discovery)
- Aligns with industry standards (FastAPI, Python best practices)
- Supports future abstraction (shared base image, common middleware)

**Applied to**:
- career-development, cloud-reason, ml-model-registry (already compliant)
- auth-service, portfolio-organizer, job-automation-agent (Phase 4.2 refactors)

**Exceptions**: arch-compass-framework (PowerShell), thought-architecture (docs), system-proof (minimal scope)

---

## Decision 2: auth-service Expansion

**Question**: Should auth-service expand from 3 files to full template?

**Decision**: ✅ **YES in Phase 4.2** - Expand to support future growth  
**Rationale**:
- Currently bare-bones (main.py only)
- Likely to grow (OAuth, SAML, 2FA features)
- Test coverage required before adding features
- No breaking changes—internal refactor only

**Implementation**:
```bash
# Create structure
mkdir -p auth-service/src/auth-service/tests/{unit,integration,e2e}
mkdir -p auth-service/src auth-service/docs
mkdir -p auth-service/scripts

# Move & refactor
mv auth-service/main.py → auth-service/src/main.py
# Update imports in Dockerfile & requirements.txt
```

**Risk**: ⚠️ Import updates needed (low risk - single file)  
**Testing**: Run docker build + pytest  
**Timeline**: 15 minutes

---

## Decision 3: portfolio-organizer Naming

**Question**: Rename `portfolio-organizer/` to `src/`?

**Decision**: ✅ **YES in Phase 4.2** - Follow standard naming  
**Rationale**:
- Confusing: directory named after service, but should be src/
- Breaks convention: other apps use src/ for source
- Easier CI/CD scripting: all apps have `src/main.py`

**Implementation**:
```bash
# Single rename (non-breaking)
git mv apps/portfolio-organizer/portfolio-organizer apps/portfolio-organizer/src
# Update relative imports if any
```

**Risk**: 🟢 Very low (no imports affected if properly namespaced)  
**Testing**: docker build + simple smoke test  
**Timeline**: 5 minutes

---

## Decision 4: job-automation-agent docker-compose.agent.yml

**Question**: Move `docker-compose.agent.yml` from app dir to deployment/?

**Decision**: ✅ **YES in Phase 4.2** - Centralize Docker configurations  
**Rationale**:
- `docker-compose.yml` files belong in deployment/ (per root-level structure)
- Easier orchestration: single docker-compose up from deployment/
- Reduces app directory bloat
- Follows repo convention

**Implementation**:
```bash
# Move file
git mv apps/job-automation-agent/docker-compose.agent.yml \
      deployment/docker-compose.job-automation-agent.yml

# Update references in:
# - .gitignore (if present)
# - CI/CD scripts
# - DEVELOPMENT.md
```

**Risk**: 🟢 Very low (path change only)  
**Testing**: `docker-compose -f deployment/docker-compose.job-automation-agent.yml up`  
**Timeline**: 10 minutes

---

## Decision 5: it-compass Top-Level Directories

**Question**: Consolidate 6 top-level dirs (portfolio/, support/, scripts/) into src/?

**Decision**: 🟡 **DEFERRED to Phase 5** - Document but don't refactor yet  
**Rationale**:
- Current structure works for its complexity
- More than just renaming—significant refactoring needed
- Risk higher: affects 21 .py files + documentation
- Decision 4.1-4.3 provide value; revisit this in Phase 5 scope review

**Current structure** (good enough for now):
```
it-compass/
├── src/                 # Core logic (OK)
├── portfolio/           # Portfolio-specific (OK - nested business logic)
├── support/             # Support utilities (OK - organized)
├── scripts/             # Helper scripts (OK - utility)
├── decisions/           # Architecture decisions (OK - ADRs)
├── examples/            # Usage examples (OK - docs+code)
├── docs/                # Documentation (OK - complete)
```

**Future decision** (Phase 5):
- If it-compass grows beyond 30 .py files → consolidate to src/{core,portfolio,support}
- Current complexity (21 .py) justifies current organization

---

## Decision 6: arch-compass-framework (PowerShell)

**Question**: How should we handle PowerShell module in Python apps directory?

**Decision**: ✅ **KEEP & LABEL** - Special case, documented  
**Rationale**:
- Part of platform ecosystem (referenced by docs)
- Different language ≠ should remove
- Clear labeling prevents confusion
- Supports Windows/PowerShell communities

**Implementation**:
- Add ⚠️ label in apps/README.md (DONE)
- Create separate contributing guide for PowerShell standards
- Document in STRUCTURE_DECISIONS.md (THIS FILE)

**Status**: ✅ Compliant - No changes needed

---

## Decision 7: thought-architecture Classification

**Question**: Is thought-architecture a service, docs, or tools collection?

**Decision**: 🟡 **CLARIFY in Phase 5** - Currently documented as special case  
**Current Status**: 0 .py files, README + tools/

**Options explored**:
1. **Move to docs/thought-architecture/** → If primarily reference material
2. **Keep in apps/ + expand** → If becoming a service
3. **Move to tools/thought-architecture/** → If utility library

**Recommendation**: Keep as-is pending Phase 5 classification  
**Owner**: Document owner should clarify intent in Q2 2026 review

---

## Decision 8: system-proof Scope

**Question**: Should system-proof be a full service, utility, or prototype?

**Decision**: 🟡 **CLARIFY in Phase 5** - Note as prototype for now  
**Current Status**: 1 .py file (proof_schema.py) + README

**Paths forward**:
1. **Expand to service** → Add tests, docs, full src/ structure
2. **Move to utils/** → If supporting utility only
3. **Archive** → If prototype complete

**Recommendation**: Add note in README clarifying scope; review in Phase 5  
**Next step**: Owner should determine classification before Phase 5

---

## Phase 4.2 Action Summary

| Action | App | Risk | Timeline | Status |
|--------|-----|------|----------|--------|
| Expand to template | auth-service | 🟢 Low | 15 min | Phase 4.2 |
| Rename dir | portfolio-organizer | 🟢 Low | 5 min | Phase 4.2 |
| Move docker-compose | job-automation-agent | 🟢 Low | 10 min | Phase 4.2 |
| Document PowerShell | arch-compass-framework | ✅ Done | 0 min | COMPLETE |
| Defer consolidation | it-compass | 🟡 Medium | - | Phase 5 review |
| Clarify intent | thought-architecture | 🟡 Medium | - | Phase 5 review |
| Clarify scope | system-proof | 🟡 Medium | - | Phase 5 review |

**Total Phase 4.2 time**: ~30 minutes  
**Expected quality improvement**: 7.9→8.2/10

---

## Rollback Plan

If Phase 4.2 encounters issues:
```bash
git reset --hard HEAD~1  # Revert last commit
git push -f origin refactor/optimize-structure
```

Changes are on separate branch; main remains unaffected.

---

## Sign-off

- **Decision date**: 2026-04-11
- **Review board**: Phase 4 implementation team
- **Next review**: Phase 5 scope planning (TBD)
- **Owner**: Repository Architecture Board

