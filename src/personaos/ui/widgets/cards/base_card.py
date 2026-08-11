from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)

from personaos.services.icon_manager import IconManager
from personaos.utils.animations import AnimatedNumber


class BaseCard(QFrame):

    def __init__(self, icon: str, title: str):
        super().__init__()

        self.setObjectName("card")

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        # Header

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

        # Value

        self.value = QLabel("--")

        font = QFont()
        font.setPointSize(28)
        font.setBold(True)

        self.value.setFont(font)
        self.value.setObjectName("cardValue")

        root.addWidget(self.value)

        # Progress

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setObjectName("cardProgress")

        root.addWidget(self.progress)

        # Subtitle

        self.subtitle = QLabel("")
        self.subtitle.setObjectName("cardSubtitle")

        root.addWidget(self.subtitle)

        root.addStretch()

        # -----------------
        # Number Animation
        # -----------------

        self.displayValue = AnimatedNumber(self._updateNumber)

        self.animation = QPropertyAnimation(
            self.displayValue,
            b"value",
        )
        self.animation.setDuration(300)

    def setValue(self, value):
        self.value.setText(value)

    def setSubtitle(self, text):
        self.subtitle.setText(text)

    def setProgress(self, value):
        if value is None:
            value = 0

        self.progress.setValue(max(0, min(100, int(value))))

    def animateNumber(self, value: int):
        self.animation.stop()

        self.animation.setStartValue(
            self.displayValue.getValue()
        )

        self.animation.setEndValue(value)

        self.animation.start()

    def _updateNumber(self, value):
        self.value.setText(str(int(value)))
