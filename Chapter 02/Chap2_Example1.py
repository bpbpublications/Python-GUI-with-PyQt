import sys 
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton # RAP1
from PyQt5 import QtGui

class Absolute_Position(QWidget): # RAP2
    def __init__(self):
        super().__init__()
        self.display_widgets() # RAP3
        self.setGeometry(0, 0, 398, 229)  # RAP4 
        self.setWindowTitle('User Credentials App') # RAP5
        self.show()
    
    def display_widgets(self):
        mylbl1 = QLabel('Enter your username:', self)  # RAP6
        myfont = QtGui.QFont()  # RAP7
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl1.setFont(myfont)
        mylbl1.move(14, 50)  # RAP8
        
        mylbl2 = QLabel('Enter your password:', self)  # RAP9
        myfont = QtGui.QFont() # RAP10
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl2.setFont(myfont)
        mylbl2.move(14, 120) # RAP11
        
        mylineedit1 = QLineEdit(self) # RAP12
        mylineedit1.move(210, 50) # RAP13
        
        mylineedit2 = QLineEdit(self) # RAP14
        mylineedit2.move(210, 120) # RAP15
        
        mybtn = QPushButton(self) # RAP16
        mybtn.setText('Confirm') # RAP17
        mybtn.move(140, 180) # RAP18

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = Absolute_Position()
    sys.exit(myapp.exec_())
