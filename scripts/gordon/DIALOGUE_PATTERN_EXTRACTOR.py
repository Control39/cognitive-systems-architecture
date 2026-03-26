#!/usr/bin/env python3
"""
Pattern Extractor из диалогов
Ищет ключевые паттерны, проверяет что уже задокументировано,
даёт рекомендации что добавить
"""

import json
import re
from collections import defaultdict
from pathlib import Path

# Паттерны для поиска в диалогах
PATTERN_KEYWORDS = {
    'architecture': [
        'architecture', 'design', 'system', 'layer', 'component',
        'pattern', 'structure', 'framework', 'blueprint'
    ],
    'methodology': [
        'methodology', 'method', 'approach', 'process', 'framework',
        'principle', 'practice', 'standard', 'convention'
    ],
    'ai_orchestration': [
        'orchestration', 'integration', 'rag', 'reasoning', 'llm',
        'model', 'prompt', 'chain', 'pipeline', 'workflow'
    ],
    'knowledge_management': [
        'knowledge', 'memory', 'storage', 'database', 'index',
        'search', 'retrieve', 'organize', 'taxonomy', 'classification'
    ],
    'decision_making': [
        'decision', 'choose', 'select', 'option', 'trade-off',
        'trade-off', 'pros', 'cons', 'risk', 'benefit'
    ],
    'learning': [
        'learn', 'learning', 'education', 'skill', 'growth',
        'progress', 'improvement', 'development', 'training'
    ],
    'business': [
        'business', 'market', 'revenue', 'cost', 'roi', 'value',
        'customer', 'user', 'adoption', 'scale'
    ],
    'technical_depth': [
        'docker', 'kubernetes', 'python', 'javascript', 'database',
        'api', 'deployment', 'testing', 'debugging', 'optimization'
    ],
    'problem_solving': [
        'problem', 'issue', 'challenge', 'solve', 'solution',
        'debug', 'troubleshoot', 'fix', 'improve', 'refactor'
    ],
    'system_thinking': [
        'system', 'feedback', 'loop', 'cycle', 'iterate',
        'evolve', 'adapt', 'resilience', 'scalability'
    ]
}

