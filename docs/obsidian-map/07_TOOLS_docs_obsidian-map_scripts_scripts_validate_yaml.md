# Scripts Scripts Validate Yaml

- **Путь**: `07_TOOLS\docs\obsidian-map\scripts_scripts_validate_yaml.md`
- **Тип**: .MD
- **Размер**: 856 байт
- **Последнее изменение**: 2026-03-13 21:09:07

## Превью

```
# Validate Yaml

- **Путь**: `scripts\scripts\validate_yaml.py`
- **Тип**: .PY
- **Размер**: 1,643 байт
- **Последнее изменение**: 2026-03-13 20:24:03

## Превью

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Валидация YAML-файлов проекта"""

import yaml
import sys
from pathlib import Path

def validate_yaml_files(file_list):
    """Проверяет список YAML-файлов на валидность"""
    errors = []
    
    for filepath in file_list:
        try:
            path = Path(filepath)
            
... (файл продолжается)
```


