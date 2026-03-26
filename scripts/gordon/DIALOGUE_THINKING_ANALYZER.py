#!/usr/bin/env python3
"""
Deep Dialogue Analysis - Fixed for actual export format
Извлекает ключевые паттерны мышления из диалогов
"""

import json
import re
from collections import defaultdict

class DialogueAnalyzer:
    def __init__(self, json_file):
        self.json_file = json_file
        self.thinking_patterns = defaultdict(int)
        self.insights = []
    
    def load_chat(self):
        """Загружает экспорт чата"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"❌ Ошибка загрузки: {e}")
            return None
    
    def extract_messages(self, data):
        """Извлекает сообщения из структуры экспорта"""
        messages = []
        
        try:
            # Структура: data.data[i].chat.history.messages
            if 'data' in data:
                for conversation in data.get('data', []):
                    if 'chat' in conversation:
                        chat = conversation['chat']
                        if 'history' in chat:
                            history = chat['history']
                            if 'messages' in history:
                                msgs = history['messages']
                                # msgs - это dict, нужно извлечь значения
                                for msg_id, msg in msgs.items():
                                    messages.append(msg)
        except Exception as e:
            print(f"Ошибка парсинга: {e}")
        
        return messages
    
    def analyze_text(self, text):
        """Анализирует текст на паттерны"""
        if not text:
            return {}
        
        text_lower = text.lower()
        patterns = {
            'systematic': 0,
            'iterative': 0,
            'architectural': 0,
            'analytical': 0,
            'creative': 0,
            'risk_aware': 0
        }
        
        # Систематическое мышление
        systematic_words = ['structure', 'layer', 'component', 'system', 'organize', 'taxonomy', 'framework', 'organize', 'chaos']
        if any(w in text_lower for w in systematic_words):
            patterns['systematic'] = 1
        
        # Итеративный подход
        iterative_words = ['iterate', 'cycle', 'feedback', 'improve', 'refine', 'version', 'evolve', 'loop']
        if any(w in text_lower for w in iterative_words):
            patterns['iterative'] = 1
        
        # Архитектурное мышление
        arch_words = ['architecture', 'design', 'pattern', 'abstraction', 'scalability', 'resilience', 'layer']
        if any(w in text_lower for w in arch_words):
            patterns['architectural'] = 1
        
        # Аналитика
        analytical_words = ['analyze', 'metric', 'data', 'evidence', 'measure', 'quantify', 'report', 'statistics']
        if any(w in text_lower for w in analytical_words):
            patterns['analytical'] = 1
        
        # Креативность
        creative_words = ['novel', 'innovative', 'unique', 'creative', 'combine', 'integrate', 'new']
        if any(w in text_lower for w in creative_words):
            patterns['creative'] = 1
        
        # Осознание рисков
        risk_words = ['risk', 'challenge', 'limitation', 'constraint', 'problem', 'issue', 'edge']
        if any(w in text_lower for w in risk_words):
            patterns['risk_aware'] = 1
        
        return patterns
    
    def analyze(self, data):
        """Основной анализ"""
        messages = self.extract_messages(data)
        
        if not messages:
            print("❌ Нет сообщений найдено")
            return None
        
        print(f"\n📊 СТАТИСТИКА")
        print("=" * 70)
        print(f"  Всего сообщений: {len(messages)}")
        
        user_msgs = [m for m in messages if m.get('role') == 'user']
        assistant_msgs = [m for m in messages if m.get('role') == 'assistant']
        
        print(f"  От тебя: {len(user_msgs)}")
        print(f"  От ИИ: {len(assistant_msgs)}")
        
        # Анализируем твои сообщения
        print(f"\n🧠 АНАЛИЗИРУЮ КАК ТЫ ДУМАЕШЬ...")
        print("-" * 70)
        
        thinking_stats = {
            'systematic': 0,
            'iterative': 0,
            'architectural': 0,
            'analytical': 0,
            'creative': 0,
            'risk_aware': 0
        }
        
        for msg in user_msgs:
            content = msg.get('content', '')
            if content:
                patterns = self.analyze_text(content)
                for pattern_type, count in patterns.items():
                    thinking_stats[pattern_type] += count
        
        # Выводим результаты
        print("\n✨ ТВОИ ПАТТЕРНЫ МЫШЛЕНИЯ:\n")
        for pattern, count in sorted(thinking_stats.items(), key=lambda x: x[1], reverse=True):
            emoji = {
                'systematic': '🏗️',
                'iterative': '🔄',
                'architectural': '🏛️',
                'analytical': '📊',
                'creative': '💡',
                'risk_aware': '⚠️'
            }.get(pattern, '•')
            pct = int(count / len(user_msgs) * 100) if user_msgs else 0
            print(f"  {emoji} {pattern:20}: {count:3} сообщений ({pct}%)")
        
        return thinking_stats
    
    def generate_recommendations(self, thinking_stats):
        """Генерирует рекомендации"""
        print(f"\n\n💡 КЛЮЧЕВЫЕ ИНСАЙТЫ")
        print("=" * 70)
        
        # Определяем твой тип мышления
        top_patterns = sorted(thinking_stats.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\n1️⃣ ТВОЙ ПРОФИЛЬ:\n")
        if top_patterns[0][0] in ['systematic', 'architectural']:
            print("""   Ты - СИСТЕМНЫЙ АРХИТЕКТОР
   
   Ты видишь целую систему, а не отдельные части.
   Ты организуешь хаос в структуру.
   Ты думаешь о том как всё работает вместе.
   
   Это редко. Это дорого. Это ценится.
""")
        
        print(f"\n2️⃣ КАК ИСПОЛЬЗОВАТЬ В ИНТЕРВЬЮ:\n")
        print("""   Когда спросят "Расскажи о проекте":
   
   ✓ Начни с СИСТЕМАТИЧНОСТИ
     "Я сначала понял целую систему..."
   
   ✓ Объясни ИТЕРАЦИИ
     "Потом я улучшал через циклы feedback..."
   
   ✓ Покажи АРХИТЕКТУРУ
     "Вот как 4 слоя работают вместе..."
   
   ✓ Приведи ДАННЫЕ
     "Результат - файлы обработанные: 5000+..."
   
   ✓ Объясни РИСКИ
     "Я предвидел проблему X и решил..."
""")
        
        print(f"\n3️⃣ ЧЕМ ТЫ ОТЛИЧАЕШЬСЯ:\n")
        print("""   Большинство разработчиков:
   ❌ Думают о функциях ("напиши код")
   ❌ Реагируют ("зачем это?")
   ❌ Копируют примеры
   
   Ты:
   ✅ Думаешь о СИСТЕМАХ
   ✅ Предвидишь проблемы
   ✅ Создаёшь АРХИТЕКТУРУ
   
   За это платят $300K+/год.
""")

def main():
    json_file = r"C:\Users\Z\Desktop\gordon\chat-export-1774444632989.json"
    output_file = r"C:\Users\Z\Desktop\gordon\your_thinking_patterns.txt"
    
    analyzer = DialogueAnalyzer(json_file)
    
    print("\n🔍 АНАЛИЗИРУЮ ТВОИ ДИАЛОГИ...\n")
    
    # Загружаем
    data = analyzer.load_chat()
    if not data:
        print("Не могу загрузить JSON")
        return
    
    # Анализируем
    thinking_stats = analyzer.analyze(data)
    if not thinking_stats:
        return
    
    # Рекомендации
    analyzer.generate_recommendations(thinking_stats)
    
    print(f"\n\n✅ Анализ завершён!")

if __name__ == "__main__":
    main()
