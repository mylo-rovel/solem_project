# -*- coding: utf-8 -*-
import difflib
import psycopg2     # pip install psycopg2-binary
from dotenv import dotenv_values

class StringProcessor():
    __venv_dict = {}
    __dbAvailable = False
    __cursor = None

    def __init__(self):
        self.__venv_dict = dict(dotenv_values(".env"))
        try:
            self.__connectToDB()
        except:
            print("Base de datos no disponible para usar")

    def __connectToDB(self):
        dbName = self.__venv_dict["POSTGRES_DB"]
        dbHost = self.__venv_dict["POSTGRES_HOST"]
        dbUser = self.__venv_dict["POSTGRES_USER"]
        dbPassW = self.__venv_dict["POSTGRES_PASSWORD"]
        dbPort = self.__venv_dict["POSTGRES_PORT"]

        conn = psycopg2.connect(
            database=dbName,
            host=dbHost,
            user=dbUser,
            password=dbPassW,
            port=dbPort
        )
        self.__cursor = conn.cursor()
        self.__dbAvailable = True

    def getSimilarWords(self, wordToCheck, seccionRevisar):
        if (not self.__dbAvailable): return "ERROR CON PALABRAS BUENAS"

        # Esto funciona preparando la query (self.__cursor.execute(sqlQuery)) SÓLO LA PREPARA
        # y obteniendo los resultados (self.__cursor.fetchmany() / self.__cursor.fetchall())
        sqlQuery = f"SELECT * FROM palabracorr WHERE seccion = '{seccionRevisar}'";
        self.__cursor.execute(sqlQuery)
        fetchedPalabras = self.__cursor.fetchall()
        
        if (not ((len(fetchedPalabras) > 0))): 
            print("\n\nno existe la seccion entregada")
            return "no existe la seccion entregada"
        else:
            print(fetchedPalabras)

        validWordsOptions = [palabraBuena for id,palabraBuena,seccion in fetchedPalabras]
        closestMatchsArr = difflib.get_close_matches(wordToCheck, validWordsOptions)
        bestMatch = closestMatchsArr[0] if (len(closestMatchsArr) > 0) else wordToCheck        
        print(f"\n\nEl mejor match encontrado fue {bestMatch}")
        return bestMatch