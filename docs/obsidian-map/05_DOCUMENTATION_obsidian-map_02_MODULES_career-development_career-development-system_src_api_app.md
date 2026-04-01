# 02 Modules Career Development Career Development System Src Api App

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_career-development_career-development-system_src_api_app.md`
- **Тип**: .MD
- **Размер**: 830 байт
- **Последнее изменение**: 2026-03-13 20:21:29

## Превью

```
# App

- **Путь**: `02_MODULES\career-development\career-development-system\src\api\app.py`
- **Тип**: .PY
- **Размер**: 16,224 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

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
c
... (файл продолжается)
```


