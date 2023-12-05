import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QPushButton # GLEG2_1
from PyQt5 import QtGui

class GridLayout_Eg2(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('GridLayout with span')# GLEG2_2
        self.show()
    
    def display_widgets(self):
        # writing the grid portion
        mygrid_layout = QGridLayout()
        self.setLayout(mygrid_layout)
        
        mybtn1 = QPushButton("Row Spanning merging 2 rows")
        mygrid_layout.addWidget(mybtn1, 0,0, 2,1)# GLEG2_3
        
        mybtn2 = QPushButton("Column Spanning")
        mygrid_layout.addWidget(mybtn2, 2,0, 1,3)# GLEG2_4
        
        for outer in range(3,5):
            for lower in range(3,5):
                mylbl = QLabel('Label' + str(outer) + str(lower),self)# GLEG2_5
                myfont = QtGui.QFont()
                myfont.setFamily("Calibri")
                myfont.setPointSize(10)
                myfont.setBold(True)
                myfont.setWeight(75)
                mylbl.setFont(myfont)
                mygrid_layout.addWidget(mylbl, outer, lower)# GLEG2_6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = GridLayout_Eg2()
    sys.exit(myapp.exec_())
