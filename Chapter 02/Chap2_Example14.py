import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton,QHBoxLayout, QLineEdit , QHBoxLayout # QFL_1
from PyQt5 import QtGui

class FormLayout_User_Credential_App(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('FormLayout with User Credential App')# QFL_2
        self.show()
    
    def display_widgets(self):
        # writing the grid portion
        myfrm_layout = QFormLayout()
        
        mylbl1 = QLabel('Enter your username:',self)
        mylbl1.setMinimumWidth(161)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl1.setFont(myfont)

        mylbl2 = QLabel('Enter your password:',self)
        mylbl2.setMinimumWidth(161)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl2.setFont(myfont)

        mylineEdit1 = QLineEdit(self)
        mylineEdit1.setMinimumWidth(161)
        mylineEdit2 = QLineEdit(self)
        mylineEdit2.setMinimumWidth(161)
        
        myhbox = QHBoxLayout()
        myhbox.addStretch()
        mybtn1 = QPushButton("Confirm")
        myhbox.addWidget(mybtn1)
        myhbox.addStretch()
        myfrm_layout.addRow(mylbl1, mylineEdit1)# QFL_3
        myfrm_layout.addRow(mylbl2, mylineEdit2)# QFL_4
        myfrm_layout.addRow(myhbox)# QFL_5

        self.setLayout(myfrm_layout)# QFL_6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = FormLayout_User_Credential_App()
    sys.exit(myapp.exec_())
