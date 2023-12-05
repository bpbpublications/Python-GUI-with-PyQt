import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from calendarwidget_eg1 import *

class MyCalendarWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # Connect the calendar's selectionChanged signal to the update_label method
        self.myui.calendarWidget.selectionChanged.connect(self.my_display_date)

        self.show()
    
    # Define a method to set the label object text with the selected date
    def my_display_date(self):
        self.myui.mylbl.setText('Selected date is: {}'.format(self.myui.calendarWidget.selectedDate().toString()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyCalendarWidget()
    screen.show()
    sys.exit(app.exec_())