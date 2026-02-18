"""
Модуль обработки ошибок для Cloud Reason.

Этот модуль предоставляет функции для
унифицированной обработки ошибок API.
"""

import logging
import traceback
from typing import Any, Dict
from flask import jsonify


def handle_api_error(exception: Exception, context: str = None) -> tuple:
    """
    Обработка ошибки API.
    
    Args:
        exception (Exception): Исключение
        context (str, optional): Контекст ошибки
        
    Returns:
        tuple: Ответ с ошибкой и кодом состояния
    """
    # Получение логгера
    logger = logging.getLogger("error_handler")
    
    # Логирование ошибки
    error_msg = f"API Error in {context}: {str(exception)}"
    logger.error(error_msg)
    logger.error(traceback.format_exc())
    
    # Возвращение ответа с ошибкой
    return jsonify({
        "error": "Внутренняя ошибка сервера",
        "message": str(exception) if isinstance(exception, (ValueError, TypeError, KeyError)) else "Произошла внутренняя ошибка"
    }), 500


def handle_validation_error(errors: list) -> tuple:
    """
    Обработка ошибки валидации.
    
    Args:
        errors (list): Список ошибок валидации
        
    Returns:
        tuple: Ответ с ошибкой валидации и кодом состояния
    """
    return jsonify({
        "error": "Ошибка валидации",
        "details": errors
    }), 400


def handle_not_found_error(resource: str) -> tuple:
    """
    Обработка ошибки "не найдено".
    
    Args:
        resource (str): Название ресурса
        
    Returns:
        tuple: Ответ с ошибкой "не найдено" и кодом состояния
    """
    return jsonify({
        "error": f"Ресурс не найден: {resource}"
    }), 404


def handle_rate_limit_error() -> tuple:
    """
    Обработка ошибки ограничения частоты запросов.
    
    Returns:
        tuple: Ответ с ошибкой ограничения частоты и кодом состояния
    """
    return jsonify({
        "error": "Превышено ограничение частоты запросов",
        "message": "Пожалуйста, повторите попытку позже"
    }), 429


def handle_unauthorized_error() -> tuple:
    """
    Обработка ошибки неавторизованного доступа.
    
    Returns:
        tuple: Ответ с ошибкой неавторизованного доступа и кодом состояния
    """
    return jsonify({
        "error": "Неавторизованный доступ",
        "message": "Требуется аутентификация"
    }), 401


def handle_forbidden_error() -> tuple:
    """
    Обработка ошибки запрещенного доступа.
    
    Returns:
        tuple: Ответ с ошибкой запрещенного доступа и кодом состояния
    """
    return jsonify({
        "error": "Доступ запрещен",
        "message": "У вас нет прав для выполнения этого действия"
    }), 403


def create_error_response(error_code: str, message: str, details: Any = None, status_code: int = 400) -> tuple:
    """
    Создание стандартного ответа с ошибкой.
    
    Args:
        error_code (str): Код ошибки
        message (str): Сообщение об ошибке
        details (Any, optional): Детали ошибки
        status_code (int): Код состояния HTTP
        
    Returns:
        tuple: Ответ с ошибкой и кодом состояния
    """
    response = {
        "error": error_code,
        "message": message
    }
    
    if details:
        response["details"] = details
    
    return jsonify(response), status_code