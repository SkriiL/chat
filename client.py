import socket
import threading
from login import login
import time


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ""
        self.last_msg = "89ruhfdkhjsdbesnbdsb"

    def connect(self, address):
        self.sock.connect((address, 5060))
        self.address = address

    def send(self):
        while True:
            msg = input("")
            self.last_msg = current_user.get_username() + " > " + msg
            self.sock.send(bytes(current_user.get_username() + " > " + msg, "utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            data = str(data, encoding="utf-8")
            if data == "./restart":
                self.restart()
            elif self.last_msg != data:
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


current_user = login()
client = Client()
client.connect("127.0.0.1")
client.run()
