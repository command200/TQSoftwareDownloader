from core import MainWin2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin2.MainWin()
    mainWin.setWindowIcon(QIcon(QPixmap(str(os.path.dirname(__file__))+"/ico.png")))
    mainWin.show()
    sys.exit(app.exec_())