import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Chat")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.ui.input.setText("Hallo")
        test = self.ui.input.text()
        print(test)

window = MainWindow()

window.show()

sys.exit(app.exec_())
