# src/ai/providers/OpenAIIntegration.psm1
# OpenAIIntegration - интеграция с OpenAI API

# Зависимости
# - SecretManager для получения API ключа
# - PowerShell 7+ для поддержки Invoke-RestMethod с JSON

# Конфигурация по умолчанию
$defaultConfig = @{
    Model = "gpt-4"
    Temperature = 0.7
    MaxTokens = 1000
    ApiVersion = "2023-07-01-preview"
}

function Invoke-OpenAIAPI {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Prompt,
        
        [string]$Model = $defaultConfig.Model,
        
        [float]$Temperature = $defaultConfig.Temperature,
        
        [int]$MaxTokens = $defaultConfig.MaxTokens,
        
        [hashtable]$AdditionalParams = @{},
        
        [switch]$JsonResponse
    )
    
    # Получаем API ключ из SecretManager
    $apiKey = [SecretManager]::GetSecret("OPENAI_API_KEY")
    if (-not $apiKey) {
        Write-Error "API ключ OpenAI не найден. Установите OPENAI_API_KEY в переменных окружения."
        return $null
    }
    
    # URL API
    $url = "https://api.openai.com/v1/chat/completions"
    
    # Заголовки
    $headers = @{
        "Content-Type" = "application/json"
        "Authorization" = "Bearer $apiKey"
    }
    
    # Тело запроса
    $body = @{
        model = $Model
        messages = @(@{ role = "user"; content = $Prompt })
        temperature = $Temperature
        max_tokens = $MaxTokens
    }
    
    # Добавляем дополнительные параметры
    foreach ($key in $AdditionalParams.Keys) {
        $body[$key] = $AdditionalParams[$key]
    }
    
    # Логирование (без секретов)
    $maskedBody = [SecretManager]::MaskSecretsInObject($body)
    Write-Host "Отправка запроса в OpenAI: $($maskedBody | ConvertTo-Json -Compress)" -ForegroundColor DarkGray
    
    try {
        # Выполняем запрос
        $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body ($body | ConvertTo-Json) -ContentType "application/json"
        
        # Возвращаем полный ответ или только текст
        if ($JsonResponse) {
            return $response
        } else {
            return $response.choices[0].message.content
        }
    } catch {
        Write-Error "Ошибка при вызове OpenAI API: $_"
        if ($_.Exception.Response) {
            $errorDetails = $_.Exception.Response | ConvertTo-Json
            Write-Error "Детали ошибки: $errorDetails"
        }
        return $null
    }
}

# Упрощенная функция для генерации текста
function Get-AICompletion {
    param(
        [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
        [string]$InputText,
        
        [string]$Model = $defaultConfig.Model,
        
        [float]$Temperature = $defaultConfig.Temperature,
        
        [int]$MaxTokens = $defaultConfig.MaxTokens
    )
    
    process {
        $result = Invoke-OpenAIAPI -Prompt $InputText -Model $Model -Temperature $Temperature -MaxTokens $MaxTokens
        return $result
    }
}

# Экспортируем функции
Export-ModuleMember -Function Invoke-OpenAIAPI, Get-AICompletion