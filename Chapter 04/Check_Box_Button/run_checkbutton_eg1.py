import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from checkbutton_eg1 import * # CBEG1_1

class MyCheckButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.myfruits = {'apple':0, 'orange':0, 'banana':0, 'pear':0} # CBEG1_2
        self.ui.chk_Apple.stateChanged.connect(lambda:self.myselfcheck(self.ui.chk_Apple)) # CBEG1_3
        self.ui.chk_Orange.stateChanged.connect(lambda:self.myselfcheck(self.ui.chk_Orange)) # CBEG1_4
        self.ui.chk_Banana.stateChanged.connect(lambda:self.myselfcheck(self.ui.chk_Banana)) # CBEG1_5
        self.ui.chk_Pear.stateChanged.connect(lambda:self.myselfcheck(self.ui.chk_Pear)) # CBEG1_6
        self.show()

    def myselfcheck(self, mychkbutton): # CBEG1_7
        if self.ui.chk_Apple.text() == "Apple" :  # CBEG1_8
            if self.ui.chk_Apple.isChecked(): # CBEG1_9
                self.myfruits['apple'] = 1
            else:
                self.myfruits['apple'] = 0

            self.mydisplay()
        
        if self.ui.chk_Orange.text() == "Orange" : # CBEG1_10
            if self.ui.chk_Orange.isChecked(): # CBEG1_11
                self.myfruits['orange'] = 1
            else:
                self.myfruits['orange'] = 0
            self.mydisplay()
        
        if self.ui.chk_Banana.text() == "Banana" : # CBEG1_12
            if self.ui.chk_Banana.isChecked(): # CBEG1_13
                self.myfruits['banana'] = 1
            else:
                self.myfruits['banana'] = 0
            self.mydisplay()
        
        if self.ui.chk_Pear.text() == "Pear" : # CBEG1_14
            if self.ui.chk_Pear.isChecked(): # CBEG1_15
                self.myfruits['pear'] = 1
            else:
                self.myfruits['pear'] = 0
            self.mydisplay()
    
    def mydisplay(self):
        checkedfruits =', '.join([mykey for mykey in self.myfruits.keys() if self.myfruits[mykey]== 1])  # CBEG1_16
        self.ui.lbl1.setText("You selected: " + checkedfruits) # CBEG1_17

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyCheckButton()
    w.show()
    sys.exit(app.exec_())