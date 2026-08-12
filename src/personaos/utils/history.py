from collections import deque


class HistoryBuffer:
    def __init__(self, size=60):
        self.values = deque([0] * size, maxlen=size)

    def add(self, value):
        self.values.append(value)

    def data(self):
        return list(self.values)
