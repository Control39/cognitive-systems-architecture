# Model Storage

- **Путь**: `components\ml-model-registry\src\storage\model_storage.py`
- **Тип**: .PY
- **Размер**: 846 байт
- **Последнее изменение**: 1772979098.4254918

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
