# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lblPrompt = QtWidgets.QLabel(Dialog)
        self.lblPrompt.setGeometry(QtCore.QRect(20, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(20)
        self.lblPrompt.setFont(font)
        self.lblPrompt.setObjectName("lblPrompt")
        self.lblFare = QtWidgets.QLabel(Dialog)
        self.lblFare.setGeometry(QtCore.QRect(10, 210, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Mali Medium")
        font.setPointSize(20)
        self.lblFare.setFont(font)
        self.lblFare.setText("")
        self.lblFare.setObjectName("lblFare")
        self.radioFirst = QtWidgets.QRadioButton(Dialog)
        self.radioFirst.setGeometry(QtCore.QRect(60, 90, 181, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioFirst.setFont(font)
        self.radioFirst.setObjectName("radioFirst")
        self.radioBusiness = QtWidgets.QRadioButton(Dialog)
        self.radioBusiness.setGeometry(QtCore.QRect(60, 120, 221, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioBusiness.setFont(font)
        self.radioBusiness.setObjectName("radioBusiness")
        self.radioEcono = QtWidgets.QRadioButton(Dialog)
        self.radioEcono.setGeometry(QtCore.QRect(60, 150, 221, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioEcono.setFont(font)
        self.radioEcono.setObjectName("radioEcono")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Flight Type"))
        self.lblPrompt.setText(_translate("Dialog", "Choose your flight type:"))
        self.radioFirst.setText(_translate("Dialog", "First Class $150"))
        self.radioBusiness.setText(_translate("Dialog", "Business Class $125"))
        self.radioEcono.setText(_translate("Dialog", "Economy Class $100"))


