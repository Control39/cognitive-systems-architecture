"""
Модуль хранения сессий для Cloud Reason.

Этот модуль предоставляет функциональность для
хранения и управления сессиями пользователей.
"""

import time
from collections import defaultdict
from typing import Dict, Any, Optional
import threading
import uuid


class SessionStore:
    """Хранилище сессий"""
    
    def __init__(self, session_timeout: int = 3600):
        """
        Инициализация хранилища сессий.
        
        Args:
            session_timeout (int): Время жизни сессии в секундах
        """
        self.session_timeout = session_timeout
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self.lock = threading.Lock()
    
    def create_session(self, session_id: str = None) -> str:
        """
        Создание новой сессии.
        
        Args:
            session_id (str, optional): Идентификатор сессии
            
        Returns:
            str: Идентификатор созданной сессии
        """
        if session_id is None:
            session_id = str(uuid.uuid4())
        
        with self.lock:
            self.sessions[session_id] = {
                "created_at": time.time(),
                "last_accessed": time.time(),
                "data": {}
            }
        
        return session_id
    
    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Получение данных сессии.
        
        Args:
            session_id (str): Идентификатор сессии
            
        Returns:
            Optional[Dict[str, Any]]: Данные сессии или None, если сессия не найдена
        """
        with self.lock:
            # Проверка существования сессии
            if session_id not in self.sessions:
                return None
            
            session = self.sessions[session_id]
            
            # Проверка времени жизни сессии
            if time.time() - session["created_at"] > self.session_timeout:
                del self.sessions[session_id]
                return None
            
            # Обновление времени последнего доступа
            session["last_accessed"] = time.time()
            
            return session
    
    def set_session_data(self, session_id: str, key: str, value: Any) -> bool:
        """
        Установка данных сессии.
        
        Args:
            session_id (str): Идентификатор сессии
            key (str): Ключ данных
            value (Any): Значение данных
            
        Returns:
            bool: True, если данные успешно установлены, иначе False
        """
        with self.lock:
            # Проверка существования сессии
            if session_id not in self.sessions:
                return False
            
            session = self.sessions[session_id]
            
            # Проверка времени жизни сессии
            if time.time() - session["created_at"] > self.session_timeout:
                del self.sessions[session_id]
                return False
            
            # Установка данных
            session["data"][key] = value
            session["last_accessed"] = time.time()
            
            return True
    
    def get_session_data(self, session_id: str, key: str, default: Any = None) -> Any:
        """
        Получение данных сессии.
        
        Args:
            session_id (str): Идентификатор сессии
            key (str): Ключ данных
            default (Any): Значение по умолчанию
            
        Returns:
            Any: Значение данных или значение по умолчанию
        """
        with self.lock:
            # Проверка существования сессии
            if session_id not in self.sessions:
                return default
            
            session = self.sessions[session_id]
            
            # Проверка времени жизни сессии
            if time.time() - session["created_at"] > self.session_timeout:
                del self.sessions[session_id]
                return default
            
            # Обновление времени последнего доступа
            session["last_accessed"] = time.time()
            
            return session["data"].get(key, default)
    
    def delete_session(self, session_id: str) -> bool:
        """
        Удаление сессии.
        
        Args:
            session_id (str): Идентификатор сессии
            
        Returns:
            bool: True, если сессия успешно удалена, иначе False
        """
        with self.lock:
            if session_id in self.sessions:
                del self.sessions[session_id]
                return True
            return False
    
    def cleanup_expired_sessions(self) -> int:
        """
        Очистка истекших сессий.
        
        Returns:
            int: Количество удаленных сессий
        """
        current_time = time.time()
        expired_sessions = []
        
        with self.lock:
            for session_id, session in self.sessions.items():
                if current_time - session["created_at"] > self.session_timeout:
                    expired_sessions.append(session_id)
            
            for session_id in expired_sessions:
                del self.sessions[session_id]
        
        return len(expired_sessions)
    
    def get_active_sessions_count(self) -> int:
        """
        Получение количества активных сессий.
        
        Returns:
            int: Количество активных сессий
        """
        current_time = time.time()
        active_count = 0
        
        with self.lock:
            for session in self.sessions.values():
                if current_time - session["created_at"] <= self.session_timeout:
                    active_count += 1
        
        return active_count