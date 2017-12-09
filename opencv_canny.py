import numpy as np
import cv2

# get source webcam or video
#
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('weirdfaces.mov')

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#out = cv2.VideoWriter('output.m4v',fourcc, 30.0, (1280,720))


# https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    # return the edged image
    return edged


# COUNTING FRAME
count = 0

while(cap.isOpened()):
    # Return frame by frame
    ret, frame = cap.read()

    if ret==True:
        frame = cv2.flip(frame,0)

        # Convert grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)

        # apply Canny edge detection using a wide threshold, tight
        # threshold, and automatically determined threshold
        #wide = cv2.Canny(blurred, 10, 200)
        #tight = cv2.Canny(blurred, 225, 250)
        #auto = auto_canny(blurred)

        #auto = auto_canny(blurred, sigma=0.69)

        auto = cv2.Canny(blurred, 10, 50)

        # WRITE JPEG
        cv2.imwrite("frame%04d.jpg" % count, auto)     # save frame as JPEG file
        count += 1

        #edges = cv2.Canny(gray, 10, 250)
        #edges = cv2.Canny(gray,lower,upper)

        # write the flipped frame
        #out.write(frame)

        #out.write(edges)

        #cv2.imshow('frame',edges)
        cv2.imshow('blur', auto)

        #cv2.imshow("Edges", np.hstack([wide, tight, auto]))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


    # cv2.imshow('frame',edges)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cap.release()
#out.release()
cv2.destroyAllWindows()
