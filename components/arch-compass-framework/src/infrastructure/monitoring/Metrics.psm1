<#
.SYNOPSIS
    Модуль сбора метрик для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для сбора, хранения и управления 
    метриками приложения.

.FUNCTIONALITY
    Сбор метрик
#>

#region Private Variables
$script:Metrics = @{}
$script:Counters = @{}
#endregion Private Variables

#region Private Functions
function Get-CurrentTimestamp {
    return [long][double]::Parse((Get-Date -UFormat %s))
}
#endregion Private Functions

#region Public Functions
<#
.SYNOPSIS
    Получает значение метрики.

.DESCRIPTION
    Эта функция возвращает значение указанной метрики.

.PARAMETER Name
    Имя метрики.

.EXAMPLE
    Get-Metrics -Name "requests_total"

    Получает значение метрики "requests_total".
#>
function Get-Metrics {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    if ($script:Metrics.ContainsKey($Name)) {
        return $script:Metrics[$Name]
    } else {
        Write-Warning "Метрика '$Name' не найдена"
        return $null
    }
}

<#
.SYNOPSIS
    Обновляет значение метрики.

.DESCRIPTION
    Эта функция обновляет значение указанной метрики.

.PARAMETER Name
    Имя метрики.

.PARAMETER Value
    Новое значение метрики.

.PARAMETER Operation
    Операция для выполнения с метрикой (Set, Increment, Decrement, Add, Subtract).

.EXAMPLE
    Update-Metrics -Name "requests_total" -Value 1 -Operation "Increment"

    Увеличивает значение метрики "requests_total" на 1.
#>
function Update-Metrics {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        
        [Parameter(Mandatory = $false)]
        [double]$Value = 1,
        
        [Parameter(Mandatory = $false)]
        [ValidateSet("Set", "Increment", "Decrement", "Add", "Subtract")]
        [string]$Operation = "Set"
    )
    
    try {
        switch ($Operation) {
            "Set" {
                $script:Metrics[$Name] = $Value
            }
            "Increment" {
                if ($script:Metrics.ContainsKey($Name)) {
                    $script:Metrics[$Name] += $Value
                } else {
                    $script:Metrics[$Name] = $Value
                }
            }
            "Decrement" {
                if ($script:Metrics.ContainsKey($Name)) {
                    $script:Metrics[$Name] -= $Value
                } else {
                    $script:Metrics[$Name] = -$Value
                }
            }
            "Add" {
                if ($script:Metrics.ContainsKey($Name)) {
                    $script:Metrics[$Name] += $Value
                } else {
                    $script:Metrics[$Name] = $Value
                }
            }
            "Subtract" {
                if ($script:Metrics.ContainsKey($Name)) {
                    $script:Metrics[$Name] -= $Value
                } else {
                    $script:Metrics[$Name] = -$Value
                }
            }
        }
        
        Write-Verbose "Метрика '$Name' обновлена. Новое значение: $($script:Metrics[$Name])"
    } catch {
        Write-Error "Ошибка при обновлении метрики '$Name': $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Сбрасывает значение метрики.

.DESCRIPTION
    Эта функция сбрасывает значение указанной метрики к нулю.

.PARAMETER Name
    Имя метрики.

.EXAMPLE
    Reset-Metrics -Name "requests_total"

    Сбрасывает значение метрики "requests_total" к нулю.
#>
function Reset-Metrics {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    $script:Metrics[$Name] = 0
    Write-Verbose "Метрика '$Name' сброшена к нулю"
}

<#
.SYNOPSIS
    Получает все метрики.

.DESCRIPTION
    Эта функция возвращает все текущие метрики.

.EXAMPLE
    Get-AllMetrics

    Получает все текущие метрики.
#>
function Get-AllMetrics {
    [CmdletBinding()]
    param()
    
    return $script:Metrics.Clone()
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Get-Metrics",
    "Update-Metrics",
    "Reset-Metrics",
    "Get-AllMetrics"
)
#endregion Export Module Members