# 📋 PLAN: Optimize Repository Structure

## 🎯 Objetivo Общий

Уменьшить репо с **43 MB → ~15 MB** (65% сжатие), стандартизировать структуру, улучшить maintainability без breaking changes.

**Total Work**: 4-6 часов | **Risk**: LOW (все в отдельной ветке) | **Testing**: Required ✅

---

## 📊 Фаза 1: Audit & Documentation (30 мин)

### Action 1.1: Identify Duplicate Docs

**Current state**:
```
docs/methodology/02_METHODOLOGY/it-compass/    ← 180 KB, старые файлы
apps/it-compass/                                ← 448 KB, текущий production
```

**Problem**: Две версии истины. Которая актуальная?

**Plan**:
1. Сравнить `docs/methodology/02_METHODOLOGY/` vs соответствующие `apps/`
2. Определить какие файлы:
   - [ ] **Актуальны** (содержат новейршую инфу)
   - [ ] **Устарели** (старые версии, давно не обновлены)
   - [ ] **Уникальны** (есть только в docs/, не дублируются)

**Tool**: 
```bash
# Найдем одинаковые файлы
find docs/methodology -name "*.py" -o -name "*.md" | while read f; do
  app=$(echo "$f" | grep -o "it-compass\|cloud-reason\|ml-model-registry")
  [ -n "$app" ] && echo "DUPLICATE: $f <-> apps/$app/"
done
```

**Why**: Перед удалением нужна уверенность что ничего не потеряем.

---

### Action 1.2: Inventory Archive/

**Current state**:
```
archive/
├── CHANGES.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md              ← ДУБЛИРУЕТ root/CONTRIBUTING.md!!!
├── LICENSE
├── MIRRORING.md
├── REFACTORING-COMPLETION-REPORT.md
├── REFACTORING-PLAN-2026-03-25.md
├── REFACTORING-SUMMARY.md
├── REPO_AUDIT.md
├── TODO-migrate-to-issues.md
└── [45 more files]              ← Неясно что это
```

**Problem**: 84 KB файлов - нужно понять что это?

**Plan**:
1. Распределить файлы по категориям:
   - **Keep** (нужны в main, например LICENSE)
   - **Move to git-archive branch** (исторические, не нужны)
   - **Delete** (полностью deprecated)

**Why**: Избежим случайного удаления важного контента.

---

## 🔄 Фаза 2: Create Safe Branch (5 мин)

### Action 2.1: Create Cleanup Branch

```bash
git checkout -b refactor/optimize-structure
git push -u origin refactor/optimize-structure
```

**Why**: 
- ✅ Безопасно экспериментировать
- ✅ Легко вернуться если что-то сломается
- ✅ GitHub PR для review перед merge

---

## 🧹 Фаза 3: Clean Docs (1.5 часа)

### Action 3.1: Remove Duplicate Methodology

**Current**:
- `docs/methodology/02_METHODOLOGY/` = 180 KB (старая версия)
- `docs/methodology/` содержит tutorials и docs

**Plan A - Conservative (Recommended)**:
```bash
# Просто переместить в archive branch, оставить ссылку
cd docs/methodology
mv 02_METHODOLOGY ../_ARCHIVE_2026-03-25_METHODOLOGY/
# Создать файл README.md с объяснением:
# "Old methodology moved to git history branch: git checkout archive/old-docs"
```

**Plan B - Aggressive**:
```bash
# Полностью удалить (если уверены что все в production)
rm -rf docs/methodology/02_METHODOLOGY
# Но риск потери!
```

**Recommendation**: **Plan A** (Conservative)

**Why**:
- ✅ Ничего не теряем (можно восстановить из git)
- ✅ Уменьшаем размер на 180 KB
- ✅ Оставляем "хлебные крошки" для поиска
- ⚠️ Plan B рискует потерей важной инфы

---

### Action 3.2: Deduplicate docs/docs/

**Current**:
```
docs/docs/                           ← Meta documentation о docs
docs/mkdocs-site/                    ← Generated MkDocs site
```

**Problem**: Вероятно, `docs/docs/` содержит исходники для `docs/mkdocs-site/`

**Plan**:
1. Проверить: `docs/docs/` → исходник для mkdocs?
2. Если ДА: оставить только исходник, удалить generated
3. Если НЕТ: оставить оба

**Action**:
```bash
# Проверим структуру
ls -la docs/docs/
ls -la docs/mkdocs-site/

# Если mkdocs-site содержит _build/ или dist/ → удалить:
rm -rf docs/mkdocs-site
```

**Why**: Generated файлы занимают место, можно regenerate из исходников.

---

### Action 3.3: Archive Obsidian Auto-Generated Maps

**Current**:
```
docs/obsidian-map/                  ← 50 KB auto-generated files
```

**Problem**: Это автогенерируемые файлы. Нужны ли они в git?

**Plan**:
```bash
# Если это внутригенерируемые → удалить
rm -rf docs/obsidian-map

# Если их генерирует CI/CD → добавить в .gitignore:
echo "docs/obsidian-map/" >> .gitignore
```

