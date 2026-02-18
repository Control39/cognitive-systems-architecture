"""
Модуль ограничения частоты запросов для Cloud Reason.

Этот модуль предоставляет функциональность для
ограничения частоты API запросов.
"""

import time
from collections import defaultdict
from typing import Dict, List
import threading


class RateLimiter:
    """Ограничитель частоты запросов"""
    
    def __init__(self, max_requests: int = 100, time_window: int = 60):
        """
        Инициализация ограничителя частоты запросов.
        
        Args:
            max_requests (int): Максимальное количество запросов за период
            time_window (int): Период времени в секундах
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.lock = threading.Lock()
    
    def is_allowed(self, client_id: str) -> bool:
        """
        Проверка, разрешен ли запрос для клиента.
        
        Args:
            client_id (str): Идентификатор клиента
            
        Returns:
            bool: True, если запрос разрешен, иначе False
        """
        with self.lock:
            current_time = time.time()
            
            # Удаление устаревших записей
            self.requests[client_id] = [
                req_time for req_time in self.requests[client_id]
                if current_time - req_time < self.time_window
            ]
            
            # Проверка лимита
            if len(self.requests[client_id]) < self.max_requests:
                self.requests[client_id].append(current_time)
                return True
            else:
                return False
    
    def get_remaining_requests(self, client_id: str) -> int:
        """
        Получение количества оставшихся запросов для клиента.
        
        Args:
            client_id (str): Идентификатор клиента
            
        Returns:
            int: Количество оставшихся запросов
        """
        with self.lock:
            current_time = time.time()
            
            # Удаление устаревших записей
            self.requests[client_id] = [
                req_time for req_time in self.requests[client_id]
                if current_time - req_time < self.time_window
            ]
            
            return max(0, self.max_requests - len(self.requests[client_id]))
    
    def reset_client(self, client_id: str) -> None:
        """
        Сброс счетчика запросов для клиента.
        
        Args:
            client_id (str): Идентификатор клиента
        """
        with self.lock:
            if client_id in self.requests:
                del self.requests[client_id]