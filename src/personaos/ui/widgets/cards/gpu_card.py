from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class GpuCard(BaseCard):
    def __init__(self):
        super().__init__("gpu", "GPU")

    def update_value(self):
        gpu = SystemMonitor.gpu_percent()

        if gpu is None:
            gpu = 0

        self.setAnimatedValue(gpu)
        self.setProgress(gpu)

        self.setSubtitle("AMD Radeon Vega 3")
