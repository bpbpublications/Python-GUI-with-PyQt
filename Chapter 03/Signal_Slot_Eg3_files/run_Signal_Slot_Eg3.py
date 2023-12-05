import sys
from PyQt5.QtWidgets import QMainWindow, QApplication  # SS2_1
from Signal_Slot_Eg3 import * # SS2_2

class MySignalSlot2_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_Signal_Slot_Eg3()
        self.myui.setupUi(self)
        self.myui.mybtn1.setCheckable(True)# SS2_3
        self.myui.mybtn1.setStyleSheet("background-color : green")# SS2_4
        self.myui.mybtn1.clicked.connect(self.mymethod_btn1)# SS2_5
        self.myui.mybtn1.clicked.connect(self.mymethod_btn2)# SS2_6
        self.show()
    
    def mymethod_btn1(self):# SS2_7
        print("MeClicked")# SS2_8
    
    def mymethod_btn2(self,checked):# SS2_9
        print("MeChecked?", checked)# SS2_10

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = MySignalSlot2_Window()# SS2_11
    sys.exit(myapp.exec_())