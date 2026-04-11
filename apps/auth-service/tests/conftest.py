"""Pytest configuration and shared fixtures for auth-service."""
import pytest

@pytest.fixture
def client():
    """FastAPI test client fixture."""
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)
