import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QTableWidgetItem,QHeaderView
from PyQt5.QtGui import QPalette, QColor
from tableWidget_eg1 import *

class MyTableWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Seting the number of rows and columns of QTableWidget object
        self.myui.tableWidget.setRowCount(2)
        self.myui.tableWidget.setColumnCount(3)

        # Set the horizontal headers for the table
        self.myui.tableWidget.setHorizontalHeaderLabels(["Name", "Age", "Sex"])

        # Adding some data to the QTableWidget object
        self.myui.tableWidget.setItem(0,0,QTableWidgetItem("Saurabh"))
        self.myui.tableWidget.setItem(0,1,QTableWidgetItem("34"))
        self.myui.tableWidget.setItem(0,2,QTableWidgetItem("Male"))
        self.myui.tableWidget.setItem(1,0,QTableWidgetItem("Aditi"))
        self.myui.tableWidget.setItem(1,1,QTableWidgetItem("30"))
        self.myui.tableWidget.setItem(1,2,QTableWidgetItem("Female"))
        
        #for fitting the QTableWidget object horizontally
        self.myui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.myui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # connect signals to slots
        self.myui.tableWidget.cellChanged.connect(self.mycellChanged)
        self.myui.tableWidget.cellClicked.connect(self.mycellClicked)
        self.myui.tableWidget.cellEntered.connect(self.mycellEntered)
        self.myui.tableWidget.cellPressed.connect(self.mycellPressed)
        
        # clicked signal of button connecting to slot btn_click
        self.myui.btn_Add.clicked.connect(self.btn_click)
        
        self.show()
    
    # defining the slots
    def mycellChanged(self, myrow, mycol):
        print("Cell is changed at row {0}, col {1}".format(myrow, mycol))

    def mycellClicked(self, myrow, mycol):
        print("Cell is clicked at row {0}, col {1}".format(myrow, mycol))

    def mycellEntered(self, myrow, mycol):
        print("Cell is entered at row {0}, col {1}".format(myrow, mycol))

    def mycellPressed(self, myrow, mycol):
        print("Cell is pressed at row {0}, col {1}".format(myrow, mycol))
    
    def btn_click(self): 
        # inserting a new row at the end of the QTableWidget object by taking rowCount
        myrow = self.myui.tableWidget.rowCount()
        self.myui.tableWidget.insertRow(myrow)

        # adding fixed name, age and sex to display to the user of inserting new data
        self.myui.tableWidget.setItem(myrow, 0, QTableWidgetItem("Divya"))
        self.myui.tableWidget.setItem(myrow, 1, QTableWidgetItem("36"))
        self.myui.tableWidget.setItem(myrow, 2, QTableWidgetItem("Male"))

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyTableWidget()
    w.show()
    sys.exit(app.exec_())