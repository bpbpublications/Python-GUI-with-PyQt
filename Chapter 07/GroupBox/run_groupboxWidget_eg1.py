import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from groupboxWidget_eg1 import *

class MyGroupBoxWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        self.myui.groupBox.setCheckable(True)
        self.myui.groupBox.setChecked(False)
        
        # Connect the group box's toggled signal to the handle_toggled slot
        self.myui.groupBox.toggled.connect(self.mytoggle)
        
        self.show()
    
    def mytoggle(self,mychecked):
        print(mychecked)
        # Updating the label based on GroupBox checked status
        if mychecked:
            self.myui.lbl1.setText("Label1 On")
            self.myui.lbl1.setStyleSheet("QLabel { color : green; }")
            self.myui.lbl2.setText("Label2 Off")
            self.myui.lbl2.setStyleSheet("QLabel { color : red; }")
        else:
            self.myui.lbl2.setText("Label2 On")
            self.myui.lbl2.setStyleSheet("QLabel { color : green; }")
            self.myui.lbl1.setText("Label1 Off")
            self.myui.lbl1.setStyleSheet("QLabel { color : red; }")
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyGroupBoxWidget()
    w.show()
    sys.exit(app.exec_())
