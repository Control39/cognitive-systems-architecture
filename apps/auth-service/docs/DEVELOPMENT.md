# Auth Service Development

## Setup

```bash
pip install -r requirements.txt
python src/main.py
```

## Testing

```bash
pytest tests/ -v
```

## Building Docker Image

```bash
docker build -t auth-service:latest .
docker run -p 8000:8000 auth-service:latest
```
