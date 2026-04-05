# Test Api

- **Путь**: `02_MODULES\ml-model-registry\tests\test_api.py`
- **Тип**: .PY
- **Размер**: 551 байт
- **Последнее изменение**: 2026-03-13 20:23:59

## Превью

```
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from ml_model_registry.app import app  # adjust to actual app import

client = TestClient(app)

def test_health():
    response = client.get(\"/health\")
    assert response.status_code == 200

@patch('ml_model_registry.models.registry.db')
def test_register_model(mock_db):
    response = client.post(\"/models\", json={\"name\": \"test\", \"version\": \"1.0\"})
    assert response.status_code == 200

# Add DB
... (файл продолжается)
```


