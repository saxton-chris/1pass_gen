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
import sys
from password_manager import config
from password_manager import generator as gen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 312)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.passGenButton = QPushButton(self.centralwidget)
        self.passGenButton.setObjectName(u"passGenButton")
        self.passGenButton.setGeometry(QRect(200, 230, 139, 26))
        self.passGenButton.clicked.connect(self.generate_password)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 34, 271, 176))

        self.passwordLayout = QVBoxLayout(self.widget)
        self.passwordLayout.setObjectName(u"passwordLayout")
        self.passwordLayout.setContentsMargins(0, 0, 0, 0)

        self.lenghtLayout = QHBoxLayout()
        self.lenghtLayout.setObjectName(u"lenghtLayout")

        self.passPromptLabel = QLabel(self.widget)
        self.passPromptLabel.setObjectName(u"passPromptLabel")

        self.lenghtLayout.addWidget(self.passPromptLabel)

        self.passLengthField = QLineEdit(self.widget)
        self.passLengthField.setObjectName(u"passLengthField")
        self.passLengthField.returnPressed.connect(self.generate_password)

        self.lenghtLayout.addWidget(self.passLengthField)


        self.passwordLayout.addLayout(self.lenghtLayout)

        self.checkBoxLayout = QVBoxLayout()
        self.checkBoxLayout.setObjectName(u"checkBoxLayout")
        self.charTypeLabel = QLabel(self.widget)
        self.charTypeLabel.setObjectName(u"charTypeLabel")

        self.checkBoxLayout.addWidget(self.charTypeLabel)

        self.upperCheck = QCheckBox(self.widget)
        self.upperCheck.setObjectName(u"upperCheck")

        self.checkBoxLayout.addWidget(self.upperCheck)

        self.lowerCheck = QCheckBox(self.widget)
        self.lowerCheck.setObjectName(u"lowerCheck")

        self.checkBoxLayout.addWidget(self.lowerCheck)

        self.numberCheck = QCheckBox(self.widget)
        self.numberCheck.setObjectName(u"numberCheck")

        self.checkBoxLayout.addWidget(self.numberCheck)

        self.specialCheck = QCheckBox(self.widget)
        self.specialCheck.setObjectName(u"specialCheck")

        self.checkBoxLayout.addWidget(self.specialCheck)

        self.spaceCheck = QCheckBox(self.widget)
        self.spaceCheck.setObjectName(u"spaceCheck")

        self.checkBoxLayout.addWidget(self.spaceCheck)


        self.passwordLayout.addLayout(self.checkBoxLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.upperCheck.setChecked(True)
        self.lowerCheck.setChecked(True)
        self.specialCheck.setChecked(True)
        self.numberCheck.setChecked(True)

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
        self.numberCheck.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.specialCheck.setText(QCoreApplication.translate("MainWindow", u"Special Characters", None))
        self.spaceCheck.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.passLengthField.setText(QCoreApplication.translate("MainWindow", f"{config.DEFAULT_LENGTH}", None))
        self.passLengthField.selectAll()    
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
        
        self.passLengthField.selectAll()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
