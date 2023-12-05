import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QToolButton  # QTBEG1_1
from toolbutton_eg1 import * # QTBEG1_2
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class MyToolButton_Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        self.myui.actionNew_2.setCheckable(True) # QTBEG1_3
        self.myui.actionNew_2.setStatusTip("New text will be displayed")# QTBEG1_4
        
        self.myui.actionEdit.setCheckable(False)# QTBEG1_5
        self.myui.actionEdit.setStatusTip("Edit text will be displayed")# QTBEG1_6
        
        self.myui.actionSave_2.setStatusTip("Save text will be displayed")# QTBEG1_7
        
        self.myui.actionQuestion.setStatusTip("Question text will be displayed")# QTBEG1_8
                
        # addition of one toolButton using code

        self.mytb_btn1 = QAction(QtGui.QIcon("C:/Users/SAURABH/Desktop/python course/search.gif"),"Search",self)# QTBEG1_9
        self.mytb_btn1.setStatusTip("Search text will be displayed")# QTBEG1_10
        self.myui.toolBar.addAction(self.mytb_btn1)# QTBEG1_11
        self.myui.toolBar.actionTriggered[QAction].connect(self.mydisplay)# QTBEG1_12

        self.mytb_btn2 = QToolButton()# QTBEG1_13
        self.mytb_btn2.setCheckable(True)# QTBEG1_14
        self.mytb_btn2.setChecked(False)# QTBEG1_15
        self.mytb_btn2.setArrowType(Qt.LeftArrow)# QTBEG1_16
        self.mytb_btn2.setAutoRaise(True)# QTBEG1_17
        self.mytb_btn2.setToolButtonStyle(Qt.ToolButtonIconOnly)# QTBEG1_18
        self.mytb_btn2.clicked.connect(self.myshowDetail)# QTBEG1_19
        self.myui.toolBar.addWidget(self.mytb_btn2)# QTBEG1_20
        
        self.mytb_btn3 = QToolButton()# QTBEG1_21
        self.mytb_btn3.setIcon(QtGui.QIcon("C:/Users/SAURABH/Desktop/python course/globe-green.png")) # QTBEG1_22
        self.mytb_btn3.setIconSize(QtCore.QSize(30,30))# QTBEG1_23
        self.mytb_btn3.setPopupMode(QToolButton.MenuButtonPopup)# QTBEG1_24
        self.myui.toolBar.addWidget(self.mytb_btn3)# QTBEG1_25

        self.myui.actionExit.triggered.connect(self.exit)# QTBEG1_26
        self.show()
    
    def mydisplay(self, mytxt):# QTBEG1_27
        self.myui.lineEdit.setText(mytxt.text())# QTBEG1_28
    
    def exit(self):
        sys.exit()# QTBEG1_29
        
    def myshowDetail(self):
        if self.mytb_btn2.isChecked(): # QTBEG1_30
            self.myui.lineEdit.setText("Display...1")
        else:
            self.myui.lineEdit.setText("Display...2")# QTBEG1_31
    
if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = MyToolButton_Example()# QTBEG1_32
    sys.exit(myapp.exec_())
