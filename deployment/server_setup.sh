#!/bin/bash
# ===========================================
# SZ Global Arabia - Server Setup Script
# Server: 68.183.92.148
# Domain: szglobalarabia.com
# GitHub: https://github.com/AbdurrabKhan198/szglobal.git
# ===========================================
# Run this script on your DigitalOcean droplet as root
# Usage: sudo bash server_setup.sh

set -e  # Exit on any error

GITHUB_REPO="https://github.com/AbdurrabKhan198/szglobal.git"
SERVER_PATH="/var/www/szglobal"

echo "=========================================="
echo "  SZ Global Arabia - Server Setup"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Please run as root (use sudo)${NC}"
    exit 1
fi

echo -e "${YELLOW}[1/10] Updating system packages...${NC}"
apt update && apt upgrade -y

echo -e "${YELLOW}[2/10] Installing required packages...${NC}"
apt install -y python3 python3-pip python3-venv nginx git ufw

echo -e "${YELLOW}[3/10] Setting up firewall (UFW)...${NC}"
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable

echo -e "${YELLOW}[4/10] Cloning repository from GitHub...${NC}"
rm -rf $SERVER_PATH
git clone $GITHUB_REPO $SERVER_PATH

echo -e "${YELLOW}[5/10] Creating Python virtual environment...${NC}"
cd $SERVER_PATH
python3 -m venv venv
source venv/bin/activate

echo -e "${YELLOW}[6/10] Installing Python dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "${YELLOW}[7/10] Creating log directories...${NC}"
mkdir -p /var/log/gunicorn
mkdir -p /var/run/gunicorn
mkdir -p $SERVER_PATH/logs
mkdir -p $SERVER_PATH/staticfiles
mkdir -p $SERVER_PATH/media
chown -R www-data:www-data /var/log/gunicorn
chown -R www-data:www-data /var/run/gunicorn

echo -e "${YELLOW}[8/10] Configuring Nginx...${NC}"
cp $SERVER_PATH/deployment/nginx_szglobal.conf /etc/nginx/sites-available/szglobal
ln -sf /etc/nginx/sites-available/szglobal /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t

echo -e "${YELLOW}[9/10] Setting up systemd service...${NC}"
cp $SERVER_PATH/deployment/szglobal.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable szglobal

echo -e "${YELLOW}[10/10] Running initial deployment...${NC}"
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=szglobal.settings_production
python manage.py collectstatic --noinput
python manage.py migrate --noinput
chown -R www-data:www-data $SERVER_PATH

echo -e "${YELLOW}Starting services...${NC}"
systemctl start szglobal
systemctl restart nginx

echo ""
echo -e "${GREEN}=========================================="
echo "  Setup Complete!"
echo "==========================================${NC}"
echo ""
echo "Your website is now live at:"
echo "  - http://68.183.92.148"
echo "  - http://szglobalarabia.com"
echo ""
echo "To update the website, run on your local machine:"
echo "  DEPLOY_ONE_CLICK.bat"
echo ""
echo "Or manually on the server:"
echo "  cd $SERVER_PATH && git pull && source venv/bin/activate"
echo "  python manage.py collectstatic --noinput"
echo "  systemctl restart szglobal"
echo ""
echo "To install SSL (recommended):"
echo "  apt install certbot python3-certbot-nginx"
echo "  certbot --nginx -d szglobalarabia.com -d www.szglobalarabia.com"
