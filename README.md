# pruebaNative

Pasos para despliegue

1. Instalar python : $ sudo apt install python3.6
2. Crear un directorio
3. Crear ambiente virtual: $ python3 -m venv myvenv
4. Acceder al ambiente virtual: $ source myvenv/bin/activate
5. Instalar archivo de requerimientos: $ pip install -r requirements.txt
6. Instalar DjangoRestFramework: $ pip install djangorestframework
7. Instalar dateUtil: $ sudo pip install python-dateutil
8. Crear migraciones: $ python manage.py makemigrations
9. Correr migraciones: $ python manage.py migrate
10. Correr Servidor: $ python manage.py runserver
