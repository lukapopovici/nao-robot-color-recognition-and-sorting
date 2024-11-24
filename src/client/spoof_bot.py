import cv2
import socket
import sys
import random
import struct

def send_image(frame, host="127.0.0.1", port=8080):
    success, encoded_image = cv2.imencode('.jpg', frame)

    if not success:
        print("Error: Failed to encode image.")
        return

    img_data = encoded_image.tobytes()  
    img_size = len(img_data)
    print(f"Sending image of size: {img_size} bytes.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(struct.pack("!I", img_size))
        sock.sendall(img_data)
        response = sock.recv(1024).decode("utf-8")
        print(f"Server response: {response}")

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
