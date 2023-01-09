INSERT INTO seccion (nombre) VALUES ('nombres_apellidos'); ==> BUSCAR NOMBRES/APELLIDOS COMUNES
INSERT INTO seccion (nombre) VALUES ('nacionalidad_sexo'); 
INSERT INTO seccion (nombre) VALUES ('fechas_ndocumento');
INSERT INTO seccion (nombre) VALUES ('profesion'); ==> BUSCAR MÁS PROFESIONES
INSERT INTO seccion (nombre) VALUES ('ciudad_natal'); ==> BUSCAR MÁS COMUNAS



INSERT INTO palabracorr (palabra, seccion) VALUES ('APELLIDOS', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('NOMBRES', 'nombres_apellidos');

INSERT INTO palabracorr (palabra, seccion) VALUES ('M', 'nacionalidad_sexo');
INSERT INTO palabracorr (palabra, seccion) VALUES ('F', 'nacionalidad_sexo');
INSERT INTO palabracorr (palabra, seccion) VALUES ('CHILENA', 'nacionalidad_sexo');

INSERT INTO palabracorr (palabra, seccion) VALUES ('Nació', 'reverso_top');
INSERT INTO palabracorr (palabra, seccion) VALUES ('en:', 'reverso_top');
INSERT INTO palabracorr (palabra, seccion) VALUES ('Profesión:', 'reverso_top');

INSERT INTO palabracorr (palabra, seccion) VALUES ('CÉDULA', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('DE', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('IDENTIDAD', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('RUN', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('REPÚBLICA', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('CHILE', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('SERVICIO', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('REGISTRO', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('CIVIL', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('E', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('IDENTIFICACIÓN', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('FIRMA', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('DEL', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('TITULAR', 'otras_secciones');

INSERT INTO palabracorr (palabra, seccion) VALUES ('ENE', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('FEB', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('MAR', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('ABR', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('MAY', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('JUN', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('JUL', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('AGO', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('SEPT', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('OCT', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('NOV', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('DIC', 'fechas_ndocumento');

INSERT INTO palabracorr (palabra, seccion) VALUES ('EMILIO', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('VERNE', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('ROJAS', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('VELIZ', 'nombres_apellidos');