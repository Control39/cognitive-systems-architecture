# Components Career Development System Src Api App.Py

- **Путь**: `docs\obsidian-map\components_career-development-system_src_api_app.py.md`
- **Тип**: .MD
- **Размер**: 845 байт
- **Последнее изменение**: 1772467524.0123227

## Предпросмотр

```
# App

- **Путь**: `components\career-development-system\src\api\app.py`
- **Тип**: .PY
- **Размер**: 16224 байт
- **Последнее изменение**: 1771483371.1261973

## Предпросмотр

```
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
import os
import hashlib
import secrets

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///career_dev.db"
)
db = SQLAlchemy(app)


# Модель пользователя
class User(db.Mo
... (файл обрезан для предпросмотра)
```
