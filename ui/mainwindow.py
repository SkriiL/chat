# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 551)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.message = QtWidgets.QLabel(self.centralWidget)
        self.message.setGeometry(QtCore.QRect(130, 60, 47, 13))
        self.message.setText("")
        self.message.setObjectName("message")
        self.send = QtWidgets.QPushButton(self.centralWidget)
        self.send.setGeometry(QtCore.QRect(700, 420, 131, 71))
        self.send.setObjectName("send")
        self.text_send = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.text_send.setGeometry(QtCore.QRect(10, 420, 671, 71))
        self.text_send.setObjectName("text_send")
        self.output = QtWidgets.QLabel(self.centralWidget)
        self.output.setGeometry(QtCore.QRect(140, 80, 111, 51))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSwag = QtWidgets.QMenu(self.menuBar)
        self.menuSwag.setTitle("")
        self.menuSwag.setObjectName("menuSwag")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuSwag.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send.setText(_translate("MainWindow", "Absenden"))
        self.output.setText(_translate("MainWindow", "TextLabel"))

