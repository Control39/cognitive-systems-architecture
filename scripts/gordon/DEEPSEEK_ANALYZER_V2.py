#!/usr/bin/env python3
"""
DeepSeek Analyzer v2 - Fixed Parser
"""

import json
from collections import defaultdict

class DeepSeekAnalyzer:
    def __init__(self, json_file):
        self.json_file = json_file
    
    def load_and_analyze(self):
        """Загружает и анализирует"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\n📊 АНАЛИЗ {len(data)} ДИАЛОГОВ DEEPSEEK")
        print("=" * 80)
        
        total_user = 0
        total_assistant = 0
        total_conversations = len(data)
        thinking_patterns = defaultdict(int)
        
        for conv_idx, conv in enumerate(data):
            if 'mapping' not in conv:
                continue
            
            mapping = conv['mapping']
            
            for node_id, node in mapping.items():
                msg = node.get('message')
                if not msg or msg is None:
                    continue
                
                role = msg.get('role')
                content = msg.get('content')
                
                if not role or not content:
                    continue
                
                # Извлекаем текст
                text = ""
                if isinstance(content, list):
                    for item in content:
                        if isinstance(item, str):
                            text += item
                        elif isinstance(item, dict) and 'text' in item:
                            text += item['text']
                elif isinstance(content, str):
                    text = content
                
                if not text:
                    continue
                
                # Считаем
                if role == 'user':
                    total_user += 1
                    # Анализируем паттерны
                    self.extract_patterns(text, thinking_patterns)
                elif role == 'assistant':
                    total_assistant += 1
        
        print(f"\n✅ Найдено:")
        print(f"  Диалогов: {total_conversations}")
        print(f"  От тебя: {total_user}")
        print(f"  От DeepSeek: {total_assistant}")
        
        # Выводим паттерны
        if thinking_patterns:
            print(f"\n🧠 ТВОИ ПАТТЕРНЫ МЫШЛЕНИЯ:")
            for pattern, count in sorted(thinking_patterns.items(), key=lambda x: x[1], reverse=True):
                pct = int(count / total_user * 100) if total_user else 0
                print(f"  • {pattern:25}: {count:3} ({pct}%)")
        
        return {
            'conversations': total_conversations,
            'user_messages': total_user,
            'assistant_messages': total_assistant,
            'patterns': thinking_patterns
        }
    
    def extract_patterns(self, text, patterns):
        """Извлекает паттерны из текста"""
        text_lower = text.lower()
        
        if any(w in text_lower for w in ['system', 'architecture', 'layer', 'design', 'structure']):
            patterns['system_architecture'] += 1
        
        if any(w in text_lower for w in ['analyze', 'data', 'metric', 'evidence', 'measure']):
            patterns['analytical'] += 1
        
        if any(w in text_lower for w in ['problem', 'solution', 'approach', 'method']):
            patterns['problem_solving'] += 1
        
        if any(w in text_lower for w in ['process', 'workflow', 'step', 'sequence']):
            patterns['process_thinking'] += 1
        
        if any(w in text_lower for w in ['innovative', 'creative', 'novel', 'unique']):
            patterns['creative'] += 1
        
        if any(w in text_lower for w in ['risk', 'challenge', 'problem', 'edge', 'fail']):
            patterns['risk_aware'] += 1
        
        if any(w in text_lower for w in ['iterate', 'cycle', 'feedback', 'improve']):
            patterns['iterative'] += 1
        
        if any(w in text_lower for w in ['scale', 'performance', 'optimization', 'efficiency']):
            patterns['optimization'] += 1

def main():
    analyzer = DeepSeekAnalyzer(r'C:\Users\Z\Desktop\gordon\conversations.json')
    result = analyzer.load_and_analyze()
    
    print("\n" + "=" * 80)
    print("✨ ГОТОВО")
    print("=" * 80)
    
    if result['user_messages'] > 0:
        print(f"\n💡 ВЫВОД:")
        print(f"Ты провел {result['conversations']} глубоких анализов с DeepSeek")
        print(f"Написал {result['user_messages']} вопросов/размышлений")
        print(f"\nОсновные паттерны - как ты думаешь:")
        for pattern, count in sorted(result['patterns'].items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  ✓ {pattern}")
        
        print(f"\n🎯 ИСПОЛЬЗУЙ ЭТОТ АНАЛИЗ:")
        print(f"  1. Добавь в README: '877 диалогов + анализ паттернов'")
        print(f"  2. Подчеркни: Системное мышление, аналитичность, creative problem-solving")
        print(f"  3. Отправляй рекрутерам!")

if __name__ == "__main__":
    main()
