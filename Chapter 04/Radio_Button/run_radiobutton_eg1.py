import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from radiobutton_eg1 import * # RBEG1_1

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rbtn_apple.toggled.connect(lambda:self.myselfcheck(self.ui.rbtn_apple)) # RBEG1_2
        self.ui.rbtn_orange.toggled.connect(lambda:self.myselfcheck(self.ui.rbtn_orange)) # RBEG1_3
        self.ui.rbtn_banana.toggled.connect(lambda:self.myselfcheck(self.ui.rbtn_banana)) # RBEG1_4
        self.show()

    def myselfcheck(self, myradiobutton): # RBEG1_5
        if myradiobutton.isChecked(): # RBEG1_6
            self.ui.lbldisplay.setText(myradiobutton.text() + " is selected") # RBEG1_7

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())