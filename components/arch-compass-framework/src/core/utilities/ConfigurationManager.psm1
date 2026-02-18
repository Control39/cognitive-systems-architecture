# src/core/utilities/ConfigurationManager.psm1
# ConfigurationManager - управление конфигурацией фреймворка

# Загрузка конфигурации из YAML файлов
function Get-Configuration {
    param(
        [string]$ConfigPath = "config/config.yaml",
        [string]$Environment = "default"
    )
    
    # Путь к конфигурации
    $fullPath = Join-Path $PSScriptRoot $ConfigPath
    
    # Проверяем существование файла
    if (-not (Test-Path $fullPath)) {
        Write-Warning "Конфигурационный файл не найден: $fullPath"
        return @{}
    }
    
    try {
        # Читаем содержимое файла
        $content = Get-Content -Path $fullPath -Raw
        
        # Парсим YAML (требует PSYaml модуль)
        # В реальной реализации нужно установить PSYaml: Install-Module -Name PSYaml
        if (Get-Module -ListAvailable -Name PSYaml) {
            Import-Module PSYaml -Force
            $config = ConvertFrom-Yaml -Yaml $content
        } else {
            Write-Warning "Модуль PSYaml не установлен. Установите: Install-Module -Name PSYaml"
            # Простейший парсер YAML для примера
            $config = Parse-SimpleYaml -Content $content
        }
        
        # Применяем окружение
        if ($config.Environments -and $config.Environments.$Environment) {
            # Объединяем глобальную конфигурацию с конфигурацией окружения
            $envConfig = $config.Environments.$Environment
            $mergedConfig = Merge-Hashtable -Base $config -Override $envConfig
            return $mergedConfig
        }
        
        return $config
        
    } catch {
        Write-Error "Ошибка при загрузке конфигурации: $_"
        return @{}
    }
}

# Простейший парсер YAML (для демонстрации)
function Parse-SimpleYaml {
    param([string]$Content)
    
    $result = @{}
    $lines = $Content -split "`n"
    
    foreach ($line in $lines) {
        $line = $line.Trim()
        if ($line -and $line[0] -ne '#') {
            if ($line.Contains(':')) {
                $parts = $line -split ':',2
                $key = $parts[0].Trim()
                $value = $parts[1].Trim()
                # Удаляем кавычки
                if ($value.StartsWith('"') -and $value.EndsWith('"')) {
                    $value = $value.Substring(1, $value.Length-2)
                }
                if ($value.StartsWith("'") -and $value.EndsWith("'")) {
                    $value = $value.Substring(1, $value.Length-2)
                }
                $result[$key] = $value
            }
        }
    }
    
    return $result
}

# Объединение хэштаблиц
function Merge-Hashtable {
    param(
        [hashtable]$Base,
        [hashtable]$Override
    )
    
    $result = @{}
    
    # Копируем базовые значения
    foreach ($key in $Base.Keys) {
        if ($key -ne "Environments") {  # Пропускаем секцию Environments
            $result[$key] = $Base[$key]
        }
    }
    
    # Переопределяем значения
    foreach ($key in $Override.Keys) {
        $result[$key] = $Override[$key]
    }
    
    return $result
}

# Экспортируем функции
Export-ModuleMember -Function Get-Configuration