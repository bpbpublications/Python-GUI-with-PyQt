import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton, QLineEdit , QHBoxLayout
from PyQt5 import QtGui

class GridLayout_User_Credential_App(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('GridLayout with User Credential App')
        self.show()
    
    def display_widgets(self):
        # writing the grid portion
        mygrid_layout = QGridLayout()
        self.setLayout(mygrid_layout)

        mylbl1 = QLabel('Enter your username:',self)
        mylbl1.setMinimumWidth(161)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl1.setFont(myfont)
        mygrid_layout.addWidget(mylbl1, 1, 0, 1, 2)
        
        mylbl2 = QLabel('Enter your password:',self)
        mylbl2.setMinimumWidth(161)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl2.setFont(myfont)
        mygrid_layout.addWidget(mylbl2, 3, 0, 1, 2)
        
        mylineEdit1 = QLineEdit(self)
        mylineEdit1.setMinimumWidth(161)
        mygrid_layout.addWidget(mylineEdit1, 1, 2,1,2)
        mygrid_layout.setColumnStretch(1,2)
        
        mylineEdit2 = QLineEdit(self)
        mylineEdit2.setMinimumWidth(161)
        mygrid_layout.addWidget(mylineEdit2, 3, 2,1,2)
        
        myhbox = QHBoxLayout()
        myhbox.addStretch()
        mybtn1 = QPushButton("Confirm")
        myhbox.addWidget(mybtn1)
        myhbox.addStretch()
        
        mygrid_layout.addLayout(myhbox,4,1,1,3)

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = GridLayout_User_Credential_App()
    sys.exit(myapp.exec_())
