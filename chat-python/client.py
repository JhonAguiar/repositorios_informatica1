import socket
import threading
import sys

def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("Su sesión ha sido desconectada desde el servidor.")
            signal = False
            break

host = input("Host: ")
port = int(input("Puerto: "))

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("No se pudo establecer conexión con el servidor.")
    input("Presione enter para salir")
    sys.exit(0)

receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

while True:
    message = input()
    sock.sendall(str.encode(message))