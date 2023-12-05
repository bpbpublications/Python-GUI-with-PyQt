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
        
        myhbox1 = QHBoxLayout() # addition1
        myhbox1.addStretch() # addition2
        myfrm_layout.addRow(myhbox1)
        myfrm_layout.addRow(mylbl1, mylineEdit1)
        myfrm_layout.setHorizontalSpacing(50) # addition3
        myfrm_layout.setVerticalSpacing(50) # addition4
        myfrm_layout.addRow(mylbl2, mylineEdit2)
        myfrm_layout.setVerticalSpacing(50) # addition5
        myfrm_layout.addRow(myhbox1)


        self.setLayout(myfrm_layout)# QFL_6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = FormLayout_User_Credential_App()
    sys.exit(myapp.exec_())
