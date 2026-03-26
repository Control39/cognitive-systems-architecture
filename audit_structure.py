#!/usr/bin/env python3
"""
Структурный аудит репо
Показывает все проблемы и дает план исправления
"""

import os
from pathlib import Path
from collections import defaultdict

def analyze_structure(root_path):
    """Анализирует структуру"""
    
    print("\n" + "=" * 80)
    print("📊 АУДИТ СТРУКТУРЫ РЕПОЗИТОРИЯ")
    print("=" * 80)
    
    issues = []
    structure = {}
    
    # 1. Проверяем дублирующиеся папки
    print("\n1️⃣ ДУБЛИРОВАНИЯ И ВЛОЖЕННОСТЬ")
    print("-" * 80)
    
    duplicate_check = [
        ('apps/it-compass', 'IT-Compass повторение'),
        ('apps/it-compass-hybrid', 'IT-Compass гибрид (дублирование?)'),
        ('apps/cloud-reason', 'Cloud-Reason'),
        ('apps/cloud-reason-integrated', 'Cloud-Reason интеграция (дублирование?)'),
        ('apps/portfolio-organizer', 'Portfolio-Organizer'),
        ('apps/system-proof', 'System-Proof'),
    ]
    
    for path_pattern, desc in duplicate_check:
        full_path = os.path.join(root_path, path_pattern)
        if os.path.exists(full_path):
            print(f"  ✅ {path_pattern}")
    
    # 2. Пустые папки
    print("\n2️⃣ ПУСТЫЕ/НЕИСПОЛЬЗУЕМЫЕ ПАПКИ")
    print("-" * 80)
    
    empty_dirs = []
    for item in os.listdir(root_path):
        path = os.path.join(root_path, item)
        if os.path.isdir(path):
            # Пропускаем служебные
            if item.startswith('.'):
                continue
            
            # Считаем файлы
            file_count = 0
            for root, dirs, files in os.walk(path):
                # Пропускаем служебные
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                file_count += len([f for f in files if not f.startswith('.')])
            
            if file_count == 0:
                empty_dirs.append(item)
                print(f"  ⚠️  {item}/ - ПУСТО")
            elif file_count < 3:
                print(f"  ⚠️  {item}/ - минимум файлов ({file_count})")
    
    # 3. Множество README/docs
    print("\n3️⃣ ДОКУМЕНТАЦИЯ")
    print("-" * 80)
    
    readme_count = 0
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.lower() in ['readme.md', 'index.md']:
                readme_count += 1
    
    print(f"  📄 README файлов: {readme_count} (много ли?)")
    
    # 4. Конфигурационные файлы
    print("\n4️⃣ КОНФИГУРАЦИЯ")
    print("-" * 80)
    
    configs = [
        'docker-compose.yml',
        'docker-compose.override.yml',
        'docker-compose.gateway.yml',
        'docker-compose.mlflow.yml',
        'docker-compose.monitoring.yml',
        'pyproject.toml',
        '.env.local',
        'pyproject.toml',
    ]
    
    for config in configs:
        config_path = os.path.join(root_path, config)
        if os.path.exists(config_path):
            size = os.path.getsize(config_path)
            print(f"  ✅ {config} ({size} bytes)")
    
    # 5. Apps
    print("\n5️⃣ ПРИЛОЖЕНИЯ (apps/)")
    print("-" * 80)
    
    apps_path = os.path.join(root_path, 'apps')
    if os.path.exists(apps_path):
        apps = [d for d in os.listdir(apps_path) if os.path.isdir(os.path.join(apps_path, d)) and not d.startswith('__')]
        print(f"  Количество: {len(apps)}")
        print(f"  Приложения:")
        for app in sorted(apps):
            app_path = os.path.join(apps_path, app)
            has_src = os.path.exists(os.path.join(app_path, 'src'))
            has_docker = os.path.exists(os.path.join(app_path, 'Dockerfile'))
            status = "✅" if (has_src and has_docker) else "⚠️"
            print(f"    {status} {app} (src:{has_src}, docker:{has_docker})")
    
    # 6. Структура "слои"
    print("\n6️⃣ ОСНОВНЫЕ СЛОИ")
    print("-" * 80)
    
    layers = {
        '01_CORE': 'Core компоненты',
        'METHODOLOGY': 'Методология (IT-Compass, etc)',
        'EVIDENCE': 'Доказательства компетенций',
        'docs': 'Документация',
        'deployment': 'Deployment конфиги',
        'tools': 'Инструменты',
    }
    
    for layer, desc in layers.items():
        layer_path = os.path.join(root_path, layer)
        if os.path.exists(layer_path):
            item_count = len(os.listdir(layer_path))
            print(f"  ✅ {layer}/ ({item_count} файлов/папок) - {desc}")
    
    return empty_dirs

def main():
    repo_path = r"C:\Users\Z\DeveloperEnvironment\projects\portfolio-system-architect"
    
    empty_dirs = analyze_structure(repo_path)
    
    print("\n" + "=" * 80)
    print("✨ РЕКОМЕНДАЦИИ")
    print("=" * 80)
    
    if empty_dirs:
        print(f"\n1. УДАЛИТЬ пустые папки:")
        for d in empty_dirs:
            print(f"   - {d}/")
    
    print(f"\n2. СЛИТЬ дублирующиеся:")
    print(f"   - it-compass + it-compass-hybrid → одна папка")
    print(f"   - cloud-reason + cloud-reason-integrated → одна папка")
    
    print(f"\n3. ОЧИСТИТЬ конфигурацию:")
    print(f"   - Слишком много docker-compose.*.yml (есть override.yml - используется?)")
    
    print(f"\n4. ДОКУМЕНТАЦИЯ:")
    print(f"   - Много README - создать ARCHITECTURE.md с картой всего")

if __name__ == "__main__":
    main()
