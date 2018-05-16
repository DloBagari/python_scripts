import socket
from time import ctime

addr=("localhost",5555)
buffer = 1024
if __name__ == "__main__":
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    soc.bind(addr)
    soc.listen(5)
    while True:
        print("waiting for client request")
        client, address = soc.accept()
        print("connected to addess:%s" %(address[0]))
        while True:
            data = client.recv(buffer)
            #if not data or data.decode("utf-8") == "END":
            if data.decode("utf-8") == "00":
                break
            print("received fro client: %s" % data.decode("utf-8"))
            print("sending to client the server time: %s" % ctime())
            try:
                client.send(bytes(ctime(),"utf-8"))
            except (KeyboardInterrupt,BrokenPipeError ):
                print("exited by user")
                break
            except socket.errno:
                break
        client.close()
    soc.close()
                    
        
            
