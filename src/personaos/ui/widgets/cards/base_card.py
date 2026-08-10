from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)

from personaos.services.icon_manager import IconManager


class BaseCard(QFrame):

    def __init__(self, icon: str, title: str):
        super().__init__()

        self.setObjectName("card")

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        # -------------------------
        # Header
        # -------------------------

        header = QHBoxLayout()

        self.icon = QLabel()
        self.icon.setPixmap(
            IconManager.get(icon).pixmap(24, 24)
        )

        self.title = QLabel(title)
        self.title.setObjectName("cardTitle")

        header.addWidget(self.icon)
        header.addWidget(self.title)
        header.addStretch()

        root.addLayout(header)

        # -------------------------
        # Value
        # -------------------------

        self.value = QLabel("--")

        font = QFont()
        font.setPointSize(28)
        font.setBold(True)

        self.value.setFont(font)

        self.value.setObjectName("cardValue")

        root.addWidget(self.value)

        # -------------------------
        # Subtitle
        # -------------------------

        self.subtitle = QLabel("")
        self.subtitle.setObjectName("cardSubtitle")

        root.addWidget(self.subtitle)

        root.addStretch()

    def setValue(self, value):
        self.value.setText(value)

    def setSubtitle(self, text):
        self.subtitle.setText(text)
