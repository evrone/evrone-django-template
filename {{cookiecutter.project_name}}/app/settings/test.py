from settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'

SECRET_KEY = "test-a-valid-secret-key"  # noqa: S105

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

