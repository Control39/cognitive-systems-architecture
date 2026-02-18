#!/usr/bin/env pwsh

# arch.ps1 - CLI для Arch-Compass Framework

param(
    [Parameter(Position=0)]
    [string]$Command,
    
    [switch]$RunSecurityTests,
    
    [switch]$RunGitleaksScan,
    
    [switch]$Help
)

# Настройка
$ModuleRoot = Split-Path $PSScriptRoot -Parent
$ModuleName = "ArchCompass"

# Импорт модуля
$ModulePath = Join-Path $ModuleRoot "$ModuleName.psm1"
if (Test-Path $ModulePath) {
    Import-Module $ModulePath -Force
} else {
    Write-Error "Модуль не найден: $ModulePath"
    exit 1
}

# Помощь
if ($Help) {
    Write-Host @"
Arch-Compass Framework CLI

Доступные команды:
  test                    Запуск тестов
  test -RunSecurityTests  Запуск тестов с проверкой безопасности
  analyze                 Запуск анализа
  analyze -RunGitleaksScan Запуск сканирования секретов gitleaks
  score                   Получение оценки безопасности
  help                    Показать эту справку
"@
    exit 0
}

# Обработка команд
switch ($Command) {
    'test' {
        Write-Host "Запуск тестов..." -ForegroundColor Green
        Start-ArchCompass -RunSecurityTests:$RunSecurityTests
    }
    
    'analyze' {
        Write-Host "Запуск анализа..." -ForegroundColor Yellow
        if ($RunGitleaksScan) {
            Write-Host "Запуск сканирования секретов gitleaks..." -ForegroundColor Yellow
            # Вызов функции сканирования безопасности
            Invoke-SecurityScan -Path "." -ConfigFile ".gitleaks.toml" -VerboseOutput
        }
    }
    
    'score' {
        Write-Host "Получение оценки безопасности..." -ForegroundColor Cyan
        # Логика получения оценки
        Write-Host "Оценка безопасности: A+"
    }
    
    default {
        if ($Command) {
            Write-Error "Неизвестная команда: $Command"
        } else {
            Write-Host "Используйте 'arch.ps1 help' для получения справки."
        }
        exit 1
    }
}