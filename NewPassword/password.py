from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")

        button = QPushButton("Press Me!")

        self.setBaseSize(QSize(400,300))

        button.setFixedSize(QSize(100, 75))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication()

window = MainWindow()
window.show()

app.exec()