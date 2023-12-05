import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QKeySequenceEdit
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt

class MyKeySequence(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QKeySequenceEdit widget
        self.my_key_edit = QKeySequenceEdit(self)
        self.my_key_edit.setKeySequence(QKeySequence(Qt.CTRL + Qt.Key_H))
        self.my_key_edit.keySequenceChanged.connect(self.my_handle_key_sequence_changed)
        self.setCentralWidget(self.my_key_edit)

    # Slot method called when the key sequence is changed
    def my_handle_key_sequence_changed(self, my_key_seq):
        print(f"My New key sequence: {my_key_seq.toString()}")

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    mywidget = MyKeySequence()
    mywidget.show()
    myapp.exec_()
