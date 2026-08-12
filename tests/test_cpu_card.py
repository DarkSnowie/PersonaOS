from personaos.ui.widgets.cards.cpu_card import CpuCard


def test_cpu_card_creation(qtbot):
    card = CpuCard()
    qtbot.addWidget(card)

    assert card is not None
