from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from personaos.ui.widgets.cards.cpu_card import CpuCard
from personaos.ui.widgets.cards.disk_card import DiskCard
from personaos.ui.widgets.cards.gpu_card import GpuCard
from personaos.ui.widgets.cards.ram_card import RamCard


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        title = QLabel("Dashboard")
        title.setObjectName("pageTitle")

        root.addWidget(title)

        cards = QGridLayout()

        cards.setHorizontalSpacing(24)
        cards.setVerticalSpacing(24)
        cards.setContentsMargins(0, 20, 0, 20)

        self.cpu_card = CpuCard()
        self.ram_card = RamCard()
        self.gpu_card = GpuCard()
        self.disk_card = DiskCard()

        cards.addWidget(self.cpu_card, 0, 0)
        cards.addWidget(self.ram_card, 0, 1)
        cards.addWidget(self.gpu_card, 0, 2)
        cards.addWidget(self.disk_card, 0, 3)

        cards.setColumnStretch(0, 1)
        cards.setColumnStretch(1, 1)
        cards.setColumnStretch(2, 1)
        cards.setColumnStretch(3, 1)

        cards.setHorizontalSpacing(20)
        cards.setVerticalSpacing(20)

        root.addLayout(cards)

        root.addStretch()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)

        # First update immediately
        self.refresh()

        # Update every second
        self.timer.start(1000)

    def refresh(self):
        self.cpu_card.update_value()
        self.ram_card.update_value()
        self.disk_card.update_value()
        self.gpu_card.update_value()
