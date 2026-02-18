<#
.SYNOPSIS
    Модуль сканирования безопасности для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для сканирования проекта на наличие 
    потенциальных уязвимостей и проблем безопасности.

.FUNCTIONALITY
    Сканирование безопасности
#>

#region Private Variables
$script:SecurityIssues = @()
#endregion Private Variables

#region Private Functions
function Test-FileForSecrets {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )
    
    try {
        $content = Get-Content -Path $FilePath -Raw
        
        # Паттерны для поиска потенциальных секретов
        $patterns = @{
            "API Key"         = "api[_-]?key['""]?\s*[:=]\s*['""]?[a-zA-Z0-9_\-]{10,}['""]?"
            "Password"        = "password['""]?\s*[:=]\s*['""]?[a-zA-Z0-9_\-!@#$%^&*()]{5,}['""]?"
            "Secret"          = "secret['""]?\s*[:=]\s*['""]?[a-zA-Z0-9_\-]{10,}['""]?"
            "Token"           = "token['""]?\s*[:=]\s*['""]?[a-zA-Z0-9_\-]{10,}['""]?"
            "ConnectionString" = "connection[_-]?string['""]?\s*[:=]\s*['""]?[^'""]{10,}['""]?"
        }
        
        foreach ($pattern in $patterns.GetEnumerator()) {
            if ($content -match $pattern.Value) {
                $script:SecurityIssues += [PSCustomObject]@{
                    Type     = "Potential Secret"
                    Issue    = $pattern.Key
                    FilePath = $FilePath
                    Line     = $matches[0]
                }
            }
        }
    } catch {
        Write-Warning "Не удалось прочитать файл $FilePath : $($_.Exception.Message)"
    }
}

function Test-FilePermissions {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath
    )
    
    try {
        $acl = Get-Acl -Path $FilePath
        $accessRules = $acl.Access
        
        foreach ($rule in $accessRules) {
            # Проверяем наличие разрешений для Everyone или Users
            if ($rule.IdentityReference -match "Everyone|Users") {
                $script:SecurityIssues += [PSCustomObject]@{
                    Type     = "File Permissions"
                    Issue    = "Небезопасные разрешения для $($rule.IdentityReference)"
                    FilePath = $FilePath
                    Details  = "$($rule.FileSystemRights) - $($rule.AccessControlType)"
                }
            }
        }
    } catch {
        Write-Warning "Не удалось получить ACL для файла $FilePath : $($_.Exception.Message)"
    }
}
#endregion Private Functions

#region Public Functions
<#
.SYNOPSIS
    Выполняет сканирование безопасности проекта.

.DESCRIPTION
    Эта функция сканирует указанный путь на наличие потенциальных уязвимостей 
    и проблем безопасности.

.PARAMETER Path
    Путь для сканирования.

.PARAMETER IncludeSubdirectories
    Включать подкаталоги в сканирование.

.PARAMETER FilePattern
    Шаблон файлов для сканирования (по умолчанию: *.ps1,*.psm1,*.psd1,*.yaml,*.yml,*.json,*.config).

.EXAMPLE
    Invoke-SecurityScan -Path "C:\Project"

    Выполняет сканирование безопасности проекта в папке "C:\Project".
#>
function Invoke-SecurityScan {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        
        [Parameter(Mandatory = $false)]
        [bool]$IncludeSubdirectories = $true,
        
        [Parameter(Mandatory = $false)]
        [string]$FilePattern = "*.ps1,*.psm1,*.psd1,*.yaml,*.yml,*.json,*.config"
    )
    
    # Очищаем предыдущие результаты
    $script:SecurityIssues = @()
    
    try {
        # Разбираем шаблоны файлов
        $patterns = $FilePattern -split ","
        
        # Получаем список файлов для сканирования
        $files = @()
        foreach ($pattern in $patterns) {
            if ($IncludeSubdirectories) {
                $files += Get-ChildItem -Path $Path -Filter $pattern -Recurse -File -ErrorAction SilentlyContinue
            } else {
                $files += Get-ChildItem -Path $Path -Filter $pattern -File -ErrorAction SilentlyContinue
            }
        }
        
        # Сканируем каждый файл
        foreach ($file in $files) {
            Write-Verbose "Сканирование файла: $($file.FullName)"
            Test-FileForSecrets -FilePath $file.FullName
            Test-FilePermissions -FilePath $file.FullName
        }
        
        # Возвращаем результаты
        return $script:SecurityIssues
    } catch {
        Write-Error "Ошибка при выполнении сканирования безопасности: $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Получает оценку безопасности проекта.

.DESCRIPTION
    Эта функция возвращает числовую оценку безопасности проекта 
    на основе результатов сканирования.

.PARAMETER SecurityIssues
    Результаты сканирования безопасности.

.EXAMPLE
    $issues = Invoke-SecurityScan -Path "C:\Project"
    $score = Get-SecurityScore -SecurityIssues $issues

    Получает оценку безопасности проекта.
#>
function Get-SecurityScore {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [array]$SecurityIssues
    )
    
    # Базовая оценка
    $score = 100
    
    # Уменьшаем оценку за каждую найденную проблему
    $score -= $SecurityIssues.Count * 5
    
    # Убеждаемся, что оценка не меньше 0
    if ($score -lt 0) { $score = 0 }
    
    return $score
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Invoke-SecurityScan",
    "Get-SecurityScore"
)
#endregion Export Module Members