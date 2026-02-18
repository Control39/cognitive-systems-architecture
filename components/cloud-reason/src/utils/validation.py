"""
Модуль валидации данных для Cloud Reason.

Этот модуль предоставляет функции для валидации
входных данных API.
"""

from typing import Dict, List, Any, Optional


def validate_decision_data(data: Dict[str, Any], required_fields: List[str] = None) -> List[str]:
    """
    Валидация данных решения.
    
    Args:
        data (Dict[str, Any]): Данные решения
        required_fields (List[str], optional): Обязательные поля
        
    Returns:
        List[str]: Список ошибок валидации
    """
    errors = []
    
    if not data:
        return ["Данные не предоставлены"]
    
    if required_fields is None:
        required_fields = ['title', 'description']
    
    # Проверка обязательных полей
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"Поле '{field}' обязательно для заполнения")
    
    # Проверка типов данных
    if 'title' in data and not isinstance(data['title'], str):
        errors.append("Поле 'title' должно быть строкой")
    
    if 'description' in data and not isinstance(data['description'], str):
        errors.append("Поле 'description' должно быть строкой")
    
    if 'context' in data and not isinstance(data['context'], str):
        errors.append("Поле 'context' должно быть строкой")
    
    if 'owner' in data and not isinstance(data['owner'], str):
        errors.append("Поле 'owner' должно быть строкой")
    
    if 'tags' in data and not isinstance(data['tags'], list):
        errors.append("Поле 'tags' должно быть списком")
    
    # Проверка длины полей
    if 'title' in data and len(data['title']) > 255:
        errors.append("Поле 'title' не должно превышать 255 символов")
    
    if 'description' in data and len(data['description']) > 10000:
        errors.append("Поле 'description' не должно превышать 10000 символов")
    
    return errors


def validate_recommendation_data(data: Dict[str, Any], required_fields: List[str] = None) -> List[str]:
    """
    Валидация данных рекомендации.
    
    Args:
        data (Dict[str, Any]): Данные рекомендации
        required_fields (List[str], optional): Обязательные поля
        
    Returns:
        List[str]: Список ошибок валидации
    """
    errors = []
    
    if not data:
        return ["Данные не предоставлены"]
    
    if required_fields is None:
        required_fields = ['text']
    
    # Проверка обязательных полей
    for field in required_fields:
        if field not in data or not data[field]:
            errors.append(f"Поле '{field}' обязательно для заполнения")
    
    # Проверка типов данных
    if 'text' in data and not isinstance(data['text'], str):
        errors.append("Поле 'text' должно быть строкой")
    
    if 'confidence' in data:
        try:
            confidence = float(data['confidence'])
            if not 0.0 <= confidence <= 1.0:
                errors.append("Поле 'confidence' должно быть числом от 0.0 до 1.0")
        except (ValueError, TypeError):
            errors.append("Поле 'confidence' должно быть числом")
    
    if 'insight' in data and not isinstance(data['insight'], str):
        errors.append("Поле 'insight' должно быть строкой")
    
    # Проверка длины полей
    if 'text' in data and len(data['text']) > 1000:
        errors.append("Поле 'text' не должно превышать 1000 символов")
    
    if 'insight' in data and len(data['insight']) > 500:
        errors.append("Поле 'insight' не должно превышать 500 символов")
    
    return errors