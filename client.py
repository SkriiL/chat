import socket
import threading


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address):
        self.sock.connect((address, 21))

    def send(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data))

    def run(self):
        thread = threading.Thread(target=self.send)
        thread.daemon = True
        thread.start()

        self.recv()


client = Client()
client.connect("127.0.0.1")
client.run()