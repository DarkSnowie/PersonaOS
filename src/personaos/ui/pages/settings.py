from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setObjectName("pageTitle")

        layout.addWidget(title)
        layout.addStretch()
