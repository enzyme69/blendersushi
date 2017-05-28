
import cv2
from mathutils import Vector

# Get user supplied values

#directAccess
imagePath = "/Users/jimmygunawan/Desktop/chinesetroop_{:04d}.jpg".format(Offset)

print(imagePath)

# Get image via Blender, but this does not update

#imageInBlender = bpy.data.images['ppap']
#imagePath = bpy.path.abspath(imageInBlender.filepath)

#print(imagePath)
cascPath = "/Users/jimmygunawan/Desktop/_PINEAPPLE_FILES/haarcascade_frontalface_default.xml"


#imagePath = images.load("/home/zeffii/Desktop/some_image.png", check_existing=True)

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

#print ( "Found {0} faces!".format(len(faces))  )

VectorList = []
FloatList = []


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #print(x,y,w,h)
    VectorList.append( Vector((x,y,0)) )
    FloatList.append(w)