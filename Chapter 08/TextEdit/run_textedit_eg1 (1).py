import sys
import re
from PyQt5.QtWidgets import QMainWindow,QApplication, QFontDialog
from textedit_eg1 import *

class MyTextEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        self.myui.mybtn1.clicked.connect(self.my_btn1)
        self.myui.mybtn2.clicked.connect(self.my_btn2)
        self.myui.mybtn3.clicked.connect(self.my_btn3)
        
        # replacing the text of TextEdit object with 'Hello'
        self.myui.textEdit.setText("Hello")
        
        self.show()
    
    def my_btn1(self):
        # prompting the user to select the font family, font style, size 
        myfont, imok = QFontDialog.getFont()
        # on pressing Ok replacing the text in the TextEdit object with the selected font
        if imok:
            self.myui.textEdit.setCurrentFont(myfont)
    
    def my_btn2(self):
        # replacing the text of TextEdit object with plain text on button click
        self.myui.textEdit.setPlainText("Hi Friends!\nWelcome to study PyQt5 textEdit widget")
    
    def my_btn3(self):
        # replacing the text of TextEdit object with text formatted by providing an html interface on button click
        self.myui.textEdit.setHtml("<font color='green' size='7'>Hi Friends!\nHello</font>")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyTextEdit()
    screen.show()
    sys.exit(app.exec_())