-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
-- SET time_zone = "+00:00";

-- Por si es necesario
DROP TABLE IF EXISTS Seccion;
DROP TABLE IF EXISTS PalabraCorrecta;

-- Crear tablas

CREATE TABLE Seccion (
    id      SERIAL NOT NULL,
    nombre  VARCHAR(30) NOT NULL,
    CONSTRAINT PKSeccionId PRIMARY KEY (id),
    CONSTRAINT UniqueSeccionNombre UNIQUE (nombre)
);

-- PalabraCorr: Palabra Correcta
CREATE TABLE PalabraCorr
(
    id          SERIAL NOT NULL,
    palabra     VARCHAR(30) NOT NULL,
    seccion     VARCHAR(30) NOT NULL,
    CONSTRAINT PKPalabraCorrId PRIMARY KEY (Id),
    CONSTRAINT FKPalabraCorrSeccion FOREIGN KEY (seccion) REFERENCES Seccion(nombre)
);

--------------------------------------------------------------------------------
-- INSERTING FIRST DATA

-- SECCIONES EN LA QUE SE PUEDE SUBDIVIDIR LA CÉDULA
INSERT INTO seccion (nombre) VALUES ('nombres_apellidos');
INSERT INTO seccion (nombre) VALUES ('nacionalidad_sexo');
INSERT INTO seccion (nombre) VALUES ('fechas_ndocumento');
INSERT INTO seccion (nombre) VALUES ('otras_secciones');
INSERT INTO seccion (nombre) VALUES ('reverso_top');
INSERT INTO seccion (nombre) VALUES ('profesion');
INSERT INTO seccion (nombre) VALUES ('ciudad_natal');


-- VALORES QUE SEGURAMENTE SE ENCONTRARÁN
INSERT INTO palabracorr (palabra, seccion) VALUES ('apellidos', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('nombres', 'nombres_apellidos');

-- INSERT INTO palabracorr (palabra, seccion) VALUES ('m', 'nacionalidad_sexo');
-- INSERT INTO palabracorr (palabra, seccion) VALUES ('f', 'nacionalidad_sexo');
INSERT INTO palabracorr (palabra, seccion) VALUES ('chilena', 'nacionalidad_sexo');

insert INTO palabracorr (palabra, seccion) VALUES ('nació', 'reverso_top');
INSERT INTO palabracorr (palabra, seccion) VALUES ('en:', 'reverso_top');
INSERT INTO palabracorr (palabra, seccion) VALUES ('profesión:', 'reverso_top');

INSERT INTO palabracorr (palabra, seccion) VALUES ('cédula', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('de', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('identidad', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('run', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('república', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('chile', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('servicio', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('registro', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('civil', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('identificación', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('firma', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('del', 'otras_secciones');
INSERT INTO palabracorr (palabra, seccion) VALUES ('titular', 'otras_secciones');

INSERT INTO palabracorr (palabra, seccion) VALUES ('ene', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('feb', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('mar', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('abr', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('may', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('jun', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('jul', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('ago', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('sept', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('oct', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('nov', 'fechas_ndocumento');
INSERT INTO palabracorr (palabra, seccion) VALUES ('dic', 'fechas_ndocumento');


-- VALORES PARA PROBAR
INSERT INTO palabracorr (palabra, seccion) VALUES ('emilio', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('verne', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('rojas', 'nombres_apellidos');
INSERT INTO palabracorr (palabra, seccion) VALUES ('veliz', 'nombres_apellidos');

COMMIT;
