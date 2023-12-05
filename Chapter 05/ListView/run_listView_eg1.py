import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QStandardItemModel
from listView_eg1 import *

class MyListView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myfruits = ['apple', 'orange', 'banana', 'pear'] # creating a list object
        # creating an object of one of the model/view class for storing custom data.
        model = QStandardItemModel()
        # A view is set up to display the items in the listView object 
        self.ui.mylV1.setModel(model)
        # iterating each elements of the myfruits list object
        for i in self.myfruits:
            # QStandardItem provides the items in a QStandardItemModel
            item = QtGui.QStandardItem(i)
            # adding items to the model using appendRow
            model.appendRow(item)
        self.show()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyListView()
    w.show()
    sys.exit(app.exec_())