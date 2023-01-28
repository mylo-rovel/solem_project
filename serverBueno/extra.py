import Levenshtein

def getMostCloseWordFromList(word, lst):
  items = sorted((Levenshtein.distance(word, w), w) for w in lst)
  # Print items here for debugging.
  if not items:
    raise ValueError('List of words is empty.')
  print(items)
  return items[0][1]

lst = ['apple','app','banana store','pear','beer']
getMostCloseWordFromList('4ppl3',lst)
# getMostCloseWordFromList('banana',lst)
















""" 
# UNUSED ENDPOINTS I DIDN'T WANT TO DELETE

@app.route("/enhanced_images_v1-ERRORES-PENDIENTES", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImageEcualized_v1():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.getTextFromImageBytesEcualized_v1(imgBytes)
    else:
        return "Por favor, envía una imagen"


@app.route("/enhanced_images_v2-ERRORES-PENDIENTES", methods=['POST'])
@cross_origin()
def httpGetTextFromUploadedImageEcualized_v2():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.getTextFromImageBytesEcualized_v2(imgBytes)
    else:
        return "Por favor, envía una imagen"


@app.route("/testHist", methods=['POST'])
@cross_origin()
def httpTestHistogramEqualization():
    if (request.files):
        imagefile = request.files['imagefile']
        imgBytes = imagefile.stream.read()
        return ImageProcessor.showHistFromImgBytes(imgBytes)
    else:
        return "Por favor, envía una imagen" 

"""