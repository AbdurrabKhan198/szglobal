@echo off
REM ===========================================
REM SZ Global Arabia - One-Click Deploy via GitHub
REM Server: 68.183.92.148
REM Domain: szglobalarabia.com
REM GitHub: https://github.com/AbdurrabKhan198/szglobal.git
REM ===========================================
REM This script:
REM 1. Builds Tailwind CSS
REM 2. Commits and pushes to GitHub
REM 3. Pulls latest code on server
REM 4. Restarts services
REM

echo ==========================================
echo   SZ Global Arabia - Deploy via GitHub
echo ==========================================
echo.
echo Server: 68.183.92.148
echo GitHub: https://github.com/AbdurrabKhan198/szglobal
echo.

set SERVER_IP=68.183.92.148
set SERVER_USER=root
set SERVER_PATH=/var/www/szglobal
set LOCAL_PATH=c:\Users\hp\Desktop\clients\sz global\szglobal

cd /d "%LOCAL_PATH%"

echo [1/6] Building Tailwind CSS...
call npm run build 2>nul
if %errorlevel% neq 0 (
    echo Note: Tailwind build skipped or not configured.
)
echo Done!
echo.

echo [2/6] Adding all changes to Git...
git add -A
echo Done!
echo.

echo [3/6] Committing changes...
set /p COMMIT_MSG="Enter commit message (or press Enter for default): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Deploy update %date% %time%
git commit -m "%COMMIT_MSG%"
echo Done!
echo.

echo [4/6] Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo Trying 'master' branch instead...
    git push origin master
)
echo Done!
echo.

echo [5/6] Pulling latest code on server...
ssh %SERVER_USER%@%SERVER_IP% "cd %SERVER_PATH% && git pull origin main || git pull origin master"
echo Done!
echo.

echo [6/6] Running deployment on server...
ssh %SERVER_USER%@%SERVER_IP% "cd %SERVER_PATH% && source venv/bin/activate && pip install -r requirements.txt && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py collectstatic --noinput && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py migrate --noinput && systemctl restart szglobal && systemctl restart nginx"
echo Done!
echo.

echo ==========================================
echo   DEPLOYMENT COMPLETE!
echo ==========================================
echo.
echo Your website is now live at:
echo   http://68.183.92.148
echo   http://szglobalarabia.com
echo   http://www.szglobalarabia.com
echo.
pause
