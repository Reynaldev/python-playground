import sys 
import socket

if __name__ == "__main__":
    hostname = sys.argv[1] 
    port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((hostname, port))
    s.listen(5)

    print(f"Server created at {hostname}:{port}")

    while True:
        (c, addr) = s.accept()
       
        print(addr)
