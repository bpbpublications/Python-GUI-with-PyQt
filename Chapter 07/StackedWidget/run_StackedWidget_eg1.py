import sys
from PyQt5.QtWidgets import *

class MyStackedWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.listWidget = QListWidget()
        
        self.listWidget.insertItem(0,"Details")
        self.listWidget.insertItem(1,"Hobby")
        self.listWidget.insertItem(2,"Sex")
        
        # creating an instance of QWidget
        self.mystack1 = QWidget()
        self.mystack2 = QWidget()
        self.mystack3 = QWidget()
        
        self.mystack1UI()
        self.mystack2UI()
        self.mystack3UI()
        
        self.listWidget.currentRowChanged.connect(self.my_on_current_changed)
        
        self.mystackwidget = QStackedWidget(self)
        # Setting the current widget to the first one in the stack
        self.mystackwidget.setCurrentIndex(0)
        
        # adding the widgets to the QStackedWidget object
        self.mystackwidget.addWidget(self.mystack1)
        self.mystackwidget.addWidget(self.mystack2)
        self.mystackwidget.addWidget(self.mystack3)
        
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.listWidget)
        hbox.addWidget(self.mystackwidget)
        self.setLayout(hbox)
        self.show()
    
    # Connect the currentChanged signal to a slot
    def my_on_current_changed(self,index):
        print("The current widget is changed to index no:", index)
        self.mystackwidget.setCurrentIndex(index)
    
    def mystack1UI(self):
        #adding the widgets to the first stack
        mylayout1 = QFormLayout()
        mylayout1.addRow("Name",QLineEdit())
        mylayout1.addRow("Age",QLineEdit())
        mylayout1.addRow("City",QLineEdit())
        self.mystack1.setLayout(mylayout1)
		
    def mystack2UI(self):
        #adding the widgets to the second stack
        mylayout2 = QFormLayout()
        mylayout2.addRow(QCheckBox("Playing Chess"))
        mylayout2.addRow(QCheckBox("Cooking"))
        mylayout2.addRow(QCheckBox("Reading Books"))
        self.mystack2.setLayout(mylayout2)
		
    def mystack3UI(self):
        #adding the widgets to the third stack
        mylayout3 = QHBoxLayout()
        mylayout3.addWidget(QLabel("Sex: "))
        mylayout3.addWidget(QRadioButton("Male"))
        mylayout3.addWidget(QRadioButton("Female"))
        self.mystack3.setLayout(mylayout3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyStackedWidget()
    w.show()
    sys.exit(app.exec_())

