# Code Quality

- **Путь**: `code-quality.yaml`
- **Тип**: .YAML
- **Размер**: 3048 байт
- **Последнее изменение**: 1772680654.472061

## Предпросмотр

```
# code-quality.yaml
# Правила качества кода для мультиязычного проекта

python:
  linting:
    tool: "ruff"
    config:
      line_length: 88
      target_version: "py38"
      select: ["E", "F", "I", "W", "C"]
      ignore: []
    paths:
      - "components/*/src/**/*.py"
      - "scripts/*.py"

  formatting:
    tool: "black"
    config:
      line_length: 88
      target_version: ["py38"]
    paths:
      - "components/*/src/**/*.py"
      - "scripts/*.py"

  type_checking:
    tool: "mypy"
 
... (файл обрезан для предпросмотра)
```
