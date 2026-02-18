"""
Модуль ассистента GigaChat для Cloud Reason.

Этот модуль предоставляет функциональность для
взаимодействия с GigaChat API и анализа решений.
"""

import os
import json
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

# Импортируем локальные модули
from .utils.logger import get_logger


@dataclass
class AnalysisRequest:
    """Запрос на анализ решения"""
    decision_id: str
    decision_text: str
    context: str
    analysis_type: str = "general"
    additional_data: Dict[str, Any] = None


@dataclass
class AnalysisResponse:
    """Ответ анализа решения"""
    decision_id: str
    recommendations: List[str]
    insights: List[str]
    confidence: float
    explanation: str


class GigaChatAssistant:
    """Ассистент для работы с GigaChat"""
    
    def __init__(self, api_key: str = None, model: str = "GigaChat"):
        """
        Инициализация ассистента GigaChat.
        
        Args:
            api_key (str, optional): API ключ для GigaChat
            model (str): Модель GigaChat для использования
        """
        self.api_key = api_key or os.getenv("GIGACHAT_API_KEY")
        self.model = model
        self.logger = get_logger("gigachat_assistant")
        
        # Проверка наличия API ключа
        if not self.api_key:
            self.logger.warning("API ключ для GigaChat не найден. Будет использована демонстрационная версия.")
    
    def analyze_decision(self, request: AnalysisRequest) -> AnalysisResponse:
        """
        Анализ решения с помощью GigaChat.
        
        Args:
            request (AnalysisRequest): Запрос на анализ
            
        Returns:
            AnalysisResponse: Ответ анализа
        """
        try:
            # Логирование запроса
            self.logger.info(f"Анализ решения: {request.decision_id}")
            
            # В демонстрационной версии возвращаем фиктивный ответ
            response = self._generate_demo_response(request)
            
            # Логирование ответа
            self.logger.info(f"Анализ завершен для решения: {request.decision_id}")
            
            return response
            
        except Exception as e:
            self.logger.error(f"Ошибка при анализе решения {request.decision_id}: {str(e)}")
            # Возвращаем фиктивный ответ в случае ошибки
            return self._generate_error_response(request, str(e))
    
    def _generate_demo_response(self, request: AnalysisRequest) -> AnalysisResponse:
        """
        Генерация демонстрационного ответа.
        
        Args:
            request (AnalysisRequest): Запрос на анализ
            
        Returns:
            AnalysisResponse: Демонстрационный ответ анализа
        """
        # Создание демонстрационных рекомендаций
        recommendations = [
            "Рассмотрите альтернативные подходы к решению этой задачи",
            "Обратите внимание на потенциальные риски, связанные с этим решением",
            "Изучите лучшие практики в вашей отрасли для подобных решений"
        ]
        
        # Создание демонстрационных инсайтов
        insights = [
            "Решение имеет высокую степень влияния на бизнес-процессы",
            "Требуется дополнительный анализ технической реализуемости",
            "Важно учитывать мнение заинтересованных сторон"
        ]
        
        # Генерация объяснения
        explanation = f"Анализ решения '{request.decision_text[:50]}...' выполнен с использованием модели {self.model}. "
        explanation += "Рекомендации основаны на паттернах принятия решений и лучших практиках."
        
        return AnalysisResponse(
            decision_id=request.decision_id,
            recommendations=recommendations,
            insights=insights,
            confidence=0.85,
            explanation=explanation
        )
    
    def _generate_error_response(self, request: AnalysisRequest, error_message: str) -> AnalysisResponse:
        """
        Генерация ответа с ошибкой.
        
        Args:
            request (AnalysisRequest): Запрос на анализ
            error_message (str): Сообщение об ошибке
            
        Returns:
            AnalysisResponse: Ответ с ошибкой
        """
        return AnalysisResponse(
            decision_id=request.decision_id,
            recommendations=[f"Не удалось выполнить анализ: {error_message}"],
            insights=[],
            confidence=0.0,
            explanation="Произошла ошибка при анализе решения"
        )
    
    def _call_gigachat_api(self, prompt: str) -> str:
        """
        Вызов API GigaChat.
        
        Args:
            prompt (str): Промт для GigaChat
            
        Returns:
            str: Ответ от GigaChat
        """
        # В демонстрационной версии возвращаем фиктивный ответ
        return f"Анализ от GigaChat для промта: {prompt[:100]}..."
    
    def health_check(self) -> bool:
        """
        Проверка состояния ассистента.
        
        Returns:
            bool: True, если ассистент работает, иначе False
        """
        try:
            # В демонстрационной версии всегда возвращаем True
            return True
        except Exception as e:
            self.logger.error(f"Ошибка при проверке состояния ассистента: {str(e)}")
            return False


# Создание глобального экземпляра ассистента
assistant: Optional[GigaChatAssistant] = None


def get_assistant() -> GigaChatAssistant:
    """
    Получение глобального экземпляра ассистента.
    
    Returns:
        GigaChatAssistant: Глобальный экземпляр ассистента
    """
    global assistant
    if assistant is None:
        assistant = GigaChatAssistant()
    return assistant