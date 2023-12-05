import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton,QFormLayout, QLineEdit,QHBoxLayout,QRadioButton,QMessageBox, QTabWidget, QWidget
from tabWidget_eg1 import *

class MyTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        self.myui.tabWidget.clear()
        self.myui.tabWidget.setTabsClosable(True) # Allow tabs to be closed by the user
        self.myui.tabWidget.tabCloseRequested.connect(self.handleCloseTab) # Connect the tabCloseRequested signal to the handleCloseTab slot

        # adding 3 LineEdit widget to tab1 and adding it to tabwidget
        mylayout = QFormLayout()
        mylayout.addRow("Name: ",QLineEdit())
        mylayout.addRow("PhoneNo: ",QLineEdit())
        mylayout.addRow("Age: ",QLineEdit())
        self.tab1 = QWidget()
        self.tab1.setLayout(mylayout)
        
        # Creating Tab1 and adding widgets
        self.myui.tabWidget.addTab(self.tab1, "Tab 1")
        
        # Adding only 1 QLineEdit to tab2 of tabwidget
        self.myui.tabWidget.addTab(QLineEdit(), "Tab 2")
        
        # Adding 2 Radio Buttons to tab3 of tabwidget
        mylayout2 = QFormLayout()
        mysex = QHBoxLayout()
        mysex.addWidget(QRadioButton("Male"))
        mysex.addWidget(QRadioButton("Female"))
        mylayout2.addRow("Sex",mysex)
        self.tab3 = QWidget()
        self.tab3.setLayout(mylayout2)
        # Creating Tab3 and adding widgets
        self.myui.tabWidget.addTab(self.tab3, "Tab 3")

        # Change the tab position to the bottom
        self.myui.tabWidget.setTabPosition(QTabWidget.South)

        # Disabling the second tab
        self.myui.tabWidget.setTabEnabled(1, False)

        # Setting the current tab as Tab 3
        self.myui.tabWidget.setCurrentIndex(2)
        self.show()

    def handleCloseTab(self, index):
        """
        Handling the tabCloseRequested signal by prompting the user to save any unsaved changes
        """
        mytab_widget = self.myui.tabWidget.widget(index)
        if isinstance(mytab_widget, QLineEdit): # if closing QLineEdit tab
            myresult = QMessageBox.question(self, "Unsaved Changes", "Do you want to save your changes and remove?", QMessageBox.Save | QMessageBox.Cancel)
            if myresult == QMessageBox.Save:
                # Save the changes
                print("Save")
                self.myui.tabWidget.removeTab(index)
                pass
            else:
                # Cancel the tab close request
                print("Cancelled")
                return
        else:
            # No unsaved changes, just remove the tab
            self.myui.tabWidget.removeTab(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyTabWidget()
    w.show()
    sys.exit(app.exec_())
