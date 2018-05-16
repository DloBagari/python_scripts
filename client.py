import socket


host = "localhost"
bufsiz = 4092

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = (host,5555 )
mysocket.connect(addr)

try:
    msg = b"hi this is test Dlo\n"
    mysocket.sendall(msg)
    data = mysocket.recv(bufsiz)
    if data:
        print(data.decode("utf-8"))
except socket.errno:
    print("error")
finally:
    mysocket.close()
