import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from dial_eg1 import *

class MyDateTimeEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        # set the min and max values of the dial
        self.myui.dial.setRange(0, 100)
        # default value is set to 30
        self.myui.dial.setValue(30)

        # the dial will move by increment of 1
        self.myui.dial.setNotchTarget(1.0)

        # valueChanged signal will be emitted continuously as the dial is rotated
        self.myui.dial.setTracking(True)

        # the dial value will wrap around from the max value to the min value and vice versa
        self.myui.dial.setWrapping(True)
        
        # connecting the valueChanged signal of the dial to my_labelupdate method
        self.myui.dial.valueChanged.connect(self.my_labelupdate)
                
        self.show()

    def my_labelupdate(self, myval):
        self.myui.mylbl1.setText("Value is: " + str(myval))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyDateTimeEdit()
    screen.show()
    sys.exit(app.exec_())