import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)

#If nothing is captured
if not cap.isOpened():
    print("Cannot open camera \n")
    print("Please Try again! ")
    exit()

#While  capture is read 
while True:
    ret,frame = cap.read()
    #if frame is not read correctly ret is False
    if not ret:
        print("Error, cannot capture frame")
        break
    #else frame has been read correctly ret is True
    #Display the frame
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Sudoku Solver', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


    