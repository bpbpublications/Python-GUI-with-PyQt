import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QPalette, QColor
from treeWidget_eg1 import *

class MyTreeWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Initially setting the column count of the treeWidget object to 2
        self.myui.treeWidget.setColumnCount(2)

        # Set the header labels for 2 columns
        self.myui.treeWidget.setHeaderLabels(["Name", "Age"])

        # Adding items to the treeWidget object
        myitem1 = QTreeWidgetItem(["Saurabh", "34"])
        myitem2 = QTreeWidgetItem(["Nilesh", "42"])
        myitem3 = QTreeWidgetItem(["Priyanka", "30"])
        myitem4 = QTreeWidgetItem(["Pranav", "31"])
        myitem5 = QTreeWidgetItem(["Papa", "61"])
        myitem6 = QTreeWidgetItem(["Mummy", "60"])
        
        # For TreeWidget1
        self.myui.treeWidget.addTopLevelItem(myitem1)
        self.myui.treeWidget.addTopLevelItem(myitem2)
        self.myui.treeWidget.addTopLevelItem(myitem3)
        self.myui.treeWidget.addTopLevelItem(myitem4)
        self.myui.treeWidget.addTopLevelItem(myitem5)
        self.myui.treeWidget.addTopLevelItem(myitem6)
        
        # Connecting the itemClicked signal to the handle_item_click method
        self.myui.treeWidget.itemClicked.connect(self.myhandle_item_click)

        # Connecting the itemDoubleClicked signal to the handle_item_double_click method
        self.myui.treeWidget.itemDoubleClicked.connect(self.myhandle_item_double_click)

        # Connecting the itemActivated signal to the handle_item_activation method
        self.myui.treeWidget.itemActivated.connect(self.myhandle_item_activation)
        
        # For TreeWidget2
        # Setting the column count to 1
        self.myui.treeWidget_2.setColumnCount(1)

        # Create the top-level items
        self.myitemA = QTreeWidgetItem(self.myui.treeWidget_2, ["Item A"])
        self.myitemB = QTreeWidgetItem(self.myui.treeWidget_2, ["Item B"])
        self.myitemC = QTreeWidgetItem(self.myui.treeWidget_2, ["Item C"])

        # Create the child items for Item A
        self.myitemA1 = QTreeWidgetItem(self.myitemA, ["Item A_1"])
        self.myitemA2 = QTreeWidgetItem(self.myitemA, ["Item A_2"])

        # Create the child items for Item B
        self.myitemB1 = QTreeWidgetItem(self.myitemB, ["Item B_1"])
        self.myitemB2 = QTreeWidgetItem(self.myitemB, ["Item B_2"])

        # Create the child items for Item C
        self.myitemC1 = QTreeWidgetItem(self.myitemC, ["Item C_1"])
        self.myitemC2 = QTreeWidgetItem(self.myitemC, ["Item C_2"])

        # Connect the itemExpanded and itemCollapsed signals to their respective slots
        self.myui.treeWidget_2.itemExpanded.connect(self.my_on_item_expanded)
        self.myui.treeWidget_2.itemCollapsed.connect(self.my_on_item_collapsed)

        self.show()
    
    # Method to handle item click event
    def myhandle_item_click(self,item, column):
        print("An Item is clicked:", item.text(column))

    # Method to handle item double click event
    def myhandle_item_double_click(self,item, column):
        print("An Item is double clicked:", item.text(column))

    # Method to handle item activation event
    def myhandle_item_activation(self,item, column):
        print("An Item is activated:", item.text(column))
    
    def my_on_item_expanded(self, item):
        # Performing some action when an item is expanded
        print(f"{item.text(0)} was expanded")

    def my_on_item_collapsed(self, item):
        # Performing some action when an item is collapsed
        print(f"{item.text(0)} was collapsed")

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyTreeWidget()
    w.show()
    sys.exit(app.exec_())