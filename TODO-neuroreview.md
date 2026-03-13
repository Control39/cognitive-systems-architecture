# Neuroreview Fixes TODO - PR #123 (migration/structure-2026)

Status: In Progress | Branch: migration/structure-2026 ✅

## 🔴 1. Security - Flask CSRF Protection & Config (3 files)

### Files:
- `02_MODULES/career-development/career-development-system/src/api/app.py`
- `02_MODULES/portfolio-organizer/portfolio-organizer/src/app.py`
- `02_MODULES/portfolio-organizer/portfolio-organizer/src/api/reasoning_api.py`

### Changes per file:
- Add `from flask_wtf.csrf import CSRFProtect`
- `csrf = CSRFProtect(app)`
- SECRET_KEY mandatory: `app.secret_key = os.environ.get('SECRET_KEY'); if not app.secret_key: raise ValueError(...)`
- `app.run(debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')`

### Dependencies:
1. [x] `02_MODULES/career-development/career-development-system/src/api/requirements.txt` + `flask-wtf>=1.2.0`
2. [x] `02_MODULES/portfolio-organizer/portfolio-organizer/requirements.txt` + `flask-wtf>=1.2.0`

**Commit: [x]** `fix(security): Add CSRF protection to Flask apps + secure config` (career-development app.py, portfolio-organizer app.py & reasoning_api.py, reqs updated)

## 🟡 2. Encoding Script
- `02_MODULES/cloud-reason/cloud_reason/scripts/convert_to_utf8.py`
1. [ ] Add comment: \"# Fully cross-platform UTF-8 handling confirmed\"

**Commit:** `docs(encoding): Confirm cross-platform UTF-8 handling`

## 🟢 3. Unfinished Code - Monitoring
### Files:
1. [ ] `02_MODULES/arch-compass-framework/src/infrastructure/monitoring/logger.py` - Implement basic structlog
2. [ ] `02_MODULES/arch-compass-framework/src/infrastructure/monitoring/metrics.py` - Basic prometheus

**Commit:** `feat(monitoring): Implement structured logging & metrics`

## 📚 4. Documentation
1. [ ] Update `02_MODULES/it-compass/README.md` + Interconnections section
2. [ ] Update `02_MODULES/arch-compass-framework/README.md` + cloud-reason integration
3. [ ] Create `05_DOCUMENTATION/docs/components-interaction.md` Mermaid diagram

**Commit:** `docs: Add component interconnections & interaction diagram`

## ✅ 5. Testing & Verification
1. [ ] `pip install -r <reqs>` for each
2. [ ] Test apps: `SECRET_KEY=test python app.py`, POST JSON (csrf.exempt if API)
3. [ ] `git commit && git push`
4. [ ] Re-run neuroreview

**Next step after this file: Read requirements.txt files**

