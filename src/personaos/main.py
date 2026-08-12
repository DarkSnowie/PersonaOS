import sys

from PySide6.QtWidgets import QApplication

from personaos.ui.theme import load_theme
from personaos.ui.windows.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()

    window.setStyleSheet(load_theme())

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
