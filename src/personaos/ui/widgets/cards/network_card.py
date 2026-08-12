from personaos.ui.widgets.cards.base_card import BaseCard


class NetworkCard(BaseCard):
    def __init__(self):
        super().__init__("wifi", "Network")

    def update_value(self):
        self.setValue("--")
        self.setProgress(0)
        self.setSubtitle("Disconnected")
