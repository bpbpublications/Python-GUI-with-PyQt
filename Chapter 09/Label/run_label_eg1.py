import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPixmap
from label_eg1 import *

class MyLabel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # displaying rich text
        self.myui.mylbl1.setText("Displaying plain text.")
        
        # displaying rich text
        self.myui.mylbl2.setText("<font color='green'>Displaying rich text.</font>")
        
        self.myui.lineEdit.setText("Buddy with Label")
        # setting the buddy property of the label to the LineEdit object
        self.myui.mylbl2.setBuddy(self.myui.lineEdit)
        
        # displaying image
        self.myui.mylbl3.setPixmap(QPixmap("myimage.jpg"))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyLabel()
    screen.show()
    sys.exit(app.exec_())