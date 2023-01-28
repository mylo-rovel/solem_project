# -*- coding: utf-8 -*-
import difflib      # built-in library
import Levenshtein  # pip install python-Levenshtein
import psycopg2     # pip install psycopg2-binary
from dotenv import dotenv_values # pip install python-dotenv


class StringProcessor():
    __venv_dict = {}
    __cursor = None
    # MODIFICAR ESTO PARA MODIFICAR LA SENSIBILIDAD DE Levenshtein
    __minAcceptableDistance = 3

    def __init__(self):
        self.__venv_dict = dict(dotenv_values(".env"))

# -------------------------------------------------------------------------------------
# -------------------- SETUP ----------------------------------------------------------
    def __connectToDB(self):
        try:
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
            return True

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
    
    def __closeConnToDB(self):
        try:
            self.__cursor.close()
            return True

        except (Exception) as error:
            return False
# -------------------- SETUP ----------------------------------------------------------
# -------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------
# -------------- RETRIEVING FROM DB AND WORKING WITH INPUT DATA -----------------------

# ------------------- GETTING MOST SIMILAR WORD TO INPUT WORD -------------------------
    def __getDataListFromSQLQuery(self,sqlQuery):
        connectionSuccess = self.__connectToDB()
        if (not connectionSuccess):
            print("CONEXIÓN FALLIDA CON LA BASE DE DATOS")
            return []

        # Esto funciona preparando la query. EJEMPLO:
        #   (self.__cursor.execute(sqlQuery)) ==> (OJO: SÓLO LA PREPARA. NO LA EJECUTA)
        #
        # y obteniendo los resultados. EJEMPLO:
        #   (OJO: AHORA SE EJECUTA LA QUERY)
        #   (self.__cursor.fetchmany(cantFilas) ó self.__cursor.fetchall()) (ambas sirven)
        self.__cursor.execute(sqlQuery)
        wordsFromDB = self.__cursor.fetchall()

        # Close the connection => not needed anymore for now
        self.__closeConnToDB()
        return wordsFromDB
    
    def getValidWordsList(self, seccionRevisar):
        sqlQuery = f"SELECT * FROM palabracorr WHERE seccion = '{seccionRevisar}'"
        wordsFromDB = self.__getDataListFromSQLQuery(sqlQuery)
        if (len(wordsFromDB) < 1): return []

        validWordsList = [palabraBuena for id,palabraBuena,seccion in wordsFromDB]
        return validWordsList



    # USANDO LA BIBLIOTECA(built-in) difflib
    def _innerGetSimilarWord_OLD_IMPLEMENTATION(self, wordToCheck, validWordsList):
        similarWordsArr = difflib.get_close_matches(wordToCheck, validWordsList)
        print('\n\n\n\n')
        print('difflib - sandias con manjar  --------------------------------------------','\n')
        print(f'wordToCheck: {wordToCheck}')
        print(f'mejores palabras guardadas: {similarWordsArr}')

        bestMatch = similarWordsArr[0] if (len(similarWordsArr) > 0) else wordToCheck                
        print(f"El mejor match encontrado fue {bestMatch}")
        return bestMatch

    def getSimilarWord_OLD_IMPLEMENTATION(self, wordToCheck, seccionRevisar):
        # This implementation use the built-in difflib library
        # Which is not as good as the Levenshtein one
        validWordsList = self.getValidWordsList(seccionRevisar)
        if (len(validWordsList) < 1): return wordToCheck
        return self._innerGetSimilarWord_OLD_IMPLEMENTATION(wordToCheck, validWordsList)

    
    


    # USANDO LA BIBLIOTECA Levenshtein
    def _innerGetSimilarWordLevenshtein(self, wordToCheck, validWordsList):
        similarWordsArr = sorted((Levenshtein.distance(wordToCheck, validWord), validWord) for validWord in validWordsList)
        print('\n\n\n\n')
        print('Levenshtein - tomates con azucar ---------------------------------------------','\n')
        print(f'wordToCheck: {wordToCheck}')
        print(f'mejores palabras guardadas: {similarWordsArr}')
        
        if (not similarWordsArr) or (similarWordsArr[0][0] > self.__minAcceptableDistance): 
            print(f"\nNo queda otra que usar {wordToCheck}")
            # raise ValueError('List of words is empty.')
            return wordToCheck

        print(f"El mejor match encontrado fue {similarWordsArr[0][1]}")
        return similarWordsArr[0][1]

    def getSimilarWord(self, wordToCheck, seccionRevisar):
        # This implementation use the Levenshtein library        
        validWordsList = self.getValidWordsList(seccionRevisar)
        if (len(validWordsList) < 1): return wordToCheck
        return self._innerGetSimilarWordLevenshtein(wordToCheck, validWordsList)





    # ? CON ESTO, QUEREMOS USAR TODAS LAS PALABRAS DE LA BASE DE DATOS
    def getSimilarWord_USING_ALL_WORDS(self, wordToCheck, allWordsList):
        if (len(allWordsList) < 1): return wordToCheck
        return self._innerGetSimilarWordLevenshtein(wordToCheck, allWordsList)

# ------------------- GETTING DB DATA TO DISPLAY --------------------------------------
    def getDBSectionsList(self):
        sqlQuery = "SELECT * FROM seccion"
        wordsFromDB = self.__getDataListFromSQLQuery(sqlQuery)
        return [word for (index, word) in wordsFromDB]


# ---------------------- GETTING ALL THE WORDS FROM THE DB -----------------------------
    def getAllDBWords(self):
        allSectionsArr = self.getDBSectionsList()
        allWordsList = []
        for seccion in allSectionsArr:
            sectionWords = self.getValidWordsList(seccion)
            allWordsList = allWordsList + sectionWords
        return allWordsList