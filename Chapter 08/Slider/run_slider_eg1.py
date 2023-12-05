import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QSlider, QWidget
from PyQt5.QtGui import QFont

class MySliderWidget(QWidget):

    def __init__(self):
        super().__init__()

        # Creating a label object for the horizontal slider
        myhlabel = QLabel('Horizontal')
        myhlabel.setAlignment(Qt.AlignCenter)

        # Creating a horizontal slider object
        myhslider = QSlider(Qt.Horizontal)
        myhslider.setFocusPolicy(Qt.NoFocus)
        myhslider.setRange(0, 100)
        myhslider.setValue(30)
        myhslider.setTickInterval(10)
        myhslider.setTickPosition(QSlider.TicksBelow)

        # Create a label object for the vertical slider
        myvlabel = QLabel('Vertical')
        myvlabel.setAlignment(Qt.AlignCenter)
        
        # Creating a vertical slider
        myvslider = QSlider(Qt.Vertical)
        myvslider.setFocusPolicy(Qt.NoFocus)
        myvslider.setRange(0, 100)
        myvslider.setValue(40)
        myvslider.setTickInterval(10)
        myvslider.setTickPosition(QSlider.TicksLeft)

        # Creating a label object to show the value of the horizontal slider
        myhvalue = QLabel(str(myhslider.value()))
        myhvalue.setAlignment(Qt.AlignCenter)
        
        # creating a font object for myhvalue and myvvalue
        myfont = QFont()
        myfont.setPointSize(12)
        myfont.setBold(True)
        myhvalue.setFont(myfont)

        # Creating a label object to show the value of the vertical slider
        myvvalue = QLabel(str(myvslider.value()))
        myvvalue.setAlignment(Qt.AlignCenter)
        myvvalue.setFont(myfont)

        # Creating a grid object layout to organize the widgets
        mygrid = QGridLayout()
        mygrid.setSpacing(10)

        # Adding the horizontal slider and label object to the grid
        mygrid.addWidget(myhlabel, 0, 0)
        mygrid.addWidget(myhslider, 1, 0)
        mygrid.addWidget(myhvalue, 2, 0)

        # Adding the vertical slider and label object to the grid
        mygrid.addWidget(myvlabel, 0, 1)
        mygrid.addWidget(myvslider, 1, 1)
        mygrid.addWidget(myvvalue, 2, 1)

        # Connecting the valueChanged signal of myhslider object to its label obj myhvalue
        myhslider.valueChanged.connect(lambda value: myhvalue.setText(str(value)))

        # Connecting the valueChanged signal of myvslider object  to its label obj myvvalue
        myvslider.valueChanged.connect(lambda value: myvvalue.setText(str(value)))

        self.setLayout(mygrid)

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('My Sliders and Labels eg')
        self.show()

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myslider_widget = MySliderWidget()
    sys.exit(myapp.exec_())
