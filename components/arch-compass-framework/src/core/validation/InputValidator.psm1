<#
.SYNOPSIS
    Модуль валидации входных данных для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для валидации входных данных,
    включая строки, числа и другие типы данных.

.FUNCTIONALITY
    Валидация входных данных
#>

#region Public Functions
<#
.SYNOPSIS
    Проверяет входные данные на соответствие заданным правилам.

.DESCRIPTION
    Эта функция проверяет входные данные на соответствие заданным правилам валидации.

.PARAMETER InputObject
    Объект для валидации.

.PARAMETER Rules
    Хэш-таблица с правилами валидации.

.EXAMPLE
    $rules = @{
        Required = $true
        Type = "string"
        MinLength = 5
        MaxLength = 50
    }
    Test-InputValidation -InputObject "test" -Rules $rules

    Проверяет строку "test" на соответствие правилам валидации.
#>
function Test-InputValidation {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        $InputObject,
        
        [Parameter(Mandatory = $true)]
        [hashtable]$Rules
    )
    
    try {
        # Проверяем обязательность
        if ($Rules.Required -and (-not $InputObject)) {
            Write-Error "Объект не может быть пустым"
            return $false
        }
        
        # Если объект пуст и не обязателен, валидация пройдена
        if (-not $InputObject) {
            return $true
        }
        
        # Проверяем тип
        if ($Rules.Type) {
            $typeCheck = switch ($Rules.Type.ToLower()) {
                "string" { $InputObject -is [string] }
                "integer" { $InputObject -is [int] -or $InputObject -is [long] }
                "boolean" { $InputObject -is [bool] }
                "array" { $InputObject -is [array] }
                "hashtable" { $InputObject -is [hashtable] }
                default { $true }
            }
            
            if (-not $typeCheck) {
                Write-Error "Объект должен быть типа $($Rules.Type)"
                return $false
            }
        }
        
        # Проверяем строковые правила
        if ($InputObject -is [string]) {
            # Минимальная длина
            if ($Rules.MinLength -and $InputObject.Length -lt $Rules.MinLength) {
                Write-Error "Длина строки должна быть не менее $($Rules.MinLength) символов"
                return $false
            }
            
            # Максимальная длина
            if ($Rules.MaxLength -and $InputObject.Length -gt $Rules.MaxLength) {
                Write-Error "Длина строки должна быть не более $($Rules.MaxLength) символов"
                return $false
            }
            
            # Регулярное выражение
            if ($Rules.Pattern -and $InputObject -notmatch $Rules.Pattern) {
                Write-Error "Строка не соответствует заданному шаблону"
                return $false
            }
        }
        
        # Проверяем числовые правила
        if ($InputObject -is [int] -or $InputObject -is [long] -or $InputObject -is [double]) {
            # Минимальное значение
            if ($Rules.MinValue -and $InputObject -lt $Rules.MinValue) {
                Write-Error "Значение должно быть не менее $($Rules.MinValue)"
                return $false
            }
            
            # Максимальное значение
            if ($Rules.MaxValue -and $InputObject -gt $Rules.MaxValue) {
                Write-Error "Значение должно быть не более $($Rules.MaxValue)"
                return $false
            }
        }
        
        # Проверяем массивы
        if ($InputObject -is [array]) {
            # Минимальное количество элементов
            if ($Rules.MinCount -and $InputObject.Count -lt $Rules.MinCount) {
                Write-Error "Массив должен содержать не менее $($Rules.MinCount) элементов"
                return $false
            }
            
            # Максимальное количество элементов
            if ($Rules.MaxCount -and $InputObject.Count -gt $Rules.MaxCount) {
                Write-Error "Массив должен содержать не более $($Rules.MaxCount) элементов"
                return $false
            }
        }
        
        return $true
    } catch {
        Write-Error "Ошибка при валидации входных данных: $($_.Exception.Message)"
        return $false
    }
}

<#
.SYNOPSIS
    Проверяет строку на соответствие заданным правилам.

.DESCRIPTION
    Эта функция проверяет строку на соответствие заданным правилам валидации.

.PARAMETER StringValue
    Строка для валидации.

.PARAMETER MinLength
    Минимальная длина строки.

.PARAMETER MaxLength
    Максимальная длина строки.

.PARAMETER Pattern
    Регулярное выражение для проверки строки.

.PARAMETER Required
    Обязательность строки.

.EXAMPLE
    Test-StringValidation -StringValue "test" -MinLength 5

    Проверяет строку "test" на минимальную длину 5 символов.
#>
function Test-StringValidation {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$StringValue,
        
        [Parameter(Mandatory = $false)]
        [int]$MinLength = 0,
        
        [Parameter(Mandatory = $false)]
        [int]$MaxLength = [int]::MaxValue,
        
        [Parameter(Mandatory = $false)]
        [string]$Pattern = $null,
        
        [Parameter(Mandatory = $false)]
        [bool]$Required = $true
    )
    
    try {
        # Проверяем обязательность
        if ($Required -and (-not $StringValue)) {
            Write-Error "Строка не может быть пустой"
            return $false
        }
        
        # Если строка пуста и не обязательна, валидация пройдена
        if (-not $StringValue) {
            return $true
        }
        
        # Проверяем минимальную длину
        if ($StringValue.Length -lt $MinLength) {
            Write-Error "Длина строки должна быть не менее $MinLength символов"
            return $false
        }
        
        # Проверяем максимальную длину
        if ($StringValue.Length -gt $MaxLength) {
            Write-Error "Длина строки должна быть не более $MaxLength символов"
            return $false
        }
        
        # Проверяем регулярное выражение
        if ($Pattern -and $StringValue -notmatch $Pattern) {
            Write-Error "Строка не соответствует заданному шаблону"
            return $false
        }
        
        return $true
    } catch {
        Write-Error "Ошибка при валидации строки: $($_.Exception.Message)"
        return $false
    }
}

<#
.SYNOPSIS
    Проверяет число на соответствие заданным правилам.

.DESCRIPTION
    Эта функция проверяет число на соответствие заданным правилам валидации.

.PARAMETER NumberValue
    Число для валидации.

.PARAMETER MinValue
    Минимальное значение числа.

.PARAMETER MaxValue
    Максимальное значение числа.

.PARAMETER Required
    Обязательность числа.

.EXAMPLE
    Test-NumberValidation -NumberValue 5 -MinValue 10

    Проверяет число 5 на минимальное значение 10.
#>
function Test-NumberValidation {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [double]$NumberValue,
        
        [Parameter(Mandatory = $false)]
        [double]$MinValue = [double]::MinValue,
        
        [Parameter(Mandatory = $false)]
        [double]$MaxValue = [double]::MaxValue,
        
        [Parameter(Mandatory = $false)]
        [bool]$Required = $true
    )
    
    try {
        # Проверяем минимальное значение
        if ($NumberValue -lt $MinValue) {
            Write-Error "Значение должно быть не менее $MinValue"
            return $false
        }
        
        # Проверяем максимальное значение
        if ($NumberValue -gt $MaxValue) {
            Write-Error "Значение должно быть не более $MaxValue"
            return $false
        }
        
        return $true
    } catch {
        Write-Error "Ошибка при валидации числа: $($_.Exception.Message)"
        return $false
    }
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Test-InputValidation",
    "Test-StringValidation",
    "Test-NumberValidation"
)
#endregion Export Module Members