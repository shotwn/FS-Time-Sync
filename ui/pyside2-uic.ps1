#pyside2-uic mainwindow2.ui | Set-Content -Encoding UTF8 -Path "..\qtgenerated\mainwindow.py"
#pyside2-uic offsetwindow2.ui | Set-Content -Encoding UTF8 -Path "..\qtgenerated\offsetwindow.py"

Get-ChildItem ".\" -Filter *.ui | 
Foreach-Object {
    pyside2-uic $_.FullName | Set-Content -Encoding UTF8 -Path ('..\qtgenerated\' + $_.BaseName + '.py')
    if($LASTEXITCODE -eq 1) {
        Pause
    }
}