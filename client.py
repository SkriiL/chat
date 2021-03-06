import socket
import threading
from login import login
import time
from functions.colors import Colors


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ""
        self.last_msg = "89ruhfdkhjsdbesnbdsb"
        self.all_users = {}
        self.colors = Colors()

    def connect(self, address):
        self.sock.connect((address, 56789))
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
                color = self.get_color(data)
                print(color + data + self.colors.reset)

    def get_color(self, data):
        data = data.split()
        for key, value in self.all_users.items():
            if key == data[0]:
                return value
        self.all_users[data[0]] = self.colors.pick()
        return self.all_users[data[0]]

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
        self.sock.connect((self.address, 56789))
        self.run()


current_user = login()
client = Client()
client.connect("skriil.ddnss.de")
client.run()
