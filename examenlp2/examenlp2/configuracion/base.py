#! coding: utf-8
from os.path import abspath, basename, dirname, join, normpath
from sys import path

###  RUTA DE CONFIGURACION ######

#La ruta del sistema de ficheros para el directorio del proyecto Django

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# La ruta del sistema de ficheros para la carpeta del proyecto de nivel superior

SITE_ROOT = dirname(DJANGO_ROOT)

# Nombre sitio:

SITE_NAME = basename(DJANGO_ROOT)

# Añadir nuestro proyecto a nuestro ruta de python, así que no necesitamos escribir
# nuestro proyecto

path.append(DJANGO_ROOT)

### FIN DE LA RUTA DE CONFIGURACION ####

#### CONFIGURACION DEL DEBUG(depurar) ###

#Lo que hace DEBUG es encontrar  los errores de visualizacion
#de la pagina

DEBUG = False

#El TEMPLATE_DEBUG es un valor booleano que activa/desactiva el modo debug plantilla

TEMPLATE_DEBUG = DEBUG
########## FIN DE LA CONFIGURACION DEL DEBUG ###

###  CONFIGURACION DEL ADMINISTRADOR ####

#El ADMINS es una tupla que enumera las personas que se hacen las notificaciones error de código.
ADMINS = (
('Your Name', 'dante_cunurana@upeu.edu.pe'),
)
#Los MANAGERS son UNA tupla con el mismo formato que LOS ADMINISTRADORES
#    que especifica que deben recibir las notificaciones
#    cuando enlace roto BrokenLinkEmailsMiddleware está activada.

MANAGERS = ADMINS

### FIN DE CONFIGURACION DEL ADMINISTRADOR

### CONFIGURACION DE LA BASE DE DATOS

#El DATABASE se usa para determinar que base de datos vas a utilizar en tus consultas
DATABASE = {
    'default':{
        'ENGINE': 'django.db.backends',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

### FIN DE LA CONFIGURACION DE LA BASE DE DATOS

### CONFIGURACION GENERAL

# El TIME_ZONE es para representar la zona horaria, no especificamente del
# servidor

TIME_ZONE = 'America/Lima'

# EL LANGUAJE_CODE es para determinar el idioma de la BASE DE DATOS
LANGUAJE_CODE = 'es-PE'

# El USE_I18N es un valor booleano que especifica si debe activarse el sistema
# de traducción de Django
USE_I18N = True

#El USE_L10N es un valor booleano que especifica si formateo de datos
#localizados se habilita por defecto o no
USE_L10N = True

# El USE_TZ es un valor booleano que especifica si fechas será consciente de
# zona horaria predeterminada o no.
USE_TZ = True

### FIN DE LA CONFIGURACION GENERAL

#### CONFIGURACION DE MEDIA

#El MEDIA_ROOT es la ruta del sistema de ficheros en el
#directorio que contiene archivos cargados por el usuario.

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

#El MEDIA_URL es la Dirección URL que maneja los medios MEDIOS de raíz,
#que se utiliza para gestionar archivos almacenados
MEDIA_URL = '/media/'

###FIN DE LA CONFIGURACION DE MEDIA

### CONFIGURACION DE LOS ARCHIVOS ESTATICOS

#El STATIC_ROOT es la ruta absoluta al directorio donde
#recogerá collectstatic archivos estáticos para el despliegue.
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

#El STATIC_URL es la Dirección URL que se va a utilizar cuando
#se hace referencia a los archivos estáticos ubicados en RAÍZ ESTÁTICA.
STATIC_URL = '/static/'

# EL STATICFILES_DIRS, este parametro define las ubicaciones adicionales de que
# la aplicación staticfiles atravesarás si está habilitado el finder
# FileSystemFinder
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# El STATICFILES_FINDERS encuentra archivos estaticos en varios lugares
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## FIN DE CONFIGURACION DE LOS ARCHIVOS ESTATICOS

########## CONFIGURACION DE LA CLAVE SECRETA

#EL SECRET_KEY es una clave secreta unica que proporciona la firma criptografica
# y debe estar configurado en un valor único impredecible.
SECRET_KEY = r"j-eos9zup5n!fl!rlsqk(6w$-#nt_)262d%tq5z9f*dv(--44t"

########## FIN DE LA CONFIGURACION DE LA CLAVE SECRETA

########## CONFIGURACION DE SITIO

# El ALLOWED_HOSTS es una lista de cadenas que representan los nombres de
# servidor
# o dominio que puede servir a este sitio de Django.
ALLOWED_HOSTS = []

##########  FIN DE CONFIGURACION DE SITIO

### CONFIGURACION DEL TEMPLATE O PLANTILLA

# EL TEMPLATE_DIRS es la lista de ubicaciones de archivos de codigo fuente de
# origen plantilla
TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)
########## FIN DE CONFIGURACION DE PLANTILLA

########## CONFIGURACION DEL MIDDLEWARE

MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## FIN DE CONFIGURACION DE MIDDLEWARE

########## CONFIGURACION DEL URL
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## FIN DE CONFIGURACION DEL URL

########## CONFIGURACION DE APLICACIONES

#En DJANGO_APPS estan todas la aplicaciones propias de django
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    # 'django.contrib.humanize',
    # Admin panel and documentation:
    'grappelli',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)
# En LOCAL_APPS se pondran todas las aplicaciones creadas por el usuario.
LOCAL_APPS = (
)

#Una tupla de cadenas que designa a todas las aplicaciones que están
#habilitadas en esta instalación de Django.
#Cada cuerda debe ser un camino punteado de Python para:
#     una clase de configuración de aplicación, o
#     un paquete que contiene una aplicación.
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
########## FIN DE CONFIGURACION DE APLICACIONES

########## CONFIGURACION DE LOGGING


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## FIN DE CONFIGURACION DE LOGGING

######## CONFIGURACION DE WSGI
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
########## FIN DE CONFIGURACION DE WSGI

########## SOUTH CONFIGURATION
INSTALLED_APPS += (
    # Database migration helpers:
    #'south',    #En la version de Django 1.7 south ya viene instalado
)
#SOUTH_TESTS_MIGRATE = False
########## FIN DE CONFIGURACION DEL SOUTH
