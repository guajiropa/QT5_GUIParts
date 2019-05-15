"""
AUTHOR      : Robert James Patterson
DATE        : 05/14/19
SYNOPSIS    : Learning to use QT5 with Python : Lesson 8 - SpinnerBox 
"""
from PyQt5.QtWidgets import QDialog
from dlgSpinnerBox import Ui_Dialog


class SpinnerBox(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBookQty.editingFinished.connect(self.bookResult)
        self.ui.dblspinSugarQty.editingFinished.connect(self.sugarResult)
        self.show()

    def bookResult(self):
        if len(self.ui.txtBookPrice.text()) != 0:
            bookPrice = int(self.ui.txtBookPrice.text())
        else:
            bookPrice = 0
            
        totalBookAmount = self.ui.spinBookQty.value() * bookPrice
        self.ui.txtBookTotal.setText(str(totalBookAmount))

    def sugarResult(self):
        pass

