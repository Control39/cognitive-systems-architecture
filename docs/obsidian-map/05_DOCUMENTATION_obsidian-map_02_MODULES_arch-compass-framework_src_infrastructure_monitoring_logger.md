# 02 Modules Arch Compass Framework Src Infrastructure Monitoring Logger

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_arch-compass-framework_src_infrastructure_monitoring_logger.md`
- **Тип**: .MD
- **Размер**: 890 байт
- **Последнее изменение**: 2026-03-13 20:21:34

## Превью

```
# Logger

- **Путь**: `02_MODULES\arch-compass-framework\src\infrastructure\monitoring\logger.py`
- **Тип**: .PY
- **Размер**: 618 байт
- **Последнее изменение**: 2026-03-05 05:17:34

## Превью

```
import structlog

logger = structlog.get_logger()

def setup_logging(app):
    # TODO: настроить структурированное логирование
    pass

# Пример использования в коде
async def update_marker(marker_id: str, status: str):
    logger.info("marker_update_started", marker_id=marker_id, new_status=status)
... (файл продолжается)
```


