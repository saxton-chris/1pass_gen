from password_manager.ui import password_generator as gen_ui
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = gen_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
