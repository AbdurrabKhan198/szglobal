@echo off
REM ===========================================
REM SZ Global Arabia - First-Time Server Setup
REM Server: 68.183.92.148
REM GitHub: https://github.com/AbdurrabKhan198/szglobal.git
REM ===========================================
REM Run this ONCE before first deployment to set up the server
REM This will clone your repo from GitHub!

echo ==========================================
echo   SZ Global Arabia - Server Setup
echo ==========================================
echo.
echo This script will:
echo 1. Set up the server with all dependencies
echo 2. Clone your project from GitHub
echo 3. Configure Nginx and Gunicorn
echo.
echo Make sure you have SSH access to root@68.183.92.148
echo.
pause

set SERVER_IP=68.183.92.148
set SERVER_USER=root
set GITHUB_REPO=https://github.com/AbdurrabKhan198/szglobal.git
set SERVER_PATH=/var/www/szglobal

echo [1/7] Connecting to server and updating system...
ssh %SERVER_USER%@%SERVER_IP% "apt update && apt upgrade -y"

echo [2/7] Installing required packages...
ssh %SERVER_USER%@%SERVER_IP% "apt install -y python3 python3-pip python3-venv nginx git ufw"

echo [3/7] Setting up firewall...
ssh %SERVER_USER%@%SERVER_IP% "ufw allow OpenSSH && ufw allow 'Nginx Full' && ufw --force enable"

echo [4/7] Cloning repository from GitHub...
ssh %SERVER_USER%@%SERVER_IP% "rm -rf %SERVER_PATH% && git clone %GITHUB_REPO% %SERVER_PATH%"

echo [5/7] Setting up Python virtual environment...
ssh %SERVER_USER%@%SERVER_IP% "cd %SERVER_PATH% && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

echo [6/8] Creating necessary directories...
ssh %SERVER_USER%@%SERVER_IP% "mkdir -p /var/log/gunicorn && mkdir -p /var/run/gunicorn && mkdir -p %SERVER_PATH%/logs && mkdir -p %SERVER_PATH%/staticfiles && mkdir -p %SERVER_PATH%/media && chown -R www-data:www-data /var/log/gunicorn && chown -R www-data:www-data /var/run/gunicorn"

echo [7/8] Configuring Nginx, Gunicorn, and Webhook...
ssh %SERVER_USER%@%SERVER_IP% "cp %SERVER_PATH%/deployment/nginx_szglobal.conf /etc/nginx/sites-available/szglobal && ln -sf /etc/nginx/sites-available/szglobal /etc/nginx/sites-enabled/ && rm -f /etc/nginx/sites-enabled/default && nginx -t"
ssh %SERVER_USER%@%SERVER_IP% "cp %SERVER_PATH%/deployment/szglobal.service /etc/systemd/system/ && cp %SERVER_PATH%/deployment/szglobal-webhook.service /etc/systemd/system/ && systemctl daemon-reload && systemctl enable szglobal && systemctl enable szglobal-webhook"

echo.
echo [8/8] Running initial deployment and starting services...
ssh %SERVER_USER%@%SERVER_IP% "cd %SERVER_PATH% && source venv/bin/activate && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py collectstatic --noinput && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py migrate --noinput && chown -R www-data:www-data %SERVER_PATH% && systemctl start szglobal && systemctl start szglobal-webhook && systemctl restart nginx && ufw allow 9000/tcp"

echo.
echo ==========================================
echo   SERVER SETUP COMPLETE!
echo ==========================================
echo.
echo Your website is now live at:
echo   http://68.183.92.148
echo   http://szglobalarabia.com
echo.
echo ==========================================
echo   ONE-CLICK DEPLOY URL (BOOKMARK THIS!):
echo   http://68.183.92.148:9000/deploy?key=szglobal2024
echo ==========================================
echo.
echo Just visit the URL above to deploy anytime!
echo No need to use command line anymore.
echo.
pause
