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
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullab
... (файл обрезан для предпросмотра)
```
