
PROYECTO DJANGO EXAMEN
======================

Un proyecto plantilla para Django 1.7
--------------------------------------

Antes de usar el proyecto tienes que hacer esto:

#. Crear tu entorno de trabajo
#. Instalar Django
#. Crear el nuevo proyecto usando la plantilla de django-examen
#. Instalar las dependencias adicionales

Creación del entorno de trabajo
==============================
Se crea asi un entorno de trabajo virtual una vez instalado virtualenvwrapper::

     $ mkproject django_project

Instalación de DJANGO
=====================
Para la instalación de django es necesario que tenga instalado pip::
    
     $ sudo apt-get install python-pip
     $ pip install django==1.7

NOTA: La instalación de django se hara en su última versión sino lo pones la
version que quieres instalar.

Creacion de tu Proyecto
=======================
Para crear un nuevo proyecto Django llamado 'anime' usamos djangoforever.
Ejecute el siguiente comando::

     $ django-admin.py startproject --template=https://github.com/danterrc/djangoforever/archive/master.zip --extension=py,rst,html anime 

Instalación de Dependencias
===========================

En Desarrollo::

     $ pip install -r requirements/local.txt

Para Producción::
   
     $ pip install -r requirements.txt



