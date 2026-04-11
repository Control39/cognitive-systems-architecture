# Auth Service Tests

Test suite structure:
- `unit/` - Unit tests for individual functions and classes
- `integration/` - API integration tests
- `e2e/` - End-to-end workflow tests

Run tests:
```
pytest tests/ -v
```

With coverage:
```
pytest --cov=src tests/
```
