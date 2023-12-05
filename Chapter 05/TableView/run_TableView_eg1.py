import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QAbstractTableModel # using QAbstractTableModel
from PyQt5.QtGui import QStandardItemModel
from TableView_eg1 import *

class MyTableView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #creating a 2-D list
        mydata = [
          [11, 12, 13, 14],
          [15, 16, 17, 18],
          [19, 20, 21, 22],
          [23, 24, 25, 26]
        ]
        self.model = MyTableModel(mydata) # calling a custom model MyTableModel and passing mydata as a parameter into the constructor
         # model is set for the Tableview
        self.ui.tableView.setModel(self.model)
        
# creating a custom model for interfacing between data object and view
class MyTableModel(QAbstractTableModel):
    def __init__(self, mydata):
            super().__init__()
            self._data = mydata

    # data is returned for given table locations and parameters index and role are passed
    def data(self, index, role):
        if role == Qt.DisplayRole: # for returning string
            # The table location for which the information is currently being requested 
            # is given by the index parameter
            # The row and column numbers in the view are provided by the 
            # functions .row() ---> (indexing into the outer list) 
            # and.column(indexing into the sub-list) ---> (), respectively.
            # in the form of nested list , data is stored
            return self._data[index.row()][index.column()]

    # number of rows is returned
    def rowCount(self, index):
        # outer list length is returned.
        return len(self._data)

    # number of columns is returned
    def columnCount(self, index):
        # first sub list is taken .i.e. no. of elements in inner list and the length is being returned 
        # if all rows are of an equal length , then only it will work
        return len(self._data[0])

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyTableView()
    w.show()
    sys.exit(app.exec_())