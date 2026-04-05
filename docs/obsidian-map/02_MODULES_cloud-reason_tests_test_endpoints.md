# Test Endpoints

- **Путь**: `02_MODULES\cloud-reason\tests\test_endpoints.py`
- **Тип**: .PY
- **Размер**: 603 байт
- **Последнее изменение**: 2026-03-13 20:23:58

## Превью

```
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from cloud_reason.api.endpoints import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert \"health\" in response.json()

@patch('cloud_reason.api.endpoints.git')  # mock git
def test_reasoning(mock_git):
    mock_git.Repo.return_value = MagicMock()
    response = client.post(\"/reason\", json={\"repo\": \"test\"})
    a
... (файл продолжается)
```


