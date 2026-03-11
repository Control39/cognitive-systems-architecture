# Tests Config

- **Путь**: `components\cloud_reason\tests\tests-config.yaml`
- **Тип**: .YAML
- **Размер**: 939 байт
- **Последнее изменение**: 1772979098.3522613

## Предпросмотр

```
test:
  component: "cloud-reason"
  directory: "tests/"
  framework: "pytest"
  options:
    verbose: true
    capture_output: false
    fail_fast: false

test_suites:
  - name: "api_tests"
    files: ["tests/test_api.py"]
    description: "Тестирование REST API endpoints"
  - name: "reasoning_tests"
    files: ["tests/test_reasoning.py"]
    description: "Тестирование движка рассуждений"

test_data:
  directory: "tests/data/"
  files:
    - "test_context.json"
    - "test_hypotheses.json"

cove
... (файл обрезан для предпросмотра)
```
