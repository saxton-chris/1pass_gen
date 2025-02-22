from PySide6.QtCore import QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from password_manager import config
from password_manager import generator as gen
from password_manager.ui import enter_credentials as creds 
from password_manager import onepassword_sync as sync

class Ui_MainWindow(QMainWindow):   
    """
    This class defines the UI layout and behavior for the Password Generator application.
    It allows users to configure password generation settings and view generated passwords.
    """
    def __init__(self):
        """Initializes the Main Window and sets up the UI."""
        super().__init__()  # Call the parent class constructor
        self.setupUi()
    
    def setupUi(self):
        """
        Sets up the UI layout for the Password Generator application using PySide6.
        """
        
        self.setWindowTitle('Password Generator')
        self.resize(470, 310)
        self.centralwidget = QWidget(self)

        self._set_fonts()
        self._setup_buttons()
        self._setup_password_input()
        self._setup_character_options()
        self._setup_1password_fields()

        # Main container for input widgets
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(10, 72, 445, 172))

        # Layout to arrange character options and 1Password fields
        self.inputLayout = QHBoxLayout(self.widget)
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout.addLayout(self.charTypeLayout)
        self.inputLayout.addLayout(self.onePassLayout)

        self.setCentralWidget(self.centralwidget)
    
    def _set_fonts(self) -> None:
        """Sets default fonts for UI elements."""
        self.defaultFont = QFont('Georgia')
        self.boldFont = QFont('Georgia', weight=QFont.Bold)

    def _setup_buttons(self) -> None:
        self.passGenButton = QPushButton(text='Generate Password', parent=self.centralwidget)
        self.passGenButton.setObjectName('passGenButton')
        self.passGenButton.setGeometry(QRect(310, 260, 139, 26))
        self.passGenButton.setFont(self.defaultFont)
        self.passGenButton.clicked.connect(self.generate_password)

    def _setup_password_input(self) -> None:
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

    def _setup_character_options(self) -> None:
        """Creates UI components for selecting character types."""
        self.charTypeLayout = QVBoxLayout()
        self.charTypeLabel = QLabel("Select Character Types:")
        self.charTypeLabel.setFont(self.boldFont)
        
        self.charTypeLayout.addWidget(self.charTypeLabel)
        self.checkboxes = {}
        
        # Dictionary containing options for character selection
        options = {
            "upperCheck": "Upper Case Letters",
            "lowerCheck": "Lower Case Letters",
            "numberCheck": "Number",
            "specialCheck": "Special Characters",
            "spaceCheck": "Space"
        }
        
        # Creating checkboxes dynamically based on options
        for key, label in options.items():
            checkbox = QCheckBox(label)
            checkbox.setFont(self.defaultFont)
            checkbox.setChecked(True if key != "spaceCheck" else False)
            self.checkboxes[key] = checkbox
            self.charTypeLayout.addWidget(checkbox)
        
    def _setup_1password_fields(self) -> None:
        """Creates input fields related to 1Password integration."""
        self.onePassLayout = QVBoxLayout()
        self.onePassLayout.setObjectName(u"onePassLayout")

        self.infoLabel = QLabel("1Password Information:")
        self.infoLabel.setFont(self.boldFont)
        
        self.gridLayout = QGridLayout()
        
        # Labels for 1Password related fields
        labels = ["1Pass Vault:", "Username:", "Password:", "Website URL:", "Website Name:"]
        self.fields = {}
        
        # Creating input fields dynamically based on labels
        for row, text in enumerate(labels):
            label = QLabel(text)
            field = QLineEdit()
            self.gridLayout.addWidget(label, row, 0)
            self.gridLayout.addWidget(field, row, 1)
            self.fields[text] = field

        self.onePassLayout.addWidget(self.infoLabel)
        self.onePassLayout.addLayout(self.gridLayout)

    def generate_password(self) -> None:
        """
        Generates a random password based on selected criteria and displays it.
        """
        dialog = creds.Ui_dialog()
        dialog.exec()

        one_username, one_password = dialog.get_credentials()

        try:
            length = int(self.passLengthField.text())  # Get length from input field
            if length <= 0:
                self.passLengthField.setText("Invalid length")
                return
            # Generate password using selected options
            password = gen.password_gen(
                length,
                upper=self.checkboxes["upperCheck"].isChecked(),
                lower=self.checkboxes["lowerCheck"].isChecked(),
                numbers=self.checkboxes["numberCheck"].isChecked(),
                special=self.checkboxes["specialCheck"].isChecked(),
                space=self.checkboxes["spaceCheck"].isChecked()
            )
            
            # Display generated password in the corresponding field
            self.fields["Password:"].setText(password)
            
            # Copy generated password to clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(password)

        except ValueError:
            self.passLengthField.setText("Enter a number")
            self.passLengthField.selectAll()
