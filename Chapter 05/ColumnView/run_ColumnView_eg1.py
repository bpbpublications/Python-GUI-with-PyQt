import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel # importing QFileSystemModel
from ColumnView_eg1 import *
from PyQt5.QtCore import QDir

class MyColumnView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # creating an object of QFileSystemModel() class
        self.myfile = QFileSystemModel()
        
        # serTootPath(): Installs a file system watcher on it and changes the directory 
        # that the model is watching to newPath. The model will update if files 
        # or directories in this directory change.
        self.myfile.setRootPath(QDir.rootPath())
        print(QDir.rootPath()) # returns the root directory's absolute path.
        print(QDir.homePath()) # returns the user's home directory's absolute path.
        print(QDir.currentPath()) # provides the current directory of the application's absolute path.
        
        for dirname in (QDir.rootPath(), QDir.homePath(), QDir.currentPath()):
            # model is set for the Columnview
            self.ui.columnView.setModel(self.myfile)
            
            # setRootIndex: Sets the item at the specified index as the root item.
            self.ui.columnView.setRootIndex(self.myfile.index(dirname))
        self.show()

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyColumnView()
    w.show()
    sys.exit(app.exec_())