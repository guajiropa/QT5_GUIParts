"""
AUTHOR      : Robert James Patterson
DATE        : 05/15/19
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
            try:
                bookPrice = float(self.ui.txtBookPrice.text())
            except:
                self.ui.txtBookPrice.setText("Please enter numeric values only!")
        else:
            bookPrice = 0
            
        totalBookAmount = self.ui.spinBookQty.value() * bookPrice
        self.ui.txtBookTotal.setText(str(round(totalBookAmount, 2)))

    def sugarResult(self):
        
        if len(self.ui.txtSugarPrice.text()) != 0:
            try:
                sugarPrice = float(self.ui.txtSugarPrice.text())
            except:
                self.ui.txtSugarPrice.setText("Please enter numeric values only!")
        else:
            sugarPrice = 0

        totalSugarAmount = self.ui.dblspinSugarQty.value() * sugarPrice
        self.ui.txtSugarTotal.setText(str(round(totalSugarAmount, 2)))
        
        totalBookAmount = float(self.ui.txtBookTotal.text())
        totalAmount = totalBookAmount + totalSugarAmount
        self.ui.lblTotal.setText(str(round(totalAmount, 2)))



        

