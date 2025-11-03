#!/bin/bash
# ============================================================
# run_app.sh
# ----------
# Helper script to launch the Secure Notes Flask application.
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
#   chmod +x run_app.sh     # Make it executable (once)
#   ./run_app.sh            # Run the app; Reuse venv if exists
#   ./run_app.sh --fresh    # Run the app; Force fresh venv
# ============================================================

# Step 1: Define app name
APP_NAME="Secure Notes App"

echo "============================================================"
echo "Launching $APP_NAME Web Application"
echo "------------------------------------------------------------"

# Step 2: Handle --fresh flag
if [ "$1" == "--fresh" ]; then
    echo "[INFO] Removing existing virtual environment (--fresh flag detected)."
    rm -rf venv
fi

# Step 3: Check if virtual environment exists
if [ -d "venv" ]; then
    echo "[INFO] Activating virtual environment."
else
    echo "[WARNING] No virtual environment found. Creating one."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Step 4: Install Dependencies
echo "[INFO] Installing dependencies."
pip install -r requirements.txt > /dev/null

# Step 5: Load environment variables (from .env)
if [ -f ".env" ]; then
    echo "[INFO] Loading environment variables."
    export $(grep -v '^#' .env | xargs)
else
    echo "[WARNING] .env file not found. Default values will be used."
fi

# Step 6: Display environment details
echo "[ENVIRONMENT INFO]"
echo "  FLASK_ENV: ${FLASK_ENV:-development}"
echo "  DEBUG: ${DEBUG:-True}"
echo "  SECRET_KEY: [hidden]"
echo "-----------------------------------------------------"

# Step 7: Run the Flask App
echo "[INFO] Starting Flask server."
python3 run.py

# Step 8: After exiting (Ctrl+C), clean up the virtual environment
echo "[CLEANUP] Deactivating and removing virtual environment."
deactivate
rm -rf venv

# Step 9: End Message
echo "------------------------------------------------------------"
echo "[DONE] Application terminated. Flask server stopped."
echo "============================================================"