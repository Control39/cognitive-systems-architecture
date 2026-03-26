#!/usr/bin/env python3
"""
ПОЛНЫЙ АУДИТ РЕПОЗИТОРИЯ
Читает ВСЕ README, определяет версии, создаёт конструктор системы
НЕ ТРОГАЕМ ничего, только анализируем!
"""

import os
import json
from pathlib import Path
from collections import defaultdict

def read_readme(filepath):
    """Читает README и возвращает первые 3 строки"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:10]
            return ''.join(lines).strip()
    except:
        return None

def analyze_app(app_path, app_name):
    """Анализирует приложение"""
    info = {
        'name': app_name,
        'path': app_path,
        'has_src': os.path.exists(os.path.join(app_path, 'src')),
        'has_dockerfile': os.path.exists(os.path.join(app_path, 'Dockerfile')),
        'has_readme': os.path.exists(os.path.join(app_path, 'README.md')),
        'has_requirements': os.path.exists(os.path.join(app_path, 'requirements.txt')),
        'readme_content': None,
        'nested_version': None,
    }
    
    # Читаем README
    if info['has_readme']:
        info['readme_content'] = read_readme(os.path.join(app_path, 'README.md'))
    
    # Проверяем вложенную версию (app/app/)
    nested_path = os.path.join(app_path, app_name)
    if os.path.exists(nested_path) and os.path.isdir(nested_path):
        nested_readme = os.path.join(nested_path, 'README.md')
        if os.path.exists(nested_readme):
            info['nested_version'] = read_readme(nested_readme)
    
    return info

def main():
    base_path = r"C:\Users\Z\DeveloperEnvironment\projects\portfolio-system-architect"
    apps_path = os.path.join(base_path, 'apps')
    
    print("\n" + "=" * 100)
    print("🔍 ПОЛНЫЙ АУДИТ РЕПОЗИТОРИЯ - БЕЗ ИЗМЕНЕНИЙ")
    print("=" * 100)
    
    # Читаем все приложения
    apps = []
    for item in sorted(os.listdir(apps_path)):
        item_path = os.path.join(apps_path, item)
        if os.path.isdir(item_path) and not item.startswith('__'):
            app_info = analyze_app(item_path, item)
            apps.append(app_info)
    
    # Анализируем
    print(f"\n📊 НАЙДЕНО ПРИЛОЖЕНИЙ: {len(apps)}\n")
    
    # Группируем по типам
    complete_apps = []
    incomplete_apps = []
    versioned_apps = []
    
    for app in apps:
        status = []
        
        # Проверяем полноту
        if app['has_src'] and app['has_dockerfile'] and app['has_readme']:
            complete_apps.append(app)
            status = ['✅ ПОЛНОЕ']
        else:
            incomplete_apps.append(app)
            status = ['⚠️ НЕПОЛНОЕ']
        
        # Проверяем версии
        if app['nested_version']:
            versioned_apps.append(app)
            status.append('📌 ЕСТЬ ВЕРСИЯ')
        
        # Печатаем
        components = []
        if app['has_src']:
            components.append('src')
        if app['has_dockerfile']:
            components.append('docker')
        if app['has_readme']:
            components.append('readme')
        if app['has_requirements']:
            components.append('reqs')
        
        print(f"  {app['name']:35} {', '.join(status):25} [{', '.join(components)}]")
        
        if app['readme_content']:
            first_line = app['readme_content'].split('\n')[0][:60]
            print(f"    → {first_line}")
    
    # ВЫВОДЫ
    print("\n" + "=" * 100)
    print("📋 АНАЛИЗ")
    print("=" * 100)
    
    print(f"\n✅ ПОЛНЫЕ ПРИЛОЖЕНИЯ ({len(complete_apps)}):")
    for app in complete_apps:
        print(f"   • {app['name']}")
    
    print(f"\n⚠️  НЕПОЛНЫЕ ПРИЛОЖЕНИЯ ({len(incomplete_apps)}):")
    for app in incomplete_apps:
        missing = []
        if not app['has_src']:
            missing.append('src')
        if not app['has_dockerfile']:
            missing.append('Dockerfile')
        if not app['has_readme']:
            missing.append('README')
        print(f"   • {app['name']:35} (недостаёт: {', '.join(missing)})")
    
    print(f"\n📌 ВЕРСИОНИРОВАННЫЕ ПРИЛОЖЕНИЯ ({len(versioned_apps)}):")
    for app in versioned_apps:
        print(f"   • {app['name']:35} (есть вложенная версия app/{app['name']}/)")
    
    # ВОПРОСЫ
    print("\n" + "=" * 100)
    print("❓ ВОПРОСЫ ДЛЯ УТОЧНЕНИЯ")
    print("=" * 100)
    
    print("""
1. IT-COMPASS (2 версии):
   - apps/it-compass/ (ПОЛНАЯ - код + docker)
   - docs/methodology/02_METHODOLOGY/it-compass/ (МЕТОДОЛОГИЯ - только доки)
   → ЭТО РАЗНЫЕ ИЛИ ДУБЛИ?

2. CLOUD-REASON (2 версии):
   - apps/cloud-reason/ (ПОЛНАЯ)
   - apps/cloud-reason-integrated/ (НЕПОЛНАЯ)
   → ЧТО РАЗНИЦА? Интегрировать? Удалить?

3. PORTFOLIO-ORGANIZER (2 версии):
   - apps/portfolio-organizer/ (КОРЕНЬ + src/)
   - apps/portfolio-organizer/portfolio-organizer/ (ВЛОЖЕННАЯ версия)
   → ЗАЧЕМ ВЛОЖЕННОСТЬ? Разные версии?

4. SYSTEM-PROOF (2 версии):
   - apps/system-proof/ (КОРЕНЬ + src/)
   - apps/system-proof/system-proof/ (ВЛОЖЕННАЯ версия)
   → ЗАЧЕМ ВЛОЖЕННОСТЬ? Разные версии?

5. НЕПОЛНЫЕ ПРИЛОЖЕНИЯ:
   - auth-service, career-development, job-automation-agent (есть src, нет docker)
   - cloud-reason-integrated, it-compass-hybrid, rag-system, thought-architecture (нет ни src ни docker)
   → АКТИВНЫЕ ИЛИ АРХИВНЫЕ?

6. 01_CORE папка:
   - Содержит только пустую папку 01_CORE/components/it-compass/
   → ДЛЯ ЧЕГО ОНА? ЧТО ТУТ ДОЛЖНО БЫТЬ?
""")

    print("\n" + "=" * 100)
    print("✋ СТОП - ЖДУ ТВОИХ ОТВЕТОВ НА ВОПРОСЫ ВЫШЕ")
    print("=" * 100)
    
    # Сохраняем отчёт
    report = {
        'total_apps': len(apps),
        'complete': len(complete_apps),
        'incomplete': len(incomplete_apps),
        'versioned': len(versioned_apps),
        'apps': apps
    }
    
    with open(os.path.join(base_path, 'AUDIT_REPORT.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Отчёт сохранён: AUDIT_REPORT.json")

if __name__ == "__main__":
    main()
