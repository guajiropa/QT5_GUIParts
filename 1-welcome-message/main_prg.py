import sys
from PyQt5.QtWidgets import QDialog, QApplication
from main_win import *

class MainForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lblResponse.setText(" ")
        self.ui.btnClickMe.clicked.connect(self.display_msg)
        self.show()

    def display_msg(self):
        self.ui.lblResponse.setText("Greetings, " + self.ui.txtName.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

