# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selection.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 320)
        self.grid_layout = QGridLayout(Dialog)
        self.grid_layout.setObjectName(u"grid_layout")
        self.text_description = QTextBrowser(Dialog)
        self.text_description.setObjectName(u"text_description")

        self.grid_layout.addWidget(self.text_description, 3, 0, 1, 1)

        self.combo_model = QComboBox(Dialog)
        self.combo_model.setObjectName(u"combo_model")

        self.grid_layout.addWidget(self.combo_model, 1, 0, 1, 1)

        self.button_box = QDialogButtonBox(Dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.grid_layout.addWidget(self.button_box, 4, 0, 1, 1)

        self.combo_character = QComboBox(Dialog)
        self.combo_character.setObjectName(u"combo_character")

        self.grid_layout.addWidget(self.combo_character, 0, 0, 1, 1)

        self.label_image = QLabel(Dialog)
        self.label_image.setObjectName(u"label_image")

        self.grid_layout.addWidget(self.label_image, 2, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Selection", None))
        self.combo_model.setPlaceholderText(QCoreApplication.translate("Dialog", u"Model", None))
        self.combo_character.setPlaceholderText(QCoreApplication.translate("Dialog", u"Character", None))
        self.label_image.setText("")
    # retranslateUi

