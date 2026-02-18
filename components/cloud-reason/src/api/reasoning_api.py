"""
REST API для Cloud Reason.

Этот модуль предоставляет REST API для управления решениями,
их анализа и получения рекомендаций.
"""

from flask import Flask, request, jsonify
from datetime import datetime
import uuid
from typing import List, Dict, Any
import os

# Импортируем локальные модули
from ..gigachat_assistant import GigaChatAssistant, AnalysisRequest
from ..utils.logger import get_logger
from ..utils.validation import validate_decision_data
from ..utils.rate_limiter import RateLimiter
from ..utils.session_store import SessionStore
from ..utils.monitoring import MetricsCollector
from ..utils.error_handler import handle_api_error


# Инициализация приложения Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Инициализация компонентов
logger = get_logger("reasoning_api")
assistant = GigaChatAssistant()
rate_limiter = RateLimiter()
session_store = SessionStore()
metrics = MetricsCollector()

# Хранилище решений (в реальном приложении это будет база данных)
decisions_store = {}
recommendations_store = {}


@app.before_request
def before_request():
    """Предобработка запроса"""
    # Проверка ограничения частоты запросов
    client_ip = request.remote_addr
    if not rate_limiter.is_allowed(client_ip):
        return jsonify({"error": "Превышено ограничение частоты запросов"}), 429
    
    # Создание сессии
    session_id = request.headers.get('X-Session-ID')
    if not session_id:
        session_id = str(uuid.uuid4())
        session_store.create_session(session_id)
    
    # Сохраняем сессию в контексте запроса
    request.session_id = session_id


@app.after_request
def after_request(response):
    """Постобработка запроса"""
    # Логирование запроса
    logger.info(f"{request.method} {request.path} - {response.status_code}")
    
    # Обновление метрик
    metrics.increment_counter("requests_total", {
        "method": request.method,
        "endpoint": request.endpoint or "unknown",
        "status": response.status_code
    })
    
    # Добавление заголовков для CORS
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Session-ID')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    
    return response


