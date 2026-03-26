# 02 Modules Career Development Career Development System Src Core Models

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_career-development_career-development-system_src_core_models.md`
- **Тип**: .MD
- **Размер**: 826 байт
- **Последнее изменение**: 2026-03-13 20:21:28

## Превью

```
# Models

- **Путь**: `02_MODULES\career-development\career-development-system\src\core\models.py`
- **Тип**: .PY
- **Размер**: 2,351 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Col
... (файл продолжается)
```

