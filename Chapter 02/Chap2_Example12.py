import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QGridLayout # GLEG3_1
from PyQt5 import QtGui

class GridLayout_Eg3(QWidget):
    def __init__(self):
        super().__init__()
        self.display_widgets()
        self.setGeometry(0, 0, 398, 229)
        self.setWindowTitle('GridLayout with stretch')# GLEG3_2
        self.show()
    
    def display_widgets(self):
        # writing the grid portion
        mygrid_layout = QGridLayout()
        self.setLayout(mygrid_layout)
        
        for outer in range(1,4):
            for lower in range(1,4):
                mytextedit = QTextEdit(self)# GLEG3_3
                mytextedit.setPlaceholderText(str(outer) + str(lower))# GLEG3_4
                mygrid_layout.addWidget(mytextedit, outer, lower)# GLEG3_5
            mygrid_layout.setColumnStretch(outer,outer+1)# GLEG3_6

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywindow = GridLayout_Eg3()
    sys.exit(myapp.exec_())
