# Developer Example

- **Путь**: `examples\it-compass\developer-example.md`
- **Тип**: .MD
- **Размер**: 1052 байт
- **Последнее изменение**: 1773247992.4724464

## Предпросмотр

```
## IT-Compass: Пример для разработчика

### Задача
Расширить IT-Compass новым типом маркера для оценки навыков в области ИИ.

### Действие
1. Создать файл `components/it-compass/src/data/markers/ai_skills.json` с определением маркера:
   ```json
   {
     "id": "ai_skills",
     "name": "Навыки ИИ",
     "category": "emerging",
     "levels": ["beginner", "intermediate", "advanced", "expert"]
   }
   ```
2. Добавить логику валидации в `components/it-compass/src/core/tracker.py`:
   ```python
   
... (файл обрезан для предпросмотра)
```
