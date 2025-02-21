from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMenuBar, QPushButton,    QStatusBar, QVBoxLayout, QWidget)
from password_manager import config
from password_manager import generator as gen
from password_manager.ui import enter_credentials as creds

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        This class defines the UI layout and behavior for the Password Generator application
        using PySide6.
        """
        
        # Set up main window properties
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 310)
        self.centralwidget = QWidget(MainWindow)

        self._set_fonts()

        # Button for generating password
        self.passGenButton = QPushButton(self.centralwidget)
        self.passGenButton.setObjectName(u"passGenButton")
        self.passGenButton.setGeometry(QRect(310, 260, 139, 26))
        self.passGenButton.setFont(self.defaultFont)
        self.passGenButton.clicked.connect(self.generate_password)

        # Layout for password length input
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 37, 269, 28))
        self.layoutWidget.setFont(self.defaultFont)

        self.passLengthLayout = QHBoxLayout(self.layoutWidget)
        self.passLengthLayout.setObjectName(u"passLengthLayout")
        self.passLengthLayout.setContentsMargins(0, 0, 0, 0)

        self.passPromptLabel = QLabel(self.layoutWidget)
        self.passPromptLabel.setObjectName(u"passPromptLabel")
        self.passPromptLabel.setFont(self.boldFont)

        self.passLengthLayout.addWidget(self.passPromptLabel)

        self.passLengthField = QLineEdit(self.layoutWidget)
        self.passLengthField.setObjectName(u"passLengthField")
        self.passLengthField.setFont(self.defaultFont)
        self.passLengthField.returnPressed.connect(self.generate_password)

        self.passLengthLayout.addWidget(self.passLengthField)

        # Main container for input widgets
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 72, 445, 172))
        self.inputLayout = QHBoxLayout(self.widget)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(0, 0, 0, 0)

        # Character type selection layout
        self.charTypeLayout = QVBoxLayout()
        self.charTypeLayout.setObjectName(u"charTypeLayout")

        self.charTypeLabel = QLabel(self.widget)
        self.charTypeLabel.setObjectName(u"charTypeLabel")
        self.charTypeLabel.setFont(self.boldFont)

        self.charTypeLayout.addWidget(self.charTypeLabel)

        # Checkboxes for character type selection
        self.upperCheck = QCheckBox(self.widget)
        self.upperCheck.setObjectName(u"upperCheck")
        self.upperCheck.setFont(self.defaultFont)
        self.upperCheck.setAutoFillBackground(False)
        self.upperCheck.setChecked(True)

        self.charTypeLayout.addWidget(self.upperCheck)

        self.lowerCheck = QCheckBox(self.widget)
        self.lowerCheck.setObjectName(u"lowerCheck")
        self.lowerCheck.setFont(self.defaultFont)
        self.lowerCheck.setChecked(True)

        self.charTypeLayout.addWidget(self.lowerCheck)

        self.numberCheck = QCheckBox(self.widget)
        self.numberCheck.setObjectName(u"numberCheck")
        self.numberCheck.setFont(self.defaultFont)
        self.numberCheck.setChecked(True)

        self.charTypeLayout.addWidget(self.numberCheck)

        self.specialCheck = QCheckBox(self.widget)
        self.specialCheck.setObjectName(u"specialCheck")
        self.specialCheck.setFont(self.defaultFont)
        self.specialCheck.setChecked(True)

        self.charTypeLayout.addWidget(self.specialCheck)

        self.spaceCheck = QCheckBox(self.widget)
        self.spaceCheck.setObjectName(u"spaceCheck")
        self.spaceCheck.setFont(self.defaultFont)

        self.charTypeLayout.addWidget(self.spaceCheck)

        self.inputLayout.addLayout(self.charTypeLayout)

        self.onePassLayout = QVBoxLayout()
        self.onePassLayout.setObjectName(u"onePassLayout")
        
        self.passInfoLabel = QLabel(self.widget)
        self.passInfoLabel.setObjectName(u"passInfoLabel")
        self.passInfoLabel.setFont(self.boldFont)

        self.onePassLayout.addWidget(self.passInfoLabel)

        self.vaultLayout = QHBoxLayout()
        self.vaultLayout.setObjectName(u"vaultLayout")
        self.vaultLabel = QLabel(self.widget)
        self.vaultLabel.setObjectName(u"vaultLabel")

        self.vaultLayout.addWidget(self.vaultLabel)

        self.vaultTextbox = QLineEdit(self.widget)
        self.vaultTextbox.setObjectName(u"vaultTextbox")

        self.vaultLayout.addWidget(self.vaultTextbox)

        self.onePassLayout.addLayout(self.vaultLayout)

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
        self.passLabel.setFont(self.defaultFont)

        self.passLayout.addWidget(self.passLabel)

        # Generate and display password
        self.passTextbox = QLineEdit(self.widget)
        self.passTextbox.setObjectName(u"passTextbox")
        self.passTextbox.setReadOnly(True)

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
        self.menubar.setGeometry(QRect(0, 0, 474, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    
    def _set_fonts(self):
        """Sets default fonts for UI elements."""
        self.defaultFont = QFont("Georgia")
        self.boldFont = QFont("Georgia", weight=QFont.Bold)

    def retranslateUi(self, MainWindow):
        """
        Translates UI elements to appropriate text values.
        """
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
        self.vaultLabel.setText(QCoreApplication.translate("MainWindow", u"1Pass Vault:", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.webUrlLayout.setText(QCoreApplication.translate("MainWindow", u"Website URL:", None))
        self.urlTextbox.setText("")
        self.urlTextbox.setPlaceholderText("")
        self.webNameLabel.setText(QCoreApplication.translate("MainWindow", u"Website Name:", None))
        self.passLengthField.setText(QCoreApplication.translate("MainWindow", f"{config.DEFAULT_LENGTH}", None))
        self.passLengthField.setFocus()
        self.passLengthField.selectAll() 
    # retranslateUi

    def generate_password(self):
        """
        Generates a random password based on selected criteria and displays it.
        """
        try:
            length = int(self.passLengthField.text())  # Get length from input field
            if length <= 0:
                self.passLengthField.setText("Invalid length")
                return
            password = gen.password_gen(length,
                                        upper=self.upperCheck.isChecked(),
                                        lower=self.lowerCheck.isChecked(),
                                        numbers=self.numberCheck.isChecked(),
                                        special=self.specialCheck.isChecked(),
                                        space=self.spaceCheck.isChecked())  # Call generator function
            
            self.passTextbox.setText(password)
            clipboard = QApplication.clipboard()
            clipboard.setText(password)

        except ValueError:
            self.passLengthField.setText("Enter a number")
            self.passLengthField.selectAll()
