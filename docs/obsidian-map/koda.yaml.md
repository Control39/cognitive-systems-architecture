# Koda

- **Путь**: `koda.yaml`
- **Тип**: .YAML
- **Размер**: 1129 байт
- **Последнее изменение**: 1773193177.551625

## Предпросмотр

```
version: "1"
models:
  # Локальные модели Ollama
  - name: Qwen Coder 7B (локально)
    provider: ollama
    model: qwen2.5-coder:7b
    apiBase: http://localhost:11434
    roles:
      - agent
      - chat
      - edit
  
  - name: Qwen Coder 3B (локально)
    provider: ollama
    model: qwen2.5-coder:3b
    apiBase: http://localhost:11434
    roles:
      - chat
      - edit
  
  - name: Gemma 3 4B (локально)
    provider: ollama
    model: gemma3:4b
    apiBase: http://localhost:11434
    rol
... (файл обрезан для предпросмотра)
```
