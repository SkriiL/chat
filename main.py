import sys
from qtpy import QtWidgets
from client import Client
from ui.mainwindow import Ui_MainWindow
import threading

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Chat")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.client = Client()
        self.client.connect()

        self.ui.send.clicked.connect(self.send)

    def send(self):
        self.client.send(self.ui.text_send.toPlainText())

    def recv(self):
        while True:
            msg = self.client.recv()

    def make_thread(self):
        t = threading.Thread(target=self.recv)
        t.daemon = True
        t.start()


window = MainWindow()
window.make_thread()

window.show()

sys.exit(app.exec_())
