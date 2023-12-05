import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import Qt
from scrollbar_eg1 import *

class MyScrollbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        
        # signal is emitted on button click and connected to the method my_btn1
        self.myui.btn1.clicked.connect(self.my_btn1)
        self.myui.btn2.clicked.connect(self.my_btn2)
        self.myui.btn3.clicked.connect(self.my_btn3)

        # Set some initial text to show in the text edit
        self.myui.mytextEdit.setPlainText("PyQt5 is a Python binding for the Qt GUI toolkit, which allows developers to create desktop applications with rich graphical user interfaces. It provides access to a wide range of Qt classes and functions, making it possible to create applications that are portable across different platforms, including Windows, Linux, and macOS. PyQt5 also includes tools for creating custom widgets and interfaces, and supports advanced features like multithreading, network programming, and OpenGL. Overall, PyQt5 is a powerful and flexible framework for building desktop applications using Python. Tkinter is a built-in Python GUI (Graphical User Interface) toolkit that provides developers with a set of widgets, such as buttons, labels, text boxes, and menus, for building desktop applications. It is based on the Tcl/Tk GUI toolkit and provides a simple and easy-to-use interface for creating cross-platform applications that run on Windows, Linux, and macOS. With Tkinter, developers can create event-driven applications that respond to user input, such as mouse clicks and keyboard events. It also provides tools for creating custom dialogs, message boxes, and other types of pop-up windows.Tkinter supports a wide range of features, such as internationalization, drag-and-drop support, and support for various font types and colors. It also provides tools for creating animated graphics, simple games, and multimedia applications.Overall, Tkinter is a powerful and flexible toolkit for creating desktop applications using Python. Its simplicity and cross-platform support make it a popular choice for developers who want to create simple GUI applications without the overhead of more complex frameworks.")
        
    def my_btn1(self):
        # set the text wrap mode to NoWrap
        self.myui.mytextEdit.setLineWrapMode(QTextEdit.NoWrap)
    def my_btn2(self):
        # set the text wrap mode to WidgetWidth
        self.myui.mytextEdit.setLineWrapMode(QTextEdit.WidgetWidth)
    def my_btn3(self):
        # set the text wrap mode to FixedPixelWidth
        self.myui.mytextEdit.setLineWrapMode(QTextEdit.FixedPixelWidth)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywidget = MyScrollbar()
    mywidget.show()
    sys.exit(myapp.exec_())
