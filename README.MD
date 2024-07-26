## Django101
Aprendiendo Django

### Lecturas importantes
- [Django](https://www.djangoproject.com/).

# Ejecutar comandos de la documentación de Django
```bash
django-admin --help
```

#iniciar poryecto el crea carpeta pasos
1 django-admin statproject my_first_project 
2 py manage.py startapp my_first_app


Ejecutar el servidor
cd my_first_project
py manage.py runserver


Django ORM permite manejar cualquier base de datos
Para la base de datos, migrar tablas implicitas de Django q sirven para los proyectos:
py manage.py migrate

toma de models 
py manage.py makemigrations

donde creo la tabla? 
ejecutar ./manage.py dbshell
sql .tables


py manage.py shell