from personaos.utils.history import HistoryBuffer


def test_history_buffer():
    history = HistoryBuffer(size=3)

    history.add(1)
    history.add(2)
    history.add(3)

    assert history.data()[-3:] == [1, 2, 3]
