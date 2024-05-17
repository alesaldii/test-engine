"""
Title:        Simple Camera Line Folling Code
Objective:    Use camera to indicate via print() funct. to turn right, left or go straight.
Methodology:  Huge Line Transform Method is used taking theta as reference to go straigh.
Author:       asaldivar
"""

import cv2
import numpy as np
import math

def main():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0 for the default camera
    
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                break
            
            """Edge Detection"""
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #grayscale
            blur = cv2.GaussianBlur(gray,(5,5),0) #gaussian blur
            ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV) #thresholding
            edges = cv2.Canny(thresh,100,200) #finding edges
            
            """Probabilistic Huge Line Transform"""
            #https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
            theta = 0
            lines = cv2.HoughLinesP(edges.copy(), 1, np.pi/180, 10, None, 50, 10)
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3) #drawing lines on frame
                    theta=theta+math.atan2((y2-y1),(x2-x1)) #theta calculation
                #print(theta)
                threshold = 7
                if theta > threshold:
                    print("Turn Left")
                elif theta < -threshold:
                    print("Turn Right")
                else:
                    print("Go Straight")

            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
            
if __name__ == "__main__":
    main()
