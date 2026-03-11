# Test Competency Tracker

- **Путь**: `components\career-development-system\src\tests\test_competency_tracker.py`
- **Тип**: .PY
- **Размер**: 5808 байт
- **Последнее изменение**: 1772979098.3319335

## Предпросмотр

```
import unittest
from src.core.competency_tracker import CompetencyTracker


class TestCompetencyTracker(unittest.TestCase):

    def setUp(self):
        """Настройка тестового окружения"""
        self.tracker = CompetencyTracker()
        self.user_id = "user_001"

        # Добавляем тестового пользователя
        self.tracker.add_user(self.user_id, "Тестовый Пользователь", "test@example.com")

        # Добавляем тестовые маркеры компетенций
        self.tracker.add_competency_marker(
      
... (файл обрезан для предпросмотра)
```
