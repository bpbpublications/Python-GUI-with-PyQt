import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu
from commandlinkbutton_eg1 import *


class MyCommandlinkButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Creating 2 QActions object
        mya1 = QAction("First Action", self)
        mya3 = QAction("Third Action", self)
        # Creating QMenu object
        mymenu = QMenu()  
        # adding 2 actions as a list to menu object
        mymenu.addActions([mya1, mya3])
  
        # Creating another QAction
        mya2 = QAction("Second Action", self)
  
        # inserting myact2 object before mya3 object
        mymenu.insertAction(mya3, mya2)
  
        # we are setting menu object to the command link button
        self.ui.clb_btn1.setMenu(mymenu)
        # initially counter is set as 0
        self.mycount = 0 
        
        # connecting clicked signal of command link button object to slot myincrement(passing
        # my count as a parameter) and we are using lambda expression
        self.ui.clb_btn2.clicked.connect(lambda: self.myincrement(self.mycount))
        
        self.show()
    
    def myincrement(self,mycount): # taking mycount as another parameter
        self.mycount +=1 # incrementing the counter by one.
        self.ui.mylbl2.setText("Text Description: : " + str(self.mycount)) # displaying the counter value to label object

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyCommandlinkButton()
    w.show()
    sys.exit(app.exec_())