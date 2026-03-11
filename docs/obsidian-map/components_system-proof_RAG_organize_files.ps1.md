# Organize Files

- **Путь**: `components\system-proof\RAG\organize_files.ps1`
- **Тип**: .PS1
- **Размер**: 3337 байт
- **Последнее изменение**: 1772979098.4448466

## Предпросмотр

```
# Organize Files Script
# Скрипт организации файлов

param(
    [Parameter(Mandatory=$true)]
    [string]$SourcePath,
    [Parameter(Mandatory=$true)]
    [string]$DestinationPath,
    [switch]$IncludeSubdirectories
)

# Функция для логирования
function Write-Log {
    param([string]$Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] $Message"
}

# Проверка существования исходной папки
if (!(Test-Path $SourcePath)) {
    Write-Log "Ошибка: Исходная папк
... (файл обрезан для предпросмотра)
```
