# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnterCredentials.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QVBoxLayout)
from typing import Tuple

class Ui_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(275, 220)
        self.setWindowTitle("Enter Credentials")

        self._set_fonts()
        self._setup_labels()
        self._setup_line_edits()
        self._setup_button_box()
        self._set_layout()

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def _set_fonts(self) -> None:
        self.defaultFont = QFont('Georgia')
        self.boldFont = QFont('Georgia', weight=QFont.Bold)
    
    def _setup_labels(self) -> None:
        self.onePassLabel = QLabel("1Password Credentials:")
        self.onePassLabel.setFont(self.boldFont)

        self.userLabel = QLabel("Username:")
        self.userLabel.setFont(self.defaultFont)

        self.passLabel = QLabel("Password:")
        self.passLabel.setFont(self.defaultFont)

    def _setup_line_edits(self) -> None:
        self.userTextbox = QLineEdit()
        self.userTextbox.setFont(self.defaultFont)

        self.passTextbox = QLineEdit(echoMode=QLineEdit.EchoMode.Password)
        self.passTextbox.setFont(self.defaultFont)

    def _setup_button_box(self) -> None:
        self.buttonBox = QDialogButtonBox(orientation=Qt.Orientation.Horizontal,
                                          standardButtons=QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok
                                          )
        self.buttonBox.setFont(self.defaultFont)

    def _set_layout(self) -> None:
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.onePassLabel)
        self.verticalLayout.addWidget(self.userLabel)
        self.verticalLayout.addWidget(self.userTextbox)
        self.verticalLayout.addWidget(self.passLabel)
        self.verticalLayout.addWidget(self.passTextbox)
        self.verticalLayout.addWidget(self.buttonBox)

        self.setLayout(self.verticalLayout)

    def get_credentials(self) -> Tuple[str, str]:
        return self.userTextbox.text(), self.passTextbox.text()