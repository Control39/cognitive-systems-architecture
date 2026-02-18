<#
.SYNOPSIS
    Модуль интеграции с OpenAI для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для взаимодействия с API OpenAI,
    включая генерацию текста, анализ данных и другие возможности ИИ.

.FUNCTIONALITY
    Интеграция с OpenAI
#>

#region Private Variables
$script:OpenAIEndpoint = "https://api.openai.com/v1"
$script:OpenAIKey = $null
#endregion Private Variables

#region Private Functions
function Invoke-OpenAIRequest {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Uri,
        
        [Parameter(Mandatory = $true)]
        [hashtable]$Body,
        
        [Parameter(Mandatory = $false)]
        [string]$Method = "Post"
    )
    
    try {
        # Формируем заголовки
        $headers = @{
            "Authorization" = "Bearer $script:OpenAIKey"
            "Content-Type"  = "application/json"
        }
        
        # Выполняем запрос
        $response = Invoke-RestMethod -Uri $Uri -Method $Method -Headers $headers -Body ($Body | ConvertTo-Json -Depth 10)
        
        return $response
    } catch {
        Write-Error "Ошибка при выполнении запроса к OpenAI: $($_.Exception.Message)"
        throw
    }
}
#endregion Private Functions

#region Public Functions
<#
.SYNOPSIS
    Устанавливает ключ API OpenAI.

.DESCRIPTION
    Эта функция устанавливает ключ API OpenAI для последующих запросов.

.PARAMETER ApiKey
    Ключ API OpenAI.

.EXAMPLE
    Set-OpenAIKey -ApiKey "sk-..."

    Устанавливает ключ API OpenAI.
#>
function Set-OpenAIKey {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$ApiKey
    )
    
    $script:OpenAIKey = $ApiKey
    Write-Verbose "Ключ API OpenAI установлен"
}

<#
.SYNOPSIS
    Генерирует текст с помощью модели GPT.

.DESCRIPTION
    Эта функция генерирует текст с помощью модели GPT на основе заданного промпта.

.PARAMETER Prompt
    Промпт для генерации текста.

.PARAMETER Model
    Модель GPT для использования (по умолчанию: gpt-3.5-turbo).

.PARAMETER MaxTokens
    Максимальное количество токенов в ответе (по умолчанию: 150).

.PARAMETER Temperature
    Температура генерации (по умолчанию: 0.7).

.EXAMPLE
    $response = Invoke-GPTCompletion -Prompt "Напиши краткое описание архитектуры микросервисов"

    Генерирует текст с помощью модели GPT.
#>
function Invoke-GPTCompletion {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Prompt,
        
        [Parameter(Mandatory = $false)]
        [string]$Model = "gpt-3.5-turbo",
        
        [Parameter(Mandatory = $false)]
        [int]$MaxTokens = 150,
        
        [Parameter(Mandatory = $false)]
        [double]$Temperature = 0.7
    )
    
    # Проверяем, установлен ли ключ API
    if (-not $script:OpenAIKey) {
        Write-Error "Ключ API OpenAI не установлен. Используйте Set-OpenAIKey для установки."
        return
    }
    
    try {
        # Формируем тело запроса
        $body = @{
            model       = $Model
            messages    = @(
                @{ role = "user"; content = $Prompt }
            )
            max_tokens  = $MaxTokens
            temperature = $Temperature
        }
        
        # Выполняем запрос
        $response = Invoke-OpenAIRequest -Uri "$script:OpenAIEndpoint/chat/completions" -Body $body
        
        # Возвращаем текст ответа
        return $response.choices[0].message.content
    } catch {
        Write-Error "Ошибка при генерации текста с помощью GPT: $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Анализирует текст с помощью модели GPT.

.DESCRIPTION
    Эта функция анализирует текст с помощью модели GPT и возвращает структурированный ответ.

.PARAMETER Text
    Текст для анализа.

.PARAMETER AnalysisType
    Тип анализа (по умолчанию: general).

.PARAMETER Model
    Модель GPT для использования (по умолчанию: gpt-3.5-turbo).

.EXAMPLE
    $analysis = Invoke-TextAnalysis -Text "Архитектура микросервисов..." -AnalysisType "architecture"

    Анализирует текст с помощью модели GPT.
#>
function Invoke-TextAnalysis {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Text,
        
        [Parameter(Mandatory = $false)]
        [string]$AnalysisType = "general",
        
        [Parameter(Mandatory = $false)]
        [string]$Model = "gpt-3.5-turbo"
    )
    
    # Формируем промпт в зависимости от типа анализа
    $prompt = switch ($AnalysisType) {
        "architecture" {
            "Проанализируйте следующую архитектуру и выделите ключевые компоненты, их взаимодействие и потенциальные проблемы:`n`n$Text`n`nПредоставьте структурированный ответ в формате JSON."
        }
        "security" {
            "Проанализируйте следующий текст на предмет потенциальных проблем безопасности:`n`n$Text`n`nПредоставьте структурированный ответ в формате JSON."
        }
        "performance" {
            "Проанализируйте следующий текст на предмет потенциальных проблем производительности:`n`n$Text`n`nПредоставьте структурированный ответ в формате JSON."
        }
        default {
            "Проанализируйте следующий текст и предоставьте краткое резюме:`n`n$Text`n`nПредоставьте структурированный ответ в формате JSON."
        }
    }
    
    try {
        # Генерируем ответ
        $response = Invoke-GPTCompletion -Prompt $prompt -Model $Model -MaxTokens 500
        
        # Пытаемся преобразовать ответ в объект PowerShell
        try {
            $jsonResponse = $response | ConvertFrom-Json
            return $jsonResponse
        } catch {
            # Если не удалось преобразовать в JSON, возвращаем исходный текст
            return $response
        }
    } catch {
        Write-Error "Ошибка при анализе текста: $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Генерирует код с помощью модели GPT.

.DESCRIPTION
    Эта функция генерирует код с помощью модели GPT на основе заданного описания.

.PARAMETER Description
    Описание требуемого кода.

.PARAMETER Language
    Язык программирования (по умолчанию: powershell).

.PARAMETER Model
    Модель GPT для использования (по умолчанию: gpt-3.5-turbo).

.EXAMPLE
    $code = Invoke-CodeGeneration -Description "Функция для проверки валидности email" -Language "powershell"

    Генерирует код с помощью модели GPT.
#>
function Invoke-CodeGeneration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Description,
        
        [Parameter(Mandatory = $false)]
        [string]$Language = "powershell",
        
        [Parameter(Mandatory = $false)]
        [string]$Model = "gpt-3.5-turbo"
    )
    
    try {
        # Формируем промпт
        $prompt = "Сгенерируйте $Language код для следующего требования:`n`n$Description`n`nПредоставьте только код без дополнительных объяснений."
        
        # Генерируем код
        $response = Invoke-GPTCompletion -Prompt $prompt -Model $Model -MaxTokens 300
        
        return $response
    } catch {
        Write-Error "Ошибка при генерации кода: $($_.Exception.Message)"
        throw
    }
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Set-OpenAIKey",
    "Invoke-GPTCompletion",
    "Invoke-TextAnalysis",
    "Invoke-CodeGeneration"
)
#endregion Export Module Members