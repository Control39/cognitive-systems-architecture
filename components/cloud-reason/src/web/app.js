/**
 * Фронтенд приложение для Cloud Reason
 * 
 * Этот файл содержит клиентский JavaScript код для взаимодействия
 * с API Cloud Reason и управления пользовательским интерфейсом.
 */

// Базовый URL для API
const API_BASE_URL = '/api/v1';

// Глобальные переменные
let currentDecisions = [];
let currentRecommendations = [];

// DOM элементы
const elements = {
    decisionsList: document.getElementById('decisions-list'),
    noDecisions: document.getElementById('no-decisions'),
    recommendationsList: document.getElementById('recommendations-list'),
    noRecommendations: document.getElementById('no-recommendations'),
    searchDecisions: document.getElementById('search-decisions'),
    statusFilter: document.getElementById('status-filter'),
    decisionSelect: document.getElementById('decision-select'),
    analysisResults: document.getElementById('analysis-results'),
    totalDecisions: document.getElementById('total-decisions'),
    analyzedDecisions: document.getElementById('analyzed-decisions'),
    totalRecommendations: document.getElementById('total-recommendations'),
    avgConfidence: document.getElementById('avg-confidence')
};

// Модальные окна
const modals = {
    createDecision: document.getElementById('create-decision-modal'),
    decisionDetails: document.getElementById('decision-details-modal')
};

// Кнопки
const buttons = {
    createDecision: document.getElementById('create-decision-btn'),
    analyze: document.getElementById('analyze-btn'),
    cancelCreate: document.getElementById('cancel-create'),
    closeDetails: document.getElementById('close-details')
};

// Формы
const forms = {
    createDecision: document.getElementById('create-decision-form')
};

/**
 * Показать уведомление
 * @param {string} message - Сообщение
 * @param {string} type - Тип уведомления (success, error, info)
 */
function showNotification(message, type = 'info') {
    // Удалить существующие уведомления
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Создать новое уведомление
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Удалить уведомление через 3 секунды
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

/**
 * Показать индикатор загрузки
 * @param {HTMLElement} container - Контейнер для индикатора
 */
function showLoading(container) {
    container.innerHTML = '<div class="loading"></div>';
}

/**
 * Скрыть индикатор загрузки
 * @param {HTMLElement} container - Контейнер с индикатором
 */
function hideLoading(container) {
    container.innerHTML = '';
}

/**
 * Выполнить HTTP запрос
 * @param {string} url - URL запроса
 * @param {Object} options - Опции запроса
 * @returns {Promise} - Promise с результатом запроса
 */
async function apiRequest(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API request error:', error);
        showNotification('Ошибка при выполнении запроса к API', 'error');
        throw error;
    }
}

/**
 * Загрузить список решений
 */
async function loadDecisions() {
    try {
        showLoading(elements.decisionsList);
        
        const decisions = await apiRequest(`${API_BASE_URL}/decisions`);
        currentDecisions = decisions;
        
        renderDecisions(decisions);
        updateDashboard();
        updateDecisionSelect();
        
    } catch (error) {
        console.error('Error loading decisions:', error);
        elements.decisionsList.innerHTML = '<p>Ошибка при загрузке решений</p>';
    }
}

/**
 * Отфильтровать решения
 * @param {Array} decisions - Список решений
 * @returns {Array} - Отфильтрованный список решений
 */
function filterDecisions(decisions) {
    const searchTerm = elements.searchDecisions.value.toLowerCase();
    const statusFilter = elements.statusFilter.value;
    
    return decisions.filter(decision => {
        const matchesSearch = decision.title.toLowerCase().includes(searchTerm) ||
                           decision.description.toLowerCase().includes(searchTerm);
        const matchesStatus = !statusFilter || decision.status === statusFilter;
        
        return matchesSearch && matchesStatus;
    });
}

/**
 * Отрендерить список решений
 * @param {Array} decisions - Список решений
 */
