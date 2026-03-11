# Components Ml Model Registry .Github Workflows Ci.Yml

- **Путь**: `docs\obsidian-map\components_ml-model-registry_.github_workflows_ci.yml.md`
- **Тип**: .MD
- **Размер**: 836 байт
- **Последнее изменение**: 1772680654.8738034

## Предпросмотр

```
# Ci

- **Путь**: `components\ml-model-registry\.github\workflows\ci.yml`
- **Тип**: .YML
- **Размер**: 830 байт
- **Последнее изменение**: 1772457684.538526

## Предпросмотр

```
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    
    - name: Install depen
... (файл обрезан для предпросмотра)
```
