"""
Title:        Simple Camera Code
Author:       asaldivar
"""

import cv2


def main():

    cap = cv2.VideoCapture(0)  # 0 for the default camera
    
    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                break
            
           

            cv2.imshow('Camera', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): #press q to exit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
            
if __name__ == "__main__":
    main()
