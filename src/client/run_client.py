#aces fisier este de copiat in folderul interpretorului python 2.7 

import socket
import sys
import random
import struct

#sys.path.append(r'C:\Users\aafdd\Downloads\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\pynaoqi-python2.7-2.8.6.23-win64-vs2015-20191127_152649\lib')

#print("Python version:", sys.version)

#from naoqi import *

#robot_ip = "198.0.0.0"  
#port = random.randint(1024, 65535) 

#try:
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    sock.settimeout(5) 
#    sock.connect((robot_ip, port))
#    print("SUCCESE")
#    sock.close()  

#except socket.error as e:
#    print("FAIL!")

#try:
 #   tts = ALProxy("ALTextToSpeech", robot_ip, port)
 #   tts.say("Hello!")
#except Exception as e:
#    print("Failed")

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