class PatternExtractor:
    def __init__(self, json_file):
        self.json_file = json_file
        self.patterns_found = defaultdict(list)
        self.pattern_frequency = defaultdict(int)
        self.recommendations = []
        
    def load_json(self):
        """Загружает JSON с файла анализа"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    
    def analyze_insights(self, data):
        """Анализирует insights из JSON"""
        if not data or 'insights' not in data:
            return
        
        for insight in data.get('insights', []):
            if insight.get('type') == 'suggestion':
                message = insight.get('message', '').lower()
                action = insight.get('action', '').lower()
                
                # Ищем ключевые слова в рекомендациях
                for category, keywords in PATTERN_KEYWORDS.items():
                    for keyword in keywords:
                        if keyword in message or keyword in action:
                            self.patterns_found[category].append({
                                'source': insight.get('title'),
                                'message': insight.get('message'),
                                'action': insight.get('action')
                            })
                            self.pattern_frequency[category] += 1
    
    def analyze_files(self, data):
        """Анализирует список файлов"""
        if not data or 'files' not in data:
            return
        
        file_categories = defaultdict(int)
        
        for file_info in data.get('files', []):
            categories = file_info.get('categories', [])
            for cat in categories:
                file_categories[cat] += 1
        
        return file_categories
    
    def generate_recommendations(self, data):
        """Генерирует рекомендации на основе анализа"""
        recommendations = []
        
        # Анализ файловой статистики
        files_by_cat = self.analyze_files(data)
        
        # Рекомендация 1: Недостающие категории
        if files_by_cat.get('case_studies', 0) < 10:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'case_studies',
                'current': files_by_cat.get('case_studies', 0),
                'target': 15,
                'action': 'Добавить реальные примеры из диалогов: Bank Modernization, Startup Scaling, Knowledge System Implementation',
                'benefit': 'Case studies увеличат credibility и понимание practical value'
            })
        
        if files_by_cat.get('evidence', 0) < 15:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'evidence',
                'current': files_by_cat.get('evidence', 0),
                'target': 20,
                'action': 'Документировать конкретные доказательства: Screenshots, Git commits, Deployment logs, Metrics',
                'benefit': 'Evidence делает claims verifiable и убедительными'
            })
        
        # Рекомендация 2: Недостающие insights
        if self.pattern_frequency.get('business', 0) < 5:
            recommendations.append({
                'priority': 'MEDIUM',
                'category': 'business_insights',
                'current': self.pattern_frequency.get('business', 0),
                'target': 8,
                'action': 'Добавить документы о ROI, Market Size, Revenue Model, Customer Problems',
                'benefit': 'Инвесторы и клиенты хотят понимать бизнес-ценность'
            })
        
        if self.pattern_frequency.get('technical_depth', 0) < 10:
            recommendations.append({
                'priority': 'MEDIUM',
                'category': 'technical_depth',
                'current': self.pattern_frequency.get('technical_depth', 0),
                'target': 15,
                'action': 'Документировать technical decisions: Why Docker, Why RAG, Why Kubernetes, Why Python',
                'benefit': 'Архитекторы оценивают technical thinking, не просто usage'
            })
        
        # Рекомендация 3: Паттерны мышления
        if self.pattern_frequency.get('system_thinking', 0) < 8:
            recommendations.append({
                'priority': 'HIGH',
                'category': 'system_thinking',
                'current': self.pattern_frequency.get('system_thinking', 0),
                'target': 12,
                'action': 'Явно документировать feedback loops, iteration cycles, scalability thinking',
                'benefit': 'Это твоё главное отличие от обычных разработчиков'
            })
        
        return recommendations
    
    def extract_dialogue_patterns(self, dialogue_text):
        """Извлекает паттерны из текста диалога"""
        if not dialogue_text:
            return {}
        
        patterns = defaultdict(list)
        lines = dialogue_text.split('\n')
        
        current_pattern = None
        for line in lines:
            line_lower = line.lower()
            
            # Ищем какой паттерн это может быть
            for category, keywords in PATTERN_KEYWORDS.items():
                for keyword in keywords:
                    if keyword in line_lower:
                        patterns[category].append(line.strip())
                        break
        
        return dict(patterns)
    
    def generate_report(self, data, output_path):
        """Генерирует итоговый отчёт"""
        
        # Анализируем insights
        self.analyze_insights(data)
        
        # Генерируем рекомендации
        recommendations = self.generate_recommendations(data)
        self.recommendations = recommendations
        
        # Создаём отчёт
        report = {
            'timestamp': data.get('timestamp'),
            'patterns_found': dict(self.patterns_found),
            'pattern_frequency': dict(self.pattern_frequency),
            'files_by_category': self.analyze_files(data),
            'recommendations': recommendations
        }
        
        # Сохраняем JSON
        json_path = output_path.replace('.txt', '.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # Сохраняем текстовый отчёт
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("DIALOGUE PATTERN EXTRACTION REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("НАЙДЕНЫ ПАТТЕРНЫ (по частоте)\n")
            f.write("-" * 80 + "\n")
            for pattern, count in sorted(self.pattern_frequency.items(), 
                                        key=lambda x: x[1], reverse=True):
                f.write(f"  {pattern:20}: {count:3} упоминаний\n")
            
            f.write("\n\nРЕКОМЕНДАЦИИ (Что добавить в документацию)\n")
            f.write("-" * 80 + "\n\n")
            
            for i, rec in enumerate(recommendations, 1):
                f.write(f"{i}. [{rec['priority']}] {rec['category'].upper()}\n")
                f.write(f"   Сейчас: {rec['current']} документов\n")
                f.write(f"   Нужно: {rec['target']} документов\n")
                f.write(f"   Действие: {rec['action']}\n")
                f.write(f"   Бенефит: {rec['benefit']}\n\n")
            
            f.write("\n\nДЕТАЛИ ПО КАТЕГОРИЯМ\n")
            f.write("-" * 80 + "\n")
            
            for category in sorted(self.patterns_found.keys()):
                f.write(f"\n📌 {category.upper()}\n")
                for pattern_info in self.patterns_found[category][:3]:
                    f.write(f"  • {pattern_info['source']}\n")
                    if pattern_info.get('message'):
                        f.write(f"    → {pattern_info['message'][:60]}...\n")
        
        return json_path, output_path

def main():
    # Пути
    pattern_json = r"C:\Users\Z\Desktop\gordon\pattern_analysis.json"
    output_txt = r"C:\Users\Z\Desktop\gordon\dialogue_patterns_report.txt"
    
    print("🔍 Анализирую паттерны из диалогов...\n")
    
    extractor = PatternExtractor(pattern_json)
    
    # Загружаем JSON
    data = extractor.load_json()
    if not data:
        print(f"❌ Не могу загрузить {pattern_json}")
        return
    
    # Генерируем отчёт
    json_path, txt_path = extractor.generate_report(data, output_txt)
    
    print("✅ Анализ завершён!\n")
    print("📊 ПАТТЕРНЫ (TOP 5):\n")
    for pattern, count in list(sorted(extractor.pattern_frequency.items(), 
                                      key=lambda x: x[1], reverse=True))[:5]:
        print(f"  • {pattern:20}: {count:3} упоминаний")
    
    print(f"\n💡 ГЛАВНЫЕ РЕКОМЕНДАЦИИ:\n")
    for rec in extractor.recommendations[:3]:
        print(f"  ⚠️  {rec['category'].upper()}")
        print(f"     {rec['action']}\n")
    
    print(f"\n💾 Отчёты сохранены:")
    print(f"  JSON: {json_path}")
    print(f"  TXT:  {txt_path}")

if __name__ == "__main__":
    main()