function renderDecisions(decisions) {
    const filteredDecisions = filterDecisions(decisions);
    
    if (filteredDecisions.length === 0) {
        elements.decisionsList.style.display = 'none';
        elements.noDecisions.style.display = 'block';
        return;
    }
    
    elements.decisionsList.style.display = 'grid';
    elements.noDecisions.style.display = 'none';
    
    elements.decisionsList.innerHTML = filteredDecisions.map(decision => `
        <div class="decision-card" data-id="${decision.id}">
            <h3>${escapeHtml(decision.title)}</h3>
            <p>${escapeHtml(truncateText(decision.description, 100))}</p>
            <div class="decision-meta">
                <span>Создано: ${formatDate(decision.created_at)}</span>
                <span class="decision-status ${decision.status}">
                    ${getStatusText(decision.status)}
                </span>
            </div>
        </div>
    `).join('');
    
    // Добавить обработчики клика на карточки решений
    document.querySelectorAll('.decision-card').forEach(card => {
        card.addEventListener('click', () => {
            const decisionId = card.dataset.id;
            showDecisionDetails(decisionId);
        });
    });
}

/**
 * Обновить селект решений
 */
function updateDecisionSelect() {
    elements.decisionSelect.innerHTML = '<option value="">Выберите решение</option>';
    
    currentDecisions.forEach(decision => {
        const option = document.createElement('option');
        option.value = decision.id;
        option.textContent = decision.title;
        elements.decisionSelect.appendChild(option);
    });
}

/**
 * Получить текст статуса
 * @param {string} status - Статус
 * @returns {string} - Текст статуса
 */
function getStatusText(status) {
    const statusMap = {
        'draft': 'Черновик',
        'in_review': 'На рассмотрении',
        'approved': 'Утверждено',
        'rejected': 'Отклонено'
    };
    
    return statusMap[status] || status;
}

/**
 * Экранировать HTML
 * @param {string} text - Текст
 * @returns {string} - Экранированный текст
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

/**
 * Обрезать текст
 * @param {string} text - Текст
 * @param {number} maxLength - Максимальная длина
 * @returns {string} - Обрезанный текст
 */
function truncateText(text, maxLength) {
    if (text.length <= maxLength) {
        return text;
    }
    return text.substring(0, maxLength) + '...';
}

/**
 * Форматировать дату
 * @param {string} dateStr - Строка даты
 * @returns {string} - Отформатированная дата
 */
function formatDate(dateStr) {
    try {
        const date = new Date(dateStr);
        return date.toLocaleDateString('ru-RU');
    } catch (error) {
        return dateStr;
    }
}

/**
 * Показать детали решения
 * @param {string} decisionId - Идентификатор решения
 */
async function showDecisionDetails(decisionId) {
    try {
        const decision = await apiRequest(`${API_BASE_URL}/decisions/${decisionId}`);
        
        const detailContent = `
            <h3>${escapeHtml(decision.title)}</h3>
            <p><strong>Описание:</strong></p>
            <p>${escapeHtml(decision.description)}</p>
            <p><strong>Контекст:</strong></p>
            <p>${escapeHtml(decision.context || 'Не указан')}</p>
            <p><strong>Статус:</strong> ${getStatusText(decision.status)}</p>
            <p><strong>Владелец:</strong> ${escapeHtml(decision.owner || 'Не указан')}</p>
            <p><strong>Создано:</strong> ${formatDate(decision.created_at)}</p>
            <p><strong>Обновлено:</strong> ${formatDate(decision.updated_at)}</p>
            ${decision.tags && decision.tags.length > 0 ? 
                `<p><strong>Теги:</strong> ${escapeHtml(decision.tags.join(', '))}</p>` : ''}
        `;
        
        document.getElementById('decision-detail-title').textContent = decision.title;
        document.getElementById('decision-detail-content').innerHTML = detailContent;
        
        modals.decisionDetails.style.display = 'block';
        
    } catch (error) {
        console.error('Error loading decision details:', error);
        showNotification('Ошибка при загрузке деталей решения', 'error');
    }
}

/**
 * Создать новое решение
 * @param {Object} decisionData - Данные решения
 */
async function createDecision(decisionData) {
    try {
        const decision = await apiRequest(`${API_BASE_URL}/decisions`, {
            method: 'POST',
            body: JSON.stringify(decisionData)
        });
        
        showNotification('Решение успешно создано!', 'success');
        closeCreateDecisionModal();
        await loadDecisions();
        
        return decision;
    } catch (error) {
        console.error('Error creating decision:', error);
        showNotification('Ошибка при создании решения', 'error');
    }
}

