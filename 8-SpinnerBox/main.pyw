"""
AUTHOR      : Robert James Patterson
DATE        : 05/14/19
SYNOPSIS    : Learning to use QT5 with Python : Lesson 8 - SpinnerBox 
"""
import sys
from PyQt5.QtWidgets import QApplication 
from SpinnerBox import SpinnerBox


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = SpinnerBox()
    dlg.show()
    sys.exit(app.exec_())