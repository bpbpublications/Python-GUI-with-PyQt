import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QDesktopWidget # QHBEG1
from PyQt5 import QtGui

class HBox_without_stretch(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('QHBoxLayout without stretch')# QHBEG2
        self.movecenter()
        self.show()
    
    def display_widgets(self):
        mylbl1 = QLabel('Label1:', self)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl1.setFont(myfont)

        mylbl2 = QLabel('Label2', self)
        myfont = QtGui.QFont()
        myfont.setFamily("Calibri")
        myfont.setPointSize(10)
        myfont.setBold(True)
        myfont.setWeight(75)
        mylbl2.setFont(myfont)

        # QHBoxlayout
        myhbox = QHBoxLayout()# QHBEG7
        myhbox.addWidget(mylbl1)# QHBEG8
        myhbox.addWidget(mylbl2)# QHBEG9
        self.setLayout(myhbox)# QHBEG10
    
    def movecenter(self):
        myfrm_gmtry = self.frameGeometry()# QHBEG3
        mycenter = QDesktopWidget().availableGeometry().center()# QHBEG4
        myfrm_gmtry.moveCenter(mycenter)# QHBEG5
        self.move(myfrm_gmtry.topLeft())# QHBEG6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = HBox_without_stretch()
    sys.exit(myapp.exec_())
