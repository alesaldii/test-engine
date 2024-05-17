"""
Title: Simple Open Camera and Display the Image
Author: alesaldii
"""
import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: unable to open camera")
            break
        cv2.imshow('Camera',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    print("Error: unable to open camera")