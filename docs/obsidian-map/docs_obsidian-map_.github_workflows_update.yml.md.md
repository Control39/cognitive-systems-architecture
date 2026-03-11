# .Github Workflows Update.Yml

- **Путь**: `docs\obsidian-map\.github_workflows_update.yml.md`
- **Тип**: .MD
- **Размер**: 902 байт
- **Последнее изменение**: 1772680654.7907605

## Предпросмотр

```
# Update

- **Путь**: `.github\workflows\update.yml`
- **Тип**: .YML
- **Размер**: 1314 байт
- **Последнее изменение**: 1771413012.6585035

## Предпросмотр

```
name: Ежедневное обновление портфолио

on:
  schedule:
    # Запуск каждый день в 03:00 UTC (06:00 MSK)
    - cron: '0 3 * * *'
  workflow_dispatch: # Позволяет запускать вручную

jobs:
  update-portfolio:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout репозитория
      uses: actions/checkout@v3
      with:
        token: ${{
... (файл обрезан для предпросмотра)
```
