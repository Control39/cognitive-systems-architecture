# src/infrastructure/security/SecurityScanner.psm1
# SecurityScanner - интеграция с gitleaks и другими инструментами безопасности

# Зависимости
# Предполагается, что gitleaks установлен в системе
# https://github.com/gitleaks/gitleaks

function Invoke-SecurityScan {
    param(
        [string]$Path = ".",
        [string]$ConfigFile = "", # Путь к конфигурации gitleaks
        [switch]$JsonOutput, # Вывод в формате JSON
        [switch]$VerboseOutput
    )
    
    Write-Host "🔍 Запуск сканирования безопасности в: $Path" -ForegroundColor Yellow
    
    # Опции команды gitleaks
    $commandArgs = @("detect", "--source=$Path", "--no-git")
    
    if ($ConfigFile) {
        if (Test-Path $ConfigFile) {
            $commandArgs += "--config-path=$ConfigFile"
        } else {
            Write-Warning "Конфигурационный файл не найден: $ConfigFile"
        }
    }
    
    if ($JsonOutput) {
        $commandArgs += "--report-format=json"
        $outputFile = "security-report-$(Get-Date -Format 'yyyyMMdd-HHmmss').json"
        $commandArgs += "--report-path=$outputFile"
    }
    
    if ($VerboseOutput) {
        $commandArgs += "--verbose"
    }
    
    # Добавляем паттерны секретов из SecretManager
    $secretPatterns = [SecretManager]::GetCurrentSecretPatterns()
    if ($secretPatterns.Count -gt 0) {
        $patternsArg = "--regex=$(($secretPatterns -join '|'))"
        $commandArgs += $patternsArg
    }
    
    # Выполняем команду
    try {
        Write-Host "Выполнение: gitleaks $commandArgs" -ForegroundColor DarkGray
        
        $result = Start-Process -FilePath "gitleaks" -ArgumentList $commandArgs -Wait -NoNewWindow -PassThru
        
        if ($result.ExitCode -eq 0) {
            Write-Host "✅ Сканирование завершено: утечек не обнаружено" -ForegroundColor Green
            return $true
        } else {
            Write-Host "❌ Сканирование завершено: обнаружены потенциальные утечки!" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Error "Ошибка при выполнении gitleaks: $_"
        return $false
    }
}

# Экспортируем функцию
Export-ModuleMember -Function Invoke-SecurityScan