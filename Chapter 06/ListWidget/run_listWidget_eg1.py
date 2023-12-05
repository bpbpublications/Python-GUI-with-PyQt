import sys
from PyQt5.QtWidgets import QMainWindow,QAbstractItemView, QApplication,QListWidgetItem,QCheckBox,QHBoxLayout,QLabel,QWidget, QMessageBox
from PyQt5.QtGui import QPalette, QColor
from listWidget_eg1 import *

class MyListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        self.myui.lw_Add.clicked.connect(self.btn1)
        self.myui.lw_Count.clicked.connect(self.btn2)
        self.myui.lw_Clear.clicked.connect(self.btn3)
        self.myui.lw_SortAsc.clicked.connect(self.btn4)
        self.myui.lw_Toggle.clicked.connect(self.btn5)
        self.myui.lw_SetCurrentItem.clicked.connect(self.btn6)
        self.myui.lw_AddCheckBox.clicked.connect(self.btn7)
        self.myui.lw1.setDragEnabled(True) # allowing dragenabled property of lw1 to be True
        self.myui.lw2.setDragEnabled(False)# allowing dragenabled property of lw2 to be False
        self.myui.lw1.setDragDropMode(QAbstractItemView.DragDrop) # setting dag drop mode of lw1
        self.myui.lw1.setAcceptDrops(False)# allowing acceptDrops property of lw1 to be False
        self.myui.lw2.setAcceptDrops(True)# allowing acceptDrops property of lw2 to be True
        self.show()
        
        # Add items to the list widget
        for loop in range(5):
            item = QListWidgetItem()
            item.setText("    Itemmno: {}".format(loop+1))
            self.myui.lw1.addItem(item)

    def btn1(self):
        # creating an instance of QListWidgetItem
        item = QListWidgetItem()
        # setting the text
        item.setText("    Itemmno: {}".format(self.myui.lw1.count()+1))
        # adding it to the listWidget using addItem method
        self.myui.lw1.addItem(item)
        
        # Add multiple items to the list widget
        mylist_items = ["    Zeeshan", "    Vicky", "    Abdul"]
        for list_item in mylist_items:
            myinst_item = QListWidgetItem()
            myinst_item.setText(list_item)
            self.myui.lw1.addItem(myinst_item)
        
    def btn2(self):
        QMessageBox.information(None, 'Item Count Title', "The number of items in the list is {}".format(self.myui.lw1.count()))
        
    def btn3(self):
        # clearing all the listWidget items
        self.myui.lw1.clear()
        
    def btn4(self):
        # Sorting the listWidget items in ascending order
        self.myui.lw1.sortItems(QtCore.Qt.AscendingOrder)
        
    def btn5(self):
        # Enable alternate row colors
        self.myui.lw1.setAlternatingRowColors(True)
        mypalette = self.myui.lw1.palette()
        mypalette.setColor(QPalette.AlternateBase, QColor("lightgray"))
        self.myui.lw1.setPalette(mypalette)
    
    def btn6(self):
        myselect_item = self.myui.lw1.item(4) # Selecting 5th item of the list
        self.myui.lw1.setCurrentItem(myselect_item) # will set the current item of the listWidget
        
        # Emitting the itemSelectionChanged signal
        self.myui.lw1.itemSelectionChanged.emit() # signal will be emitted when the selection of items in the list widget is changed

        
    def btn7(self):
        #Create a checkbox for each ListWidget item
        for myitm in range(self.myui.lw1.count()):
            myitem = self.myui.lw1.item(myitm)
            mycheck_box = QCheckBox()
            self.myui.lw1.setItemWidget(myitem, mycheck_box)
    
    

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyListWidget()
    w.show()
    sys.exit(app.exec_())