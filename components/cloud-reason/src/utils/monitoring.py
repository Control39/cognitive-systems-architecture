"""
Модуль мониторинга для Cloud Reason.

Этот модуль предоставляет функциональность для
сбора и хранения метрик системы.
"""

import time
from collections import defaultdict
from typing import Dict, Any, Union
import threading


class MetricsCollector:
    """Сборщик метрик"""
    
    def __init__(self):
        """Инициализация сборщика метрик"""
        self.counters: Dict[str, Dict[str, Union[int, Dict[str, str]]]] = defaultdict(lambda: {
            "value": 0,
            "labels": {}
        })
        self.gauges: Dict[str, Dict[str, Union[float, Dict[str, str]]]] = defaultdict(lambda: {
            "value": 0.0,
            "labels": {}
        })
        self.histograms: Dict[str, Dict[str, Union[list, Dict[str, str]]]] = defaultdict(lambda: {
            "values": [],
            "labels": {}
        })
        self.lock = threading.Lock()
    
    def increment_counter(self, name: str, labels: Dict[str, str] = None) -> None:
        """
        Увеличение счетчика.
        
        Args:
            name (str): Имя счетчика
            labels (Dict[str, str], optional): Метки для счетчика
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            if key not in self.counters:
                self.counters[key] = {
                    "value": 0,
                    "labels": labels
                }
            self.counters[key]["value"] += 1
    
    def set_gauge(self, name: str, value: float, labels: Dict[str, str] = None) -> None:
        """
        Установка значения измерителя.
        
        Args:
            name (str): Имя измерителя
            value (float): Значение измерителя
            labels (Dict[str, str], optional): Метки для измерителя
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            if key not in self.gauges:
                self.gauges[key] = {
                    "value": 0.0,
                    "labels": labels
                }
            self.gauges[key]["value"] = value
    
    def observe_histogram(self, name: str, value: float, labels: Dict[str, str] = None) -> None:
        """
        Добавление значения в гистограмму.
        
        Args:
            name (str): Имя гистограммы
            value (float): Значение для добавления
            labels (Dict[str, str], optional): Метки для гистограммы
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            if key not in self.histograms:
                self.histograms[key] = {
                    "values": [],
                    "labels": labels
                }
            self.histograms[key]["values"].append(value)
    
    def get_counter_value(self, name: str, labels: Dict[str, str] = None) -> int:
        """
        Получение значения счетчика.
        
        Args:
            name (str): Имя счетчика
            labels (Dict[str, str], optional): Метки для счетчика
            
        Returns:
            int: Значение счетчика
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            return self.counters.get(key, {"value": 0})["value"]
    
    def get_gauge_value(self, name: str, labels: Dict[str, str] = None) -> float:
        """
        Получение значения измерителя.
        
        Args:
            name (str): Имя измерителя
            labels (Dict[str, str], optional): Метки для измерителя
            
        Returns:
            float: Значение измерителя
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            return self.gauges.get(key, {"value": 0.0})["value"]
    
    def get_histogram_values(self, name: str, labels: Dict[str, str] = None) -> list:
        """
        Получение значений гистограммы.
        
        Args:
            name (str): Имя гистограммы
            labels (Dict[str, str], optional): Метки для гистограммы
            
        Returns:
            list: Список значений гистограммы
        """
        if labels is None:
            labels = {}
        
        key = self._get_metric_key(name, labels)
        
        with self.lock:
            return list(self.histograms.get(key, {"values": []})["values"])
    
    def get_all_metrics(self) -> Dict[str, Any]:
        """
        Получение всех метрик.
        
        Returns:
            Dict[str, Any]: Все метрики системы
        """
        with self.lock:
            return {
                "counters": dict(self.counters),
                "gauges": dict(self.gauges),
                "histograms": dict(self.histograms)
            }
    
    def reset_metrics(self) -> None:
        """Сброс всех метрик"""
        with self.lock:
            self.counters.clear()
            self.gauges.clear()
            self.histograms.clear()
    
    def _get_metric_key(self, name: str, labels: Dict[str, str]) -> str:
        """
        Получение ключа метрики.
        
        Args:
            name (str): Имя метрики
            labels (Dict[str, str]): Метки метрики
            
        Returns:
            str: Ключ метрики
        """
        if not labels:
            return name
        
        # Сортировка меток для обеспечения консистентности
        sorted_labels = sorted(labels.items())
        label_str = ",".join([f"{k}={v}" for k, v in sorted_labels])
        return f"{name}{{{label_str}}}"