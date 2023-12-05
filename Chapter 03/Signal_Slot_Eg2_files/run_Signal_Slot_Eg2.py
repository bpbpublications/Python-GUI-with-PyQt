import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton  # SS_1
from Signal_Slot_Eg2 import * # SS_2

class MySignalSlot_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        self.myui.mybtn1.clicked.connect(self.mymethod_btn1)# SS_3
        self.myui.mybtn2.clicked.connect(self.mymethod_btn2)# SS_4        
        self.show()
    
    def mymethod_btn1(self):# SS_5
        QMessageBox.information(self, "Button 1", "Button1 is clicked", QMessageBox.Ok, QMessageBox.Ok)# SS_6
        return
    
    def mymethod_btn2(self):# SS_7
        QMessageBox.information(self, "Button 2", "Button2 is clicked", QMessageBox.Ok, QMessageBox.Ok)# SS_8
        return

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = MySignalSlot_Window()# SS_9
    sys.exit(myapp.exec_())