/**
 * Анализировать решение
 * @param {string} decisionId - Идентификатор решения
 */
async function analyzeDecision(decisionId) {
    try {
        showLoading(elements.analysisResults);
        
        const response = await apiRequest(`${API_BASE_URL}/decisions/${decisionId}/analyze`, {
            method: 'POST',
            body: JSON.stringify({
                analysis_type: 'general'
            })
        });
        
        renderAnalysisResults(response);
        await loadRecommendations(decisionId);
        
    } catch (error) {
        console.error('Error analyzing decision:', error);
        elements.analysisResults.innerHTML = '<p>Ошибка при анализе решения</p>';
        showNotification('Ошибка при анализе решения', 'error');
    }
}

/**
 * Отрендерить результаты анализа
 * @param {Object} analysis - Результаты анализа
 */
function renderAnalysisResults(analysis) {
    if (!analysis.recommendations || analysis.recommendations.length === 0) {
        elements.analysisResults.innerHTML = '<p>Рекомендации не найдены</p>';
        return;
    }
    
    const recommendationsHtml = analysis.recommendations.map((rec, index) => `
        <div class="recommendation-item">
            <p><strong>Рекомендация ${index + 1}:</strong></p>
            <p>${escapeHtml(rec.text)}</p>
            <div class="confidence-bar">
                <div class="confidence-level" style="width: ${rec.confidence * 100}%"></div>
            </div>
            <p>Уровень уверенности: ${(rec.confidence * 100).toFixed(1)}%</p>
        </div>
    `).join('');
    
    const insightsHtml = analysis.insights && analysis.insights.length > 0 ? 
        `<div class="insights">
            <h4>Инсайты:</h4>
            <ul>
                ${analysis.insights.map(insight => `<li>${escapeHtml(insight)}</li>`).join('')}
            </ul>
        </div>` : '';
    
    elements.analysisResults.innerHTML = `
        <h4>Результаты анализа</h4>
        ${recommendationsHtml}
        ${insightsHtml}
        <p><strong>Объяснение:</strong> ${escapeHtml(analysis.explanation)}</p>
    `;
}

/**
 * Загрузить рекомендации
 * @param {string} decisionId - Идентификатор решения
 */
async function loadRecommendations(decisionId = null) {
    try {
        let recommendations = [];
        
        if (decisionId) {
            const response = await apiRequest(`${API_BASE_URL}/decisions/${decisionId}/recommendations`);
            recommendations = response;
        } else {
            // Загрузить все рекомендации (если нужно)
            // Пока просто загружаем рекомендации для всех решений
            for (const decision of currentDecisions) {
                try {
                    const decisionRecs = await apiRequest(`${API_BASE_URL}/decisions/${decision.id}/recommendations`);
                    recommendations = recommendations.concat(decisionRecs);
                } catch (error) {
                    // Игнорируем ошибки для отдельных решений
                    console.warn(`Failed to load recommendations for decision ${decision.id}:`, error);
                }
            }
        }
        
        currentRecommendations = recommendations;
        renderRecommendations(recommendations);
        updateDashboard();
        
    } catch (error) {
        console.error('Error loading recommendations:', error);
        elements.recommendationsList.innerHTML = '<p>Ошибка при загрузке рекомендаций</p>';
    }
}

/**
 * Отрендерить список рекомендаций
 * @param {Array} recommendations - Список рекомендаций
 */
function renderRecommendations(recommendations) {
    if (recommendations.length === 0) {
        elements.recommendationsList.style.display = 'none';
        elements.noRecommendations.style.display = 'block';
        return;
    }
    
    elements.recommendationsList.style.display = 'grid';
    elements.noRecommendations.style.display = 'none';
    
    elements.recommendationsList.innerHTML = recommendations.map(rec => `
        <div class="recommendation-item">
            <p>${escapeHtml(rec.text)}</p>
            <div class="confidence-bar">
                <div class="confidence-level" style="width: ${rec.confidence * 100}%"></div>
            </div>
            <p>Уровень уверенности: ${(rec.confidence * 100).toFixed(1)}%</p>
        </div>
    `).join('');
}

