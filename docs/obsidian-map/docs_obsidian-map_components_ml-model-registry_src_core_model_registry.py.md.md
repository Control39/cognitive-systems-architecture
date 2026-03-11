# Components Ml Model Registry Src Core Model Registry.Py

- **Путь**: `docs\obsidian-map\components_ml-model-registry_src_core_model_registry.py.md`
- **Тип**: .MD
- **Размер**: 928 байт
- **Последнее изменение**: 1772680654.8904843

## Предпросмотр

```
# Model Registry

- **Путь**: `components\ml-model-registry\src\core\model_registry.py`
- **Тип**: .PY
- **Размер**: 2135 байт
- **Последнее изменение**: 1772456444.3117213

## Предпросмотр

```
class ModelRegistry:
    """Основной класс для управления реестром моделей"""
    
    def __init__(self):
        self.models = {}
    
    def register_model(self, model_id, model_data):
        """Регистрация новой модели"""
        self.models[model_id] = model_data
        return {"status": "success
... (файл обрезан для предпросмотра)
```
