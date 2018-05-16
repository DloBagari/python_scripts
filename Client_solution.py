#!/usr/bin/python3
import socket
from sys import argv,exit
if len(argv) != 4:
    print("command is not currect")
    exit()
#get inputs from command line
address = argv[1]
port = argv[2]
filename = argv[3]
bufferSize = 1024
addr = (address,port)
#create soicket
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketClient.connect(addr)
    http = "GET \%s" % filename
    #send http request
    for i in range(len(http)):
        socketClient.sendall(http[i].encode())

    data =""
    #recv response
    while True:
        recv = socketClient.recv(bufferSize).decode()
        if not recv:
            break
        data += recv
    print(data)
except socket.error:
    print("socket Error")
    socketClient.close()
