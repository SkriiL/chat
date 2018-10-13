import socket
import threading
from login import login


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address):
        self.sock.connect((address, 5060))

    def send(self):
        while True:
            msg = input("")
            self.sock.send(bytes(current_user.get_username() + " > " + msg, "utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, encoding="utf-8"))

    def run(self):
        thread = threading.Thread(target=self.send)
        thread.daemon = True
        thread.start()

        self.recv()

    def close(self):
        self.sock.close()


current_user = login()
client = Client()
client.connect("127.0.0.1")
client.run()