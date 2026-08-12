from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget


class InfoRow(QWidget):
    def __init__(self, name):
        super().__init__()

        layout = QHBoxLayout(self)

        layout.setContentsMargins(6, 6, 6, 6)

        self.left = QLabel(name)
        self.right = QLabel("--")

        self.left.setAlignment(Qt.AlignLeft)
        self.right.setAlignment(Qt.AlignRight)

        self.left.setObjectName("infoLabel")
        self.right.setObjectName("infoValue")

        layout.addWidget(self.left)
        layout.addStretch()
        layout.addWidget(self.right)

    def setValue(self, value):
        self.right.setText(str(value))
