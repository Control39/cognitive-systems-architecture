# Cognitive Architect Manifesto 02 Methodology Arch Compass Src Infrastructure Monitoring Metrics.Py

- **Путь**: `docs\obsidian-map\cognitive-architect-manifesto_02_METHODOLOGY_arch-compass_src_infrastructure_monitoring_metrics.py.md`
- **Тип**: .MD
- **Размер**: 870 байт
- **Последнее изменение**: 1772680654.806386

## Предпросмотр

```
# Metrics

- **Путь**: `cognitive-architect-manifesto\02_METHODOLOGY\arch-compass\src\infrastructure\monitoring\metrics.py`
- **Тип**: .PY
- **Размер**: 640 байт
- **Последнее изменение**: 1772460824.811356

## Предпросмотр

```
from prometheus_client import Counter, Histogram, start_http_server
from functools import wraps

REQUEST_COUNT = Counter('api_requests_total', 'Total API requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('api_request_duration_seconds', 'Request latency')

de
... (файл обрезан для предпросмотра)
```
