
# Image Board

## Descripcion del programa.

A fin de completar los objetivos propuestos, se desarrollo una aplicación simple que permite a un usuario registrarse, autenticarse y subir imágenes a un portal. En el pantalla principal se pueden observar todas las imágenes de los usuarios. Una vez que se esta autenticado se puede acceder a la consola del usuario donde se permite adjuntar imagenes nuevas. En otro apartado de la consola, se muestran las imagenes que tiene actualmente el usuario y se permite realizar la eliminacion y edicion de las mismas.

## Resumen de funcionalidades.

* Subir imagenes.
* Mostrar imagenes (en indice y por id).
* Actualizar imagenes.
* Eliminar imagenes.
* Autenticacion y registro.

## Tecnologias utilizadas.

Para realizar dicha herramienta se considero el uso de base de datos *mongo*. Para el backend se utilizo el framework *flask* por su sencillez, junto con la libreria *Flask-Login* para la autenticacion. Para la aplicacion de migraciones se utilizo la herramienta *pymongo-migrate*. Finalmente, para realizar pruebas se utilizo la libreria *pytest-flask*. 

## A realizar.

- [ ] Preparar la aplicacion para desplegarla en ambientes en produccion con Docker.
- [ ] Comprobar imagenes vacias en el proceso de actualizacion de imagenes.
- [ ] Automatizar la ejecucion de pymongo-migrate.
- [ ] Realizar mas pruebas (incompletas).

## Comandos para iniciarlizar el ambiente.

```
./mongodb.sh
python3 -m venv env
source env/bin/activate
pip3 install -r .requirements.txt
export FLASK_APP=project
export FLASK_DEBUG=1
flask run 
```

Fuentes utilizadas

* [Authentication with Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
* [Flask with TDD](https://github.com/mjhea0/flaskr-tdd)
