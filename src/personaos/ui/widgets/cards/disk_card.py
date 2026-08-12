from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class DiskCard(BaseCard):
    def __init__(self):
        super().__init__("disk", "Storage")

    def update_value(self):
        percent = SystemMonitor.disk_percent()
        used = SystemMonitor.disk_used()

        self.setAnimatedValue(int(percent))
        self.setProgress(percent)

        self.setSubtitle(f"{used:.1f} GB Used")
