"""
Модуль логирования для Cloud Reason.

Этот модуль предоставляет настроенное логирование
для всех компонентов системы.
"""

import logging
import os
from typing import Optional


def get_logger(name: str, level: Optional[int] = None) -> logging.Logger:
    """
    Получение настроенного логгера.
    
    Args:
        name (str): Имя логгера
        level (int, optional): Уровень логирования
        
    Returns:
        logging.Logger: Настроенный логгер
    """
    # Создание логгера
    logger = logging.getLogger(name)
    
    # Установка уровня логирования
    if level is None:
        level = getattr(logging, os.getenv('LOG_LEVEL', 'INFO').upper(), logging.INFO)
    logger.setLevel(level)
    
    # Проверка, есть ли уже обработчики
    if not logger.handlers:
        # Создание обработчика для вывода в консоль
        handler = logging.StreamHandler()
        
        # Создание форматировщика
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        
        # Добавление обработчика к логгеру
        logger.addHandler(handler)
    
    return logger