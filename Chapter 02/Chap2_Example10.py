import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout # GLEG1_1
from PyQt5 import QtGui

class GridLayout_Eg1(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('Basic GridLayout example') #GLEG1_2
        self.show()
    
    def display_widgets(self):
        # writing the grid portion
        mygrid_layout = QGridLayout()# GLEG1_3
        self.setLayout(mygrid_layout)# GLEG1_4
        
        for outer in range(4):
            for lower in range(3):
                mylbl = QLabel('Label' + str(outer) + str(lower),self)# GLEG1_5
                myfont = QtGui.QFont()
                myfont.setFamily("Calibri")
                myfont.setPointSize(10)
                myfont.setBold(True)
                myfont.setWeight(75)
                mylbl.setFont(myfont)
                mygrid_layout.addWidget(mylbl, outer, lower)# GLEG1_6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = GridLayout_Eg1()
    sys.exit(myapp.exec_())
