import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QTextEdit, QMenu, QMenuBar, QAction
from mdiarea_eg1 import *

class MyMdiArea(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myui = Ui_MainWindow()
        self.myui.setupUi(self)

        # Setting QMDIArea object as the central widget
        # mdi = QMdiArea()
        self.setCentralWidget(self.myui.mdiArea)

        # Adding three QTextEdit sub-windows to the QMdiArea object
        mysub1 = QMdiSubWindow()
        mysub1.setWidget(QTextEdit())
        mysub1.setWindowTitle("Window 1")
        self.myui.mdiArea.addSubWindow(mysub1)

        mysub2 = QMdiSubWindow()
        mysub2.setWidget(QTextEdit())
        mysub2.setWindowTitle("Window 2")
        self.myui.mdiArea.addSubWindow(mysub2)

        mysub3 = QMdiSubWindow()
        mysub3.setWidget(QTextEdit())
        mysub3.setWindowTitle("Window 3")
        self.myui.mdiArea.addSubWindow(mysub3)

        # Creating a menu bar instance and adding two actions to it
        mymenubar = self.menuBar()
        mywindowMenu = mymenubar.addMenu("Display As")
        mycascadeAction = QAction("Cascade", self)
        mycascadeAction.triggered.connect(self.myui.mdiArea.cascadeSubWindows)
        mywindowMenu.addAction(mycascadeAction)
        mytileAction = QAction("Tile", self)
        mytileAction.triggered.connect(self.myui.mdiArea.tileSubWindows)
        mywindowMenu.addAction(mytileAction)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = MyMdiArea()
    screen.show()
    sys.exit(app.exec_())
