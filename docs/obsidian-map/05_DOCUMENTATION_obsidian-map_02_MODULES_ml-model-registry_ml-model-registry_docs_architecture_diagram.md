# 02 Modules Ml Model Registry Ml Model Registry Docs Architecture Diagram

- **Путь**: `05_DOCUMENTATION\obsidian-map\02_MODULES_ml-model-registry_ml-model-registry_docs_architecture_diagram.md`
- **Тип**: .MD
- **Размер**: 927 байт
- **Последнее изменение**: 2026-03-13 20:21:28

## Превью

```
# Architecture Diagram

- **Путь**: `02_MODULES\ml-model-registry\ml-model-registry\docs\architecture_diagram.md`
- **Тип**: .MD
- **Размер**: 2,985 байт
- **Последнее изменение**: 2026-03-08 16:11:38

## Превью

```
# Архитектурная диаграмма системы версионирования ML-моделей

## Общая архитектура

```mermaid
graph TD
    A[Клиентские приложения] --> B[API Gateway]
    B --> C[ML Model Registry API]
    
    C --> D[Model Registry]
    C --> E[Model Storage]
    C --> F[Metadata Store]
    
   
... (файл продолжается)
```


