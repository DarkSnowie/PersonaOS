from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from personaos.services.icon_manager import IconManager


class Sidebar(QWidget):

    pageChanged = Signal(int)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        pages = [
            ("dashboard", "Dashboard"),
            ("monitoring", "Monitoring"),
            ("docker", "Docker"),
            ("github", "GitHub"),
            ("minecraft", "Minecraft"),
            ("weather", "Weather"),
            ("settings", "Settings"),
        ]

        self.buttons = []

        for index, (icon, name) in enumerate(pages):
            button = QPushButton(name)
            button.setMinimumHeight(54)
            button.setIcon(
                IconManager.get(icon)
            )

            button.setIconSize(QSize(20, 20))

            layout.addWidget(button)
            self.buttons.append(button)

        layout.addStretch()
