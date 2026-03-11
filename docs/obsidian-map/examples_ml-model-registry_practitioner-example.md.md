# Practitioner Example

- **Путь**: `examples\ml-model-registry\practitioner-example.md`
- **Тип**: .MD
- **Размер**: 936 байт
- **Последнее изменение**: 1773248095.9501562

## Предпросмотр

```
## ML Model Registry: Пример для практика

### Задача
Оценить качество нескольких моделей для задачи классификации текста.

### Действие
1. Загрузить модели в реестр:
   ```bash
   cd components/ml-model-registry
   python src/api/main.py upload --model bert-base --task text-classification
   python src/api/main.py upload --model roberta-base --task text-classification
   ```
2. Запустить сравнительное тестирование:
   ```bash
   python src/api/main.py benchmark --models bert-base,roberta-base -
... (файл обрезан для предпросмотра)
```
