# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 222)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(110, 60, 141, 91))
        self.dial.setObjectName("dial")
        self.mylbl1 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl1.setGeometry(QtCore.QRect(90, 160, 191, 21))
        self.mylbl1.setText("")
        self.mylbl1.setWordWrap(True)
        self.mylbl1.setObjectName("mylbl1")
        self.mylbl1_2 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl1_2.setGeometry(QtCore.QRect(100, 20, 251, 21))
        self.mylbl1_2.setWordWrap(True)
        self.mylbl1_2.setObjectName("mylbl1_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dial_eg1"))
        self.mylbl1_2.setText(_translate("MainWindow", "Kindly rotate the Dial:"))
