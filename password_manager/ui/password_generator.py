from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QLabel,
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
        self._setup_1password_fields()

        # Main container for input widgets
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(10, 72, 445, 172))

        self.inputLayout = QHBoxLayout(self.widget)
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.addLayout(self.charTypeLayout)
        self.inputLayout.addLayout(self.onePassLayout)

        MainWindow.setCentralWidget(self.centralwidget)

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
        
    def _setup_1password_fields(self):
        self.onePassLayout = QVBoxLayout()
        self.onePassLayout.setObjectName(u"onePassLayout")

        self.infoLabel = QLabel("1Password Information:")
        self.infoLabel.setFont(self.boldFont)
        
        self.gridLayout = QGridLayout()
        
        labels = ["1Pass Vault:", "Username:", "Password:", "Website URL:", "Website Name:"]
        self.fields = {}
        
        for row, text in enumerate(labels):
            label = QLabel(text)
            field = QLineEdit()
            self.gridLayout.addWidget(label, row, 0)
            self.gridLayout.addWidget(field, row, 1)
            self.fields[text] = field

        self.onePassLayout.addWidget(self.infoLabel)
        self.onePassLayout.addLayout(self.gridLayout)

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
            
            self.fields["Password:"].setText(password)
            clipboard = QApplication.clipboard()
            clipboard.setText(password)

        except ValueError:
            self.passLengthField.setText("Enter a number")
            self.passLengthField.selectAll()
