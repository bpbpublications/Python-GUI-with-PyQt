# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textedit_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 20, 401, 181))
        self.textEdit.setObjectName("textEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 230, 381, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mybtn1 = QtWidgets.QPushButton(self.widget)
        self.mybtn1.setObjectName("mybtn1")
        self.horizontalLayout.addWidget(self.mybtn1)
        self.mybtn2 = QtWidgets.QPushButton(self.widget)
        self.mybtn2.setObjectName("mybtn2")
        self.horizontalLayout.addWidget(self.mybtn2)
        self.mybtn3 = QtWidgets.QPushButton(self.widget)
        self.mybtn3.setObjectName("mybtn3")
        self.horizontalLayout.addWidget(self.mybtn3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TextEdit eg."))
        self.mybtn1.setText(_translate("MainWindow", "Change Font"))
        self.mybtn2.setText(_translate("MainWindow", "Setting Plain Text"))
        self.mybtn3.setText(_translate("MainWindow", "Setting Html Text"))
