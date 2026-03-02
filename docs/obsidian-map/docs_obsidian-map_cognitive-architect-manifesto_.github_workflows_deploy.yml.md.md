# Cognitive Architect Manifesto .Github Workflows Deploy.Yml

- **Путь**: `docs\obsidian-map\cognitive-architect-manifesto_.github_workflows_deploy.yml.md`
- **Тип**: .MD
- **Размер**: 841 байт
- **Последнее изменение**: 1772467524.0543256

## Предпросмотр

```
# Deploy

- **Путь**: `cognitive-architect-manifesto\.github\workflows\deploy.yml`
- **Тип**: .YML
- **Размер**: 881 байт
- **Последнее изменение**: 1772461109.9086783

## Предпросмотр

```
name: Deploy to Production

on:
    push:
        branches: [main]
    pull_request:
        branches: [main]

jobs:
    test-and-deploy:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v3

            - name: Set up Python
              uses: actions/setup-python@v4
       
... (файл обрезан для предпросмотра)
```
