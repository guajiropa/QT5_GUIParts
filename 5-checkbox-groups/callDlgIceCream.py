"""
AUTHOR      : Robert James Patterson
DATE        : 04/24/19
SYNOPSIS    : Learning to use QT5 with Python
"""
from PyQt5.QtWidgets import QDialog, QWidget, QPushButton
from dlgIceCreamShop import Ui_dlgIceCreamShop


class IceCreamShop(QDialog):

    def __init__(self):
        super().__init__()
        
        self.ui = Ui_dlgIceCreamShop()
        self.ui.setupUi(self)
        self.ui.chkCookieDough.stateChanged.connect(self.displayAmount)
        self.ui.chkMintChip.stateChanged.connect(self.displayAmount)
        self.ui.chkRockyRoad.stateChanged.connect(self.displayAmount)
        self.ui.chkSpumoni.stateChanged.connect(self.displayAmount)
        self.ui.chkCoffee.stateChanged.connect(self.displayAmount)
        self.ui.chkScotch.stateChanged.connect(self.displayAmount)
        self.ui.chkSoda.stateChanged.connect(self.displayAmount)
        self.show()


    def displayAmount(self):
        
        amount = 0.00

        if self.ui.chkCookieDough.isChecked() == True:
            amount = amount + 2.00
        if self.ui.chkMintChip.isChecked() == True:
            amount = amount + 2.25
        if self.ui.chkRockyRoad.isChecked() == True:
            amount = amount + 2.75
        if self.ui.chkSpumoni.isChecked() == True:
            amount = amount + 2.50
        if self.ui.chkCoffee.isChecked() == True:
            amount = amount + 1.50
        if self.ui.chkSoda.isChecked() == True:
            amount = amount + 1.25
        if self.ui.chkScotch.isChecked() == True:
            amount = amount + 3.00

        self.ui.lblTotal.setText("Your total is : $" + str(amount))