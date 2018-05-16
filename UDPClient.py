import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("",6789)
msg = "Hi there"
try:
    sock.sendto(msg.encode("utf-8"),addr)

    data, address = sock.recvfrom(4092)
    print(data.decode())
except socket.error:
    print("socket Error")
    sock.close()
