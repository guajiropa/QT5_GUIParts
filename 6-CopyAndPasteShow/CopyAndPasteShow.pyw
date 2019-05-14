# -*- coding: utf-8 -*-
"""
AUTHOR      : Robert James Patterson
DATE        : 04/28/19
SYNOPSIS    : Learning to use QT5 with Python
"""
# Form implementation generated from reading ui file 'CopyAndPasteShow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgCopyAndPasteShow(object):
    def setupUi(self, dlgCopyAndPasteShow):
        dlgCopyAndPasteShow.setObjectName("dlgCopyAndPasteShow")
        dlgCopyAndPasteShow.resize(480, 369)
        self.txtLineEditSource = QtWidgets.QLineEdit(dlgCopyAndPasteShow)
        self.txtLineEditSource.setGeometry(QtCore.QRect(9, 78, 461, 20))
        self.txtLineEditSource.setObjectName("txtLineEditSource")
        self.txtLineEditPasted = QtWidgets.QLineEdit(dlgCopyAndPasteShow)
        self.txtLineEditPasted.setGeometry(QtCore.QRect(9, 120, 461, 20))
        self.txtLineEditPasted.setObjectName("txtLineEditPasted")
        self.cmdCopy = QtWidgets.QPushButton(dlgCopyAndPasteShow)
        self.cmdCopy.setGeometry(QtCore.QRect(10, 220, 461, 23))
        self.cmdCopy.setObjectName("cmdCopy")
        self.cmdPaste = QtWidgets.QPushButton(dlgCopyAndPasteShow)
        self.cmdPaste.setGeometry(QtCore.QRect(10, 260, 462, 23))
        self.cmdPaste.setObjectName("cmdPaste")
        # Wire up events configured in the 'QT Designer'
        self.retranslateUi(dlgCopyAndPasteShow)
        self.cmdCopy.pressed.connect(self.txtLineEditSource.selectAll)
        self.cmdCopy.released.connect(self.txtLineEditSource.cut)
        self.cmdCopy.pressed.connect(self.txtLineEditPasted.clear)
        self.cmdPaste.pressed.connect(self.txtLineEditSource.clear)
        self.cmdPaste.released.connect(self.txtLineEditPasted.paste)
        QtCore.QMetaObject.connectSlotsByName(dlgCopyAndPasteShow)

    def retranslateUi(self, dlgCopyAndPasteShow):
        _translate = QtCore.QCoreApplication.translate
        dlgCopyAndPasteShow.setWindowTitle(_translate("dlgCopyAndPasteShow", "Dialog"))
        self.cmdCopy.setText(_translate("dlgCopyAndPasteShow", "Copy"))
        self.cmdPaste.setText(_translate("dlgCopyAndPasteShow", "Paste"))


