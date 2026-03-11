# App

- **Путь**: `components\portfolio-organizer\src\app.py`
- **Тип**: .PY
- **Размер**: 1766 байт
- **Последнее изменение**: 1773162168.1529887

## Предпросмотр

```
"""
Основное приложение Portfolio Organizer.
Объединяет все API модули.
"""

from flask import Flask
from api.reasoning_api import app as reasoning_app
from api.ml_model_registry_integration import bp as ml_model_registry_bp

app = Flask(__name__)

# Регистрируем blueprint для интеграции с ML Model Registry
app.register_blueprint(ml_model_registry_bp)

# Копируем маршруты из reasoning_api
# Поскольку reasoning_api определяет маршруты напрямую на объекте app,
# мы не можем просто импортировать ег
... (файл обрезан для предпросмотра)
```
