import sys
import re
from PyQt5.QtWidgets import QMainWindow,QApplication, QFontDialog
from plaintextedit_eg1 import *

class MyPlainTextEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)
        # setting the placeholder text in the QPlainTexEdit object
        self.myui.plainTextEdit.setPlaceholderText("Kindly enter any plain text")
        self.myui.plainTextEdit.textChanged.connect(self.mytextchanged)
        self.myui.plainTextEdit.cursorPositionChanged.connect(self.my_on_cursor_position_changed)
        self.myui.mybtn.clicked.connect(self.my_btn1)
        # Connecting the blockCountChanged signal to the my_on_block_count_changed slot
        self.myui.plainTextEdit.blockCountChanged.connect(self.my_on_block_count_changed)

        self.show()

    def my_btn1(self):
        # appending the text to QPlainTextEdit object
        self.myui.plainTextEdit.appendPlainText("Some Text is Added")
    
    def mytextchanged(self):
        self.myui.mylbl.setText("QPlainTextEdit signal is emitted")
    
    # Method for the cursorPositionChanged signal
    def my_on_cursor_position_changed(self):
        mycursor = self.myui.plainTextEdit.textCursor()
        print("Cursor position is changed to column no.:", mycursor.position())
        
    # Method for the blockCountChanged signal
    def my_on_block_count_changed(self, my_new_block_count):
        print("Block count changed to:", my_new_block_count)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyPlainTextEdit()
    screen.show()
    sys.exit(app.exec_())