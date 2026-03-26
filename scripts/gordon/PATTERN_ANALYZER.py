#!/usr/bin/env python3
"""
Pattern Analyzer для Markdown документов
Анализирует файлы, ищет паттерны, даёт подсказки
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class PatternAnalyzer:
    def __init__(self, source_dir):
        self.source_dir = source_dir
        self.patterns = {
            'methodology': [],
            'architecture': [],
            'case_studies': [],
            'evidence': [],
            'guides': [],
            'reports': []
        }
        self.stats = defaultdict(int)
        self.insights = []
    
    def categorize_file(self, filename, content):
        """Категоризирует файл по содержимому"""
        lower_name = filename.lower()
        lower_content = content.lower()
        
        categories = []
        
        if any(x in lower_name for x in ['methodology', 'method']):
            categories.append('methodology')
        if any(x in lower_name for x in ['architecture', 'arch']):
            categories.append('architecture')
        if any(x in lower_name for x in ['case', 'example']):
            categories.append('case_studies')
        if any(x in lower_name for x in ['evidence', 'proof']):
            categories.append('evidence')
        if any(x in lower_name for x in ['guide', 'how', 'readme']):
            categories.append('guides')
        if any(x in lower_name for x in ['report']):
            categories.append('reports')
        
        # Анализ содержимого
        if 'objective' in lower_content and 'marker' in lower_content:
            if 'methodology' not in categories:
                categories.append('methodology')
        
        if 'rag' in lower_content or 'reasoning' in lower_content:
            if 'architecture' not in categories:
                categories.append('architecture')
        
        return categories if categories else ['other']
    
    def extract_headers(self, content):
        """Извлекает заголовки из Markdown"""
        headers = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
        return headers
    
    def extract_links(self, content):
        """Извлекает ссылки на другие документы"""
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        return links
    
    def analyze_file(self, filepath):
        """Анализирует один файл"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            filename = os.path.basename(filepath)
            rel_path = os.path.relpath(filepath, self.source_dir)
            
            # Категоризация
            categories = self.categorize_file(filename, content)
            
            # Извлечение информации
            headers = self.extract_headers(content)
            links = self.extract_links(content)
            word_count = len(content.split())
            lines = content.count('\n')
            
            file_info = {
                'path': rel_path,
                'filename': filename,
                'categories': categories,
                'headers': headers[:5],  # Первые 5 заголовков
                'links': links[:10],  # Первые 10 ссылок
                'word_count': word_count,
                'lines': lines,
                'size': len(content)
            }
            
            # Обновляем статистику
            for cat in categories:
                self.stats[cat] += 1
            self.stats['total_files'] += 1
            self.stats['total_words'] += word_count
            
            return file_info
            
        except Exception as e:
            return {'path': rel_path, 'error': str(e)}
    
    def analyze_directory(self):
        """Анализирует всю директорию"""
        files_analysis = []
        
        print("🔍 Анализ Markdown файлов...")
        
        for root, dirs, files in os.walk(self.source_dir):
            for filename in files:
                if filename.endswith(('.md', '.markdown')):
                    filepath = os.path.join(root, filename)
                    print(f"  📄 {os.path.relpath(filepath, self.source_dir)}")
                    
                    analysis = self.analyze_file(filepath)
                    files_analysis.append(analysis)
        
        return files_analysis
    
    def generate_insights(self, files_analysis):
        """Генерирует инсайты на основе анализа"""
        
        # Инсайт 1: Распределение по категориям
        self.insights.append({
            'type': 'distribution',
            'title': 'Распределение документов по категориям',
            'data': dict(self.stats)
        })
        
        # Инсайт 2: Недостающие документы
        if self.stats['methodology'] < 5:
            self.insights.append({
                'type': 'suggestion',
                'title': 'Рекомендация: Расширить методологию',
                'message': f'У вас {self.stats["methodology"]} методологических документов. Рекомендуется 5-10.',
                'action': 'Создать: Competency Markers Deep Dive, Methodology Extensions'
            })
        
        if self.stats['case_studies'] < 5:
            self.insights.append({
                'type': 'suggestion',
                'title': 'Рекомендация: Добавить case studies',
                'message': f'У вас {self.stats["case_studies"]} case studies. Рекомендуется 5-10.',
                'action': 'Создать примеры: Bank Modernization, AI Integration, Knowledge Management'
            })
        
        # Инсайт 3: Связность документов
        total_links = sum(1 for f in files_analysis if 'links' in f for _ in f.get('links', []))
        self.insights.append({
            'type': 'metric',
            'title': 'Связность документации',
            'value': total_links,
            'recommendation': 'Хорошо' if total_links > 50 else 'Нужно больше кросс-ссылок'
        })
        
        return self.insights
    
    def save_report(self, files_analysis, output_path):
        """Сохраняет отчёт анализа"""
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'source': self.source_dir,
            'statistics': dict(self.stats),
            'insights': self.insights,
            'files': files_analysis
        }
        
        # JSON отчёт
        json_path = os.path.join(output_path, 'pattern_analysis.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        # Текстовый отчёт
        txt_path = os.path.join(output_path, 'pattern_analysis.txt')
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write("PATTERN ANALYSIS REPORT\n")
            f.write("=" * 70 + "\n\n")
            
            f.write("СТАТИСТИКА\n")
            f.write("-" * 70 + "\n")
            for key, value in sorted(self.stats.items()):
                f.write(f"  {key:20}: {value}\n")
            
            f.write("\n\nИНСАЙТЫ И РЕКОМЕНДАЦИИ\n")
            f.write("-" * 70 + "\n")
            for i, insight in enumerate(self.insights, 1):
                f.write(f"\n{i}. {insight['title']}\n")
                if insight['type'] == 'suggestion':
                    f.write(f"   Проблема: {insight['message']}\n")
                    f.write(f"   Решение: {insight['action']}\n")
                elif insight['type'] == 'metric':
                    f.write(f"   Значение: {insight['value']}\n")
                    f.write(f"   Оценка: {insight['recommendation']}\n")
                elif insight['type'] == 'distribution':
                    f.write(f"   {insight['data']}\n")
            
            f.write("\n\nФАЙЛЫ ПО КАТЕГОРИЯМ\n")
            f.write("-" * 70 + "\n")
            
            # Группируем файлы по категориям
            by_category = defaultdict(list)
            for file_info in files_analysis:
                if 'categories' in file_info:
                    for cat in file_info['categories']:
                        by_category[cat].append(file_info['filename'])
            
            for category in sorted(by_category.keys()):
                f.write(f"\n📁 {category.upper()}\n")
                for filename in sorted(by_category[category]):
                    f.write(f"  ├── {filename}\n")
        
        return json_path, txt_path

def main():
    source = r"C:\Users\Z\Desktop\gordon\portfolio_markdown"
    output = r"C:\Users\Z\Desktop\gordon"
    
    if not os.path.exists(source):
        print(f"❌ Папка не найдена: {source}")
        return
    
    analyzer = PatternAnalyzer(source)
    
    print(f"📂 Анализирую: {source}\n")
    
    # Анализ
    files_analysis = analyzer.analyze_directory()
    
    # Генерация инсайтов
    analyzer.generate_insights(files_analysis)
    
    # Сохранение отчёта
    json_path, txt_path = analyzer.save_report(files_analysis, output)
    
    print(f"\n✅ Анализ завершён!")
    print(f"\n📊 Результаты:")
    print(f"  JSON: {json_path}")
    print(f"  TXT:  {txt_path}")
    
    # Выводим инсайты
    print(f"\n💡 ИНСАЙТЫ:\n")
    for insight in analyzer.insights:
        print(f"  • {insight['title']}")
        if insight['type'] == 'suggestion':
            print(f"    → {insight['message']}")

if __name__ == "__main__":
    main()
