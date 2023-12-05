import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import *
from datetimeedit_eg1 import *

class MyDateTimeEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # setting the date and time for the widget
        self.myui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        # Setting the display format for the QDateTimeEdit widget
        self.myui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")

        # Setting the calendar popup to be enabled
        self.myui.dateTimeEdit.setCalendarPopup(True)

        # Setting the maximum and minimum dates that can be selected
        self.myui.dateTimeEdit.setMaximumDate(QDate.currentDate().addYears(1))
        self.myui.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-365))

        # Connecting the signals to their respective handlers
        self.myui.dateTimeEdit.timeChanged.connect(self.my_handle_time_changed)
        self.myui.dateTimeEdit.dateChanged.connect(self.my_handle_date_changed)
        # signal is emitted on button click and connected to the method my_btn1
        self.myui.mybtn.clicked.connect(self.my_btn1)
        
        self.show()

    def my_btn1(self):
        self.myui.mylbl2.setText("Displaying Date and Time to: " + str(self.myui.dateTimeEdit.dateTime()))
    
    def my_handle_time_changed(self, time):
        self.myui.mylbl2.setText("Time changed to: " + time.toString())

    def my_handle_date_changed(self, date):
        self.myui.mylbl2.setText("Date changed to: " + date.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyDateTimeEdit()
    screen.show()
    sys.exit(app.exec_())