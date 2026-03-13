# Package

- **Путь**: `07_TOOLS\.ai-config-gui\package.json`
- **Тип**: .JSON
- **Размер**: 1,519 байт
- **Последнее изменение**: 2026-03-13 21:05:04

## Превью

```
{
  "name": "ai-config-gui",
  "version": "1.0.0",
  "description": "Графический интерфейс для управления AI-конфигами",
  "main": "src/main/index.js",
  "scripts": {
    "start": "electron .",
    "build": "electron-builder",
    "dev": "electron . --debug",
    "test": "jest",
    "test:watch": "jest --watch",
    "monitor": "node scripts/monitor.js",
    "monitor:watch": "nodemon --watch ../.ai-config/master-config.yaml --exec 'node scripts/monitor.js'"
  },
  "dependencies": {
    "chart.js"
... (файл продолжается)
```

