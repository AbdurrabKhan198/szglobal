"""
Gunicorn configuration file for SZ Global Arabia
Server: 68.183.92.148
Domain: szglobalarabia.com
"""

import multiprocessing

# Server socket
bind = "127.0.0.1:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests (helps prevent memory leaks)
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "/var/log/gunicorn/szglobal_access.log"
errorlog = "/var/log/gunicorn/szglobal_error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "szglobal"

# Server mechanics
daemon = False
pidfile = "/var/run/gunicorn/szglobal.pid"
user = "www-data"
group = "www-data"
tmp_upload_dir = None

# SSL (uncomment when you have SSL certificates)
# keyfile = "/etc/letsencrypt/live/szglobalarabia.com/privkey.pem"
# certfile = "/etc/letsencrypt/live/szglobalarabia.com/fullchain.pem"
