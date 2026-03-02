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
              with:
                  python-version: "3.11"

            - name: Install dependencies
              run: pip install -r requirements.txt && pip install pytest pytest-cov

         
... (файл обрезан для предпросмотра)
```
