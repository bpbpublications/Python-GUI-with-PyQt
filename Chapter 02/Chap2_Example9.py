import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget, QLineEdit, QPushButton # QBX1
from PyQt5 import QtGui

class BoxLayout_user_credential_App(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('BoxLayout User Credential App') # QBX2
        self.movecenter()
        self.show()
    
    def display_widgets(self):
        mylbl1 = QLabel('Enter your username:', self)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl1.setFont(myfont)

        mylbl2 = QLabel('Enter your password:', self)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl2.setFont(myfont)
        
        mylineedit1 = QLineEdit(self)
        mylineedit2 = QLineEdit(self)
        mybtn = QPushButton(self)
        mybtn.setText('Confirm')
        
        myhbox1 = QHBoxLayout() # QBX3
        myhbox1.setSpacing(60) # QBX4
        myhbox1.addStretch() # QBX5
        myhbox1.addWidget(mylbl1) # QBX6
        myhbox1.addWidget(mylineedit1) # QBX7
        myhbox1.addStretch() # QBX8
        
        # QBX9
        myhbox2 = QHBoxLayout()
        myhbox2.setSpacing(60)
        myhbox2.addStretch()
        myhbox2.addWidget(mylbl2)
        myhbox2.addWidget(mylineedit2)
        myhbox2.addStretch()
        
        # QBX10
        myhbox3 = QHBoxLayout()
        myhbox3.addStretch()
        myhbox3.addWidget(mybtn)
        myhbox3.addStretch()

        # QHBoxlayout
        myvbox = QVBoxLayout() # QBX11
        myvbox.addStretch() # QBX12
        myvbox.addLayout(myhbox1) # QBX13
        myvbox.addStretch() # QBX14
        myvbox.addLayout(myhbox2) # QBX15
        myvbox.addStretch() # QBX16
        myvbox.addLayout(myhbox3) # QBX17
        self.setLayout(myvbox) # QBX18
    
    def movecenter(self):
        myfrm_gmtry = self.frameGeometry()
        mycenter = QDesktopWidget().availableGeometry().center()
        myfrm_gmtry.moveCenter(mycenter)
        self.move(myfrm_gmtry.topLeft())

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = BoxLayout_user_credential_App()
    sys.exit(myapp.exec_())