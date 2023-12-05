import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel, QToolBox
from toolBoxWidget_eg1 import *

class MyToolBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        # creating an instance of QToolBox item
        self.myui.toolBox = QToolBox()
        # aading the widget QToolBox to the GridLayout
        self.myui.gridLayout.addWidget(self.myui.toolBox ,0,0)
        
        # Adding 3 Label items to the ToolBox widget
        mylbl1 = QLabel()
        self.myui.toolBox.addItem(mylbl1, "Item1")
        mylbl2 = QLabel()
        self.myui.toolBox.addItem(mylbl2, "Item3")
        mylbl3 = QLabel()
        self.myui.toolBox.addItem(mylbl3, "Item4")
     
        # disabling first tab --> 0
        self.myui.toolBox.setItemEnabled(0, False)

        # returns true if tems at specifiied positions are enabled
        print(self.myui.toolBox.isItemEnabled(0))
        print(self.myui.toolBox.isItemEnabled(1))

        # inserting Label at index specified position:1
        myitem = QLabel()
        self.myui.toolBox.insertItem(1, myitem, "Item2")
        
         # displaying number of items
        print(self.myui.toolBox.count())
        
         # mouseover tooltip at different tabs
        self.myui.toolBox.setItemToolTip(0, "This is Item1") # displaying at tab1
        self.myui.toolBox.setItemToolTip(1, "This is Item2") # displaying at tab2
        self.myui.toolBox.setItemToolTip(2, "This is Item3") # displaying at tab3
        self.myui.toolBox.setItemToolTip(3, "This is Item4") # displaying at tab4
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyToolBox()
    screen.show()
    sys.exit(app.exec_())