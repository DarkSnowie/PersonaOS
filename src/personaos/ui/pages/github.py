from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class GitHubPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("GitHub")
        title.setObjectName("pageTitle")

        layout.addWidget(title)
        layout.addStretch()
