from core import MainWin2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os
import ctypes

# auto-py-to-exe



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



if __name__ == '__main__':
    if is_admin():
        app = QApplication(sys.argv)
        mainWin = MainWin2.MainWin()
        mainWin.setWindowIcon(QIcon(QPixmap(str(os.path.dirname(__file__)) + "/images/ico.png")))
        mainWin.show()
        sys.exit(app.exec_())
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
