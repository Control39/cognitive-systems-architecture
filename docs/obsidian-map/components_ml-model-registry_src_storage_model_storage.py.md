# Model Storage

- **Путь**: `components\ml-model-registry\src\storage\model_storage.py`
- **Тип**: .PY
- **Размер**: 827 байт
- **Последнее изменение**: 1772453888.8057344

## Предпросмотр

```
class ModelStorage:
    """Класс для хранения моделей"""
    
    def __init__(self):
        self.storage_path = "./models"
    
    def save_model(self, model_id, model_data):
        """Сохранение модели"""
        # Заглушка для сохранения модели
        return {"status": "success", "message": f"Model {model_id} saved"}
    
    def load_model(self, model_id):
        """Загрузка модели"""
        # Заглушка для загрузки модели
        return {"status": "success", "model_id": model_id}
    

... (файл обрезан для предпросмотра)
```
