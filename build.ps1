Function info {
    param([string]$string)
    Write-Host $string -ForegroundColor Green
}

info("Activate Environment")
.\env\Scripts\activate

info("Build FS Time Sync")
py -3.7-32 -m PyInstaller .\main.spec

info("Compress Executable")
$version = py .\_version.py
info("> Program Version $version")

Move-Item ".\dist\FS Time Sync.exe" ".\dist\FS Time Sync v$version.exe" -Force
Compress-Archive -Path ".\dist\FS Time Sync v$version.exe" ".\dist\FS Time Sync v$version.zip" -Force
pause