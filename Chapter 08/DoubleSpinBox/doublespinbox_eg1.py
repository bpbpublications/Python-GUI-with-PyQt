# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doublespinbox_eg1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 60, 161, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mylbl2 = QtWidgets.QLabel(self.centralwidget)
        self.mylbl2.setGeometry(QtCore.QRect(60, 120, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mylbl2.setFont(font)
        self.mylbl2.setText("")
        self.mylbl2.setObjectName("mylbl2")
        self.my_btn = QtWidgets.QPushButton(self.centralwidget)
        self.my_btn.setGeometry(QtCore.QRect(320, 60, 171, 28))
        self.my_btn.setObjectName("my_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DoubleSpinBox _eg1"))
        self.label.setText(_translate("MainWindow", "Kindly Change the value of Double spin box widget:"))
        self.my_btn.setText(_translate("MainWindow", "Set Range of type double"))