/**
 * Обновить дашборд
 */
function updateDashboard() {
    // Общее количество решений
    elements.totalDecisions.textContent = currentDecisions.length;
    
    // Количество проанализированных решений
    const analyzedCount = currentDecisions.filter(d => 
        currentRecommendations.some(r => r.decision_id === d.id)
    ).length;
    elements.analyzedDecisions.textContent = analyzedCount;
    
    // Общее количество рекомендаций
    elements.totalRecommendations.textContent = currentRecommendations.length;
    
    // Средний уровень уверенности
    if (currentRecommendations.length > 0) {
        const avgConfidence = currentRecommendations.reduce((sum, rec) => sum + rec.confidence, 0) / currentRecommendations.length;
        elements.avgConfidence.textContent = `${(avgConfidence * 100).toFixed(1)}%`;
    } else {
        elements.avgConfidence.textContent = '0%';
    }
}

/**
 * Открыть модальное окно создания решения
 */
function openCreateDecisionModal() {
    forms.createDecision.reset();
    modals.createDecision.style.display = 'block';
}

/**
 * Закрыть модальное окно создания решения
 */
function closeCreateDecisionModal() {
    modals.createDecision.style.display = 'none';
}

/**
 * Закрыть модальное окно деталей решения
 */
function closeDecisionDetailsModal() {
    modals.decisionDetails.style.display = 'none';
}

/**
 * Инициализировать обработчики событий
 */
function initializeEventListeners() {
    // Кнопки
    if (buttons.createDecision) {
        buttons.createDecision.addEventListener('click', openCreateDecisionModal);
    }
    
    if (buttons.analyze) {
        buttons.analyze.addEventListener('click', () => {
            const decisionId = elements.decisionSelect.value;
            if (decisionId) {
                analyzeDecision(decisionId);
            } else {
                showNotification('Пожалуйста, выберите решение для анализа', 'info');
            }
        });
    }
    
    if (buttons.cancelCreate) {
        buttons.cancelCreate.addEventListener('click', closeCreateDecisionModal);
    }
    
    if (buttons.closeDetails) {
        buttons.closeDetails.addEventListener('click', closeDecisionDetailsModal);
    }
    
    // Формы
    if (forms.createDecision) {
        forms.createDecision.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(forms.createDecision);
            const decisionData = {
                title: formData.get('decision-title'),
                description: formData.get('decision-description'),
                context: formData.get('decision-context'),
                owner: formData.get('decision-owner'),
                tags: formData.get('decision-tags') ? 
                    formData.get('decision-tags').split(',').map(tag => tag.trim()) : []
            };
            
            await createDecision(decisionData);
        });
    }
    
    // Фильтры
    if (elements.searchDecisions) {
        elements.searchDecisions.addEventListener('input', () => {
            renderDecisions(currentDecisions);
        });
    }
    
    if (elements.statusFilter) {
        elements.statusFilter.addEventListener('change', () => {
            renderDecisions(currentDecisions);
        });
    }
    
    // Закрытие модальных окон по клику вне контента
    window.addEventListener('click', (e) => {
        if (e.target === modals.createDecision) {
            closeCreateDecisionModal();
        }
        if (e.target === modals.decisionDetails) {
            closeDecisionDetailsModal();
        }
    });
    
    // Закрытие модальных окон по нажатию Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeCreateDecisionModal();
            closeDecisionDetailsModal();
        }
    });
    
    // Кнопки закрытия модальных окон
    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.addEventListener('click', () => {
            closeCreateDecisionModal();
            closeDecisionDetailsModal();
        });
    });
}

/**
 * Инициализировать приложение
 */
async function initializeApp() {
    console.log('Initializing Cloud Reason Web App...');
    
    // Инициализировать обработчики событий
    initializeEventListeners();
    
    // Загрузить начальные данные
    await loadDecisions();
    await loadRecommendations();
    
    console.log('Cloud Reason Web App initialized successfully');
}

// Запустить инициализацию при загрузке страницы
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeApp);
} else {
    initializeApp();
}