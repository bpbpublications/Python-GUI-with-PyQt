import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel, QPushButton, QVBoxLayout,QHBoxLayout,QGroupBox,QWidget
from scrollAreaWidget_eg1 import *

class MyScrollAreaWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)

        self.myui.top_widget = QWidget()
        self.myui.top_layout = QVBoxLayout()
        
        # Step-1: Already a QScrollArea object was created in Qt Designer
        
        # Step-2 : Creation of 8 different child widgets (groupbox having label and pushbutton) within the scroll area 
        for loop in range(8):
            # creating groupbox widget instance
            self.myui.group_box = QGroupBox()
            # setting the groupbox title
            self.myui.group_box.setTitle('GroupBox Item No. {0}'.format(loop))
            # creating a hboxlayout instance to the groupox widget
            self.myui.layout = QHBoxLayout(self.myui.group_box)

            # creating a label object, setting the text and adding it to the hboxlayout instance
            self.myui.label = QLabel()
            self.myui.label.setText('Label For Item No. {0}'.format(loop))
            self.myui.layout.addWidget(self.myui.label)
            
            # creating a [pushbutton] object, setting the text and size and adding it to the hboxlayout instance
            self.myui.push_button = QPushButton()
            self.myui.push_button.setText('Display Button')
            self.myui.push_button.setFixedSize(100, 32)
            self.myui.layout.addWidget(self.myui.push_button)

            # adding the groupbox object to the vboxlayout
            self.myui.top_layout.addWidget(self.myui.group_box)
        
        # adding the vbox layout to the child widget
        self.myui.top_widget.setLayout(self.myui.top_layout)
        
        # Step-3: Setting the widget property of the QScrollArea object to the child widget 
        self.myui.scrollArea.setWidget(self.myui.top_widget)
        
        # Step-4: Already the QScrollarea object is added to the vboxlayout in Qt Designer
        
        self.show()
        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyScrollAreaWidget()
    w.show()
    sys.exit(app.exec_())
