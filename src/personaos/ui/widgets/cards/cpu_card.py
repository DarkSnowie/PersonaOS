from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class CpuCard(BaseCard):
    def __init__(self):
        super().__init__("cpu", "CPU")

    def update_value(self):
        cpu = SystemMonitor.cpu_percent()

        self.setAnimatedValue(int(cpu))
        self.setProgress(cpu)

        self.setSubtitle(
            f"{SystemMonitor.cpu_name()}\n{SystemMonitor.cpu_freq():.2f} GHz"
        )
