import sys
import re
from PyQt5.QtWidgets import QMainWindow,QApplication
from doublespinbox_eg1 import *

class MyDoubleSpinBoxEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Setting the initial value of QDoubleSpinBox object
        self.myui.doubleSpinBox.setValue(0.10)

        # Setting the minimum value of QDoubleSpinBox object
        self.myui.doubleSpinBox.setMinimum(-1.10)

        # Setting the maximum value of QDoubleSpinBox object
        self.myui.doubleSpinBox.setMaximum(1.10)
        
        # Setting the step value to 0.2 of QDoubleSpinBox object
        self.myui.doubleSpinBox.setSingleStep(0.2)
        
        # signal is emitted when the QDoubleSpinBox object value changes
        self.myui.doubleSpinBox.valueChanged.connect(self.my_valuechange)

        # signal is emitted on button click and connected to the method my_btn1
        self.myui.my_btn.clicked.connect(self.my_btn1)

        self.show()

    def my_btn1(self):
        # Setting the range of values of QDoubleSpinBox object
        self.myui.doubleSpinBox.setRange(-2.10, 2.10)
    
    def my_valuechange(self,myval):
        # setting the label text when valueChanged signal is emitted
        self.myui.mylbl2.setText("My current value is:"+str(myval))
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyDoubleSpinBoxEdit()
    screen.show()
    sys.exit(app.exec_())