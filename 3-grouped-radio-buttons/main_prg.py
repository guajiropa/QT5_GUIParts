"""
AUTHOR      :
DATE        :
SYNOPSIS    :
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from main_win import *

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # wire up the event handlers upon object creation
        self.ui.radioSmall.toggled.connect(self.display_selected)
        self.ui.radioMedium.toggled.connect(self.display_selected)
        self.ui.radioLarge.toggled.connect(self.display_selected)
        self.ui.radioXlarge.toggled.connect(self.display_selected)
        self.ui.radioCard.toggled.connect(self.display_selected)
        self.ui.radioPaypal.toggled.connect(self.display_selected)
        self.ui.radioECheck.toggled.connect(self.display_selected)

    def display_selected(self):
        selected1 = ""
        selected2 = ""

        if self.ui.radioSmall.isChecked() == True:
            selected1 = "Small"
        if self.ui.radioMedium.isChecked() == True:
            selected1 = "Medium"
        if self.ui.radioLarge.isChecked() == True:
            selected1 = "Large"
        if self.ui.radioXlarge.isChecked() == True:
            selected1 = "Extra Large"

        if self.ui.radioCard.isChecked() == True:
            selected2 = "Debit/Credit Card"
        if self.ui.radioPaypal.isChecked() == True:
            selected2 = "Pay with PayPal"
        if self.ui.radioECheck.isChecked() == True:
            selected2 = "Electronic Check"

        self.ui.lblSelected.setText("Chosen shirt size is " + selected1 + " and payment method is " + selected2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    sys.exit(app.exec_())