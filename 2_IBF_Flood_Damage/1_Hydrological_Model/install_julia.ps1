# Parameters
$Version = "1.11.2"
$MajorMinor = "1.11"
$InstallerURL = "https://julialang-s3.julialang.org/bin/winnt/x64/$MajorMinor/julia-$Version-win64.exe"
$InstallerPath = "$env:TEMP\julia_installer.exe"
$JuliaInstallDir = "C:\Julia-$Version"

# Check if Julia is already installed
$JuliaExe = "$JuliaInstallDir\bin\julia.exe"
if (Test-Path $JuliaExe) {
    Write-Host "Julia $Version is already installed at $JuliaInstallDir"
    & $JuliaExe --version
    exit 0
}

# Download installer
Write-Host "Downloading Julia $Version..."
try {
    Invoke-WebRequest -Uri $InstallerURL -OutFile $InstallerPath
} catch {
    Write-Host "ERROR: Failed to download Julia from $InstallerURL" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    exit 1
}

# Install silently
Write-Host "Installing Julia silently..."
Start-Process -FilePath $InstallerPath -ArgumentList "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/DIR=$JuliaInstallDir" -Wait -NoNewWindow

# Add to PATH (current session)
$env:PATH += ";$JuliaInstallDir\bin"

# Add to PATH (user environment)
[Environment]::SetEnvironmentVariable(
    "PATH",
    "$env:PATH;$JuliaInstallDir\bin",
    [System.EnvironmentVariableTarget]::User
)

# Verify installation
if (Test-Path $JuliaExe) {
    Write-Host "Julia $Version successfully installed to $JuliaInstallDir"
    & $JuliaExe --version
} else {
    Write-Host "ERROR: Julia installation failed!" -ForegroundColor Red
    exit 1
}