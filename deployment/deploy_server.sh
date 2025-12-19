#!/bin/bash
# ===========================================
# SZ Global Arabia - Quick Deploy Script
# Run this on the SERVER to pull latest changes from GitHub
# ===========================================

set -e

SERVER_PATH="/var/www/szglobal"

echo "=========================================="
echo "  SZ Global Arabia - Quick Deploy"
echo "=========================================="

cd $SERVER_PATH

echo "[1/5] Pulling latest code from GitHub..."
git pull origin main || git pull origin master

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Installing/updating dependencies..."
pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=szglobal.settings_production

echo "[4/5] Collecting static files and running migrations..."
python manage.py collectstatic --noinput
python manage.py migrate --noinput

echo "[5/5] Restarting services..."
chown -R www-data:www-data $SERVER_PATH
systemctl restart szglobal
systemctl restart nginx

echo ""
echo "=========================================="
echo "  Deployment Complete!"
echo "=========================================="
echo ""
echo "Your site is live at:"
echo "  - http://68.183.92.148"
echo "  - http://szglobalarabia.com"
