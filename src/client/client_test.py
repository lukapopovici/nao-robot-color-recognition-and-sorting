import socket
import sys
import random
import struct


def send_image(file_path, host="127.0.0.1", port=8080):
    with open(file_path, "rb") as f:
        img_data = f.read()

    img_size = len(img_data)
    print(f"Sending image of size: {img_size} bytes.")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        sock.sendall(struct.pack("!I", img_size))  

        sock.sendall(img_data)

        response = sock.recv(1024).decode("utf-8")
        print(f"Server response: {response}")

if __name__ == "__main__":
    send_image("test.png")