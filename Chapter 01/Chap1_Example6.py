import sys # CL1
from PyQt5.QtWidgets import QWidget, QApplication # CL2

class GUIWindow(QWidget):
    def __init__(self):
        super(GUIWindow, self).__init__() # CL6
        self.initializationUI() # CL7
    
    def initializationUI(self):
        self.setGeometry(300,300,400,300) # CL10
        self.setWindowTitle("Basic GUI Form") # CL9
        self.show() # CL8

if __name__ == '__main__':
    myapp = QApplication(sys.argv) # CL3
    mywindow = GUIWindow() #CL4
    sys.exit(myapp.exec_()) # CL5
