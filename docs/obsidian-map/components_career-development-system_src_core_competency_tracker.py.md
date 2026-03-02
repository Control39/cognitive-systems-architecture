# Competency Tracker

- **Путь**: `components\career-development-system\src\core\competency_tracker.py`
- **Тип**: .PY
- **Размер**: 5824 байт
- **Последнее изменение**: 1771483370.8604653

## Предпросмотр

```
class CompetencyTracker:
    """Класс для отслеживания компетенций и карьерного развития"""

    def __init__(self):
        self.users = {}
        self.competency_markers = {}

    def add_user(self, user_id, username, email):
        """Добавить пользователя в систему"""
        self.users[user_id] = {
            "username": username,
            "email": email,
            "skills": {},
            "progress_history": [],
        }

    def add_skill(self, user_id, skill_name, level=1):
   
... (файл обрезан для предпросмотра)
```
