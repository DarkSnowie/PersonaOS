from personaos.ui.widgets.cards.base_card import BaseCard


class NetworkCard(BaseCard):

    def __init__(self):
        super().__init__("Network")

        self.setValue("--")
