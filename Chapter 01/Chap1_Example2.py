import sys
from PyQt5.QtWidgets import QWidget, QApplication

myapp = QApplication(sys.argv)
mywindow = QWidget()
mywindow.setWindowTitle('Basic GUI Form') # BG1
mywindow.show()
sys.exit(myapp.exec_())
