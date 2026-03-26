param()

$extensions = @('gigacode', 'koda')

foreach ($ext in $extensions) {
    Write-Host "Installing: $ext" -ForegroundColor Green
    & code --install-extension $ext
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK" -ForegroundColor Green
    } else {
        Write-Host "  FAILED" -ForegroundColor Red
    }
}

Write-Host "Done." -ForegroundColor Cyan