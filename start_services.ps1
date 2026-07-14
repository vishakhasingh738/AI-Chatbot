param(
    [int]$BackendPort = 8000,
    [int]$FrontendPort = 8501
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $pythonExe)) {
    Write-Error "Python executable not found at $pythonExe. Create/activate .venv first."
}

Write-Host "Starting backend on http://127.0.0.1:$BackendPort ..."
Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "Set-Location '$projectRoot'; & '$pythonExe' -m uvicorn input:app --reload --port $BackendPort"
)

Write-Host "Starting frontend on http://127.0.0.1:$FrontendPort ..."
Start-Process powershell -ArgumentList @(
    "-NoExit",
    "-Command",
    "Set-Location '$projectRoot'; & '$pythonExe' -m streamlit run streamlit_app.py --server.port $FrontendPort"
)

Write-Host ""
Write-Host "Services launched in separate PowerShell windows."
Write-Host "Backend:  http://127.0.0.1:$BackendPort"
Write-Host "Frontend: http://127.0.0.1:$FrontendPort"
