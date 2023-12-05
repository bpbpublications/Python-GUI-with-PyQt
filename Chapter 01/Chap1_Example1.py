import sys # L1
from PyQt5.QtWidgets import QWidget, QApplication # L2

myapp = QApplication(sys.argv) # L3
mywindow = QWidget() # L4
mywindow.show() # L5
sys.exit(myapp.exec_()) # L6
