@echo off
echo ========================================
echo    SZ Global Arabia - Deployment Script
echo ========================================
echo.

:: Navigate to project directory
cd /d "c:\Users\hp\Desktop\clients\sz global\szglobal"

echo [1/5] Collecting static files...
python manage.py collectstatic --noinput
if %errorlevel% neq 0 (
    echo ERROR: Failed to collect static files!
    pause
    exit /b 1
)
echo ✓ Static files collected successfully!
echo.

echo [2/5] Running database migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations!
    pause
    exit /b 1
)
echo ✓ Database migrations applied!
echo.

echo [3/5] Building Tailwind CSS...
call npm run build
if %errorlevel% neq 0 (
    echo WARNING: Tailwind build failed or not configured. Continuing...
)
echo ✓ Tailwind CSS built!
echo.

echo ========================================
echo    Starting Development Server
echo ========================================
echo.
echo Your website will be available at:
echo   - Local:   http://127.0.0.1:8000
echo   - Network: http://68.183.92.148:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

echo [4/5] Starting Django server on 0.0.0.0:8000...
python manage.py runserver 0.0.0.0:8000

echo.
echo Server stopped.
pause