@app.route('/api/v1/decisions', methods=['POST'])
def create_decision():
    """
    Создание нового решения.
    
    Request Body:
        title (str): Заголовок решения
        description (str): Описание решения
        context (str): Контекст решения
        owner (str, optional): Владелец решения
        tags (list, optional): Список тегов
        
    Returns:
        JSON: Созданное решение с идентификатором
    """
    try:
        data = request.get_json()
        
        # Валидация данных
        validation_errors = validate_decision_data(data, required_fields=['title', 'description'])
        if validation_errors:
            return jsonify({"error": "Некорректные данные", "details": validation_errors}), 400
        
        # Генерация идентификатора
        decision_id = str(uuid.uuid4())
        
        # Создание решения
        decision = {
            "id": decision_id,
            "title": data['title'],
            "description": data['description'],
            "context": data.get('context', ''),
            "owner": data.get('owner', ''),
            "tags": data.get('tags', []),
            "status": "draft",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        # Сохранение решения
        decisions_store[decision_id] = decision
        
        # Обновление метрик
        metrics.increment_counter("decisions_created_total")
        
        logger.info(f"Создано решение: {decision_id}")
        
        return jsonify(decision), 201
        
    except Exception as e:
        return handle_api_error(e, "create_decision")


@app.route('/api/v1/decisions', methods=['GET'])
def get_decisions():
    """
    Получение списка решений.
    
    Query Parameters:
        status (str, optional): Фильтр по статусу
        owner (str, optional): Фильтр по владельцу
        tag (str, optional): Фильтр по тегу
        
    Returns:
        JSON: Список решений
    """
    try:
        # Получение параметров фильтрации
        status_filter = request.args.get('status')
        owner_filter = request.args.get('owner')
        tag_filter = request.args.get('tag')
        
        # Фильтрация решений
        filtered_decisions = list(decisions_store.values())
        
        if status_filter:
            filtered_decisions = [d for d in filtered_decisions if d.get('status') == status_filter]
        
        if owner_filter:
            filtered_decisions = [d for d in filtered_decisions if d.get('owner') == owner_filter]
        
        if tag_filter:
            filtered_decisions = [d for d in filtered_decisions if tag_filter in d.get('tags', [])]
        
        # Сортировка по дате создания (новые первыми)
        filtered_decisions.sort(key=lambda x: x['created_at'], reverse=True)
        
        logger.info(f"Получен список решений: {len(filtered_decisions)} элементов")
        
        return jsonify(filtered_decisions), 200
        
    except Exception as e:
        return handle_api_error(e, "get_decisions")


@app.route('/api/v1/decisions/<decision_id>', methods=['GET'])
def get_decision(decision_id):
    """
    Получение решения по идентификатору.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Returns:
        JSON: Решение
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        logger.info(f"Получено решение: {decision_id}")
        
        return jsonify(decision), 200
        
    except Exception as e:
        return handle_api_error(e, "get_decision")


@app.route('/api/v1/decisions/<decision_id>', methods=['PUT'])
def update_decision(decision_id):
    """
    Обновление решения.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Request Body:
        title (str, optional): Заголовок решения
        description (str, optional): Описание решения
        context (str, optional): Контекст решения
        owner (str, optional): Владелец решения
        tags (list, optional): Список тегов
        status (str, optional): Статус решения
        
    Returns:
        JSON: Обновленное решение
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        data = request.get_json()
        
        # Обновление полей
        updatable_fields = ['title', 'description', 'context', 'owner', 'tags', 'status']
        for field in updatable_fields:
            if field in data:
                decision[field] = data[field]
        
        # Обновление времени изменения
        decision['updated_at'] = datetime.now().isoformat()
        
        # Сохранение обновленного решения
        decisions_store[decision_id] = decision
        
        logger.info(f"Обновлено решение: {decision_id}")
        
        return jsonify(decision), 200
        
    except Exception as e:
        return handle_api_error(e, "update_decision")


@app.route('/api/v1/decisions/<decision_id>', methods=['DELETE'])
def delete_decision(decision_id):
    """
    Удаление решения.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Returns:
        JSON: Результат удаления
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        # Удаление решения
        del decisions_store[decision_id]
        
        # Удаление связанных рекомендаций
        recommendations_store.pop(decision_id, None)
        
        logger.info(f"Удалено решение: {decision_id}")
        
        return jsonify({"message": "Решение успешно удалено"}), 200
        
    except Exception as e:
        return handle_api_error(e, "delete_decision")


@app.route('/api/v1/decisions/<decision_id>/analyze', methods=['POST'])
def analyze_decision(decision_id):
    """
    Анализ решения с помощью GigaChat.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Request Body:
        analysis_type (str, optional): Тип анализа (по умолчанию "general")
        additional_data (dict, optional): Дополнительные данные для анализа
        
    Returns:
        JSON: Результат анализа
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        data = request.get_json() or {}
        analysis_type = data.get('analysis_type', 'general')
        additional_data = data.get('additional_data', {})
        
        # Создание запроса на анализ
        analysis_request = AnalysisRequest(
            decision_id=decision_id,
            decision_text=f"{decision['title']}\n\n{decision['description']}",
            context=decision.get('context', ''),
            analysis_type=analysis_type,
            additional_data=additional_data
        )
        
        # Выполнение анализа
        analysis_response = assistant.analyze_decision(analysis_request)
        
        # Сохранение рекомендаций
        recommendations = []
        for i, rec_text in enumerate(analysis_response.recommendations):
            recommendation = {
                "id": str(uuid.uuid4()),
                "decision_id": decision_id,
                "text": rec_text,
                "confidence": analysis_response.confidence,
                "insight": analysis_response.insights[i] if i < len(analysis_response.insights) else "",
                "created_at": datetime.now().isoformat()
            }
            recommendations.append(recommendation)
        
        # Сохранение рекомендаций в хранилище
        if decision_id not in recommendations_store:
            recommendations_store[decision_id] = []
        recommendations_store[decision_id].extend(recommendations)
        
        # Обновление статуса решения
        decision['status'] = 'analyzed'
        decision['updated_at'] = datetime.now().isoformat()
        decisions_store[decision_id] = decision
        
        # Обновление метрик
        metrics.increment_counter("decisions_analyzed_total")
        
        logger.info(f"Анализ решения завершен: {decision_id}")
        
        return jsonify({
            "decision_id": decision_id,
            "recommendations": recommendations,
            "insights": analysis_response.insights,
            "confidence": analysis_response.confidence,
            "explanation": analysis_response.explanation
        }), 200
        
    except Exception as e:
        return handle_api_error(e, "analyze_decision")


@app.route('/api/v1/decisions/<decision_id>/recommendations', methods=['GET'])
def get_recommendations(decision_id):
    """
    Получение рекомендаций для решения.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Returns:
        JSON: Список рекомендаций
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        recommendations = recommendations_store.get(decision_id, [])
        
        # Сортировка по уровню уверенности (высокие первыми)
        recommendations.sort(key=lambda x: x.get('confidence', 0), reverse=True)
        
        logger.info(f"Получены рекомендации для решения: {decision_id}")
        
        return jsonify(recommendations), 200
        
    except Exception as e:
        return handle_api_error(e, "get_recommendations")


@app.route('/api/v1/decisions/<decision_id>/recommendations', methods=['POST'])
def add_recommendation(decision_id):
    """
    Добавление рекомендации к решению.
    
    Args:
        decision_id (str): Идентификатор решения
        
    Request Body:
        text (str): Текст рекомендации
        confidence (float, optional): Уровень уверенности (0.0 - 1.0)
        insight (str, optional): Инсайт
        
    Returns:
        JSON: Добавленная рекомендация
    """
    try:
        decision = decisions_store.get(decision_id)
        
        if not decision:
            return jsonify({"error": "Решение не найдено"}), 404
        
        data = request.get_json()
        
        # Валидация данных
        if not data or 'text' not in data:
            return jsonify({"error": "Текст рекомендации обязателен"}), 400
        
        # Создание рекомендации
        recommendation = {
            "id": str(uuid.uuid4()),
            "decision_id": decision_id,
            "text": data['text'],
            "confidence": float(data.get('confidence', 0.5)),
            "insight": data.get('insight', ''),
            "created_at": datetime.now().isoformat()
        }
        
        # Сохранение рекомендации
        if decision_id not in recommendations_store:
            recommendations_store[decision_id] = []
        recommendations_store[decision_id].append(recommendation)
        
        logger.info(f"Добавлена рекомендация к решению: {decision_id}")
        
        return jsonify(recommendation), 201
        
    except Exception as e:
        return handle_api_error(e, "add_recommendation")


@app.route('/api/v1/metrics', methods=['GET'])
def get_metrics():
    """
    Получение метрик системы.
    
    Returns:
        JSON: Метрики системы
    """
    try:
        metrics_data = {
            "total_decisions": len(decisions_store),
            "total_recommendations": sum(len(recs) for recs in recommendations_store.values()),
            "analyzed_decisions": len([d for d in decisions_store.values() if d.get('status') == 'analyzed']),
            "requests_total": metrics.get_counter_value("requests_total"),
            "decisions_created_total": metrics.get_counter_value("decisions_created_total"),
            "decisions_analyzed_total": metrics.get_counter_value("decisions_analyzed_total")
        }
        
        logger.info("Получены метрики системы")
        
        return jsonify(metrics_data), 200
        
    except Exception as e:
        return handle_api_error(e, "get_metrics")


@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """
    Проверка состояния системы.
    
    Returns:
        JSON: Статус системы
    """
    try:
        health_status = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "components": {
                "api": "ok",
                "gigachat_assistant": "ok" if assistant else "error",
                "storage": "ok"
            }
        }
        
        logger.info("Проверка состояния системы выполнена")
        
        return jsonify(health_status), 200
        
    except Exception as e:
        return handle_api_error(e, "health_check")


@app.route('/', methods=['GET'])
def index():
    """
    Главная страница.
    
    Returns:
        HTML: Главная страница веб-интерфейса
    """
    try:
        # Возвращаем простую HTML страницу
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cloud Reason</title>
            <meta charset="utf-8">
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .header { text-align: center; }
                .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 30px; }
                .feature { border: 1px solid #ddd; padding: 20px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Cloud Reason</h1>
                <p>Система облачных рассуждений для принятия решений с использованием ИИ</p>
            </div>
            
            <div class="features">
                <div class="feature">
                    <h3>Анализ решений</h3>
                    <p>Анализ решений с помощью GigaChat</p>
                </div>
                <div class="feature">
                    <h3>Рекомендации</h3>
                    <p>Генерация рекомендаций на основе анализа</p>
                </div>
                <div class="feature">
                    <h3>API</h3>
                    <p>REST API для интеграции с другими системами</p>
                </div>
            </div>
            
            <div style="margin-top: 30px; text-align: center;">
                <p><a href="/api/v1/health">Проверить состояние системы</a></p>
                <p><a href="/api/docs">Документация API</a></p>
            </div>
        </body>
        </html>
        ''', 200
        
    except Exception as e:
        return handle_api_error(e, "index")


@app.route('/api/docs', methods=['GET'])
def api_docs():
    """
    Документация API.
    
    Returns:
        HTML: Страница с документацией API
    """
    try:
        return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cloud Reason API Документация</title>
            <meta charset="utf-8">
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .endpoint { border: 1px solid #ddd; padding: 20px; margin: 10px 0; border-radius: 5px; }
                .method { display: inline-block; padding: 5px 10px; border-radius: 3px; color: white; font-weight: bold; }
                .get { background-color: #28a745; }
                .post { background-color: #007bff; }
                .put { background-color: #ffc107; color: black; }
                .delete { background-color: #dc3545; }
            </style>
        </head>
        <body>
            <h1>Cloud Reason API Документация</h1>
            
            <div class="endpoint">
                <span class="method post">POST</span> /api/v1/decisions
                <p>Создание нового решения</p>
                <pre>
{
  "title": "string",
  "description": "string",
  "context": "string",
  "owner": "string",
  "tags": ["string"]
}
                </pre>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span> /api/v1/decisions
                <p>Получение списка решений</p>
                <p>Параметры: status, owner, tag</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span> /api/v1/decisions/{id}
                <p>Получение решения по ID</p>
            </div>
            
            <div class="endpoint">
                <span class="method put">PUT</span> /api/v1/decisions/{id}
                <p>Обновление решения</p>
            </div>
            
            <div class="endpoint">
                <span class="method delete">DELETE</span> /api/v1/decisions/{id}
                <p>Удаление решения</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span> /api/v1/decisions/{id}/analyze
                <p>Анализ решения с помощью GigaChat</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span> /api/v1/decisions/{id}/recommendations
                <p>Получение рекомендаций для решения</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span> /api/v1/decisions/{id}/recommendations
                <p>Добавление рекомендации к решению</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span> /api/v1/metrics
                <p>Получение метрик системы</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span> /api/v1/health
                <p>Проверка состояния системы</p>
            </div>
        </body>
        </html>
        ''', 200
        
    except Exception as e:
        return handle_api_error(e, "api_docs")


# Обработчик для OPTIONS запросов (CORS)
@app.route('/api/v1/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    """Обработка OPTIONS запросов для CORS"""
    return '', 200


if __name__ == '__main__':
    # Запуск приложения
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)