#!/usr/bin/env python3
"""
SZ Global Arabia - Deployment Webhook Server
==============================================
This creates a simple webhook endpoint that triggers deployment
when you visit the URL in your browser.

Access: http://68.183.92.148:9000/deploy
Secret Access: http://68.183.92.148:9000/deploy?key=szglobal2024

Setup on server:
    pip install flask
    python3 deploy_webhook.py &
    
Or run with systemd (see deployment/webhook.service)
"""

from flask import Flask, request, jsonify
import subprocess
import os
import logging
from datetime import datetime

app = Flask(__name__)

# Configuration
DEPLOY_KEY = "szglobal2024"  # Change this to your own secret key!
PROJECT_PATH = "/var/www/szglobal"
LOG_FILE = "/var/www/szglobal/logs/deploy_webhook.log"

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_deployment():
    """Run the deployment steps"""
    results = []
    
    try:
        # Step 1: Git pull
        logging.info("Starting deployment...")
        results.append("🔄 Starting deployment...")
        
        os.chdir(PROJECT_PATH)
        
        # Pull latest code
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            capture_output=True, text=True, timeout=60
        )
        results.append(f"📥 Git Pull: {result.stdout.strip() or result.stderr.strip()}")
        logging.info(f"Git pull: {result.stdout}")
        
        # Activate venv and install requirements
        result = subprocess.run(
            [f"{PROJECT_PATH}/venv/bin/pip", "install", "-r", "requirements.txt"],
            capture_output=True, text=True, timeout=120
        )
        results.append(f"📦 Dependencies: Updated")
        logging.info("Dependencies installed")
        
        # Collect static files
        env = os.environ.copy()
        env["DJANGO_SETTINGS_MODULE"] = "szglobal.settings_production"
        
        result = subprocess.run(
            [f"{PROJECT_PATH}/venv/bin/python", "manage.py", "collectstatic", "--noinput"],
            capture_output=True, text=True, timeout=60, env=env
        )
        results.append(f"📁 Static Files: Collected")
        logging.info("Static files collected")
        
        # Run migrations
        result = subprocess.run(
            [f"{PROJECT_PATH}/venv/bin/python", "manage.py", "migrate", "--noinput"],
            capture_output=True, text=True, timeout=60, env=env
        )
        results.append(f"🗄️ Migrations: Applied")
        logging.info("Migrations applied")
        
        # Restart services
        subprocess.run(["systemctl", "restart", "szglobal"], timeout=30)
        subprocess.run(["systemctl", "restart", "nginx"], timeout=30)
        results.append(f"🔄 Services: Restarted")
        logging.info("Services restarted")
        
        results.append(f"✅ Deployment Complete! {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logging.info("Deployment completed successfully")
        
        return True, results
        
    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        results.append(error_msg)
        logging.error(error_msg)
        return False, results


@app.route('/')
def home():
    """Home page with instructions"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SZ Global Arabia - Deploy</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #1a1a2e; color: #eee; }
            h1 { color: #00d9ff; }
            .btn { display: inline-block; padding: 15px 30px; background: #00d9ff; color: #1a1a2e; text-decoration: none; border-radius: 5px; font-weight: bold; margin: 10px 0; }
            .btn:hover { background: #00b8d4; }
            code { background: #16213e; padding: 2px 8px; border-radius: 3px; }
            .warning { background: #ff9800; color: #000; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>🚀 SZ Global Arabia - Deployment</h1>
        <p>Click the button below to deploy the latest code from GitHub:</p>
        <a class="btn" href="/deploy?key=szglobal2024">🔄 Deploy Now</a>
        <br><br>
        <p class="warning">⚠️ Make sure you've pushed your changes to GitHub first!</p>
        <hr>
        <h3>How it works:</h3>
        <ol>
            <li>Push your code to GitHub</li>
            <li>Click "Deploy Now" or visit <code>/deploy?key=szglobal2024</code></li>
            <li>Wait for deployment to complete</li>
            <li>Your site is updated!</li>
        </ol>
    </body>
    </html>
    """
    return html


@app.route('/deploy')
def deploy():
    """Trigger deployment"""
    # Check secret key
    key = request.args.get('key', '')
    if key != DEPLOY_KEY:
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Access Denied</title>
        <style>body{font-family:Arial;max-width:600px;margin:50px auto;padding:20px;background:#1a1a2e;color:#eee;}</style>
        </head>
        <body>
            <h1>🔒 Access Denied</h1>
            <p>Invalid or missing deploy key.</p>
            <p>Use: <code>/deploy?key=YOUR_SECRET_KEY</code></p>
        </body>
        </html>
        """, 403
    
    # Run deployment
    success, results = run_deployment()
    
    # Build response HTML
    results_html = "<br>".join(results)
    status = "✅ Success!" if success else "❌ Failed"
    color = "#00ff88" if success else "#ff4444"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deploy - {status}</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background: #1a1a2e; color: #eee; }}
            h1 {{ color: {color}; }}
            .results {{ background: #16213e; padding: 20px; border-radius: 10px; line-height: 2; }}
            a {{ color: #00d9ff; }}
        </style>
    </head>
    <body>
        <h1>{status}</h1>
        <div class="results">
            {results_html}
        </div>
        <br>
        <p><a href="http://szglobalarabia.com" target="_blank">🌐 View Website</a> | <a href="/">🏠 Back</a></p>
    </body>
    </html>
    """
    return html


@app.route('/status')
def status():
    """Check service status"""
    try:
        gunicorn = subprocess.run(["systemctl", "is-active", "szglobal"], capture_output=True, text=True)
        nginx = subprocess.run(["systemctl", "is-active", "nginx"], capture_output=True, text=True)
        
        return jsonify({
            "gunicorn": gunicorn.stdout.strip(),
            "nginx": nginx.stdout.strip(),
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Create logs directory if not exists
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    print("=" * 50)
    print("SZ Global Arabia - Deployment Webhook Server")
    print("=" * 50)
    print(f"Deploy URL: http://68.183.92.148:9000/deploy?key={DEPLOY_KEY}")
    print("=" * 50)
    
    # Run on port 9000
    app.run(host='0.0.0.0', port=9000, debug=False)
