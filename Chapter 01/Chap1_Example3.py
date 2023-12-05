import sys
from PyQt5.QtWidgets import QWidget, QApplication

myapp = QApplication(sys.argv)
mywindow = QWidget()
mywindow.setWindowTitle('Basic GUI Form')
mywindow.resize(400,350) # RS1
mywindow.show()
sys.exit(myapp.exec_())
