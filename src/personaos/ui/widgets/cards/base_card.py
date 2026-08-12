from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QFrame,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)

from personaos.services.icon_manager import IconManager
from personaos.ui.widgets.mini_graph import MiniGraph
from personaos.utils.animations import AnimatedNumber
from personaos.utils.history import HistoryBuffer


class BaseCard(QFrame):
    def __init__(self, icon: str, title: str):
        super().__init__()

        self.setObjectName("card")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(28)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 90))
        self.setGraphicsEffect(shadow)

        root = QVBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(12)

        header = QHBoxLayout()

        self.icon = QLabel()
        self.icon.setPixmap(IconManager.get(icon).pixmap(24, 24))

        self.title = QLabel(title)
        self.title.setObjectName("cardTitle")

        header.addWidget(self.icon)
        header.addWidget(self.title)
        header.addStretch()

        root.addLayout(header)

        self.value = QLabel("--")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.value.setFont(font)
        self.value.setObjectName("cardValue")
        root.addWidget(self.value)

        self.graph = MiniGraph()
        root.addWidget(self.graph)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setTextVisible(False)
        self.progress.setObjectName("cardProgress")
        root.addWidget(self.progress)

        self.subtitle = QLabel("")
        self.subtitle.setObjectName("cardSubtitle")
        root.addWidget(self.subtitle)

        root.addStretch()

        self.history = HistoryBuffer()

        self.progressAnimation = QPropertyAnimation(self.progress, b"value")
        self.progressAnimation.setDuration(300)

        self.displayValue = AnimatedNumber(self._updateNumber)

        self.animation = QPropertyAnimation(self.displayValue, b"value")
        self.animation.setDuration(300)

        self.numberSuffix = "%"

    def setValue(self, text):
        self.value.setText(text)

    def setSubtitle(self, text):
        self.subtitle.setText(text)

    def setAnimatedValue(self, value: int, suffix="%"):
        self.numberSuffix = suffix
        self.animateNumber(value)

    def animateNumber(self, value):
        self.animation.stop()

        self.animation.setStartValue(self.displayValue.getValue())

        self.animation.setEndValue(value)

        self.animation.start()

    def _updateNumber(self, value):
        self.value.setText(f"{int(value)}{self.numberSuffix}")

    def setProgress(self, value):
        if value is None:
            value = 0

        value = max(0, min(100, int(value)))

        self.progressAnimation.stop()

        self.progressAnimation.setStartValue(self.progress.value())

        self.progressAnimation.setEndValue(value)

        self.progressAnimation.start()

        self.history.add(value)
        self.graph.setData(self.history.data())
