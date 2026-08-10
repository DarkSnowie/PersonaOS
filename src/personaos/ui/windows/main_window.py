from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from personaos.ui.layouts.header import Header
from personaos.ui.layouts.sidebar import Sidebar
from personaos.ui.pages.dashboard import DashboardPage
from personaos.ui.pages.docker import DockerPage
from personaos.ui.pages.github import GitHubPage
from personaos.ui.pages.minecraft import MinecraftPage
from personaos.ui.pages.monitoring import MonitoringPage
from personaos.ui.pages.settings import SettingsPage
from personaos.ui.pages.weather import WeatherPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("PersonaOS")
        self.resize(1600, 900)

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)

        # Sidebar
        self.sidebar = Sidebar()
        root.addWidget(self.sidebar)

        # Right side
        right = QVBoxLayout()

        self.header = Header()

        # Stacked pages
        self.stack = QStackedWidget()

        self.stack.addWidget(DashboardPage())
        self.stack.addWidget(MonitoringPage())
        self.stack.addWidget(DockerPage())
        self.stack.addWidget(GitHubPage())
        self.stack.addWidget(MinecraftPage())
        self.stack.addWidget(WeatherPage())
        self.stack.addWidget(SettingsPage())

        right.addWidget(self.header)
        right.addWidget(self.stack)

        root.addLayout(right)

        # Connect sidebar buttons to pages
        self.sidebar.pageChanged.connect(self.stack.setCurrentIndex)
