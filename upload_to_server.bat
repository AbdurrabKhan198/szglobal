@echo off
REM ===========================================
REM SZ Global Arabia - Upload to DigitalOcean
REM Server: 68.183.92.148
REM Domain: szglobalarabia.com
REM ===========================================
REM 
REM PREREQUISITES:
REM 1. Install OpenSSH client (Windows 10/11 has it built-in)
REM 2. Set up SSH key authentication (recommended) or use password
REM 3. Ensure the server setup has been run first
REM
REM To set up SSH key:
REM   ssh-keygen -t rsa -b 4096
REM   ssh-copy-id root@68.183.92.148
REM

echo ==========================================
echo   SZ Global Arabia - Upload to Server
echo ==========================================
echo.

set SERVER_IP=68.183.92.148
set SERVER_USER=root
set SERVER_PATH=/var/www/szglobal
set LOCAL_PATH=c:\Users\hp\Desktop\clients\sz global\szglobal

echo Server: %SERVER_IP%
echo Destination: %SERVER_PATH%
echo.

echo [1/4] Preparing files for upload...
cd /d "%LOCAL_PATH%"

echo [2/4] Uploading project files to server...
echo Note: You will be prompted for password if SSH key is not set up
echo.

REM Using SCP to upload files (exclude unnecessary folders)
REM First, create a temporary exclude file
echo node_modules > "%TEMP%\exclude.txt"
echo .git >> "%TEMP%\exclude.txt"
echo __pycache__ >> "%TEMP%\exclude.txt"
echo *.pyc >> "%TEMP%\exclude.txt"
echo .env >> "%TEMP%\exclude.txt"
echo db.sqlite3 >> "%TEMP%\exclude.txt"
echo staticfiles >> "%TEMP%\exclude.txt"

REM Upload using SCP (you may need to run this manually if rsync is not available)
echo Uploading files via SCP...
scp -r manage.py requirements.txt gunicorn.conf.py szglobal website deployment %SERVER_USER%@%SERVER_IP%:%SERVER_PATH%/

echo.
echo [3/4] Setting up on server...
echo Running deployment script on server...
ssh %SERVER_USER%@%SERVER_IP% "cd %SERVER_PATH% && bash deployment/deploy_server.sh"

echo.
echo [4/4] Cleaning up...
del "%TEMP%\exclude.txt" 2>nul

echo.
echo ==========================================
echo   Upload Complete!
echo ==========================================
echo.
echo Your website should now be live at:
echo   http://68.183.92.148
echo   http://szglobalarabia.com
echo.
pause
