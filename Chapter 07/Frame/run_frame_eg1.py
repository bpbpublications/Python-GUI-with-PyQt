import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel, QLineEdit, QPushButton,QVBoxLayout
from frame_eg1 import *

class MyFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Setting the frame shape to a box
        self.myui.frame.setFrameShape(QFrame.Box)
        
        # Setting the frame shadow to raised
        self.myui.frame.setFrameShadow(QFrame.Raised)
        
        # Setting the line width of the border to 2
        self.myui.frame.setLineWidth(2)
        
        # Creating a QVBoxLayout to hold our widgets
        layout = QVBoxLayout()

        # Adding a label and a line edit to the layout
        layout.addWidget(QLabel("My Name:"))
        layout.addWidget(QLineEdit())
        layout.addWidget(QPushButton("Frame Btn"))

        # Adding the layout to the frame
        self.myui.frame.setLayout(layout)

        self.show()
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyFrame()
    w.show()
    sys.exit(app.exec_())
