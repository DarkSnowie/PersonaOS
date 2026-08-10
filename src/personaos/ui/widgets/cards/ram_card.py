from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class RamCard(BaseCard):

    def __init__(self):
        super().__init__("ram", "Memory")

    def update_value(self):
        used = SystemMonitor.ram_used()
        percent = SystemMonitor.ram_percent()

        self.setValue(f"{used:.1f} GB ({percent:.0f}%)")
