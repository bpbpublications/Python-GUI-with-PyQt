import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFontComboBox
from fontcombobox_eg1 import *

class MyFontComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # setting the font filters which are used to limit the available font families of QFOntComboBox object 
        self.myui.fontComboBox.setFontFilters(QFontComboBox.NonScalableFonts)
        
        # Connecting the currentFontChanged signal of QFOntComboBox object to the myfontchanged slot
        self.myui.fontComboBox.currentFontChanged.connect(self.myfontchanged)

        self.show()
    
    def myfontchanged(self, myfont):
        self.myui.mylb2.setText("Current font changed to:" + myfont.family())

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyFontComboBox()
    w.show()
    sys.exit(app.exec_())
