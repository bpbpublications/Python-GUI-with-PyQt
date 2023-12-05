import sys
from PyQt5.QtWidgets import QMainWindow, QApplication  # QPBEG1_1
from pushbutton_eg1 import * # QPBEG1_2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon # QPBEG1_3

class MyPushButton_Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_Form()
        self.myui.setupUi(self)
        # Case1
        self.myui.btn_checkable.setCheckable(True) # QPBEG1_4
        self.myui.btn_checkable.toggle()# QPBEG1_5
        self.myui.btn_checkable.clicked.connect(self.case1)# QPBEG1_6
        # Case2
        self.myui.btn_displaytxt.clicked.connect(lambda: self.case2(self.myui.btn_displaytxt))# QPBEG1_7
        # Case3
        self.myui.btn_display_icon.clicked.connect(self.case3)# QPBEG1_8
        # Case4
        self.myui.btn_default_set.setDefault(True)# QPBEG1_9
        # Case5
        self.myui.btn_enable.clicked.connect(self.case5_1)# QPBEG1_10
        self.myui.btn_disable.clicked.connect(self.case5_2)# QPBEG1_11
        self.show()
    
    def case1(self):
        if self.myui.btn_checkable.isChecked():# QPBEG1_12
            self.myui.mylbl1.setText("I am checked")
        else:
            self.myui.mylbl1.setText("I am unchecked")
    
    def case2(self, mybtn):
        self.myui.mylbl2.setText("Text name is: " + mybtn.text())# QPBEG1_13
    
    def case3(self):
        display_icon_image = "E:/my_pythonbook/PyQt5/Chapter_4/Push_Button/help-contents copy.png"# QPBEG1_14
        try:
            with open(display_icon_image):
                self.myui.btn_display_icon.setIcon(QIcon(QPixmap(display_icon_image)))# QPBEG1_15
                self.myui.mylbl3.setPixmap(QPixmap(display_icon_image))
        except FileNotFoundError:
            print("Wrong image selection")
    
    def case5_1(self):
        self.myui.btn_myself.setEnabled(True)# QPBEG1_16
    def case5_2(self):
        self.myui.btn_myself.setEnabled(False)# QPBEG1_17
    
if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = MyPushButton_Example()# QPBEG1_18
    sys.exit(myapp.exec_())
