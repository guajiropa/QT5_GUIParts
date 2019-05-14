"""
AUTHOR      : Robert James Patterson
DATE        : 04/04/19
SYNOPSIS    : Learning to use QT5 with Python
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton
from dlgExtraItems import *


class MyExtraItems(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_dlgExtraItems()
        self.ui.setupUi(self)
        self.ui.chkExtraCheese.stateChanged.connect(self.display_amount)
        self.ui.chkBlackOlives.stateChanged.connect(self.display_amount)
        self.ui.chkGreenOlives.stateChanged.connect(self.display_amount)
        self.show()
        

    def display_amount(self):
        amount = 12.00

        if self.ui.chkExtraCheese.isChecked() == True:
            amount = amount + 1.25

        if self.ui.chkBlackOlives.isChecked() == True:
            amount = amount + 0.75

        if self.ui.chkGreenOlives.isChecked() == True:
            amount = amount + 1

        self.ui.lblAmount.setText("Your total is: $" + str(amount))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyExtraItems()
    win.show()
    sys.exit(app.exec_())