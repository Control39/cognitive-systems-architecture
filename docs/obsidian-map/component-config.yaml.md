# Component Config

- **Путь**: `component-config.yaml`
- **Тип**: .YAML
- **Размер**: 3660 байт
- **Последнее изменение**: 1772680654.503313

## Предпросмотр

```
component:
  name: "cloud-reason"
  description: "Система облачного рассуждения с REST API и интеграцией с Git"
  version: "0.1.0"
  path: "components/cloud-reason/"

dependencies:
  python:
    - "python>=3.8"
    - "fastapi>=0.68.0"
    - "uvicorn>=0.15.0"
    - "pydantic>=1.8.0"
    - "requests>=2.25.0"
    - "gitpython>=3.1.0"
    - "chardet>=5.0.0"
    - "colorama>=0.4.6"

modules:
  - name: "reasoning_engine"
    path: "core/reasoning_engine.py"
    description: "Основной движок рассуждени
... (файл обрезан для предпросмотра)
```
