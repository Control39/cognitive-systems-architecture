# Components Career Development System Src Core Models.Py

- **Путь**: `docs\obsidian-map\components_career-development-system_src_core_models.py.md`
- **Тип**: .MD
- **Размер**: 841 байт
- **Последнее изменение**: 1772680654.8381066

## Предпросмотр

```
# Models

- **Путь**: `components\career-development-system\src\core\models.py`
- **Тип**: .PY
- **Размер**: 2351 байт
- **Последнее изменение**: 1771483370.7979417

## Предпросмотр

```
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80),
... (файл обрезан для предпросмотра)
```