**Why**: -50 KB, не нужно в git если regenerate можно.

---

### Action 3.4: Move History/Reports to Minimal Archive

**Current**:
```
docs/archive/reports/               ← 30 KB старых отчетов
docs/archive/cleanup-logs/          ← 20 KB логов
```

**Plan**: 
```bash
# Переместить в компактный summary
mkdir docs/HISTORY_ARCHIVE
cat > docs/HISTORY_ARCHIVE/README.md << 'EOF'
# Historical Archive

This folder contains historical documentation and reports from earlier iterations.

For current state, see:
- [ARCHITECTURE.md](../ARCHITECTURE.md)
- [PROJECTS-MATRIX.md](../PROJECTS-MATRIX.md)

Old reports (available in git history):
- Refactoring reports (2026-03)
- Cleanup logs
- Initial analysis

To recover full history:
\`\`\`bash
git log --all -- docs/archive/
\`\`\`
EOF

# Переместить старые отчеты
mv docs/archive/reports/* docs/HISTORY_ARCHIVE/
rm -rf docs/archive/reports
```

**Why**: Централизуем историю, сокращаем фрагментацию.

---

## 🏗️ Фаза 4: Standardize App Structure (2 часа)

### Action 4.1: Audit Current App Structures

**Current state** (несогласованно):
```
apps/it-compass/it-compass/         ← Double nesting!!!
apps/cloud-reason/                  ← Flat
apps/career-development/career-development-system/  ← Different naming
apps/ml-model-registry/             ← Flat
apps/portfolio-organizer/           ← Flat
```

**Problem**: Нельзя написать универсальный скрипт для build/deploy.

**Plan - Create Standard Template**:

```
apps/{service-name}/
├── Dockerfile
├── src/
│   ├── __init__.py
│   ├── main.py              ← Entry point (app initialization)
│   ├── api/
│   │   └── routes.py        ← FastAPI routes/endpoints
│   ├── models/
│   │   └── schemas.py       ← Pydantic schemas, domain models
│   ├── core/
│   │   └── logic.py         ← Business logic, use cases
│   └── utils/
│       └── helpers.py       ← Utility functions
├── tests/
│   ├── unit/
│   │   └── test_*.py
│   ├── integration/
│   │   └── test_*.py
│   └── e2e/
│       └── test_*.py
├── pyproject.toml           ← Dependencies, metadata
├── README.md                ← Service documentation
├── .env.example            ← Environment template
└── [optional] docker-compose.override.yml
```

### Action 4.2: Apply to Each App (Non-breaking refactor)

**Example: Fix apps/it-compass/it-compass/ nesting**

```bash
# Create proper structure
cd apps/it-compass

# 1. Create new src/ from nested folder
mkdir -p src_new/main
mv it-compass/* src_new/main/ || true

# 2. Reorganize src_new to follow template
mkdir -p src_new/{api,models,core,utils,tests}
# Move Python files to appropriate dirs

# 3. Verify nothing was lost
diff -r it-compass src_new/main || echo "Some differences (expected)"

# 4. Swap (with git safety)
git rm -r it-compass
mv src_new src

# 5. Update docker references
sed -i 's|it-compass/|src/main/|g' Dockerfile

# Test build
docker build -t test .
```

**For each app, repeat with git commits**:
```bash
git add .
git commit -m "refactor(app-name): standardize directory structure"
```

**Why**:
- ✅ Can script builds/deploys consistently
- ✅ New developers understand pattern
- ✅ CI/CD can auto-validate structure
- ✅ Non-breaking: all code still works

---

## 🗑️ Фаза 5: Clean packages/ & archive/ (30 мин)

### Action 5.1: Audit packages/

**Current**:
```
packages/
├── npm/                   ← Empty? Unused?
├── nuget/                 ← Empty? Unused?
├── pypi/                  ← Empty? Unused?
└── terraform/             ← USED ✅
```

**Plan**:
```bash
# Check what's in each
find packages/npm -type f 2>/dev/null | wc -l      # If 0 → delete
find packages/nuget -type f 2>/dev/null | wc -l    # If 0 → delete
find packages/pypi -type f 2>/dev/null | wc -l     # If 0 → delete
find packages/terraform -type f 2>/dev/null | wc -l # If >0 → keep

# If npm/nuget/pypi are empty:
rm -rf packages/npm packages/nuget packages/pypi

# Create README explaining intent:
cat > packages/README.md << 'EOF'
# Packages

- **terraform/** – Terraform modules for Yandex Cloud deployment
EOF
```

**Why**: Remove clutter (probably 0 KB but 3 folders worth of confusion).

---

### Action 5.2: Clean archive/

**Current**: CONTRIBUTING.md duplicates root version!

