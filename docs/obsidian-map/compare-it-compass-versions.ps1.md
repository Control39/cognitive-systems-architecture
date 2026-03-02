# Compare It Compass Versions

- **Путь**: `compare-it-compass-versions.ps1`
- **Тип**: .PS1
- **Размер**: 1276 байт
- **Последнее изменение**: 1771570697.4696329

## Предпросмотр

```
#! /bin/powershell
Write-Host "🔍 Сравнение версий IT-Compass..." -ForegroundColor Yellow

$versions = @(
    @{Path = "additional/it-compass"; Name = "Main (current)"},
    @{Path = "additional/leadarchitect-ai-repos/ekaterina-kudelya-it-compass"; Name = "Ekaterina-Kudelya"},
    @{Path = "additional/leadarchitect-ai-repos/my-ecosystem/core/it-compass"; Name = "My-Ecosystem-Core"}
)

foreach ($v in $versions) {
    if (Test-Path $v.Path) {
        Write-Host "📁 Версия: $($v.Name) ($($v.Path))" -
... (файл обрезан для предпросмотра)
```
