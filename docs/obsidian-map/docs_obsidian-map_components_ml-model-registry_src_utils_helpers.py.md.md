# Components Ml Model Registry Src Utils Helpers.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_src_utils_helpers.py.md`
- **Тип**: .MD
- **Размер**: 877 байт
- **Последнее изменение**: 1772467523.9473238

## Предпросмотр

```
# Helpers

- **Путь**: `components\ml-model-registry\src\utils\helpers.py`
- **Тип**: .PY
- **Размер**: 662 байт
- **Последнее изменение**: 1772453972.241858

## Предпросмотр

```
def validate_model_metadata(metadata):
    """Проверка метаданных модели"""
    required_fields = ['name', 'version', 'framework']
    for field in required_fields:
        if field not in metadata:
            return False, f"Missing required field: {field}"
    return True, "Valid"

def format_model_info(model_data):
... (файл обрезан для предпросмотра)
```
