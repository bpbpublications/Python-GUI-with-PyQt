import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QLCDNumber
from lcdnumber_eg1 import *

class MyLCDNumber(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Set the minimum and maximum values for the vertical slider
        self.myui.verticalSlider.setMinimum(0)
        self.myui.verticalSlider.setMaximum(100)
        self.myui.verticalSlider.setValue(0)

        # change the segment style to flat 
        self.myui.lcdNumber.setSegmentStyle(QLCDNumber.Flat)

        # Connect the slider's valueChanged signal to the lcd's display slot
        self.myui.verticalSlider.valueChanged.connect(self.myui.lcdNumber.display)
        
        self.show()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyLCDNumber()
    screen.show()
    sys.exit(app.exec_())