# FalconTest
Pruebas basicas con *Python* y conexión al motor de base de datos *MySQL* con *MySQLdb*, también uso básico  del ORM *SQLAlquemy*.
#### Instalar cliente para mysql
Debemos instalar pip luego la librería libmysqlclient-dev.
```
sudo apt-get install libmysqlclient-dev
```
Seguidamente ejecutamos los siguientes comandos
```
sudo easy_install -U distribute
sudo pip install mysql-python
```
#### Clonar el repositorio
```
git clone https://github.com/josu3e/alchemyTest.git
cd alchemyTest/
```
#### Entorno virtual
Para ello ejecutamos los siguientes comandos, y obtenemos un contenedor para nuestras dependencias agregadas en el archivo requirements.txt:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
#### Configuramos y testeamos
Modificamos los accesos de acuerdo en `singletonTest.py`
```
DB_HOST =  'localhost'
DB_PORT =  3307
DB_USER =  'root'
DB_PASSWORD =  'root'
DB_NAME =  'testdb'
```
Creamos una base de datos con el nombe "**testdb**". Ejecutamos el siguiente comando para realizar nuestra primera prueba con el patron "**Singleton**". Es necesario cambiar la configuracion de 
```
python singletonTest.py
```
