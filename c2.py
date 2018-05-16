import socket
import sys

host = ""
port = 5555
buffersize = 4096

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))

while True:
    try:
        msg = input()
        if msg =="00":
            break
        soc.sendall(msg.encode("utf=8"))
    except socket.errno:
        print("error")
        sys.exit()

    try:
        data = soc.recv(buffersize)
        if data:
            print(data.decode("utf-8"))
    except socket.errno:
        print("error")
        sys.exit()
                
                
