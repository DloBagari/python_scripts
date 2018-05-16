import socket

port = 6789
maxsize = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))

while True:
    try:
        data, addr = sock.recvfrom(maxsize)
        print(data.decode("utf-8"))
        with open("log.txt","a") as f:
            f.write(data.decode("utf-8"))
        msg = data.decode("utf-8").upper()
        sock.sendto(msg.encode("utf-8"), addr)
    except socket.error:
        print("socket Error")
        sock.close()
    

