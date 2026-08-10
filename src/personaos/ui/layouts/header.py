from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QWidget


class Header(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)

        self.title = QLabel("PersonaOS")

        self.cpu = QLabel("CPU 0%")
        self.ram = QLabel("RAM 0%")
        self.clock = QLabel("00:00:00")

        self.theme = QPushButton("🌙")

        layout.addWidget(self.title)

        layout.addStretch()

        layout.addWidget(self.cpu)
        layout.addWidget(self.ram)
        layout.addWidget(self.clock)
        layout.addWidget(self.theme)
