import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)

# Creating an instance of QWidget and will be the main window of the application
mywidget = QWidget()

# Setting the size and position of the screen widget
mywidget.resize(350, 150)
mywidget.move(250, 250)

# Setting the widget title
mywidget.setWindowTitle("Basic QWidget Eg")

# Display the widget on the screen
mywidget.show()

sys.exit(app.exec_())
