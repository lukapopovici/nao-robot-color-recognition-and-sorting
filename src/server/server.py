import socket
import struct
import os
from PIL import Image
import io

class SERVER:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SERVER, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, host="127.0.0.1", port=8080):
        if not hasattr(self, "_initialized"):
            self.host = host
            self.port = port
            self._socket = None
            self._initialized = True

    def start(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self._socket.accept()
                print(f"Connection established with {client_address}")
                self.handle_client(client_socket)
        except KeyboardInterrupt:
            print("Shutting down server.")
        finally:
            self._socket.close()

    def handle_client(self, client_socket):
        try:
            packed_size = client_socket.recv(4)  
            if not packed_size:
                return
            img_size = struct.unpack("!I", packed_size)[0]  
            print(f"Expecting image of size: {img_size} bytes.")

            img_data = b""
            while len(img_data) < img_size:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                img_data += packet
            img = Image.open(io.BytesIO(img_data))
            print(f"Received image: {img.size}, format: {img.format}")

            response = "Image received and saved."
            client_socket.send(response.encode("utf-8"))
        except Exception as e:
            print(f"Error handling client: {e}")
       

def main():
    server = SERVER()
    server.start()

if __name__ == "__main__":
    main()
