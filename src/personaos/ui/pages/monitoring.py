from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.info_row import InfoRow


class MonitoringPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("System Monitoring")
        title.setObjectName("pageTitle")

        layout.addWidget(title)

        self.cpu = InfoRow("CPU Usage")
        self.freq = InfoRow("CPU Frequency")
        self.thread = InfoRow("Threads")
        self.memory = InfoRow("Memory")
        self.disk = InfoRow("Disk")
        self.battery = InfoRow("Battery")
        self.kernel = InfoRow("Kernel")
        self.uptime = InfoRow("Uptime")

        layout.addWidget(self.cpu)
        layout.addWidget(self.freq)
        layout.addWidget(self.thread)
        layout.addWidget(self.memory)
        layout.addWidget(self.disk)
        layout.addWidget(self.battery)
        layout.addWidget(self.kernel)
        layout.addWidget(self.uptime)

        layout.addStretch()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)

        self.refresh()
        self.timer.start(1000)

    def refresh(self):

        self.cpu.setValue(f"{SystemMonitor.cpu_percent():.0f}%")

        self.freq.setValue(
            f"{SystemMonitor.cpu_freq()/1000:.2f} GHz"
        )

        self.thread.setValue(SystemMonitor.cpu_threads())

        self.memory.setValue(
            f"{SystemMonitor.ram_used():.1f} / {SystemMonitor.ram_total():.1f} GB"
        )

        self.disk.setValue(
            f"{SystemMonitor.disk_used():.1f} GB ({SystemMonitor.disk_percent():.0f}%)"
        )

        battery = SystemMonitor.battery()

        if battery:
            status = "Charging" if battery.power_plugged else "Battery"
            self.battery.setValue(
                f"{battery.percent:.0f}% ({status})"
            )
        else:
            self.battery.setValue("Desktop")

        self.kernel.setValue(SystemMonitor.kernel())

        self.uptime.setValue(SystemMonitor.uptime())
