# SZ Global Arabia - Deployment Guide

## Server Information
- **Server IP:** 68.183.92.148
- **Domain:** szglobalarabia.com
- **Hosting:** DigitalOcean Droplet
- **GitHub:** https://github.com/AbdurrabKhan198/szglobal

---

## 🚀 Quick Start

### First-Time Setup (Run Once)
```
Double-click: SETUP_SERVER_FIRST.bat
```

### Deploy Updates (Anytime)
```
Double-click: DEPLOY_ONE_CLICK.bat
```

That's it! One click to deploy! 🎉

---

## 📁 Files Overview

| File | Purpose |
|------|---------|
| `DEPLOY_ONE_CLICK.bat` | **⭐ Main deployment - commits, pushes to GitHub, deploys to server** |
| `SETUP_SERVER_FIRST.bat` | First-time server setup (clones from GitHub) |
| `deploy.bat` | Local development with full setup |
| `start_local.bat` | Quick local development start |

---

## 🔄 How One-Click Deploy Works

When you run `DEPLOY_ONE_CLICK.bat`, it:

1. ✅ Builds Tailwind CSS (if configured)
2. ✅ Adds all changes to Git
3. ✅ Commits with your message (or auto-generated)
4. ✅ Pushes to GitHub (`main` or `master` branch)
5. ✅ SSHs into server and runs `git pull`
6. ✅ Installs dependencies, collects static files, runs migrations
7. ✅ Restarts Gunicorn and Nginx

---

## 🔧 First-Time Server Setup Details

When you run `SETUP_SERVER_FIRST.bat`, it:

1. Updates the server's system packages
2. Installs Python, Nginx, Git, UFW
3. Configures the firewall
4. **Clones your repo from GitHub**
5. Creates Python virtual environment
6. Installs all dependencies
7. Configures Nginx with your domain
8. Sets up systemd service for auto-restart
9. Runs initial migrations and collects static files
10. Starts the website!

---

## 🔐 Setting Up SSL (HTTPS) - Recommended!

After deployment, SSH into your server:

```bash
ssh root@68.183.92.148
apt install certbot python3-certbot-nginx
certbot --nginx -d szglobalarabia.com -d www.szglobalarabia.com
```

---

## 🌐 DNS Configuration

Point your domain to the server (in your domain registrar):

| Type | Name | Value |
|------|------|-------|
| A | @ | 68.183.92.148 |
| A | www | 68.183.92.148 |

---

## 🔧 Manual Server Commands

### SSH into Server
```bash
ssh root@68.183.92.148
```

### Check Service Status
```bash
systemctl status szglobal
systemctl status nginx
```

### View Logs
```bash
# Gunicorn logs
tail -f /var/log/gunicorn/szglobal_error.log

# Nginx logs
tail -f /var/log/nginx/error.log
```

### Manual Deploy on Server
```bash
cd /var/www/szglobal
git pull origin main
source venv/bin/activate
DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py collectstatic --noinput
DJANGO_SETTINGS_MODULE=szglobal.settings_production python manage.py migrate --noinput
systemctl restart szglobal
```

### Restart Services
```bash
systemctl restart szglobal
systemctl restart nginx
```

---

## 📞 Quick Reference

| What you want to do | What to do |
|---------------------|------------|
| **Deploy website** | Double-click `DEPLOY_ONE_CLICK.bat` |
| **First-time setup** | Double-click `SETUP_SERVER_FIRST.bat` |
| **Local development** | Double-click `deploy.bat` |
| **SSH to server** | `ssh root@68.183.92.148` |
| **Check if site is up** | Visit http://szglobalarabia.com |

---

## ⚠️ Important Notes

1. Make sure you have SSH access to `root@68.183.92.148`
2. Your Git should be configured to push to GitHub
3. The server pulls from the `main` branch (or `master` if main doesn't exist)
4. Always commit your changes before deploying!
