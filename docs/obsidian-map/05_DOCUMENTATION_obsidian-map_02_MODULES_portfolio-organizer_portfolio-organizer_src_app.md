# 02 Modules Portfolio Organizer Portfolio Organizer Src App

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_portfolio-organizer_portfolio-organizer_src_app.md`
- **Тип**: .MD
- **Размер**: 956 байт
- **Последнее изменение**: 2026-03-13 20:21:36

## Превью

```
# App

- **Путь**: `02_MODULES\portfolio-organizer\portfolio-organizer\src\app.py`
- **Тип**: .PY
- **Размер**: 1,766 байт
- **Последнее изменение**: 2026-03-10 19:02:48

## Превью

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
app.r
... (файл продолжается)
```

