import sys 
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox # RUCA1
from user_credential_app import * # RUCA2

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.myui = Ui_Form() # RUCA3
        self.myui.setupUi(self) # RUCA4
        self.myui.mybtn_confirm.clicked.connect(self.myuser_credentials_check) # RUCA5
        self.show() # RUCA6
    
    def myuser_credentials_check(self):
        if(self.myui.lineEdit_username.text() == ""): # RUCA7
            QMessageBox.information(self, "Enter Username", "Username cannot be  empty!", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        if(self.myui.lineEdit_username.text() != "" and self.myui.lineEdit_password.text() == ""): # RUCA8
            QMessageBox.information(self, "Enter Password", "Password cannot be empty!", QMessageBox.Ok, QMessageBox.Ok)
            return
        
        if(self.myui.lineEdit_username.text() == self.myui.lineEdit_password.text() ): # RUCA9
            QMessageBox.information(self, "Credentials check", "Welcome", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Credentials check", "Credentials does not match", QMessageBox.Ok, QMessageBox.Ok)
    
if __name__ == '__main__':
    myapp = QApplication(sys.argv) # RUCA10
    mywindow = MyWidget() # RUCA11
    sys.exit(myapp.exec_()) # RUCA12
