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