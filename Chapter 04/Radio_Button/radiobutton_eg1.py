# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radiobutton_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, 131, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rbtn_apple = QtWidgets.QRadioButton(self.frame)
        self.rbtn_apple.setGeometry(QtCore.QRect(20, 10, 82, 17))
        self.rbtn_apple.setChecked(False)
        self.rbtn_apple.setAutoExclusive(True)
        self.rbtn_apple.setObjectName("rbtn_apple")
        self.rbtn_orange = QtWidgets.QRadioButton(self.frame)
        self.rbtn_orange.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.rbtn_orange.setChecked(True)
        self.rbtn_orange.setObjectName("rbtn_orange")
        self.rbtn_banana = QtWidgets.QRadioButton(self.frame)
        self.rbtn_banana.setGeometry(QtCore.QRect(20, 90, 82, 17))
        self.rbtn_banana.setObjectName("rbtn_banana")
        self.lbldisplay = QtWidgets.QLabel(self.centralwidget)
        self.lbldisplay.setGeometry(QtCore.QRect(40, 190, 191, 16))
        self.lbldisplay.setText("")
        self.lbldisplay.setObjectName("lbldisplay")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 15, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rbtn_apple.setText(_translate("MainWindow", "Apple"))
        self.rbtn_orange.setText(_translate("MainWindow", "Orange"))
        self.rbtn_banana.setText(_translate("MainWindow", "Banana"))
        self.label.setText(_translate("MainWindow", "Choose any fruit from the choice:"))
