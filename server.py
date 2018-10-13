import socket
import threading


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("0.0.0.0", 5060))
        self.sock.listen(1)
        self.connections = []

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            thread = threading.Thread(target=self.handler, args=(c, a))
            thread.daemon = True
            thread.start()
            self.connections.append(c)
            print(self.connections)


server = Server()
server.run()