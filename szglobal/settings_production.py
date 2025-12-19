"""
Production settings for szglobal project on DigitalOcean.
Server IP: 68.183.92.148
Domain: szglobalarabia.com
"""

from .settings import *
import os

# SECURITY: Override these in production
DEBUG = False

# Generate a new secret key for production and store in environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-production-secret-key-here-change-this!')

# Allowed hosts for production
ALLOWED_HOSTS = [
    '68.183.92.148',
    'szglobalarabia.com',
    'www.szglobalarabia.com',
]

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://szglobalarabia.com',
    'https://www.szglobalarabia.com',
    'http://68.183.92.148',
    'https://68.183.92.148',
]

# Security settings for production
SECURE_SSL_REDIRECT = False  # Set to True once SSL is configured
SESSION_COOKIE_SECURE = False  # Set to True once SSL is configured
CSRF_COOKIE_SECURE = False  # Set to True once SSL is configured
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# WhiteNoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django_error.log',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
