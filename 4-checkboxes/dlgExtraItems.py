# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgExtraItems.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgExtraItems(object):
    def setupUi(self, dlgExtraItems):
        dlgExtraItems.setObjectName("dlgExtraItems")
        dlgExtraItems.resize(610, 456)
        self.lblPizzaSize = QtWidgets.QLabel(dlgExtraItems)
        self.lblPizzaSize.setGeometry(QtCore.QRect(20, 20, 571, 61))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblPizzaSize.setFont(font)
        self.lblPizzaSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblPizzaSize.setObjectName("lblPizzaSize")
        self.lblAmount = QtWidgets.QLabel(dlgExtraItems)
        self.lblAmount.setGeometry(QtCore.QRect(10, 330, 581, 81))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblAmount.setFont(font)
        self.lblAmount.setText("")
        self.lblAmount.setObjectName("lblAmount")
        self.verticalLayoutWidget = QtWidgets.QWidget(dlgExtraItems)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 110, 221, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chkExtraCheese = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(14)
        self.chkExtraCheese.setFont(font)
        self.chkExtraCheese.setObjectName("chkExtraCheese")
        self.verticalLayout.addWidget(self.chkExtraCheese)
        self.chkBlackOlives = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(14)
        self.chkBlackOlives.setFont(font)
        self.chkBlackOlives.setObjectName("chkBlackOlives")
        self.verticalLayout.addWidget(self.chkBlackOlives)
        self.chkGreenOlives = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(14)
        self.chkGreenOlives.setFont(font)
        self.chkGreenOlives.setObjectName("chkGreenOlives")
        self.verticalLayout.addWidget(self.chkGreenOlives)
        self.label_3 = QtWidgets.QLabel(dlgExtraItems)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dlgExtraItems)
        QtCore.QMetaObject.connectSlotsByName(dlgExtraItems)

    def retranslateUi(self, dlgExtraItems):
        _translate = QtCore.QCoreApplication.translate
        dlgExtraItems.setWindowTitle(_translate("dlgExtraItems", "Select your extra items"))
        self.lblPizzaSize.setText(_translate("dlgExtraItems", "Medium Pizza $12.00"))
        self.chkExtraCheese.setText(_translate("dlgExtraItems", "Extra Cheese + $1.25"))
        self.chkBlackOlives.setText(_translate("dlgExtraItems", "Black Olives   + $0.75"))
        self.chkGreenOlives.setText(_translate("dlgExtraItems", "Green Olives  + $1.00"))
        self.label_3.setText(_translate("dlgExtraItems", "Select your extra toppings"))


