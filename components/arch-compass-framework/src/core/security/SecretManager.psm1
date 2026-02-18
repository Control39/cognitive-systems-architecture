<#
.SYNOPSIS
    Модуль управления секретами для Arch Compass Framework.

.DESCRIPTION
    Этот модуль предоставляет функции для безопасного хранения и управления секретами,
    такими как ключи API, пароли и другие конфиденциальные данные.

.FUNCTIONALITY
    Управление секретами
#>

#region Private Variables
$script:Secrets = @{}
#endregion Private Variables

#region Private Functions
function Get-EncryptedSecret {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PlainText,
        
        [Parameter(Mandatory = $true)]
        [string]$Key
    )
    
    try {
        $secureString = ConvertTo-SecureString -String $PlainText -AsPlainText -Force
        $encrypted = ConvertFrom-SecureString -SecureString $secureString -Key ([System.Text.Encoding]::UTF8.GetBytes($Key.PadRight(32).Substring(0, 32)))
        return $encrypted
    } catch {
        Write-Error "Ошибка при шифровании секрета: $($_.Exception.Message)"
        throw
    }
}

function Get-DecryptedSecret {
    param(
        [Parameter(Mandatory = $true)]
        [string]$EncryptedText,
        
        [Parameter(Mandatory = $true)]
        [string]$Key
    )
    
    try {
        $secureString = ConvertTo-SecureString -String $EncryptedText -Key ([System.Text.Encoding]::UTF8.GetBytes($Key.PadRight(32).Substring(0, 32)))
        $decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureString))
        return $decrypted
    } catch {
        Write-Error "Ошибка при расшифровке секрета: $($_.Exception.Message)"
        throw
    }
}
#endregion Private Functions

#region Public Functions
<#
.SYNOPSIS
    Сохраняет секрет в памяти.

.DESCRIPTION
    Эта функция сохраняет секрет в памяти с шифрованием.

.PARAMETER Name
    Имя секрета.

.PARAMETER Value
    Значение секрета.

.PARAMETER EncryptionKey
    Ключ шифрования.

.EXAMPLE
    Set-Secret -Name "APIKey" -Value "sk-..." -EncryptionKey "my-encryption-key"

    Сохраняет секрет с именем "APIKey" и значением "sk-...".
#>
function Set-Secret {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        
        [Parameter(Mandatory = $true)]
        [string]$Value,
        
        [Parameter(Mandatory = $true)]
        [string]$EncryptionKey
    )
    
    try {
        $encryptedValue = Get-EncryptedSecret -PlainText $Value -Key $EncryptionKey
        $script:Secrets[$Name] = $encryptedValue
        Write-Verbose "Секрет '$Name' успешно сохранен"
    } catch {
        Write-Error "Ошибка при сохранении секрета '$Name': $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Получает секрет из памяти.

.DESCRIPTION
    Эта функция получает и расшифровывает секрет из памяти.

.PARAMETER Name
    Имя секрета.

.PARAMETER EncryptionKey
    Ключ шифрования.

.EXAMPLE
    Get-Secret -Name "APIKey" -EncryptionKey "my-encryption-key"

    Получает секрет с именем "APIKey".
#>
function Get-Secret {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        
        [Parameter(Mandatory = $true)]
        [string]$EncryptionKey
    )
    
    if (-not $script:Secrets.ContainsKey($Name)) {
        Write-Error "Секрет с именем '$Name' не найден"
        return $null
    }
    
    try {
        $decryptedValue = Get-DecryptedSecret -EncryptedText $script:Secrets[$Name] -Key $EncryptionKey
        return $decryptedValue
    } catch {
        Write-Error "Ошибка при получении секрета '$Name': $($_.Exception.Message)"
        throw
    }
}

<#
.SYNOPSIS
    Удаляет секрет из памяти.

.DESCRIPTION
    Эта функция удаляет секрет из памяти.

.PARAMETER Name
    Имя секрета.

.EXAMPLE
    Remove-Secret -Name "APIKey"

    Удаляет секрет с именем "APIKey".
#>
function Remove-Secret {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name
    )
    
    if ($script:Secrets.ContainsKey($Name)) {
        $script:Secrets.Remove($Name)
        Write-Verbose "Секрет '$Name' успешно удален"
    } else {
        Write-Warning "Секрет с именем '$Name' не найден"
    }
}

<#
.SYNOPSIS
    Получает список всех сохраненных секретов.

.DESCRIPTION
    Эта функция возвращает список имен всех сохраненных секретов.

.EXAMPLE
    Get-SecretList

    Получает список всех сохраненных секретов.
#>
function Get-SecretList {
    [CmdletBinding()]
    param()
    
    return $script:Secrets.Keys
}
#endregion Public Functions

#region Export Module Members
Export-ModuleMember -Function @(
    "Set-Secret",
    "Get-Secret",
    "Remove-Secret",
    "Get-SecretList"
)
#endregion Export Module Members