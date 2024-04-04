# SECURITY WARNING: keep the secret key used in production secret!
from core.project.settings import ENV, DEBUG

SECRET_KEY = ENV.config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG

ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', cast=ENV.Csv())
