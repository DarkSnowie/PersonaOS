from PySide6.QtGui import (
    QColor,
    QPainter,
    QPainterPath,
    QPen,
)
from PySide6.QtWidgets import QWidget


class MiniGraph(QWidget):
    def __init__(self):
        super().__init__()

        self.points = [0] * 60
        self.setMinimumHeight(55)

    def setData(self, data):
        self.points = data
        self.update()

    def paintEvent(self, event):
        if len(self.points) < 2:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        w = self.width()
        h = self.height()

        step = w / (len(self.points) - 1)

        path = QPainterPath()
        path.moveTo(0, h)

        for i, value in enumerate(self.points):
            x = i * step
            y = h - (value / 100) * h

            path.lineTo(x, y)

        path.lineTo(w, h)
        path.closeSubpath()

        painter.fillPath(path, QColor(94, 200, 255, 40))

        pen = QPen(QColor("#5ec8ff"))
        pen.setWidth(2)

        painter.setPen(pen)

        line = QPainterPath()

        for i, value in enumerate(self.points):
            x = i * step
            y = h - (value / 100) * h

            if i == 0:
                line.moveTo(x, y)
            else:
                line.lineTo(x, y)

        painter.drawPath(line)
