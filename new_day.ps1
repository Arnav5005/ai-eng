param(
    [Parameter(Mandatory = $true)]
    [string]$DayName,

    [string[]]$Packages = @(
        'groq',
        'python-dotenv',
        'numpy',
        'sentence-transformers'
    )
)

$root = 'C:\Projects\ai-eng'
$dayPath = Join-Path $root $DayName

if (-not (Test-Path $root)) {
    New-Item -ItemType Directory -Path $root -Force | Out-Null
}

if (-not (Test-Path $dayPath)) {
    New-Item -ItemType Directory -Path $dayPath -Force | Out-Null
}

Set-Location $dayPath

if (Test-Path '.venv') {
    Remove-Item -Recurse -Force '.venv'
}

python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install $Packages

Write-Host ""
Write-Host "Environment is ready at: $dayPath"
Write-Host "Activate it with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "Run Python with:"
Write-Host "  .\.venv\Scripts\python.exe"
