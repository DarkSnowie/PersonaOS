from personaos.services.monitors.system_monitor import SystemMonitor
from personaos.ui.widgets.cards.base_card import BaseCard


class GpuCard(BaseCard):

    def __init__(self):
        super().__init__("gpu", "GPU")

    def update_value(self):
        gpu = SystemMonitor.gpu_percent()

        if gpu is None:
            self.setValue("N/A")
            self.setProgress(0)
        else:
            self.setValue(f"{gpu}%")
            self.setProgress(gpu)
            self.animateNumber(int(gpu))

        self.setSubtitle("AMD Radeon Vega 3")
