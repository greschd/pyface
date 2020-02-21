from . import qt_api

if qt_api == 'pyqt':
    from PyQt4.QtMultimedia import *

elif qt_api == 'pyqt5':
    from PyQt5.QtMultimedia import *

elif qt_api == 'pyside2':
    from PySide2.QtMultimedia import *

else:
    from PySide.QtMultimedia import *
