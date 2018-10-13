import socket
import threading
import os


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("0.0.0.0", 5060))
        self.sock.listen(2)
        self.connections = []

    def handler(self, c, a):
        while True:
            try:
                data = c.recv(1024)
                for connection in self.connections:
                    connection.send(data)
                if not data:
                    break
            except:
                self.restart()

    def run(self):
        while True:
            c, a = self.sock.accept()
            thread = threading.Thread(target=self.handler, args=(c, a))
            thread.daemon = True
            thread.start()
            self.connections.append(c)
            print(self.connections)

    def restart(self):
        os.system("end.bat")


server = Server()
server.run()