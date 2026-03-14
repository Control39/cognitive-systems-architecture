import pytest
import httpx
import time
from contextlib import contextmanager

@contextmanager
def wait_services():
    time.sleep(10)  # Wait docker up
    yield

class TestMetricsEndpoints:
    BASE_URLS = {
        'cloud_reason': 'http://localhost:8000',
        'ml_registry': 'http://localhost:8001',
        'it_compass': 'http://localhost:8501'
    }

    @pytest.fixture(scope='module')
    def client(self):
        with wait_services():
            yield httpx.Client(timeout=10.0)

    @pytest.mark.parametrize('service, path', [
        ('cloud_reason', '/metrics'),
        ('ml_registry', '/metrics'),
        ('it_compass', '/health')  # Streamlit proxy health
    ])
    def test_metrics_available(self, client, service, path):
        url = f"{self.BASE_URLS[service]}{path}"
        resp = client.get(url)
        assert resp.status_code == 200
        assert len(resp.text) > 100  # Non-empty metrics
        if 'prometheus' in resp.text.lower():
            print(f"✅ {service} Prometheus metrics OK")

    def test_baselines(self, client):
        # Latency <200ms sample
        start = time.time()
        client.get(self.BASE_URLS['cloud_reason'] + '/api/v1/status')
        latency = (time.time() - start) * 1000
        assert latency < 200, f"Latency {latency:.0f}ms > 200ms"

