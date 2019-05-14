"""
AUTHOR      : Robert James Patterson
DATE        : 05/03/19
SYNOPSIS    : Learning to use QT5 with Python
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from dlgSimpleCalc import Ui_Dialog

class CalcForm(QDialog):

    def __init__(self):
       super().__init__()
       
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.ui.cmdAdd.clicked.connect(self.addtwonum)
       self.ui.cmdSubtract.clicked.connect(self.subtracttwonum)
       self.ui.cmdMultiply.clicked.connect(self.multiplytwonum)
       self.ui.cmdDivide.clicked.connect(self.dividetwonum)
       self.ui.cmdClear.clicked.connect(self.clear_ui)
       self.show()
    
    def clear_ui(self):
        
        self.ui.txtOperandOne.setText("")
        self.ui.txtOperandTwo.setText("")
        self.ui.lblResult.setText("")

    def addtwonum(self):
        a = 0
        b = 0

        if len(self.ui.txtOperandOne.text()) != 0:
            try:
                a = int(self.ui.txtOperandOne.text())
            except:
                self.ui.txtOperandOne.setText("Please enter a numeric value!")
        else:
            a = 0
            
        if len(self.ui.txtOperandTwo.text()) != 0:
            try:
                b = int(self.ui.txtOperandTwo.text())
            except:
                self.ui.txtOperandTwo.setText("Please enter a numeric value!")
        else:
            b = 0
        
        sum = a + b
        self.ui.lblResult.setText("The sum is : " + str(sum))

    def subtracttwonum(self):
        a = 0
        b = 0
        
        if len(self.ui.txtOperandOne.text()) != 0:
            try:
                a = int(self.ui.txtOperandOne.text())
            except:
                self.ui.txtOperandOne.setText("Please enter a numeric value!")
        else:
            a = 0

        if len(self.ui.txtOperandTwo.text()) != 0:
            try:
                b = int(self.ui.txtOperandTwo.text())
            except:
                self.ui.txtOperandTwo.setText("Please enter a numeric value!")
        else:
            b = 0

        diff = a - b
        self.ui.lblResult.setText("The difference is : " + str(diff))

    def multiplytwonum(self):
        a = 0
        b = 0

        if len(self.ui.txtOperandOne.text()) != 0:
            try:
                a = int(self.ui.txtOperandOne.text())
            except:
                self.ui.txtOperandOne.setText("Please enter a numeric value!")
        else:
            a = 0

        if len(self.ui.txtOperandTwo.text()) != 0:
            try:
                b = int(self.ui.txtOperandTwo.text())
            except:
                self.ui.txtOperandTwo.setText("Please enter a numeric value!")
        else:
            b = 0

        prod = a * b
        self.ui.lblResult.setText("The product is : " + str(prod))

    def dividetwonum(self):
        a = 0
        b = 0

        if len(self.ui.txtOperandOne.text()) != 0:
            try:
                a = int(self.ui.txtOperandOne.text())
            except:
                self.ui.txtOperandOne.setText("Please enter a numeric value!")
        else:
            a = 0

        if len(self.ui.txtOperandTwo.text()) != 0:
            try:
                b = int(self.ui.txtOperandTwo.text())
            except:
                self.ui.txtOperandTwo.setText("Please enter a numeric value!")
        else:
            b = 0      
        
        if (b == 0):
            self.ui.lblResult.setText("Dividing by zero is not allowed")
        else:
            quot = a / b
            self.ui.lblResult.setText("The quotient is : " + str(round(quot, 2)))
             

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CalcForm()
    w.show()
    sys.exit(app.exec_())
