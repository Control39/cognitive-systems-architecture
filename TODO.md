# TODO List for Portfolio System Architect - GitHub Actions Enhancement

## Current Task: GitHub Actions for AI Translation + Deploy Notifications + Broken Links
✅ All steps complete! Workflows ready.

**Последовательные шаги (выполни по порядку):**
1. GitHub → repo → Settings → Secrets and variables → Actions → New repository secret:
   - `GIGACHAT_API_KEY`: твой ключ GigaChat (не в .env, в GitHub secrets!)
   - `EMAIL_USERNAME`: leadarchitect@yandex.ru
   - `EMAIL_PASSWORD`: app password Yandex (https://yandex.ru/password/app)
2. `gh workflow run translate-docs.yml` (тест перевода)
3. git add . && git commit -m "Add AI workflows" && git push origin main (триггер deploy + email)
4. Проверь Actions tab и почту leadarchitect@yandex.ru

## Previous Tasks
- ✅ Add Author Role Section to README.md  
- ✅ Repo translation TODO  

## Other Pending
*(Auto-updated as tasks complete)*





