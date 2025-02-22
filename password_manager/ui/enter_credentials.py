# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnterCredentials.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QVBoxLayout, QWidget)
import sys

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.resize(275, 220)
        dialog.setWindowTitle("Enter Credentials")

        self.widget = QWidget(dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(31, 22, 183, 164))

        self._set_fonts()
        self._setup_labels()
        self._setup_line_edits()
        self._setup_button_box()
        self._set_layout()

        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

    def _set_fonts(self):
        self.defaultFont = QFont('Georgia')
        self.boldFont = QFont('Georgia', weight=QFont.Bold)
    
    def _setup_labels(self):
        self.onePassLabel = QLabel("1Password Credentials:")
        self.onePassLabel.setFont(self.boldFont)

        self.userLabel = QLabel("Username:")
        self.userLabel.setFont(self.defaultFont)

        self.passLabel = QLabel("Password:")
        self.passLabel.setFont(self.defaultFont)

    def _setup_line_edits(self):
        self.userTextbox = QLineEdit()
        self.userTextbox.setFont(self.defaultFont)

        self.passTextbox = QLineEdit(echoMode=QLineEdit.EchoMode.Password)
        self.passTextbox.setFont(self.defaultFont)

    def _setup_button_box(self):
        self.buttonBox = QDialogButtonBox(orientation=Qt.Orientation.Horizontal,
                                          standardButtons=QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok
                                          )
        self.buttonBox.setFont(self.defaultFont)

    def _set_layout(self):
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.onePassLabel)
        self.verticalLayout.addWidget(self.userLabel)
        self.verticalLayout.addWidget(self.userTextbox)
        self.verticalLayout.addWidget(self.passLabel)
        self.verticalLayout.addWidget(self.passTextbox)
        self.verticalLayout.addWidget(self.buttonBox)
