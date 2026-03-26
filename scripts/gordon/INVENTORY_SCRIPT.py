#!/usr/bin/env python3
"""
Автоматическая инвентаризация системы разработки
Сканирует диск, классифицирует файлы, создаёт отчёт для RAG + анализа
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Конфигурация
SCAN_ROOT = r"C:\Users\Z"
OUTPUT_DIR = r"C:\Users\Z\DeveloperEnvironment\projects\INVENTORY_OUTPUT"
IGNORE_DIRS = {
    '.git', '.vscode', '.idea', 'node_modules', '__pycache__', '.env',
    'venv', '.venv', '.cache', 'dist', 'build', '.next', '.nuxt'
}
IGNORE_FILES = {'.gitignore', '.DS_Store', 'Thumbs.db'}

# Расширения файлов — классификация
FILE_TYPES = {
    'code': {'.py', '.js', '.ts', '.jsx', '.tsx', '.go', '.java', '.cpp', '.c', '.rs', '.rb', '.php', '.cs', '.swift'},
    'config': {'.json', '.yaml', '.yml', '.toml', '.xml', '.conf', '.env', '.ini', '.cfg'},
    'docs': {'.md', '.txt', '.rst', '.adoc', '.doc', '.docx', '.pdf'},
    'data': {'.csv', '.xlsx', '.xls', '.sql', '.db', '.sqlite', '.parquet', '.json'},
    'docker': {'Dockerfile', 'docker-compose.yml', '.dockerignore'},
    'git': {'.gitmodules', '.gitignore'},
    'scripts': {'.ps1', '.sh', '.bash', '.bat', '.cmd'},
    'media': {'.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mp3', '.wav', '.svg'},
    'archive': {'.zip', '.tar', '.gz', '.7z', '.rar'},
}

def classify_file(filename, ext):
    """Классифицирует файл по типу"""
    if filename in FILE_TYPES['docker']:
        return 'docker'
    for category, extensions in FILE_TYPES.items():
        if ext.lower() in extensions:
            return category
    return 'other'

def scan_directory(root_path):
    """Сканирует директорию, собирает статистику"""
    stats = defaultdict(int)
    file_list = []
    error_list = []

    for dirpath, dirnames, filenames in os.walk(root_path):
        # Фильтруем игнорируемые папки
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for filename in filenames:
            if filename in IGNORE_FILES:
                continue
            
            try:
                filepath = os.path.join(dirpath, filename)
                ext = os.path.splitext(filename)[1]
                ftype = classify_file(filename, ext)
                size = os.path.getsize(filepath)
                
                stats[ftype] += 1
                file_list.append({
                    'path': filepath,
                    'name': filename,
                    'type': ftype,
                    'size': size,
                    'dir': dirpath
                })
            except Exception as e:
                error_list.append({'file': filepath, 'error': str(e)})
    
    return dict(stats), file_list, error_list

def find_projects():
    """Находит основные проекты (папки с .git или src)"""
    projects = []
    for item in Path(r"C:\Users\Z\DeveloperEnvironment\projects").iterdir():
        if item.is_dir() and item.name not in IGNORE_DIRS:
            has_git = (item / '.git').exists()
            has_src = any(item.glob('**/src')) or any(item.glob('**/main.*'))
            if has_git or has_src:
                projects.append({
                    'name': item.name,
                    'path': str(item),
                    'has_git': has_git
                })
    return projects

def main():
    print("🔍 Инвентаризация системы разработки...")
    print(f"📂 Сканирование: {SCAN_ROOT}")
    
    # Создаём выходную директорию
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Сканируем
    stats, files, errors = scan_directory(SCAN_ROOT)
    projects = find_projects()
    
    # Результаты
    report = {
        'timestamp': datetime.now().isoformat(),
        'scan_root': SCAN_ROOT,
        'statistics': stats,
        'total_files': sum(stats.values()),
        'projects': projects,
        'errors': len(errors)
    }
    
    # Сохраняем отчёт
    report_file = os.path.join(OUTPUT_DIR, 'INVENTORY_REPORT.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Сохраняем список файлов
    files_file = os.path.join(OUTPUT_DIR, 'ALL_FILES.json')
    with open(files_file, 'w', encoding='utf-8') as f:
        json.dump(files, f, indent=2, ensure_ascii=False)
    
    # Тектовый отчёт
    txt_report = os.path.join(OUTPUT_DIR, 'INVENTORY_REPORT.txt')
    with open(txt_report, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("INVENTORY REPORT\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"📅 Дата: {report['timestamp']}\n")
        f.write(f"📂 Сканирование: {SCAN_ROOT}\n")
        f.write(f"📊 Всего файлов: {report['total_files']}\n\n")
        
        f.write("СТАТИСТИКА ПО ТИПАМ:\n")
        f.write("-" * 40 + "\n")
        for ftype, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            f.write(f"  {ftype:15} : {count:6} файлов\n")
        
        f.write("\n\nПРОЕКТЫ (с Git или src):\n")
        f.write("-" * 40 + "\n")
        for proj in projects:
            git_mark = "✓ Git" if proj['has_git'] else "✗ No Git"
            f.write(f"  • {proj['name']:30} [{git_mark}]\n")
        
        if errors:
            f.write(f"\n⚠️  Ошибок при сканировании: {len(errors)}\n")
    
    # Печатаем результаты
    print("\n✅ Инвентаризация завершена!")
    print(f"\n📊 Статистика:")
    for ftype, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"   {ftype:15} : {count:6} файлов")
    
    print(f"\n🗂️  Найдено проектов: {len(projects)}")
    for proj in projects[:10]:  # Первые 10
        print(f"   • {proj['name']}")
    if len(projects) > 10:
        print(f"   ... и ещё {len(projects) - 10}")
    
    print(f"\n💾 Результаты сохранены в: {OUTPUT_DIR}")
    print(f"   • INVENTORY_REPORT.json (для RAG)")
    print(f"   • ALL_FILES.json (список файлов)")
    print(f"   • INVENTORY_REPORT.txt (читаемый отчёт)")

if __name__ == "__main__":
    main()
