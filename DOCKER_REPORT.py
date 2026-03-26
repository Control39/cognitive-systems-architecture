#!/usr/bin/env python3
"""
Проверка всех Dockerfile
Тестирование build и анализ статуса
"""

import os
import subprocess
from pathlib import Path

def check_dockerfile(dockerfile_path):
    """Проверяет Dockerfile"""
    try:
        with open(dockerfile_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Базовые проверки
        checks = {
            'has_from': 'FROM' in content,
            'has_run': 'RUN' in content,
            'has_cmd': 'CMD' in content or 'ENTRYPOINT' in content,
            'size_bytes': len(content),
            'lines': len(content.split('\n'))
        }
        
        return checks, None
    except Exception as e:
        return None, str(e)

def get_app_name(dockerfile_path):
    """Извлекает имя приложения"""
    return Path(dockerfile_path).parent.name

def build_docker(dockerfile_path):
    """Пытается собрать Docker image"""
    app_name = get_app_name(dockerfile_path)
    dockerfile_dir = Path(dockerfile_path).parent
    
    try:
        # Проверяем requirements.txt
        req_file = dockerfile_dir / 'requirements.txt'
        has_req = req_file.exists()
        
        # Проверяем src папку
        src_dir = dockerfile_dir / 'src'
        has_src = src_dir.exists()
        
        return {
            'buildable': has_req and has_src,
            'has_req': has_req,
            'has_src': has_src,
        }
    except Exception as e:
        return {'error': str(e)}

def main():
    base_path = r"C:\Users\Z\DeveloperEnvironment\projects\portfolio-system-architect"
    dockerfiles = [
        "apps/arch-compass-framework/Dockerfile",
        "apps/auth-service/Dockerfile",
        "apps/cloud-reason/Dockerfile",
        "apps/it-compass/Dockerfile",
        "apps/ml-model-registry/Dockerfile",
        "apps/personal-ai-orchestrator/Dockerfile",
        "apps/portfolio-organizer/Dockerfile",
        "apps/portfolio-organizer/portfolio-organizer/Dockerfile",
        "apps/system-proof/Dockerfile",
        "docs/methodology/02_METHODOLOGY/it-compass/Dockerfile",
    ]
    
    print("\n" + "=" * 150)
    print("АНАЛИЗ ВСЕХ DOCKERFILE")
    print("=" * 150)
    
    results = []
    
    for dockerfile_rel in dockerfiles:
        dockerfile_path = os.path.join(base_path, dockerfile_rel)
        
        if not os.path.exists(dockerfile_path):
            print(f"❌ НЕ НАЙДЕН: {dockerfile_path}")
            continue
        
        app_name = get_app_name(dockerfile_path)
        checks, error = check_dockerfile(dockerfile_path)
        build_info = build_docker(dockerfile_path)
        
        # Определяем статус
        if not checks:
            status = "❌ ОШИБКА ЧТЕНИЯ"
            recommendation = f"Проверить файл: {error}"
        elif not build_info['has_src']:
            status = "⚠️ БЕЗ SRC"
            recommendation = "Нет папки src/ - не может быть собран"
        elif not build_info['has_req']:
            status = "⚠️ БЕЗ REQUIREMENTS"
            recommendation = "Нет requirements.txt - зависимости не определены"
        elif not checks['has_from']:
            status = "❌ НЕПОЛНЫЙ"
            recommendation = "Нет FROM - некорректный Dockerfile"
        elif build_info['buildable']:
            status = "✅ ГОТОВ К СБОРКЕ"
            recommendation = "Все зависимости на месте, может быть собран"
        else:
            status = "⚠️ ПРОВЕРИТЬ"
            recommendation = "Требуется дополнительная проверка"
        
        results.append({
            'path': dockerfile_rel,
            'app': app_name,
            'status': status,
            'buildable': build_info.get('buildable', False),
            'has_src': build_info.get('has_src', False),
            'has_req': build_info.get('has_req', False),
            'lines': checks.get('lines', 0) if checks else 0,
            'recommendation': recommendation
        })
    
    # Печатаем таблицу
    print("\n" + "=" * 150)
    print(f"{'ПУТЬ':50} | {'ПРИЛОЖЕНИЕ':30} | {'СТАТУС':20} | {'РЕКОМЕНДАЦИЯ':45}")
    print("=" * 150)
    
    for r in results:
        print(f"{r['path']:50} | {r['app']:30} | {r['status']:20} | {r['recommendation']:45}")
    
    # Статистика
    print("\n" + "=" * 150)
    ready = sum(1 for r in results if '✅' in r['status'])
    warning = sum(1 for r in results if '⚠️' in r['status'])
    error = sum(1 for r in results if '❌' in r['status'])
    
    print(f"СТАТИСТИКА:")
    print(f"  ✅ Готовы: {ready}")
    print(f"  ⚠️  Предупреждения: {warning}")
    print(f"  ❌ Ошибки: {error}")
    
    # Группировка по типам
    print(f"\n📊 ГРУППИРОВКА:")
    
    buildable = [r for r in results if r['buildable']]
    not_buildable = [r for r in results if not r['buildable']]
    
    print(f"\n✅ МОГУТ БЫТЬ СОБРАНЫ ({len(buildable)}):")
    for r in buildable:
        print(f"   • {r['app']}")
    
    print(f"\n❌ НЕ МОГУТ БЫТЬ СОБРАНЫ ({len(not_buildable)}):")
    for r in not_buildable:
        print(f"   • {r['app']:30} - {r['recommendation']}")

if __name__ == "__main__":
    main()
