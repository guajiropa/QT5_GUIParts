"""
AUTHOR      : Robert James Patterson
DATE        : 05/18/19
SYNOPSIS    : Learning to use QT5 with Python
"""
import sys
from PyQt5.QtWidgets import QApplication
from CalcForm import CalcForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CalcForm()
    w.show()
    sys.exit(app.exec_())
