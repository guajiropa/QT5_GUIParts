# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myLineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 300)
        self.lblEnterName = QtWidgets.QLabel(Dialog)
        self.lblEnterName.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.lblEnterName.setObjectName("lblEnterName")
        self.lblResponse = QtWidgets.QLabel(Dialog)
        self.lblResponse.setGeometry(QtCore.QRect(36, 120, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(20)
        self.lblResponse.setFont(font)
        self.lblResponse.setObjectName("lblResponse")
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(130, 30, 271, 20))
        self.txtName.setObjectName("txtName")
        self.btnClickMe = QtWidgets.QPushButton(Dialog)
        self.btnClickMe.setGeometry(QtCore.QRect(160, 210, 111, 41))
        self.btnClickMe.setAutoDefault(True)
        self.btnClickMe.setDefault(True)
        self.btnClickMe.setFlat(False)
        self.btnClickMe.setObjectName("btnClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblEnterName.setText(_translate("Dialog", "Please enter your name"))
        self.lblResponse.setText(_translate("Dialog", "TextLabel"))
        self.btnClickMe.setText(_translate("Dialog", "Click Me!"))


