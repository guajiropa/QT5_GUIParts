"""
AUTHOR      : Robert James Patterson
DATE        : 04/28/19
SYNOPSIS    : Learning to use QT5 with Python
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from CopyAndPasteShow import Ui_dlgCopyAndPasteShow


class CopyAndPasteForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dlgCopyAndPasteShow()
        self.ui.setupUi(self)
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CopyAndPasteForm()
    win.show()
    sys.exit(app.exec_())