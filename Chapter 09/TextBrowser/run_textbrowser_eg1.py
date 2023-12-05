import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QTextCursor
from textbrowser_eg1 import *

class MyTextBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        self.myui.textBrowser.setOpenExternalLinks(True)
        self.myui.textBrowser.setStyleSheet('font-size: 24px;')
        
        self.myui.btn.clicked.connect(self.my_btn_clickme)
        
        self.show()
    
    def my_btn_clickme(self):
        self.myui.textBrowser.moveCursor(QTextCursor.Start)
        self.myui.textBrowser.append('Displaying Bolloywood movies list')
        self.myui.textBrowser.append('<a href=https://en.wikipedia.org/wiki/List_of_Hindi_films_of_2023>Bollywood Movies 2023</a>')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyTextBrowser()
    screen.show()
    sys.exit(app.exec_())