import sys
import re
from PyQt5.QtWidgets import QMainWindow,QApplication, QMessageBox
from PyQt5.QtGui import QFont
from lineedit_eg1 import *

class MyLineEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # LineEdit1 ----------------------------------------------------------------------
        
        # Set the maximum number of characters that can be entered
        self.myui.mylineEdit_1.setMaxLength(10)
        self.myui.mylineEdit_1.setFont(QFont("Calibri",16))
        self.myui.mylineEdit_1.setPlaceholderText("Enter username")
        
        # LineEdit2 ----------------------------------------------------------------------
        self.myui.mylineEdit_2.setPlaceholderText("Enter password")
        self.myui.mylineEdit_2.setEchoMode(self.myui.mylineEdit_2.Password)
        
        # LineEdit3 ----------------------------------------------------------------------
        self.myui.mylineEdit_3.setPlaceholderText("Enter email @ is must")
        # Connecting the textChanged signal to a custom function
        self.myui.mylineEdit_3.editingFinished.connect(self.myvalidate_email)
        
        # LineEdit4 ----------------------------------------------------------------------
        self.myui.mylineEdit_4.setInputMask('+99_99999_99999')
        
        # LineEdit5 ----------------------------------------------------------------------
        self.myui.mylineEdit_5.setText("Only Read Only Text")
        self.myui.mylineEdit_5.setReadOnly(True)
        
        # LineEdit6 ----------------------------------------------------------------------
        self.myui.mylineEdit_6.textChanged.connect(self.mytextchanged)

        self.show()
    
    def myvalidate_email(self):
        # Regex for valid email addresses
        myemail_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        # Getting the text from the QLineEdit widget
        myemail = self.myui.mylineEdit_3.text()

        # Checking if the email address is valid
        if not myemail_regex.match(myemail):
            # Set the input method to invalid if the email address is not valid
            self.myui.mylineEdit_3.setStyleSheet("border: 1px solid red")
            
            # Displaying an error message
            QMessageBox.warning(self, "Error!", "Email address is invalid")
            
            # focusing on the LineEdit if wrong email id is entered
            self.myui.mylineEdit_3.setFocus()
        else:
            # Set the input method to valid if the email address is valid
            self.myui.mylineEdit_3.setStyleSheet("border: 1px solid green")
    
    def mytextchanged(self, mytext):
        print("Changed contents: "+ mytext)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyLineEdit()
    screen.show()
    sys.exit(app.exec_())