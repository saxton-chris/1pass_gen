# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordGenerator.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(475, 337)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.passGenButton = QPushButton(self.centralwidget)
        self.passGenButton.setObjectName(u"passGenButton")
        self.passGenButton.setGeometry(QRect(310, 260, 139, 26))
        font = QFont()
        font.setFamilies([u"Georgia"])
        self.passGenButton.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 37, 269, 28))
        self.layoutWidget.setFont(font)
        self.passLengthLayout = QHBoxLayout(self.layoutWidget)
        self.passLengthLayout.setObjectName(u"passLengthLayout")
        self.passLengthLayout.setContentsMargins(0, 0, 0, 0)
        self.passPromptLabel = QLabel(self.layoutWidget)
        self.passPromptLabel.setObjectName(u"passPromptLabel")
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        font1.setBold(True)
        self.passPromptLabel.setFont(font1)

        self.passLengthLayout.addWidget(self.passPromptLabel)

        self.passLengthField = QLineEdit(self.layoutWidget)
        self.passLengthField.setObjectName(u"passLengthField")
        self.passLengthField.setFont(font)

        self.passLengthLayout.addWidget(self.passLengthField)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 72, 445, 172))
        self.inputLayout = QHBoxLayout(self.widget)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.charTypeLayout = QVBoxLayout()
        self.charTypeLayout.setObjectName(u"charTypeLayout")
        self.charTypeLabel = QLabel(self.widget)
        self.charTypeLabel.setObjectName(u"charTypeLabel")
        self.charTypeLabel.setFont(font1)

        self.charTypeLayout.addWidget(self.charTypeLabel)

        self.upperCheck = QCheckBox(self.widget)
        self.upperCheck.setObjectName(u"upperCheck")
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setUnderline(False)
        self.upperCheck.setFont(font2)
        self.upperCheck.setAutoFillBackground(False)
        self.upperCheck.setChecked(True)

        self.charTypeLayout.addWidget(self.upperCheck)

        self.lowerCheck = QCheckBox(self.widget)
        self.lowerCheck.setObjectName(u"lowerCheck")
        self.lowerCheck.setFont(font)
        self.lowerCheck.setChecked(False)

        self.charTypeLayout.addWidget(self.lowerCheck)

        self.numberCheck = QCheckBox(self.widget)
        self.numberCheck.setObjectName(u"numberCheck")
        self.numberCheck.setFont(font)

        self.charTypeLayout.addWidget(self.numberCheck)

        self.specialCheck = QCheckBox(self.widget)
        self.specialCheck.setObjectName(u"specialCheck")
        self.specialCheck.setFont(font)

        self.charTypeLayout.addWidget(self.specialCheck)

        self.spaceCheck = QCheckBox(self.widget)
        self.spaceCheck.setObjectName(u"spaceCheck")
        self.spaceCheck.setFont(font)

        self.charTypeLayout.addWidget(self.spaceCheck)


        self.inputLayout.addLayout(self.charTypeLayout)

        self.onePassLayout = QVBoxLayout()
        self.onePassLayout.setObjectName(u"onePassLayout")
        self.passInfoLabel = QLabel(self.widget)
        self.passInfoLabel.setObjectName(u"passInfoLabel")
        font3 = QFont()
        font3.setFamilies([u"Georgia"])
        font3.setBold(True)
        font3.setItalic(False)
        self.passInfoLabel.setFont(font3)

        self.onePassLayout.addWidget(self.passInfoLabel)

        self.userLayout = QHBoxLayout()
        self.userLayout.setObjectName(u"userLayout")
        self.userLabel = QLabel(self.widget)
        self.userLabel.setObjectName(u"userLabel")

        self.userLayout.addWidget(self.userLabel)

        self.userTextbox = QLineEdit(self.widget)
        self.userTextbox.setObjectName(u"userTextbox")

        self.userLayout.addWidget(self.userTextbox)


        self.onePassLayout.addLayout(self.userLayout)

        self.passLayout = QHBoxLayout()
        self.passLayout.setObjectName(u"passLayout")
        self.passLabel = QLabel(self.widget)
        self.passLabel.setObjectName(u"passLabel")
        font4 = QFont()
        font4.setFamilies([u"Georgia"])
        font4.setBold(False)
        self.passLabel.setFont(font4)

        self.passLayout.addWidget(self.passLabel)

        self.passTextbox = QLineEdit(self.widget)
        self.passTextbox.setObjectName(u"passTextbox")
        self.passTextbox.setEnabled(False)

        self.passLayout.addWidget(self.passTextbox)


        self.onePassLayout.addLayout(self.passLayout)

        self.urlLayout = QHBoxLayout()
        self.urlLayout.setObjectName(u"urlLayout")
        self.webUrlLayout = QLabel(self.widget)
        self.webUrlLayout.setObjectName(u"webUrlLayout")

        self.urlLayout.addWidget(self.webUrlLayout)

        self.urlTextbox = QLineEdit(self.widget)
        self.urlTextbox.setObjectName(u"urlTextbox")
        self.urlTextbox.setClearButtonEnabled(False)

        self.urlLayout.addWidget(self.urlTextbox)


        self.onePassLayout.addLayout(self.urlLayout)

        self.webNameLayout = QHBoxLayout()
        self.webNameLayout.setObjectName(u"webNameLayout")
        self.webNameLabel = QLabel(self.widget)
        self.webNameLabel.setObjectName(u"webNameLabel")

        self.webNameLayout.addWidget(self.webNameLabel)

        self.webNameTextbox = QLineEdit(self.widget)
        self.webNameTextbox.setObjectName(u"webNameTextbox")

        self.webNameLayout.addWidget(self.webNameTextbox)


        self.onePassLayout.addLayout(self.webNameLayout)


        self.inputLayout.addLayout(self.onePassLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 475, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.passGenButton.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.passPromptLabel.setText(QCoreApplication.translate("MainWindow", u"Password Length:", None))
        self.charTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Select Character Types:", None))
        self.upperCheck.setText(QCoreApplication.translate("MainWindow", u"Upper Case Letters", None))
        self.lowerCheck.setText(QCoreApplication.translate("MainWindow", u"Lower Case Letters", None))
        self.numberCheck.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.specialCheck.setText(QCoreApplication.translate("MainWindow", u"Special Characters", None))
        self.spaceCheck.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.passInfoLabel.setText(QCoreApplication.translate("MainWindow", u"1Password Information:", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.webUrlLayout.setText(QCoreApplication.translate("MainWindow", u"Website URL:", None))
        self.urlTextbox.setText("")
        self.urlTextbox.setPlaceholderText("")
        self.webNameLabel.setText(QCoreApplication.translate("MainWindow", u"Website Name:", None))
    # retranslateUi

