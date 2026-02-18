<#
.SYNOPSIS
    Клиент Prometheus для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для взаимодействия с Prometheus,
    включая отправку метрик и выполнение запросов.

.FUNCTIONALITY
    Клиент Prometheus
#>

#region Private Variables
$script:PrometheusEndpoint = $null
$script:PrometheusJob = "arch-compass"
$script:PrometheusInstance = $env:COMPUTERNAME
#endregion Private Variables

#region Private Functions
function Send-PrometheusMetrics {
    param(
        [Parameter(Mandatory = $true)]
        [hashtable]$Metrics
    )
    
    try {
        # Формируем текстовые метрики в формате Prometheus
        $metricsText = ""
        foreach ($metric in $Metrics.GetEnumerator()) {
            $metricsText += "$($metric.Key) $($metric.Value)`n"
        }
        
        # Формируем URL для отправки метрик
        $url = "$script:PrometheusEndpoint/metrics/job/$script:PrometheusJob/instance/$script:PrometheusInstance"
        
        # Отправляем метрики
        Invoke-RestMethod -Uri $url -Method Post -Body $metricsText -ContentType "text/plain"
        
        Write-Verbose "Метрики успешно отправлены в Prometheus"
    } catch {
        Write-Error "Ошибка при отправке метрик в Prometheus: $($_.Exception.Message)"
        throw
    }
}

function Invoke-PrometheusQuery {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Query
    )
    
    try {
        # Формируем URL для выполнения запроса
        $encodedQuery = [System.Web.HttpUtility]::UrlEncode($Query)
        $url = "$script:PrometheusEndpoint/api/v1/query?query=$encodedQuery"
        
        # Выполняем запрос
        $response = Invoke-RestMethod -Uri $url -Method Get
        
        return $response
    } catch {
        Write-Error "Ошибка при выполнении запроса к Prometheus: $($_.Exception.Message)"
        throw
    }
}
#endregion Private Functions

#region Public Functions
<#
.SYNOPSIS
    Устанавливает конечную точку Prometheus.

.DESCRIPTION
    Эта функция устанавливает конечную точку Prometheus для отправки метрик.

.PARAMETER Endpoint
    URL конечной точки Prometheus.

.EXAMPLE
    Set-PrometheusEndpoint -Endpoint "http://localhost:9091"

    Устанавливает конечную точку Prometheus.
#>
function Set-PrometheusEndpoint {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Endpoint
    )
    
    $script:PrometheusEndpoint = $Endpoint
    Write-Verbose "Конечная точка Prometheus установлена: $Endpoint"
}

<#
.SYNOPSIS
    Устанавливает имя задания Prometheus.

.DESCRIPTION
    Эта функция устанавливает имя задания Prometheus.

.PARAMETER JobName
    Имя задания Prometheus.

.EXAMPLE
    Set-PrometheusJob -JobName "my-app"

    Устанавливает имя задания Prometheus.
#>
function Set-PrometheusJob {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$JobName
    )
    
    $script:PrometheusJob = $JobName
    Write-Verbose "Имя задания Prometheus установлено: $JobName"
}

<#
.SYNOPSIS
    Устанавливает имя экземпляра Prometheus.

.DESCRIPTION
    Эта функция устанавливает имя экземпляра Prometheus.

.PARAMETER InstanceName
    Имя экземпляра Prometheus.

.EXAMPLE
    Set-PrometheusInstance -InstanceName "server01"

    Устанавливает имя экземпляра Prometheus.
#>
function Set-PrometheusInstance {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$InstanceName
    )
    
    $script:PrometheusInstance = $InstanceName
    Write-Verbose "Имя экземпляра Prometheus установлено: $InstanceName"
}

<#
.SYNOPSIS
    Отправляет метрики в Prometheus.

.DESCRIPTION
    Эта функция отправляет указанные метрики в Prometheus.

.PARAMETER Metrics
    Хэш-таблица с метриками для отправки.

.EXAMPLE
    $metrics = @{
        "requests_total" = 100
        "errors_total" = 5
    }
    Send-MetricsToPrometheus -Metrics $metrics

    Отправляет метрики в Prometheus.
#>
function Send-MetricsToPrometheus {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [hashtable]$Metrics
    )
    
    # Проверяем, установлена ли конечная точка
    if (-not $script:PrometheusEndpoint) {
        Write-Error "Конечная точка Prometheus не установлена. Используйте Set-PrometheusEndpoint для установки."
        return
    }
    
    try {
        Send-PrometheusMetrics -Metrics $Metrics
        Write-Verbose "Метрики успешно отправлены в Prometheus"
        return $true
    } catch {
        Write-Error "Ошибка при отправке метрик в Prometheus: $($_.Exception.Message)"
        return $false
    }
}

<#
.SYNOPSIS
    Выполняет запрос к Prometheus.

.DESCRIPTION
    Эта функция выполняет запрос к Prometheus и возвращает результаты.

.PARAMETER Query
    Запрос PromQL для выполнения.

.EXAMPLE
    Invoke-PrometheusQuery -Query "rate(requests_total[5m])"

    Выполняет запрос к Prometheus.
#>
function Invoke-PrometheusQuery {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Query
    )
    
    # Проверяем, установлена ли конечная точка
    if (-not $script:PrometheusEndpoint) {
        Write-Error "Конечная точка Prometheus не установлена. Используйте Set-PrometheusEndpoint для установки."
        return
    }
    
    try {
        $result = Invoke-PrometheusQuery -Query $Query
        return $result
    } catch {
        Write-Error "Ошибка при выполнении запроса к Prometheus: $($_.Exception.Message)"
        throw
    }
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Set-PrometheusEndpoint",
    "Set-PrometheusJob",
    "Set-PrometheusInstance",
    "Send-MetricsToPrometheus",
    "Invoke-PrometheusQuery"
)
#endregion Export Module Members