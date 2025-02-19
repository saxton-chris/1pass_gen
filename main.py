from password_manager.ui import main_window as main
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
