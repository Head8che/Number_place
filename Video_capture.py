import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
apertureSize = 3
# ratio = 3
# threshold = 90

#If nothing is captured; Camera isn't present or connected 
if not cap.isOpened():
    print("Cannot open camera \n")
    print("Please Try again! ")
    exit()
    

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error, cannot capture frame")
        break

    # Our operations on the frame come here
    Sudoku = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(Sudoku,90,150,apertureSize)
    cv.imshow('Edges', edges)  
    lines = cv.HoughLines(edges,1,np.pi/180,270)

    
    if (lines is not None):
        lines = sorted(lines, key=lambda line:line[0][0])
        x = 0
        y = 0
        new_line = []
        position = []
        for line in lines:
            rho = line[0][0]
            theta = line[0][1]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            # x1 =(r * cos(theta) - 1000 * sin(theta))
            x1 = int(x0 + 1000 * (-b))
            # y1 = (r * sin(theta)+ 1000 * cos(theta))
            y1 = int(y0 + 1000 * (a))
            # x2 = (r * cos(theta)+ 1000 * sin(theta))
            x2 = int(x0 - 1000 * (-b))
            # y2 = (r * sin(theta)- 1000 * cos(theta))
            y2 = int(y0 - 1000 * (a))
            
            #Angle checking > 45 == Veritcal Line
            if(b > 0.45):
                if(rho - x > 5):
                    #Horizontal position update 
                    x = rho
                    # Horizontal Line
                    cv.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
                    new_line.append([rho,theta,0])
            #Horizontal Line 
            else:
                if (rho - y > 5):
                    #Vertical position update
                    y = rho
                    # Verital Line
                    cv.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
                    new_line.append([rho,theta,1])
        
    # Display the resulting frame
    cv.imshow('Sudoku Solver', frame)   
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()