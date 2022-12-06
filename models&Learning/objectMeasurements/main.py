import cv2
import numpy as np
import utils

scale = 3
widthP, heightP = 279*scale, 216*scale
# widthP, heightP = 379*scale, 216*scale

webcam = False
path = 'fotito.jpg'

# camera object
cap = cv2.VideoCapture(0)
cap.set(10, 160)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    if webcam:
        success, img = cap.read()
    else:
        img = cv2.imread(path)

    img = cv2.resize(img, utils.getNewDim(img, 25), None, 0.5, 0.5)
    img, conts = utils.getContours(
        img, showCanny=True, minArea=50000, filter=4)
    if (len(conts) != 0):
        # getting "approx" from finalCountours.append([len(approx), area, approx, bbox, i])
        biggest = conts[0][2]
        imgWarp = utils.warpImg(img, biggest, widthP, heightP)
        imgContours2, conts2 = utils.getContours(imgWarp, minArea=2000, filter=4,
                                                 cThreshold=[50, 50], draw=True)

        if len(conts) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = utils.reorder(obj[2])
                widthCm = round(utils.findDis(
                    nPoints[0][0]//scale, nPoints[1][0]//scale)/10, 1)
                heightCm = round(utils.findDis(
                    nPoints[0][0]//scale, nPoints[2][0]//scale)/10, 1)

                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),
                                (0, 0, 0), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),
                                (0, 0, 0), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, '{}cm'.format(widthCm), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (0, 0, 0), 2)
                cv2.putText(imgContours2, '{}cm'.format(heightCm), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (0, 0, 0), 2)
        cv2.imshow('A4', imgContours2)

    # cv2.imshow('Original', img)
    cv2.waitKey(1)
