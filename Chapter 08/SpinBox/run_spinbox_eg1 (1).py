import sys
import re
from PyQt5.QtWidgets import QMainWindow,QApplication
from spinbox_eg1 import *

class MySpinBoxEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Setting the initial value
        self.myui.spinBox.setValue(0)

        # Setting the minimum value
        self.myui.spinBox.setMinimum(-2)

        # Setting the maximum value
        self.myui.spinBox.setMaximum(2)
        
        # signal is emitted when the QSpinBox object value changes
        self.myui.spinBox.valueChanged.connect(self.my_valuechange)

        # signal is emitted on button click and connected to the method my_btn1
        self.myui.mybtn.clicked.connect(self.my_btn1)

        self.show()

    def my_btn1(self):
        # Setting the range of values
        self.myui.spinBox.setRange(-3, 3)
    
    def my_valuechange(self,myval):
        self.myui.mylbl2.setText("My current value is:"+str(myval))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MySpinBoxEdit()
    screen.show()
    sys.exit(app.exec_())