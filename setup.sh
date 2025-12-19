#!/bin/bash
# ===========================================
# SZ Global Arabia - Complete Server Setup
# Run this with: curl -sSL https://raw.githubusercontent.com/AbdurrabKhan198/szglobal/main/setup.sh | sudo bash
# ===========================================

set -e

echo "=========================================="
echo "  SZ Global Arabia - Auto Setup"
echo "=========================================="
echo ""

# Update system
echo "[1/10] Updating system..."
apt update && apt upgrade -y

# Install packages
echo "[2/10] Installing packages..."
apt install -y python3 python3-pip python3-venv nginx git ufw

# Setup firewall
echo "[3/10] Setting up firewall..."
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw allow 9000/tcp
ufw --force enable

# Clone repository
echo "[4/10] Cloning repository..."
rm -rf /var/www/szglobal
git clone https://github.com/AbdurrabKhan198/szglobal.git /var/www/szglobal

# Setup Python environment
echo "[5/10] Setting up Python environment..."
cd /var/www/szglobal
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Create directories
echo "[6/10] Creating directories..."
mkdir -p /var/log/gunicorn /var/run/gunicorn
mkdir -p /var/www/szglobal/logs /var/www/szglobal/staticfiles /var/www/szglobal/media
chown -R www-data:www-data /var/log/gunicorn /var/run/gunicorn

# Configure Nginx
echo "[7/10] Configuring Nginx..."
cp /var/www/szglobal/deployment/nginx_szglobal.conf /etc/nginx/sites-available/szglobal
ln -sf /etc/nginx/sites-available/szglobal /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t

# Setup systemd services
echo "[8/10] Setting up services..."
cp /var/www/szglobal/deployment/szglobal.service /etc/systemd/system/
cp /var/www/szglobal/deployment/szglobal-webhook.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable szglobal szglobal-webhook

# Django setup
echo "[9/10] Setting up Django..."
cd /var/www/szglobal
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=szglobal.settings_production
python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Start services
echo "[10/10] Starting services..."
chown -R www-data:www-data /var/www/szglobal
systemctl start szglobal
systemctl start szglobal-webhook
systemctl restart nginx

echo ""
echo "=========================================="
echo "  SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "Website: http://68.183.92.148"
echo "Website: http://szglobalarabia.com"
echo ""
echo "One-Click Deploy URL:"
echo "http://68.183.92.148:9000/deploy?key=szglobal2024"
echo ""
echo "=========================================="
