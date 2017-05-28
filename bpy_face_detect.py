import sys

cv2_path = r"/Applications/Pineapple.app/Contents/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/cv2" #it depend on your OS but just paste the path where is scipy

if not cv2_path in sys.path:
    sys.path.append(cv2_path)


import cv2

#print(cv2)

import bpy
import os

filepath = bpy.data.filepath
directory = os.path.dirname(filepath)

# Get user supplied values
imagePath = directory + "/chinesetroop_0001.jpg"
cascPath = directory + "/cascade/haarcascade_frontalface_alt2.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(1, 1),
    #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    flags = cv2.CASCADE_SCALE_IMAGE
)

print ( "Found {0} faces!".format(len(faces))  )

# Draw a rectangle around the faces
for num, (x, y, w, h) in enumerate(faces):
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(num, ":", x,y,w,h)
    
