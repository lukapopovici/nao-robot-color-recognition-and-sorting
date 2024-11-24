from ToServer import send_image
import cv2

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return

    print("Press 's' to save an image, or 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow('Webcam - Press "s" to Save or "q" to Quit', frame)
        key = cv2.waitKey(1)

        if key == ord('s'):
            send_image(frame)
            print("Image sent.")

        elif key == ord('q'):
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()
