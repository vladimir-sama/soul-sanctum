# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.12
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 640)
        self.action_selection = QAction(MainWindow)
        self.action_selection.setObjectName(u"action_selection")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grid_layout_central = QGridLayout(self.centralwidget)
        self.grid_layout_central.setObjectName(u"grid_layout_central")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")
        self.line_edit = QLineEdit(self.centralwidget)
        self.line_edit.setObjectName(u"line_edit")

        self.grid_layout.addWidget(self.line_edit, 3, 0, 1, 1)

        self.button_send = QPushButton(self.centralwidget)
        self.button_send.setObjectName(u"button_send")

        self.grid_layout.addWidget(self.button_send, 3, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.grid_layout_image = QGridLayout(self.frame)
        self.grid_layout_image.setObjectName(u"grid_layout_image")
        self.label_image = QLabel(self.frame)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setAlignment(Qt.AlignCenter)

        self.grid_layout_image.addWidget(self.label_image, 0, 0, 1, 1)


        self.grid_layout.addWidget(self.frame, 0, 0, 1, 2)

        self.list_chat = QListWidget(self.centralwidget)
        self.list_chat.setObjectName(u"list_chat")

        self.grid_layout.addWidget(self.list_chat, 2, 0, 1, 2)

        self.label_character = QLabel(self.centralwidget)
        self.label_character.setObjectName(u"label_character")
        self.label_character.setAlignment(Qt.AlignCenter)

        self.grid_layout.addWidget(self.label_character, 1, 0, 1, 2)


        self.grid_layout_central.addLayout(self.grid_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 27))
        self.menuModel = QMenu(self.menubar)
        self.menuModel.setObjectName(u"menuModel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuModel.menuAction())
        self.menuModel.addAction(self.action_selection)
        self.menuModel.addAction(self.action_clear)
        self.menuModel.addSeparator()
        self.menuModel.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Soul Sanctum", None))
        self.action_selection.setText(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Text...", None))
        self.button_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_image.setText("")
        self.label_character.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuModel.setTitle(QCoreApplication.translate("MainWindow", u"Model", None))
    # retranslateUi

