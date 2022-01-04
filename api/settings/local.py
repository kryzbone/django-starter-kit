from .base import *  # noqa
from .base import env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="V6rtCTpJyVVQPJ9KQVlMNzE0nWO7bndVDSPgUfeKYS2ge5aCQ1LZhrPPiYKwweDJ",
)
