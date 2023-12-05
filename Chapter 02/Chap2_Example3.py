import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QDesktopWidget
from PyQt5 import QtGui

class HBox_with_stretch(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('QHBoxLayout with addstretch')
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
        myhbox = QHBoxLayout()
        myhbox.addStretch() # added
        myhbox.addWidget(mylbl1)
        myhbox.addWidget(mylbl2)
        self.setLayout(myhbox)

    
    def movecenter(self):
        myfrm_gmtry = self.frameGeometry()
        mycenter = QDesktopWidget().availableGeometry().center()
        myfrm_gmtry.moveCenter(mycenter)
        self.move(myfrm_gmtry.topLeft())

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = HBox_with_stretch()
    sys.exit(myapp.exec_())