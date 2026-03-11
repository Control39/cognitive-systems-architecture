# Process Document

- **Путь**: `components\system-proof\RAG\process_document.ps1`
- **Тип**: .PS1
- **Размер**: 3256 байт
- **Последнее изменение**: 1772979098.4458477

## Предпросмотр

```
# Process Document Script
# Скрипт обработки документов

param(
    [Parameter(Mandatory=$true)]
    [string]$Path,
    [string]$OutputFolder = ".\documents\processed"
)

# Функция для логирования
function Write-Log {
    param([string]$Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$Timestamp] $Message"
}

# Проверка существования файла
if (!(Test-Path $Path)) {
    Write-Log "Ошибка: Файл не найден - $Path"
    exit 1
}

# Создание папки для вывода
if (!(Test
... (файл обрезан для предпросмотра)
```
