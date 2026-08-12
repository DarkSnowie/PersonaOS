from PySide6.QtCore import (
    Property,
    QObject,
)


class AnimatedNumber(QObject):
    def __init__(self, callback):
        super().__init__()
        self._value = 0
        self.callback = callback

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        self.callback(value)

    value = Property(int, getValue, setValue)
