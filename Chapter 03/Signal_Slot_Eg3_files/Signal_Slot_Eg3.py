# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signal_Slot_Eg3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signal_Slot_Eg3(object):
    def setupUi(self, Signal_Slot_Eg3):
        Signal_Slot_Eg3.setObjectName("Signal_Slot_Eg3")
        Signal_Slot_Eg3.resize(264, 155)
        self.centralwidget = QtWidgets.QWidget(Signal_Slot_Eg3)
        self.centralwidget.setObjectName("centralwidget")
        self.mybtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.mybtn1.setGeometry(QtCore.QRect(60, 40, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mybtn1.setFont(font)
        self.mybtn1.setCheckable(False)
        self.mybtn1.setObjectName("mybtn1")
        Signal_Slot_Eg3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Signal_Slot_Eg3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 26))
        self.menubar.setObjectName("menubar")
        Signal_Slot_Eg3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Signal_Slot_Eg3)
        self.statusbar.setObjectName("statusbar")
        Signal_Slot_Eg3.setStatusBar(self.statusbar)

        self.retranslateUi(Signal_Slot_Eg3)
        QtCore.QMetaObject.connectSlotsByName(Signal_Slot_Eg3)

    def retranslateUi(self, Signal_Slot_Eg3):
        _translate = QtCore.QCoreApplication.translate
        Signal_Slot_Eg3.setWindowTitle(_translate("Signal_Slot_Eg3", "MainWindow"))
        self.mybtn1.setText(_translate("Signal_Slot_Eg3", "Btn1"))