#!/usr/bin/env python3
"""
Fix Nesting - Исправляет избыточную вложенность в репо
"""

import os
import shutil
from pathlib import Path

def fix_nesting(app_dir, app_name):
    """Исправляет структуру app/app/"""
    
    nested_path = os.path.join(app_dir, app_name)
    
    if not os.path.exists(nested_path):
        return False
    
    print(f"\n🔧 Исправляю: {app_name}")
    print("-" * 70)
    
    # Файлы для перемещения из nested в основную папку
    files_to_move = ['Dockerfile', 'README.md', 'requirements.txt', '.gitignore', 'setup.py']
    dirs_to_move = ['src', 'tests', 'config']
    
    moved_files = []
    moved_dirs = []
    
    # Перемещаем файлы
    for file in files_to_move:
        src_file = os.path.join(nested_path, file)
        dst_file = os.path.join(app_dir, file)
        
        if os.path.exists(src_file):
            # Если в корне уже есть - пропускаем
            if os.path.exists(dst_file):
                print(f"  ⚠️  {file} - уже в корне, пропускаем")
            else:
                shutil.move(src_file, dst_file)
                print(f"  ✅ {file} - перемещён")
                moved_files.append(file)
    
    # Перемещаем директории
    for dir_name in dirs_to_move:
        src_dir = os.path.join(nested_path, dir_name)
        dst_dir = os.path.join(app_dir, dir_name)
        
        if os.path.exists(src_dir):
            # Если в корне уже есть - объединяем
            if os.path.exists(dst_dir):
                print(f"  ⚠️  {dir_name}/ - уже в корне, объединяю...")
                for item in os.listdir(src_dir):
                    src_item = os.path.join(src_dir, item)
                    dst_item = os.path.join(dst_dir, item)
                    if os.path.isdir(src_item):
                        if os.path.exists(dst_item):
                            print(f"     - {item}/ уже существует")
                        else:
                            shutil.move(src_item, dst_item)
                    else:
                        shutil.move(src_item, dst_item)
            else:
                shutil.move(src_dir, dst_dir)
                print(f"  ✅ {dir_name}/ - перемещена")
                moved_dirs.append(dir_name)
    
    # Удаляем пустую вложенную папку
    try:
        os.rmdir(nested_path)
        print(f"  ✅ Пустая папка {app_name}/ удалена")
    except Exception as e:
        print(f"  ⚠️  Не удалось удалить {app_name}/: {e}")
    
    return len(moved_files) > 0 or len(moved_dirs) > 0

def main():
    base_path = r"C:\Users\Z\DeveloperEnvironment\projects\portfolio-system-architect\apps"
    
    print("🔍 ИСПРАВЛЕНИЕ ВЛОЖЕННОСТИ СТРУКТУРЫ")
    print("=" * 70)
    
    # Проблемные приложения
    problematic_apps = {
        'portfolio-organizer': os.path.join(base_path, 'portfolio-organizer'),
        'system-proof': os.path.join(base_path, 'system-proof')
    }
    
    fixed_count = 0
    
    for app_name, app_dir in problematic_apps.items():
        if os.path.exists(app_dir):
            if fix_nesting(app_dir, app_name):
                fixed_count += 1
    
    print("\n" + "=" * 70)
    print(f"✅ ИСПРАВЛЕНО: {fixed_count} приложений")
    print("\n📋 Проверь структуру:")
    print("  apps/portfolio-organizer/ - должна быть прямая (без вложенности)")
    print("  apps/system-proof/ - должна быть прямая (без вложенности)")

if __name__ == "__main__":
    main()
