import socket,sys,threading

def cli(ip):
    HOST = ip  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    

        
    def recv():
        while True:
            data = s.recv(1024).decode()
            if not data: sys.exit(0)
            print(data)

    threading.Thread(target=recv).start()

    while True:
            i=input("")
            s.sendall(i.encode())

def ser():
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    print(f"Connected by {addr}")


        
    def recv():
        while True:
            data = conn.recv(1024).decode()
            if not data: sys.exit(0)
            print(data)

    threading.Thread(target=recv).start()

    while True:
            i=input("")
            conn.sendall(i.encode())




opt=input("opt")
if(opt=="s"):
     ser()
else:
     ip=input("insert ip: ")
     cli(ip)

