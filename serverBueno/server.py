from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
# THIS IS NEEDED TO IMPORT "ImageProcessor" WHICH IS STORED IN ANOTHER DIRECTORY
sys.path.append('./cvf')
# from ImageProcessor import getTextFromSampleImage, getTextFromImageBytes
from ImageProcessor import ImageProcessor
from StringProcessor import StringProcessor

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

stringProcessor = StringProcessor()
# TESTING THE STRING SIMILARITY MATCHER
# sectionToUse = "otras_secciones"
# processedPhraseList = []
# # todo: agregar palabras como "chilena" "chileno"
# for originalWord in "Mi cédula de íd3ntidad n0 es chil3na".split(" "):
#     correctedWord = stringProcessor.getSimilarWord(originalWord.lower(), sectionToUse)
#     processedPhraseList.append(correctedWord)
# print('\n\n', " ".join(processedPhraseList))


@app.route("/", methods=['GET'])
@cross_origin()
def httpGetTextFromSampleImage():    
    return ImageProcessor.getTextFromSampleImage()

@app.route("/images", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImage():
    if (request.files and request.form['section']):
        print("section requested", request.form['section'])
        
        sectionToGet = request.form['section']
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        detectedWords = ImageProcessor.getTextFromImageBytes(imgBytes)
        
        storedSections = stringProcessor.getDBSectionsList()
        if (sectionToGet in storedSections):
            for (index,word) in enumerate(detectedWords):
                correctedWord = stringProcessor.getSimilarWord(word, sectionToGet)
                detectedWords[index] = correctedWord
        
        return detectedWords
    else:
        return ["Por favor, envía una imagen"]


@app.route("/custom_phrases", methods=['POST'])
@cross_origin()
def httpFixCustomPhrase():
    if (request.form['custom_phrase'] and request.form['section']):
        print("phrase sended", request.form['custom_phrase'])
        print("section requested", request.form['section'])
        
        sectionToGet = request.form['section']
        wordsToFix = request.form['custom_phrase'].split(" ")
        
        storedSections = stringProcessor.getDBSectionsList()
        if (sectionToGet in storedSections):
            for (index,word) in enumerate(wordsToFix):
                correctedWord = stringProcessor.getSimilarWord(word, sectionToGet)
                wordsToFix[index] = correctedWord
        
        return wordsToFix
    else:
        return ["Por favor, envía una frase separada por espacios"]


@app.route("/custom_phrases/all_words", methods=['POST'])
@cross_origin()
def httpFixCustomPhraseUsingAllWords():
    if (request.form['custom_phrase'] ):
        print("phrase sended", request.form['custom_phrase'])
        wordsToFix = request.form['custom_phrase'].split(" ")
        
        allWordsList = stringProcessor.getAllDBWords()

        for (index,word) in enumerate(wordsToFix):
            wordsToFix[index] = stringProcessor.getSimilarWord_USING_ALL_WORDS(word, allWordsList)
        
        return wordsToFix
    else:
        return ["Por favor, envía una frase separada por espacios"]



@app.route("/sections", methods=['GET'])
@cross_origin()
def httpGetDBSectionsList():
    return stringProcessor.getDBSectionsList()

    
@app.route("/sections/valid_words", methods=['POST'])
@cross_origin()
def httpGetDBSectionValidWords():
    if (request.form['section']):
        sectionToGet = request.form['section']
        storedSections = stringProcessor.getDBSectionsList()
        if (sectionToGet in storedSections):
            return stringProcessor.getValidWordsList(sectionToGet)
        else:
            return []


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
