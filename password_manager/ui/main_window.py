# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PasswordGeneratorVCAjMI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, #QClipboard,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import sys
from password_manager import generator as gen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(285, 122)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.passPromptLabel = QLabel(self.centralwidget)
        self.passPromptLabel.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.passPromptLabel)

        self.passLengthField = QLineEdit(self.centralwidget)
        self.passLengthField.setObjectName(u"passwordLength")
        self.passLengthField.returnPressed.connect(self.generate_password)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.passLengthField)

        self.passGenButton = QPushButton(self.centralwidget)
        self.passGenButton.setObjectName(u"passGenButton")
        self.passGenButton.clicked.connect(self.generate_password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passGenButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 285, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.passPromptLabel.setText(QCoreApplication.translate("MainWindow", u"Password Length:", None))
        self.passGenButton.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
    # retranslateUi

    def generate_password(self):
        try:
            length = int(self.passLengthField.text())  # Get length from input field
            if length <= 0:
                self.passLengthField.setText("Invalid length")
                return
            
            password = gen.password_gen(length)  # Call generator function
            
            self.passLengthField.setText(password)  # Display the password in input field
            clipboard = QApplication.clipboard()
            clipboard.setText(password)
        except ValueError:
            self.passLengthField.setText("Enter a number")
        
        # self.passLengthField.setFocus()
        self.passLengthField.selectAll()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
