import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from TreeView_eg1 import *

class MyTreeView(QMainWindow):
    # setting object Name, Contact_Number, City, Profession 
    # with values as    0      1             2        3 
    Name, Contact_Number, City, Profession = range(4)
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # set to False means making a single level tree structure appear like a simple list of items
        self.ui.treeView.setRootIsDecorated(False)
        
        # set to True means To draw the item's background, Base and AlternateBase will be used. 
        # observe the output with background color to be changed on alternate rows
        self.ui.treeView.setAlternatingRowColors(True)
        
        # calling myTreeViewModelCreation method
        mymodel = self.myTreeViewModelCreation(self)
        
        # model is set for the Treeview
        self.ui.treeView.setModel(mymodel)
        
        # filling Data on passing Name, Contact_Number, City and Profession headers 
        # by calling myaddition method
        self.myaddition(mymodel, 'Divya', '9857611111','Delhi','Scientist')
        self.myaddition(mymodel, 'Sargam', '9857622222','Kolkata','HouseWife')
        self.myaddition(mymodel, 'Sugandh', '9857633333','Aligarh','Engineer')
        self.myaddition(mymodel, 'Munnu', '9857644444','Mumbai','Cricketer')
        self.show()
    
    def myTreeViewModelCreation(self, myparent):
        # creating a new item model with the initial rows = 0, initial columns = 4 and specified parent
        mymodel = QStandardItemModel(0, 4, myparent)
        
        #Sets the data in the header for the provided section(0, 1, 2 and 3) 
        #with the specified orientation as Horizontal to the 
        # given value (Name, Contact_Number, City and Profession).
        # if the header's data is updated will be returning True
        mymodel.setHeaderData(0, Qt.Horizontal, "Name")
        mymodel.setHeaderData(1, Qt.Horizontal, "Contact_Number")
        mymodel.setHeaderData(2, Qt.Horizontal, "City")
        mymodel.setHeaderData(3, Qt.Horizontal, "Profession")
        
        # returning the item model
        return mymodel
    
    def myaddition(self,mymodel, myname, mycontactnumber, mycity, myprofession):
        # insetRow for displaying the data 
        mymodel.insertRow(0)
        # index(): gives the QModelIndex associated with the item
        # setData(): set the specified value (which are passed as arguments)
        # to the item's data for the given role. 
        # ----> Also, setData() is in charge of changing the details 
        # information of a role related to a QModelIndex.
        mymodel.setData(mymodel.index(0, self.Name), myname)
        mymodel.setData(mymodel.index(0, self.Contact_Number), mycontactnumber)
        mymodel.setData(mymodel.index(0, self.City), mycity)
        mymodel.setData(mymodel.index(0, self.Profession), myprofession)

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyTreeView()
    w.show()
    sys.exit(app.exec_())