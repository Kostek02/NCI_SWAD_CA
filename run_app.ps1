# ============================================================
# run_app.ps1
# -----------
# PowerShell helper script to launch the Secure Notes Flask application.
# 
# Purpose:
# - Optionally create a fresh virtual environment each run (--fresh)
# - Automatically set up environment
# - Install dependencies from requirements.txt
# - Load .env environment variables
# - Run the Flask application via run.py
# - Clean up venv when the app closes
#
# Usage:
#   PowerShell:
#       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#       .\run_app.ps1           # Run app: Reuse venv if exists
#       .\run_app.ps1 --fresh   # Run app: Rorce fresh venv
# ============================================================

param(
    [string]$mode = ""
)

# Step 1: Define app name
$APP_NAME = "Secure Notes App"

Write-Host "============================================================"
Write-Host "Launching $APP_NAME Web Application"
Write-Host "------------------------------------------------------------"

# Step 2: Handle --fresh flag
if ($mode -eq "--fresh"){
    Write-Host "[INFO] Removing existing virtual environment (--fresh flag detected)"
    if (Test-Path "venv"){
        Remove-Item -Recurse -Force "venv"
    }
}

# Step 3: Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "[INFO] Activating virtual environment."
} else {
    Write-Host "[WARNING] No virtual environment found. Creating one."
    python -m venv venv
}

# Activate the virtual environment
. .\venv\Scripts\Activate.ps1 

# Step 4: Install Dependencies
Write-Host "[INFO] Installing dependencies."
pip install -r requirements.txt | Out-Null

# Step 5: Load environment variables (from .env)
if (Test-Path ".env"){
    Write-Host "[INFO] Loading environment variables."
    Get-Content .env | ForEach-Object {
        if ($_ -match "^(?!#)(\w+)=(.+)$") {
            $name = $matches[1]
            $value = $matches[2]
            [System.Environment]::SetEnvironmentVariable($name, $value)
        }
    }
} else {
    Write-Host "[WARNING] .env file not found. Default values will be used."
}

# Step 6: Display environment details
$flaskEnv = [System.Environment]::GetEnvironmentVariable("FLASK_ENV")
$debugMode = [System.Environment]::GetEnvironmentVariable("DEBUG")

Write-Host "[ENVIRONMENT INFO]"
Write-Host ("  FLASK_ENV: {0}" -f ($flaskEnv ?? "development"))
Write-Host ("  DEBUG: {0}" -f ($debugMode ?? "True"))
Write-Host "  SECRET_KEY: [hidden]"
Write-Host "-----------------------------------------------------"

# Step 7: Run the Flask App
Write-Host "[INFO] Starting Flask server."
python run.py 

# Step 8: After exiting (Ctrl+C), clean up the virtual environment
Write-Host "[CLEANUP] Deactivating and removing virtual environment."
deactivate
Remove-Item -Recurse -Force "venv"

# Step 9: End Message
Write-Host "------------------------------------------------------------"
Write-Host "[DONE] Application terminated. Flask server stopped."
Write-Host "============================================================"