import socket
import threading
from login import login
import time
from functions.colors import Colors
import services.user_service as user_service
from functions.encryption import full_encrypt
from functions.decryption import full_decrypt


class Client:
    def __init__(self, current_user):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ""
        self.last_msg = "89ruhfdkhjsdbesnbdsb"
        self.all_users = {}
        self.colors = Colors()
        self.current_user = current_user
        self.last_recv = ""

    def connect(self, address):
        self.sock.connect((address, 56789))
        self.address = address

    def send(self):
        while True:
            msg = input("")
            if msg == "/c":
                if self.current_user.get_security().can_create:
                    user_service.new_user()
                else:
                    print(self.colors.red + "Sie haben nicht die nötigen Rechte um einen neuen Nutzer zu erstellen." + self.colors.reset)
            elif msg == "/m":
                if self.current_user.get_security().can_modify:
                    user_service.print_ids()
                    user = user_service.get_single(int(input("Welchen Nutzer wollen sie bearbeiten? (Bitte ID eingeben!)")))
                    user_service.modify_user(user)
                else:
                    print(self.colors.red + "Sie haben nicht die nötigen Rechte um einen vorhandenen Nutzer zu bearbeiten." + self.colors.reset)
            elif msg == "/e":
                if self.current_user.get_security().can_encrypt:
                    msg = full_encrypt(input("Zu verschlüsselnde Nachricht: "))
                    self.last_msg = self.current_user.get_username() + " > " + msg + " | diese Nachricht ist verschlüsselt, /d um die Nachricht zu entschlüsseln!"
                    self.sock.send(bytes(self.current_user.get_username() + " > " + msg + " | diese Nachricht ist verschlüsselt, /d um die Nachricht zu entschlüsseln!", "utf-8"))
                else:
                    print(self.colors.red + "Sie haben nicht die nötigen Rechte um Nachrichten zu verschlüsseln." + self.colors.reset)
            elif msg == "/d":
                if self.current_user.get_security().can_decrypt:
                    data = full_decrypt(self.last_recv.split(">")[1].split("|")[0].strip())
                    print("Entschlüsselte Nachricht: " + data)
                else:
                    print(self.colors.red + "Sie haben nicht die nötigen Rechte um Nachrichten zu entschlüsseln." + self.colors.reset)
            else:
                self.last_msg = self.current_user.get_username() + " > " + msg
                self.sock.send(bytes(self.current_user.get_username() + " > " + msg, "utf-8"))

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
                self.last_recv = data
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


cu = login()
print("/c = create new user \n"
      "/m = modify existing user \n"
      "/e = encrypt message \n"
      "/id = print all ids + usernames \n")
client = Client(cu)
client.connect("skriil.ddnss.de")
client.run()
