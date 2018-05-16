import socket

host = ""
size = 512
port = 5555

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
mysocket.bind((host,port))
mysocket.listen(5)
while True:
    client, addr = mysocket.accept()
    data = client.recv(size)
    if data:
        print(addr[0],data.decode("utf-8"))
        client.sendall(b"fuck off")
mysocket.close()
