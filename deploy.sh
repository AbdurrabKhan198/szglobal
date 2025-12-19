#!/bin/bash
# ===========================================
# SZ Global Arabia - Quick Deploy
# Run this with: curl -sSL https://raw.githubusercontent.com/AbdurrabKhan198/szglobal/main/deploy.sh | sudo bash
# ===========================================

echo "=========================================="
echo "  SZ Global Arabia - Deploying..."
echo "=========================================="

cd /var/www/szglobal

echo "[1/5] Pulling latest code..."
git pull origin main

echo "[2/5] Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "[3/5] Collecting static files..."
export DJANGO_SETTINGS_MODULE=szglobal.settings_production
python manage.py collectstatic --noinput

echo "[4/5] Running migrations..."
python manage.py migrate --noinput

echo "[5/5] Restarting services..."
chown -R www-data:www-data /var/www/szglobal
systemctl restart szglobal
systemctl restart szglobal-webhook
systemctl restart nginx

echo ""
echo "=========================================="
echo "  DEPLOY COMPLETE!"
echo "=========================================="
echo "Website: http://szglobalarabia.com"
