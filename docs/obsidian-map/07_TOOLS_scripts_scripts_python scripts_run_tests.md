# Run Tests

- **Путь**: `07_TOOLS\scripts\scripts\python scripts\run_tests.sh`
- **Тип**: .SH
- **Размер**: 334 байт
- **Последнее изменение**: 2026-03-13 21:05:04

## Превью

```
#!/bin/bash
# Получаем директорию тестов из конфигурации
TEST_DIR=$(python -c "import yaml; c=yaml.safe_load(open('component-config.yaml')); print(c['tests']['directory'])")

echo "Запуск тестов в: $TEST_DIR"
pytest $TEST_DIR -v --cov=components/cloud-reason --cov-report=html

```

