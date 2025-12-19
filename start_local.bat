@echo off
echo ========================================
echo    SZ Global Arabia - Quick Start
echo ========================================
echo.

:: Navigate to project directory
cd /d "c:\Users\hp\Desktop\clients\sz global\szglobal"

echo Starting Django development server...
echo.
echo Your website will be available at:
echo   - http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python manage.py runserver

echo.
pause
