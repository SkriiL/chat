import socket
import threading

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect(("skriil.ddnss.de", 56789))

    def send(self):
        msg = input("")
        self.sock.send(bytes(msg, "utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            data = str(data, encoding="utf-8")
            print(data)

    def run(self):
        thread = threading.
        thread.daemon = True
