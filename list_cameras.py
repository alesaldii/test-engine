import cv2

def list_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def test_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"Cannot open camera index {index}")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f"Camera {index}", frame)
        cv2.waitKey(1000)  # Display the frame for 1 second
        cv2.destroyAllWindows()
    else:
        print(f"Failed to grab frame from camera index {index}")
    cap.release()

cameras = list_cameras()
print("Available camera indices:", cameras)

for index in cameras:
    print(f"Testing camera index {index}")
    test_camera(index)
