# TODO: Migration Plan Execution

## Current Status: Analyzing repository structure

### Step 1: Analyze content in cognitive-architect-manifesto/ (IN PROGRESS)
- [x] List all files in cognitive-architect-manifesto/
- [x] Identify what needs to be migrated vs duplicates
- [ ] Read key methodology files

### Step 2: Create backup tag (PENDING)
- [ ] Create git backup tag before changes

### Step 3: Migrate content from cognitive-architect-manifesto/ (PENDING)
- [ ] Migrate methodology documents → docs/methodology/
- [ ] Migrate architecture documents → docs/architecture/
- [ ] Migrate cases → cases/
- [ ] Migrate grants → docs/ or integration/
- [ ] Migrate support/psychological → docs/methodology/

### Step 4: Update references and paths (PENDING)
- [ ] Find and update Markdown links
- [ ] Find and update Python imports
- [ ] Update config file paths

### Step 5: Remove old directories (PENDING)
- [ ] Remove cognitive-architect-manifesto/
- [ ] Remove old narrative folders (01_CONTEXT, 01_STRATEGY, etc.)

### Step 6: Test the system (PENDING)
- [ ] Run generate_website.py
- [ ] Run generate_obsidian_map.py
- [ ] Run validation scripts

### Step 7: Update documentation (PENDING)
- [ ] Update migration-plan.md
- [ ] Update docs/history/evolution.md
- [ ] Create RELEASE_NOTES.md

