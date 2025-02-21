# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EnterCredentials.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(253, 225)
        self.widget = QWidget(dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(31, 22, 183, 164))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.onePassLabel = QLabel(self.widget)
        self.onePassLabel.setObjectName(u"onePassLabel")
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setBold(True)
        self.onePassLabel.setFont(font)

        self.verticalLayout.addWidget(self.onePassLabel)

        self.userLabel = QLabel(self.widget)
        self.userLabel.setObjectName(u"userLabel")
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        self.userLabel.setFont(font1)

        self.verticalLayout.addWidget(self.userLabel)

        self.userTextbox = QLineEdit(self.widget)
        self.userTextbox.setObjectName(u"userTextbox")
        self.userTextbox.setFont(font1)

        self.verticalLayout.addWidget(self.userTextbox)

        self.passLabel = QLabel(self.widget)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setFont(font1)

        self.verticalLayout.addWidget(self.passLabel)

        self.passTextbox = QLineEdit(self.widget)
        self.passTextbox.setObjectName(u"passTextbox")
        self.passTextbox.setFont(font1)
        self.passTextbox.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.passTextbox)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Enter Credentials", None))
        self.onePassLabel.setText(QCoreApplication.translate("dialog", u"1Password Credentials:", None))
        self.userLabel.setText(QCoreApplication.translate("dialog", u"Username:", None))
        self.passLabel.setText(QCoreApplication.translate("dialog", u"Password:", None))
    # retranslateUi