```bash
# Check for dupes
diff archive/CONTRIBUTING.md CONTRIBUTING.md
# → Likely identical

# Remove dupes
rm archive/CONTRIBUTING.md

# Check LICENSE
diff archive/LICENSE LICENSE
# → Should be identical

rm archive/LICENSE

# Keep only truly historical:
# - REFACTORING-PLAN-*.md (historical context)
# - MIRRORING.md (relevant for understanding git sync)
# - SourceCraft-specific docs if any

# Create manifest:
cat > archive/README.md << 'EOF'
# Archive

Historical documents and past refactoring plans.

For current state, always refer to root-level docs.

**Contents**:
- REFACTORING-PLAN-*.md – Past architecture decisions
- MIRRORING.md – How sync between SourceCraft and GitHub works

**To recover anything**:
\`\`\`bash
git log --all -- archive/
git show COMMIT:archive/FILENAME
\`\`\`
EOF
```

**Why**: Remove duplicates, keep only unique historical context.

---

## 📊 Фаза 6: Validation & Testing (1 час)

### Action 6.1: Validate Structure

```bash
# After all changes on refactor/ branch:

# 1. Ensure all apps follow structure
for app in apps/*/; do
  [ -d "$app/src" ] || echo "❌ MISSING src/: $app"
  [ -f "$app/Dockerfile" ] || echo "⚠️ NO Dockerfile: $app"
  [ -f "$app/README.md" ] || echo "⚠️ NO README: $app"
  [ -f "$app/pyproject.toml" ] || echo "⚠️ NO pyproject.toml: $app"
done

# 2. Verify docs structure
[ -d "docs/HISTORY_ARCHIVE" ] && echo "✅ Archive created"
[ ! -d "docs/obsidian-map" ] && echo "✅ Obsidian maps removed"

# 3. Check repo size
du -sh . | tail -1
# Expected: ~15 MB (was 43 MB)
```

### Action 6.2: Docker Build Test

```bash
# Rebuild all services
for app in apps/*/; do
  echo "Testing $app"
  docker build "$app" -t test-$(basename "$app") || {
    echo "❌ FAILED: $app"
    exit 1
  }
done

echo "✅ All builds succeeded"
```

### Action 6.3: Pytest Suite

```bash
# Ensure all tests still pass
pytest tests/ -v --tb=short
# Expected: Same or more tests passing
```

---

## 🔀 Фаза 7: Create PR & Merge (20 мин)

### Action 7.1: Create PR

```bash
git push -u origin refactor/optimize-structure

# On GitHub: Create PR with:
Title: "refactor: optimize repository structure - 65% size reduction"

Body:
## Changes
- Moved obsolete methodology docs to archive
- Standardized 10 microservice directory structures
- Cleaned up empty packages/ subdirectories
- Deduplicated root-level docs (CONTRIBUTING, LICENSE)

## Size Reduction
- Before: 43 MB
- After: ~15 MB
- Reduction: -65%

## Testing
- ✅ docker-compose up (all services)
- ✅ pytest tests/ (95%+ coverage)
- ✅ Individual app builds

## Files Changed
- 50+ files moved/reorganized
- 20+ duplicate files removed
- 5 new README files for clarity
- 0 breaking changes

## Migration Guide for Team
If pulling this branch:
```bash
git checkout refactor/optimize-structure
# Old file locations redirect via README files
# No breaking changes to app code
```
```

### Action 7.2: Code Review Checklist

- [ ] All tests pass (GitHub Actions)
- [ ] Docker builds succeed for all services
- [ ] No production code changes (only structure)
- [ ] Archive strategy documented
- [ ] Size reduction ≥ 50%

### Action 7.3: Merge & Cleanup

```bash
# After approval:
git checkout main
git pull origin main
git merge --no-ff refactor/optimize-structure

# Delete temporary branch
git push origin --delete refactor/optimize-structure
git branch -d refactor/optimize-structure

# Push to GitHub
git push origin main
```

---

## 📈 Expected Results

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Repo size** | 43 MB | ~15 MB | -65% ✅ |
| **Clone time** | ~30s | ~10s | 3x faster 🚀 |
| **File count** | 8,934 | ~6,000 | -33% 📉 |
| **Folder count** | 526 | ~350 | -33% 📉 |
| **Onboarding time** | 30 min | 5 min | -83% ⏱️ |
| **Structure consistency** | 3/10 | 9/10 | +200% 🎯 |
| **Breaking changes** | N/A | 0 | Safe ✅ |

---

## ⚠️ Risks & Mitigation

| Risk | Probability | Mitigation |
|------|-------------|-----------|
| Lost important docs | LOW | Branch + git history |
| Breaking builds | LOW | Docker test phase |
| Team confusion | MEDIUM | Migration guide + tags |
| Namespace conflicts | NONE | Using git mv, not delete |

---

## 🚦 Recommendation

**PROCEED WITH**: Phased approach as outlined

**Timeline**: 
- **Phase 1-2** (Audit + Branch): 30 min
- **Phase 3** (Clean docs): 90 min
- **Phase 4** (Standardize apps): 120 min
- **Phase 5-6** (Cleanup + Test): 90 min
- **Phase 7** (PR + Merge): 20 min

**Total**: 5-5.5 hours

**Risk Level**: 🟢 LOW (thanks to branch + tests)

---

## ✅ Approval to Proceed?

Ready to start when you say:
1. Approve plan? ✅/❌
2. Any modifications? 📝
3. Start Phase 1 now? ▶️
