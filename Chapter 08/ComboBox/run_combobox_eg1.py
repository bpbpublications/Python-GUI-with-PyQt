import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from combobox_eg1 import *

class MyComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # adding items to the QComboBox object
        self.myui.comboBox.addItems(["Orange", "Papaya", "Banana"])

        # setting the current index to 1
        self.myui.comboBox.setCurrentIndex(1)
        
        # inserting the item at index position 0 of QComboBox widget
        self.myui.comboBox.insertItem(0, "Mango")
        
        # display of all the items of QComboBox widget
        for mycount in range(self.myui.comboBox.count()):
            print("Current Index is: " + str(mycount) + " and the text is: " + self.myui.comboBox.itemText(mycount))
        
        # connecting the activated and currentIndexChanged signals to the corresponding slot methods
        self.myui.comboBox.activated.connect(self.myactivated)
        self.myui.comboBox.currentIndexChanged.connect(self.mycurrentIndexChanged)
        
        self.show()
    
    def myactivated(self, myindex):
        self.myui.mylbl2.setText("Item Activated is: " + self.myui.comboBox.currentText())
    
    def mycurrentIndexChanged(self, myindex):
        self.myui.mylbl3.setText("Index is: " + str(myindex) + " & Text is: " + self.myui.comboBox.currentText())
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyComboBox()
    w.show()
    sys.exit(app.exec_())
