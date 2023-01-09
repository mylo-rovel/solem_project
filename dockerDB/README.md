PARA CORRER EL BACKEND TAL CUAL ESTÁ ES NECESARIO TENER UNA BASE DE DATOS MYSQL CORRIENDO
PARA SOLUCIONAR LA FALTA DE BASE DE DATOS SEGUIR LOS SIGUIENTES PASOS:

1. Abrir una terminal que apunte a este directorio (/home/satita/Desktop/sataDockerDB)


2. 👉️Si es primera vez que se hace todo esto, ejecutar:
	
	sudo docker-compose up --build --detach
	
   👉️Si ya se ha ejecutado el comando anterior en previas ocasiones (por lo tanto, ya se ha 
   hecho el build de la imagen), el comando a ejecutar sería el siguiente:
   	
   	sudo docker-compose up --detach
   	
   (NOTAR QUE NO ES NECESARIO CONSTRUIR LA IMAGEN)
   (--detach es para dejar el proceso en background, así no termina si salimos de la consola)

3. Ejecutar esto para corroborar que todo salió bien y que tenemos el contenedor corriendo:
	
	sudo docker ps
	
---------------------------------------------------------------------------------------------

	
NOTA: ES IMPERATIVO UTILIZAR LA keyword "sudo" PARA EJECUTAR COMANDOS DE DOCKER


---------------------------------------------------------------------------------------------


💾️ Si se busca llenar la base de datos de forma previa (dummy datos y tablas), hacer:
1. En una terminal ejecutar:
	sudo docker-compose exec mysql mysql -u root satadb
				  (1)           (2)    (3)
En donde
(1): Es el nombre del servicio(el que está en docker-compose.yml) que corre el contenedor de docker.
(2): Es el nombre de usuario usado en el servicio anteriormente mencionado (corresponde a MYSQL_USER=${MYSQL_USER} => MYSQL_USER=root  [archivo .env]).
(3): Es el nombre de la base de datos usada en el servicio anteriormente mencionado (corresponde a MYSQL_DATABASE=${MYSQL_DATABASE} => MYSQL_DATABASE=satadb  [archivo .env]).

CABE DESTACAR QUE NO INGRESAMOS CONTRASEÑA DADO QUE EN EL SERVICIO mysql DEL ARCHIVO docker-compose.yml le dimos el valor true a MYSQL_ALLOW_EMPTY_PASSWORD (MYSQL_ALLOW_EMPTY_PASSWORD=${MYSQL_ALLOW_EMPTY_PASSWORD} => MYSQL_ALLOW_EMPTY_PASSWORD=true  [archivo .env]).


2. Abrir el archivo:
	/home/satita/Desktop/sataDockerDB/mysql_docker/tables/db_tables.sql

3. Copiar el contenido todo el contenido del archivo anterior y pegarlo en la terminal con el cliente mysql abierto del paso 1. (naturalmente apretar Enter para ingresar las queries).

4. Para chequear si todo salió bien, ingresar el siguiente comando en el cliente mysql:
	SHOW TABLES;
Esto debería mostrar una lista de tablas confirmando el éxito del proceso.
