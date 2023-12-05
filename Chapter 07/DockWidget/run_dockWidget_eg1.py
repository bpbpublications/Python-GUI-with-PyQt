import sys
from PyQt5 import QtWidgets, QtCore

myapp = QtWidgets.QApplication(sys.argv)

# Creating a main window object
mymainWindow = QtWidgets.QMainWindow()

# Creating a dock widget object
dockWidget = QtWidgets.QDockWidget("Dock Widget", mymainWindow)

# Setting the allowed dock widget areas
dockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)

# Adding a pushbutton to the dock widget
mybtn = QtWidgets.QPushButton("This is a dock widget")
dockWidget.setWidget(mybtn)

# Adding the dock widget to the main window
mymainWindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockWidget)

# Checking if the dock widget is floating
if dockWidget.isFloating():
    print("Dock widget is floating")
    print('-'*50)
else:
    print("Dock widget is docked")
    print('-'*50)

# Connecting to the allowedAreasChanged signal
dockWidget.allowedAreasChanged.connect(lambda myallowedAreas: print("Allowed areas changed to", myallowedAreas))

# Connecting to the dockLocationChanged signal
dockWidget.dockLocationChanged.connect(lambda myarea: print("Dock location changed to", myarea))

# Connecting to the featuresChanged signal
dockWidget.featuresChanged.connect(lambda myfeatures: print("Features changed to", myfeatures))

# Connecting to the topLevelChanged signal
dockWidget.topLevelChanged.connect(lambda mytopLevel: print("Top level changed to", mytopLevel))

# Connecting to the visibilityChanged signal
dockWidget.visibilityChanged.connect(lambda myvisible: print("Visibility changed to", myvisible))

# Setting the dock widget floating
dockWidget.setFloating(True)

mymainWindow.show()

sys.exit(myapp.exec_())
