# 07 Tools .Ai Config Gui Master Config

- **Путь**: `05_DOCUMENTATION\obsidian-map\07_TOOLS_.ai-config-gui_master-config.md`
- **Тип**: .MD
- **Размер**: 507 байт
- **Последнее изменение**: 2026-03-13 20:21:38

## Превью

```
# Master Config

- **Путь**: `07_apps\\ai-config-manager\master-config.yaml`
- **Тип**: .YAML
- **Размер**: 272 байт
- **Последнее изменение**: 2026-03-12 18:11:48

## Превью

```


- id: huggingface-llama
  name: Llama 3 (Hugging Face)
  provider:
    type: huggingface
    model: meta-llama/Meta-Llama-3-8B
    auth:
      keyEnv: HUGGINGFACE_API_KEY
  capabilities:
    context: 8192
    maxTokens: 2048
  defaults:
    temperature: 0.3
```

```


