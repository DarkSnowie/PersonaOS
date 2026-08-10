from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class CpuCard(BaseCard):

    def __init__(self):
        super().__init__("cpu", "CPU")

    def update_value(self):
        cpu = SystemMonitor.cpu_percent()

        self.setValue(f"{cpu:.0f}%")
        self.setSubtitle(SystemMonitor.cpu_name())
