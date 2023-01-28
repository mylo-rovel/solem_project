PARA CORRER EL BACKEND TAL CUAL ESTÁ ES NECESARIO TENER UNA BASE DE DATOS POSTGRES CORRIENDO
PARA SOLUCIONAR LA FALTA DE BASE DE DATOS SEGUIR LOS SIGUIENTES PASOS:

1. Abrir una terminal que apunte a este directorio

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
	sudo docker-compose exec postgres psql -U solem solemDb
				  (1)           (2)    (3)
En donde
(1): Es el nombre del servicio(el que está en docker-compose.yml) que corre el contenedor de docker.
(2): Es el nombre de usuario usado en el servicio anteriormente mencionado (corresponde a POSTGRES_USER: ${POSTGRES_USER} => POSTGRES_USER=solem  [archivo .env]).
(3): Es el nombre de la base de datos usada en el servicio anteriormente mencionado (corresponde a POSTGRES_DB: ${POSTGRES_DB}=> POSTGRES_DB=solemDb  [archivo .env]).

2. Para chequear si todo salió bien, ingresar el siguiente comando en el cliente postgres (luego de ejecutar "sudo docker-compose exec postgres psql -U solem solemDb"):
\d
Esto debería retornar algo similar a esto:
	solemDb=# \d
				List of relations
	Schema |        Name        |   Type   | Owner 
	--------+--------------------+----------+-------
	public | palabracorr        | table    | solem
	public | palabracorr_id_seq | sequence | solem
	public | seccion            | table    | solem
	public | seccion_id_seq     | sequence | solem
	(4 rows)
