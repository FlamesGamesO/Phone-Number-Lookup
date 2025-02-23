@echo off
title Installing Python Dependencies
color 6
echo [+] Checking for Python installation...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed. Please install Python first.
    pause
    exit /b
)

echo [+] Installing required Python packages...
pip install --upgrade pip
pip install pyfiglet colorama phonenumbers

echo [+] Installation complete!
pause
