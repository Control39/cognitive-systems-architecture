# Components Ml Model Registry Docs Architecture Diagram.Md

- **Путь**: `docs\obsidian-map\components_ml-model-registry_docs_architecture_diagram.md.md`
- **Тип**: .MD
- **Размер**: 943 байт
- **Последнее изменение**: 1772680654.8738034

## Предпросмотр

```
# Architecture Diagram

- **Путь**: `components\ml-model-registry\docs\architecture_diagram.md`
- **Тип**: .MD
- **Размер**: 2896 байт
- **Последнее изменение**: 1772454333.0572896

## Предпросмотр

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
    
    D --> G[Model
... (файл обрезан для предпросмотра)
```
