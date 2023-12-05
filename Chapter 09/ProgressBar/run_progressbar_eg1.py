import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from progressbar_eg1 import *

class MyProgressBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)

    def my_start_counting(self):
        self.myui.progressBar.setRange(0, 1000)
        self.myui.progressBar.setValue(0)
        for i in range(1, 1001):
            self.myui.progressBar.setValue(i)
            self.myui.mylbl.setText(f"Count No is: {i}")
            QApplication.processEvents() # processing any pending events for updating the UI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myprogress_bar_widget = MyProgressBar()
    myprogress_bar_widget.show()
    myprogress_bar_widget.my_start_counting()
    sys.exit(app.exec_())