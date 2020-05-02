# Cupos condor

## Instrucciones para compilar
- Crear un entorno virtual
```sh
virtualenv env
```
- Activar el entorno
 ```sh
 source env/bin/activate
 ```
- Instalar librerias requeridas
 ```sh
 pip install -r requerimientos.txt
 ```
- Agregar variables de entorno
```sh
nano env/bin/activate
```
- Agregar al final
~~~
export FLASK_APP="entrypoint.py"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.local"
~~~
