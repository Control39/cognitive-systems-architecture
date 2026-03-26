#!/usr/bin/env python3
"""
Real-Time Pattern Suggester
Когда ты добавляешь новый документ, система:
1. Анализирует его
2. Проверяет паттерны
3. Даёт рекомендации что дальше добавить
"""

import json
import re
from pathlib import Path

PATTERN_CATEGORIES = {
    'methodology': {
        'keywords': ['methodology', 'method', 'principle', 'practice'],
        'importance': 'HIGH',
        'examples': ['Competency Markers', 'Decision Framework', 'Process Flow']
    },
    'architecture': {
        'keywords': ['architecture', 'design', 'layer', 'component', 'pattern'],
        'importance': 'HIGH',
        'examples': ['System Design', 'Data Flow', 'Integration Points']
    },
    'case_studies': {
        'keywords': ['case', 'example', 'project', 'implementation', 'real-world'],
        'importance': 'HIGH',
        'examples': ['Bank Migration', 'Startup Scaling', 'Knowledge System']
    },
    'business_value': {
        'keywords': ['roi', 'cost', 'revenue', 'market', 'customer', 'value', 'business'],
        'importance': 'MEDIUM',
        'examples': ['ROI Analysis', 'Market Sizing', 'Cost Savings']
    },
    'technical_decisions': {
        'keywords': ['why', 'docker', 'kubernetes', 'python', 'decision', 'trade-off'],
        'importance': 'MEDIUM',
        'examples': ['Why Docker', 'Technology Choices', 'Trade-off Analysis']
    },
    'evidence': {
        'keywords': ['proof', 'evidence', 'data', 'metrics', 'result', 'outcome'],
        'importance': 'HIGH',
        'examples': ['Metrics', 'Screenshots', 'Git History', 'Test Results']
    },
    'system_thinking': {
        'keywords': ['system', 'feedback', 'loop', 'cycle', 'scale', 'evolve', 'adapt'],
        'importance': 'HIGH',
        'examples': ['Feedback Loops', 'Iteration Process', 'Scalability Plan']
    }
}

class PatternSuggester:
    def __init__(self):
        self.suggestions = []
    
    def analyze_text(self, text):
        """Анализирует текст на паттерны"""
        text_lower = text.lower()
        found_patterns = {}
        
        for category, info in PATTERN_CATEGORIES.items():
            keywords = info['keywords']
            matches = sum(1 for kw in keywords if kw in text_lower)
            if matches > 0:
                found_patterns[category] = {
                    'matches': matches,
                    'importance': info['importance'],
                    'examples': info['examples']
                }
        
        return found_patterns
    
    def generate_suggestions(self, found_patterns, filename):
        """Генерирует рекомендации на основе найденных паттернов"""
        suggestions = []
        
        print(f"\n📄 Анализирую файл: {filename}\n")
        print("=" * 70)
        
        # Найдены паттерны
        if found_patterns:
            print(f"✅ НАЙДЕНО ПАТТЕРНОВ: {len(found_patterns)}\n")
            for pattern, data in sorted(found_patterns.items(), 
                                       key=lambda x: x[1]['importance'] == 'HIGH', 
                                       reverse=True):
                print(f"  📌 {pattern.upper()}")
                print(f"     Matches: {data['matches']}")
                print(f"     Importance: {data['importance']}")
                print()
        
        # Рекомендации на основе текущего содержимого
        print("💡 РЕКОМЕНДАЦИИ:\n")
        
        if 'architecture' in found_patterns and 'case_studies' not in found_patterns:
            print("  1️⃣  Ты писал об архитектуре.")
            print("     → Добавь CASE STUDY как это работает в реальном проекте")
            print("     Примеры: Bank System Migration, Startup Knowledge Management")
            suggestions.append('case_study')
        
        if 'methodology' in found_patterns and 'business_value' not in found_patterns:
            print("  2️⃣  Ты описал методологию.")
            print("     → Добавь как это экономит ВРЕМЯ и ДЕНЬГИ (ROI)")
            print("     Пример: 'Saves 2 weeks onboarding per employee = $100K/year'")
            suggestions.append('roi')
        
        if 'system_thinking' not in found_patterns and len(found_patterns) > 2:
            print("  3️⃣  Много паттернов найдено.")
            print("     → Свяжи их в один СИСТЕМУ (feedback loops, cycles)")
            print("     Покажи как части работают вместе")
            suggestions.append('system_integration')
        
        if 'evidence' not in found_patterns and 'technical_decisions' in found_patterns:
            print("  4️⃣  Ты объяснил technical decisions.")
            print("     → Добавь ДОКАЗАТЕЛЬСТВА (ссылки, metrics, results)")
            print("     Пример: GitHub commit links, performance metrics")
            suggestions.append('evidence')
        
        if 'business_value' not in found_patterns:
            print("  5️⃣  Нет бизнес-ценности.")
            print("     → Ответь: 'Зачем это компании? Сколько это стоит?'")
            print("     Добавь раздел 'Business Impact'")
            suggestions.append('business_impact')
        
        print("\n" + "=" * 70)
        
        return suggestions
    
    def interactive_mode(self):
        """Интерактивный режим - анализирует файл при добавлении"""
        
        print("\n" + "🎯 PATTERN SUGGESTER - Interactive Mode")
        print("=" * 70)
        print("Копируй текст нового документа ниже.")
        print("Система проанализирует паттерны и даст рекомендации.")
        print("Вводи многострочный текст. Закончи пустой строкой.\n")
        
        lines = []
        filename = input("📝 Название файла: ").strip()
        print("\n📖 Текст документа (Ctrl+D to finish or blank line to end):\n")
        
        try:
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
        except EOFError:
            pass
        
        text = "\n".join(lines)
        
        if not text:
            print("❌ Текст не введён")
            return
        
        # Анализируем
        patterns = self.analyze_text(text)
        suggestions = self.generate_suggestions(patterns, filename)
        
        # Сохраняем в JSON
        result = {
            'filename': filename,
            'patterns_found': patterns,
            'suggestions': suggestions,
            'text_length': len(text),
            'word_count': len(text.split())
        }
        
        json_file = r"C:\Users\Z\Desktop\gordon\last_suggestion.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Анализ сохранён в: {json_file}")

def main():
    suggester = PatternSuggester()
    
    # Примеры анализа
    examples = {
        'example1.md': """
# System Architecture for Knowledge Management

We built a 4-layer system:
1. RAG layer - retrieves context
2. Reasoning layer - analyzes patterns
3. Classification layer - organizes findings
4. Output layer - generates artifacts

The system handles 5000+ files automatically.
        """,
        
        'example2.md': """
# Case Study: Bank Modernization

Client: Russian Bank (5000+ employees)
Problem: Legacy system, no documentation, AI tools scattered
Solution: Built cognitive architecture for knowledge management
Result: 40% faster onboarding, zero compliance violations, $500K savings
        """
    }
    
    print("🔍 PATTERN SUGGESTER\n")
    print("Примеры анализа:\n")
    
    for filename, text in examples.items():
        patterns = suggester.analyze_text(text)
        suggestions = suggester.generate_suggestions(patterns, filename)
    
    print("\n\n" + "=" * 70)
    print("Что дальше?")
    print("=" * 70)
    print("1. Когда добавляешь новый документ, запусти этот скрипт")
    print("2. Скопируй текст документа")
    print("3. Система проанализирует и даст рекомендации")
    print("4. Добавь недостающие части")
    print("\nЗапустить интерактивный режим? (y/n): ", end="")
    
    if input().lower() == 'y':
        suggester.interactive_mode()

if __name__ == "__main__":
    main()
