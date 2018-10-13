import socket
import threading
from login import login
import time
import atexit
import os


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ""

    def connect(self, address):
        self.sock.connect((address, 5060))
        self.address = address

    def send(self):
        while True:
            msg = input("")
            self.sock.send(bytes(current_user.get_username() + " > " + msg, "utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            data = str(data, encoding="utf-8")
            if data == "./restart":
                self.restart()
            else:
                print(data)

    def run(self):
        thread = threading.Thread(target=self.send)
        thread.daemon = True
        thread.start()

        self.recv()

    def close(self):
        self.sock.close()

    def restart(self):
        time.sleep(1)
        self.sock.close()
        self.sock.connect((self.address, 5060))
        self.run()

    def test(self):
        os.system("python client.py")


current_user = login()
client = Client()
atexit.register(client.test)
client.connect("127.0.0.1")
client.run()
