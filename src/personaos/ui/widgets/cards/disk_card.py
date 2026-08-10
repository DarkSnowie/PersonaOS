from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class DiskCard(BaseCard):

    def __init__(self):
        super().__init__("disk", "Storage")

    def update_value(self):
        disk = SystemMonitor.disk_percent()
        self.setValue(f"{disk:.0f}%")
