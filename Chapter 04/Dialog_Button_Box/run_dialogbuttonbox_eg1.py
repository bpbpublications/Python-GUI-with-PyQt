import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from dialogbuttonbox_eg1 import *
import webbrowser # importing webbrowser module

class MyDialogButtonBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
         # will act when OK button is clicked and displayinfo method is executed
        self.myui.buttonBox.accepted.connect(self.displayinfo)
        # will act when close button is clicked and will close the GUI form
        self.myui.buttonBox.rejected.connect(self.close) 
        # will act when help button is clicked
        self.myui.buttonBox.helpRequested.connect(lambda: webbrowser.open("https://auth0.com/blog/username-password-authentication/"))
        self.show()

    def displayinfo(self): 
        if self.myui.lineEdit_2.text() == "1234": # will check whether password is 1234
            # will display the message to the user
            self.myui.lbl_display.setText("Username with " + self.myui.lineEdit.text() + " has login successfully")
        else:
            # will display wring password if 1234 is not typed
            self.myui.lbl_display.setText("Wrong Password:") 
    
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyDialogButtonBox()
    w.show()
    sys.exit(app.exec_())