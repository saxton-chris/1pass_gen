from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from password_manager import config
from password_manager import generator as gen
from password_manager.ui import enter_credentials as creds

class Ui_MainWindow(QMainWindow):   
    def setupUi(self, MainWindow):
        """
        This class defines the UI layout and behavior for the Password Generator application
        using PySide6.
        """
        
        # Set up main window properties
        MainWindow.setObjectName('MainWindow')
        MainWindow.setWindowTitle('Password Generator')
        MainWindow.resize(470, 310)
        self.centralwidget = QWidget(MainWindow)

        self._set_fonts()
        self._setup_buttons()
        self._setup_password_input()
        self._setup_character_options()

        # Main container for input widgets
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 72, 445, 172))
        self.inputLayout = QHBoxLayout(self.widget)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
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

        self.retranslateUi()

        QMetaObject.connectSlotsByName(MainWindow)
    
    def _set_fonts(self):
        """Sets default fonts for UI elements."""
        self.defaultFont = QFont('Georgia')
        self.boldFont = QFont('Georgia', weight=QFont.Bold)

    def _setup_buttons(self):
        self.passGenButton = QPushButton(text='Generate Password', parent=self.centralwidget)
        self.passGenButton.setObjectName('passGenButton')
        self.passGenButton.setGeometry(QRect(310, 260, 139, 26))
        self.passGenButton.setFont(self.defaultFont)
        self.passGenButton.clicked.connect(self.generate_password)

    def _setup_password_input(self):
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 37, 269, 28))

        self.passLengthLayout = QHBoxLayout(self.layoutWidget)
        self.passLengthLayout.setContentsMargins(0, 0, 0, 0)

        self.passPromptLabel = QLabel('Password Length: ')
        self.passPromptLabel.setFont(self.boldFont)

        self.passLengthField = QLineEdit(str(config.DEFAULT_LENGTH))
        self.passLengthField.setFont(self.defaultFont)
        self.passLengthField.setFocus()
        self.passLengthField.selectAll() 
        self.passLengthField.returnPressed.connect(self.generate_password)
        
        self.passLengthLayout.addWidget(self.passPromptLabel)
        self.passLengthLayout.addWidget(self.passLengthField)

    def _setup_character_options(self):
        """Creates UI components for selecting character types."""
        self.charTypeLayout = QVBoxLayout()
        self.charTypeLabel = QLabel("Select Character Types:")
        self.charTypeLabel.setFont(self.boldFont)
        
        self.charTypeLayout.addWidget(self.charTypeLabel)
        self.checkboxes = {}
        
        options = {
            "upperCheck": "Upper Case Letters",
            "lowerCheck": "Lower Case Letters",
            "numberCheck": "Number",
            "specialCheck": "Special Characters",
            "spaceCheck": "Space"
        }
        
        for key, label in options.items():
            checkbox = QCheckBox(label)
            checkbox.setFont(self.defaultFont)
            checkbox.setChecked(True if key != "spaceCheck" else False)
            self.checkboxes[key] = checkbox
            self.charTypeLayout.addWidget(checkbox)
        
        # self.leftColumnLayout.addLayout(self.charTypeLayout)

    def retranslateUi(self):
        """
        Translates UI elements to appropriate text values.
        """
        self.passPromptLabel.setText(QCoreApplication.translate("MainWindow", u"Password Length:", None))
        self.charTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Select Character Types:", None))
        self.passInfoLabel.setText(QCoreApplication.translate("MainWindow", u"1Password Information:", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.vaultLabel.setText(QCoreApplication.translate("MainWindow", u"1Pass Vault:", None))
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.webUrlLayout.setText(QCoreApplication.translate("MainWindow", u"Website URL:", None))
        self.webNameLabel.setText(QCoreApplication.translate("MainWindow", u"Website Name:", None))

    def generate_password(self):
        """
        Generates a random password based on selected criteria and displays it.
        """
        try:
            length = int(self.passLengthField.text())  # Get length from input field
            if length <= 0:
                self.passLengthField.setText("Invalid length")
                return
            password = gen.password_gen(
                length,
                upper=self.checkboxes["upperCheck"].isChecked(),
                lower=self.checkboxes["lowerCheck"].isChecked(),
                numbers=self.checkboxes["numberCheck"].isChecked(),
                special=self.checkboxes["specialCheck"].isChecked(),
                space=self.checkboxes["spaceCheck"].isChecked()
            )
            
            self.passTextbox.setText(password)
            clipboard = QApplication.clipboard()
            clipboard.setText(password)

        except ValueError:
            self.passLengthField.setText("Enter a number")
            self.passLengthField.selectAll()
