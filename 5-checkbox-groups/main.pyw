"""
AUTHOR      : Robert James Patterson
DATE        : 04/24/19
SYNOPSIS    : Learning to use QT5 with Python
"""
import sys
from PyQt5.QtWidgets import QApplication
from callDlgIceCream import IceCreamShop


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ics_win = IceCreamShop()
    ics_win.show()
    sys.exit(app.exec_())