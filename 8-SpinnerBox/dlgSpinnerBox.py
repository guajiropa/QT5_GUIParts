# -*- coding: utf-8 -*-
"""
AUTHOR      : Robert James Patterson
DATE        : 05/14/19
SYNOPSIS    : Learning to use QT5 with Python : Lesson 8 - SpinnerBox 
"""
# Form implementation generated from reading ui file 'dlgSpinner.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 260)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblTotal = QtWidgets.QLabel(Dialog)
        self.lblTotal.setGeometry(QtCore.QRect(250, 180, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Mali SemiBold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblTotal.setFont(font)
        self.lblTotal.setText("")
        self.lblTotal.setObjectName("lblTotal")
        self.spinBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBookQty.setGeometry(QtCore.QRect(290, 40, 71, 22))
        self.spinBookQty.setObjectName("spinBookQty")
        self.dblspinSugarQty = QtWidgets.QDoubleSpinBox(Dialog)
        self.dblspinSugarQty.setGeometry(QtCore.QRect(290, 110, 71, 22))
        self.dblspinSugarQty.setObjectName("dblspinSugarQty")
        self.txtBookPrice = QtWidgets.QLineEdit(Dialog)
        self.txtBookPrice.setGeometry(QtCore.QRect(120, 40, 131, 20))
        self.txtBookPrice.setObjectName("txtBookPrice")
        self.txtSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.txtSugarPrice.setGeometry(QtCore.QRect(120, 110, 131, 20))
        self.txtSugarPrice.setObjectName("txtSugarPrice")
        self.txtBookTotal = QtWidgets.QLineEdit(Dialog)
        self.txtBookTotal.setEnabled(False)
        self.txtBookTotal.setGeometry(QtCore.QRect(392, 40, 131, 20))
        self.txtBookTotal.setObjectName("txtBookTotal")
        self.txtSugarTotal = QtWidgets.QLineEdit(Dialog)
        self.txtSugarTotal.setEnabled(False)
        self.txtSugarTotal.setGeometry(QtCore.QRect(392, 110, 131, 20))
        self.txtSugarTotal.setObjectName("txtSugarTotal")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))


