import sys
from PyQt5.QtWidgets import QDialog, QApplication
from main_win import *

class MyForm(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioFirst.toggled.connect(self.display_fare)
        self.ui.radioBusiness.toggled.connect(self.display_fare)
        self.ui.radioEcono.toggled.connect(self.display_fare)
        self.show()

    def display_fare(self):
        fare = 0

        if self.ui.radioFirst.isChecked() == True:
            fare = 150

        if self.ui.radioBusiness.isChecked() == True:
            fare = 125

        if self.ui.radioEcono.isChecked() == True:
            fare = 100

        self.ui.lblFare.setText("Air Fare is: $" + str(fare) + ".00")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyForm()
    win.show()
    sys.exit(app.exec_())