<<<<<<< Updated upstream
# 🧭 IT Compass

**Системный мыслитель и продуктовый архитектор. Создаю и веду к production open-source проект IT Compass.**

**IT Compass** — платформа, которая превращает субъективный карьерный рост в IT в объективные, верифицируемые метрики на основе авторской методологии.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Methodology](https://img.shields.io/badge/Methodology-CC--BY--ND--4.0-orange)](docs/METHODOLOGY.md)
[![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)](https://github.com/Control39/it-compass)

---

## 🎯 Что такое IT Compass?

IT Compass — это система объективной оценки карьерного роста в IT, основанная на авторской методологии **«Объективные маркеры компетенций»**.

**Вместо субъективного:**
- ❌ «Знаю Python на 4/5»
- ❌ «Умею работать с Docker»
- ❌ «Изучаю MLOps»

**Мы получаем объективное:**
- ✅ «Написал скрипт для автоматизации, выложил на GitHub»
- ✅ «Создал Dockerfile для Python-приложения и запустил контейнер»
- ✅ «Настроил MLflow для логирования экспериментов»

Каждый маркер — **конкретное, проверяемое действие**, подтверждённое артефактом (код, скриншот, ссылка).

---

## 🚀 Ключевые особенности

### Методология
- **17 направлений развития** (Python, Docker, DevOps, MLOps, Git, Linux и др.)
- **32+ объективных маркера** с SMART-критериями
- Верифицируемые доказательства компетенций

### Архитектура
- **Эволюция системы:** от MVP на CPU-ВМ до распределённой архитектуры (RAG + Reasoning, CPU/GPU)
- **Распределённая система:** RAG-сервер (CPU) + Reasoning-сервер (GPU)
- **Автоматический анализ:** интеграция с LLM для сопоставления действий с маркерами

### Функционал
- 📊 **Трекинг прогресса** — отслеживание выполненных маркеров
- 📄 **Генерация портфолио** — автоматическое создание Markdown-портфолио
- 🎯 **Рекомендации** — приоритизация следующих шагов развития
- 🌐 **Web-интерфейс** — Streamlit-дашборд для визуализации
- 🔧 **CLI** — консольный интерфейс для работы с системой

---

## 🛠 Технологический стек

### Продукт & Архитектура
- **От идеи и методологии** до проектирования распределённых систем
- **Пользовательский опыт** — CLI и Web-интерфейсы
- **Эволюция архитектуры** — анализ bottlenecks и оптимизация

### Технологии
- **Python 3.8+** — основной язык разработки
- **DevOps:** Docker, CI/CD
- **MLOps:** RAG-пайплайны, LLM-интеграция
- **Web:** Streamlit для дашборда

### Ключевой навык: AI-Assisted Development
Эффективное использование LLM как инструмента для:
- Прототипирования решений
- Архитектурного анализа и оптимизации
- Автоматизации сопоставления действий с маркерами

---

## 🏗 Архитектура системы

### Эволюция проекта

**MVP (начальная версия):**
- RAG-система + лёгкая LLM на CPU-ВМ (4 ГБ ОЗУ)
- Доказательство концепции в условиях ограничений

**Текущая архитектура (результат мета-анализа):**
- **Распределённая система:**
  - RAG-сервер (CPU, 16 ГБ ОЗУ) — поиск по заметкам
  - Reasoning-сервер (GPU) — сложный анализ и синтез

**Ключевой инсайт:**
Система проанализировала собственные диалоги об архитектуре и пришла к выводу о необходимости распределённой архитектуры. Это демонстрирует **системное мышление** и **архитектурный подход** к оптимизации.

### Компоненты

```
Заметки/диалоги → RAG-поиск → Reasoning-анализ → 
→ Сопоставление с маркерами → Автоматическое портфолио
```

**Подробная документация:** [ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 🚀 Быстрый старт

### Установка

**Через setup-скрипт:**
```bash
git clone https://github.com/Control39/it-compass.git
cd it-compass
chmod +x setup.sh
./setup.sh
```

**Или вручную:**
```bash
git clone https://github.com/Control39/it-compass.git
cd it-compass
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Запуск

**CLI-интерфейс:**
```bash
python src/main.py
```

**Web-интерфейс (Streamlit):**
```bash
streamlit run src/ui/app.py
```

**Docker:**
```bash
docker build -t it-compass .
docker run -it it-compass
```

---

## 📖 Использование

### Основные команды (CLI)

1. **Показать прогресс** — отображение выполненных маркеров
2. **Отметить маркер** — отметить выполненный маркер компетенции
3. **Рекомендации** — получить рекомендации по развитию (high priority)
4. **Генерация портфолио** — создать Markdown-портфолио
5. **Статистика** — детальная статистика по навыкам

### Интеграция с Reasoning-моделью

Для автоматического анализа заметок и сопоставления с маркерами:

```bash
python scripts/reasoning_integration.py
```

Требуется настройка API-ключа для LLM (OpenAI-совместимое API).

**Документация:** [ARCHITECTURE.md](docs/ARCHITECTURE.md#интеграционный-процесс)

---

## 📊 Методология «Объективные маркеры компетенций»

### Суть подхода

Методология основана на принципе объективности и верифицируемости:

- **Маркер** — конкретное, проверяемое действие
- **Валидация** — доказательство через артефакт (код, ссылка, скриншот)
- **SMART-критерии** — специфичные, измеримые, достижимые, релевантные, ограниченные по времени цели

### Направления развития (17 направлений)

1. 🐍 **Python** — программирование и автоматизация
2. 🐳 **Docker** — контейнеризация
3. 🚀 **DevOps** — CI/CD, инфраструктура
4. 🤖 **MLOps** — ML-инфраструктура и пайплайны
5. 🔧 **Git** — система контроля версий
6. 🐧 **Linux** — работа с командной строкой
7. 📊 **Data Analysis** — анализ данных
8. 🗄️ **Database** — работа с базами данных
9. 🎨 **Frontend** — веб-разработка
10. 🏗️ **System Design** — проектирование систем
11. ☁️ **Cloud Computing** — облачные сервисы
12. 🔒 **Cybersecurity** — информационная безопасность
13. 📱 **Mobile Development** — мобильная разработка
14. 🤖 **AI Applications** — применение AI
15. 📋 **Business Analysis** — бизнес-анализ
16. 📱 **Product Management** — продуктовый менеджмент
17. 💬 **Communication** — коммуникации

**Полная методология:** [METHODOLOGY.md](docs/METHODOLOGY.md)

---

## 🎯 Целевая аудитория

- **IT-новички** — карта роста и объективная оценка прогресса
- **HR и рекрутеры** — инструмент для оценки компетенций кандидатов
- **EdTech** — методология для построения образовательных траекторий
- **Разработчики** — открытый исходный код для интеграции и кастомизации

---

## 📁 Структура проекта

```
it-compass/
├── src/
│   ├── core/
│   │   └── tracker.py          # Основной класс трекера
│   ├── utils/
│   │   └── portfolio_gen.py    # Генератор портфолио
│   ├── ui/
│   │   └── app.py              # Streamlit-интерфейс
│   ├── data/
│   │   └── markers/            # JSON-файлы с маркерами (17 направлений)
│   └── main.py                 # CLI-интерфейс
├── docs/
│   ├── METHODOLOGY.md          # Описание методологии
│   ├── ARCHITECTURE.md         # Архитектура системы
│   └── PROJECT_ANALYSIS.md     # Анализ проекта
├── scripts/
│   └── reasoning_integration.py # Интеграция с Reasoning-моделью
├── portfolio/                  # Портфолио проектов
├── tests/                      # Тесты
├── Dockerfile                  # Docker-конфигурация
└── requirements.txt            # Зависимости
```

---

## 📄 Лицензии

- **Код** — [MIT License](LICENSE)
- **Методология** — © 2025 Ekaterina Kudelya, [CC BY-ND 4.0](docs/METHODOLOGY.md)

**Важно:** При использовании методологии необходимо указывать автора.

---

## 🔗 Полезные ссылки

- 📚 **Документация:** [docs/](docs/)
- 🏗️ **Архитектура:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- 🧠 **Методология:** [docs/METHODOLOGY.md](docs/METHODOLOGY.md)
- 🔗 **Репозиторий:** [GitHub](https://github.com/Control39/it-compass)

---

## 💡 О проекте

IT Compass создан как результат **системного подхода** к проблеме субъективной оценки карьерного роста. Проект демонстрирует:

- **Системное мышление** — от проблемы к архитектурному решению
- **Продуктовый подход** — от идеи до production-ready решения
- **Архитектурную эволюцию** — анализ и оптимизация на основе данных
- **AI-assisted development** — эффективное использование LLM для ускорения разработки

**Открыта к задачам на стыке продукта, архитектуры и разработки.**

---

*Методология: © 2025 Ekaterina Kudelya, CC BY-ND 4.0*  
*Код: MIT License*
=======
# 🧭 IT Compass - Objective IT Career Growth Tracker

**Карта твоего IT-роста: по фактам, а не по ощущениям**

> Вместо *«знаю Python на 4»* — *«написал скрипт, собрал в Docker, выложил на GitHub»*.
> 🧠 *На основе авторской методологии «Объективные маркеры компетенций»*
> © 2025 Ekaterina Kudelya. [CC BY-ND 4.0](docs/METHODOLOGY.md)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-MVP--Ready-brightgreen)](https://github.com/Control39/it-compass)
[![Markers](https://img.shields.io/badge/Markers-32-brightgreen)](https://github.com/Control39/it-compass)

---

## 🚀 Быстрый старт

### Установка в 1 команду:
```bash
git clone https://github.com/Control39/it-compass.git
cd it-compass
chmod +x setup.sh
./setup.sh
```

### Запуск:
```bash
python src/main.py
```

---

## 📊 17 направлений (32 маркера)

1. **🐍 Python** - 3 маркера
2. **🐳 Docker** - 2 маркера
3. **📊 Data Analysis** - 2 маркера
4. **🎨 Frontend** - 2 маркера
5. **🏗️ System Design** - 2 маркера
6. **🗄️ Database** - 2 маркера
7. **📱 Product Management** - 2 маркера
8. **☁️ Cloud Computing** - 2 маркера
9. **🔒 Cybersecurity** - 2 маркера
10. **📱 Mobile Development** - 2 маркера
11. **🤖 AI Applications** - 2 маркера
12. **🔧 Git** - 2 маркера
13. **🐧 Linux** - 2 маркера
14. **📋 Business Analysis** - 2 маркера
15. **🚀 DevOps** - 3 маркера
16. **🧪 QA** - 2 маркера
17. **💬 Communication** - 2 маркера

---

## 📄 Лицензии
- **Код** — [MIT License](LICENSE)
- **Методология** — © Ekaterina Kudelya, [CC BY-ND 4.0](docs/METHODOLOGY.md)

🔗 Репозиторий: https://github.com/Control39/it-compass
>>>>>>> Stashed changes
