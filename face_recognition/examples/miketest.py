import cv2 as cv
import numpy as np
import sys

print("opening camera")

cap = cv.VideoCapture(0)

print("done")

while True:
    cap.set(cv.CAP_PROP_FRAME_WIDTH,640);
    cap.set(cv.CAP_PROP_FRAME_HEIGHT,480);
    ret, frame = cap.read()
    print(ret)

    if(frame is None):
        print("Received empty frame. Exiting")
        sys.exit()

    cv.imshow('frame', frame)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()