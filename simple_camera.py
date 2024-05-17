import cv2

def main():
    # Open a connection to the first camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Set the resolution of the capture (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Define the codec and create VideoWriter object if you want to save the video
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Perform operations on the frame here, if needed

        # Uncomment below if you want to save the video
        # out.write(frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and the video writer if used
    cap.release()
    # Uncomment below if you want to save the video
    # out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
