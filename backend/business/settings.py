from pathlib import Path
import os
from dotenv import load_dotenv
BASE_DIR=Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/'.env')
SECRET_KEY=os.getenv('SECRET_KEY','dev-only-change-me')
DEBUG=os.getenv('DEBUG','True').lower()=='true'
ALLOWED_HOSTS=[x.strip() for x in os.getenv('ALLOWED_HOSTS','127.0.0.1,localhost').split(',') if x.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','corsheaders','rest_framework','rest_framework.authtoken','api']
MIDDLEWARE=['corsheaders.middleware.CorsMiddleware','django.middleware.security.SecurityMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware']
ROOT_URLCONF='business.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='business.wsgi.application'
DB_NAME=os.getenv('DB_NAME',''); DB_USER=os.getenv('DB_USER',''); DB_PASSWORD=os.getenv('DB_PASSWORD',''); DB_HOST=os.getenv('DB_HOST',''); DB_PORT=os.getenv('DB_PORT','5432')
if DB_NAME and DB_USER:
    DATABASES={'default':{'ENGINE':'django.db.backends.postgresql','NAME':DB_NAME,'USER':DB_USER,'PASSWORD':DB_PASSWORD,'HOST':DB_HOST,'PORT':DB_PORT}}
else:
    DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
AUTH_PASSWORD_VALIDATORS=[]
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Kolkata'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATIC_ROOT=BASE_DIR/'staticfiles'; MEDIA_URL='media/'; MEDIA_ROOT=BASE_DIR/'media'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
CORS_ALLOWED_ORIGINS=[x.strip() for x in os.getenv('CORS_ALLOWED_ORIGINS','http://localhost:5173,http://127.0.0.1:5173').split(',') if x.strip()]
REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.SessionAuthentication','rest_framework.authentication.BasicAuthentication','rest_framework.authentication.TokenAuthentication'],'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticated']}
