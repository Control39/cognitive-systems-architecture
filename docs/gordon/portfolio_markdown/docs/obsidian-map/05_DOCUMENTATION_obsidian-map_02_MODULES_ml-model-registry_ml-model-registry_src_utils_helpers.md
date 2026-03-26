# 02 Modules Ml Model Registry Ml Model Registry Src Utils Helpers

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_src_utils_helpers.md`
- **Тип**: .MD
- **Размер**: 861 байт
- **Последнее изменение**: 2026-03-13 20:21:35

## Превью

```
# Helpers

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\src\utils\helpers.py`
- **Тип**: .PY
- **Размер**: 678 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
def validate_model_metadata(metadata):
    """Проверка метаданных модели"""
    required_fields = ['name', 'version', 'framework']
    for field in required_fields:
        if field not in metadata:
            return False, f"Missing required field: {field}"
    return True, "Valid"

def format_model_inf
... (файл продолжается)
```

