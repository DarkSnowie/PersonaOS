from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class WeatherPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Weather")
        title.setObjectName("pageTitle")

        layout.addWidget(title)
        layout.addStretch()
