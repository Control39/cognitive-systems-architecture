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
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run unit tests
      run: |
        python -m unittest tes
... (файл обрезан для предпросмотра)
```
