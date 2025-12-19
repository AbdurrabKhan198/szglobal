@echo off
echo ==========================================
echo   SZ Global Arabia - One Click Deploy
echo ==========================================
echo.

cd /d "c:\Users\hp\Desktop\clients\sz global\szglobal"

echo [1/4] Adding changes to Git...
git add -A

echo [2/4] Committing changes...
git commit -m "Deploy update %date% %time%"

echo [3/4] Pushing to GitHub...
git push origin main

echo [4/4] Deploying on server...
ssh root@68.183.92.148 "cd /var/www/szglobal && git pull origin main && source venv/bin/activate && pip install -r requirements.txt && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py collectstatic --noinput && DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py migrate --noinput && sudo chown -R www-data:www-data /var/www/szglobal && sudo systemctl restart szglobal && sudo systemctl restart nginx"

echo.
echo ==========================================
echo   DEPLOYMENT COMPLETE!
echo ==========================================
echo.
echo Website: http://szglobalarabia.com
echo.
pause
