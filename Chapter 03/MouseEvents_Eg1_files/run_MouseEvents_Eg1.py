import sys
from PyQt5.QtWidgets import QMainWindow, QApplication  # RME_1
from MouseEvents_Eg1 import *# RME_2
from PyQt5.QtCore import Qt

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MouseEvents_Eg1()
        self.myui.setupUi(self)
        self.setMouseTracking(True)# RME_3
        self.myui.hover_mouse_btn_2.leaveEvent = lambda e: self.myui.hover_mouse_btn_2.setStyleSheet("background-color : blue")  # RME_4
        self.myui.hover_mouse_btn_2.enterEvent = lambda e: self.myui.hover_mouse_btn_2.setStyleSheet("background-color : violet")  # RME_5
        self.show()
    
    def mousePressEvent(self, e): # RME_6
        if e.button() == Qt.LeftButton:# RME_7
            self.myui.lm_click_btn_2.setStyleSheet("background-color : green")# RME_8

        if e.button() == Qt.RightButton:# RME_9
            self.myui.rm_click_btn_2.setStyleSheet("background-color : red")# RME_10

    def mouseDoubleClickEvent(self, e):# RME_11
        if e.button() == Qt.LeftButton:# RME_12
            self.myui.left_double_click_btn_2.setStyleSheet("background-color : yellow")# RME_13
    
if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = MyMainWindow()# RME_14
    sys.exit(myapp.exec_())
