# Test Archcompass.Tests

- **Путь**: `02_MODULES\arch-compass-framework\tests\test_archcompass.Tests.ps1`
- **Тип**: .PS1
- **Размер**: 416 байт
- **Последнее изменение**: 2026-03-13 21:04:54

## Превью

```
Import-Module -Force ./ArchCompass.psm1

Describe 'ArchCompass Functions' {
    It 'Tests Get-ArchPattern' {
        $result = Get-ArchPattern -Name 'Microservices'
        $result | Should -Not -BeNullOrEmpty
    }
    # Add tests for all exported functions
    It 'Throws on invalid pattern' {
        { Get-ArchPattern -Name 'Invalid' } | Should -Throw
    }
}

# Run with Invoke-Pester this file


```


