from pathlib import Path

from PySide6.QtGui import QIcon


class IconManager:
    _cache = {}

    @classmethod
    def get(cls, name: str) -> QIcon:
        if name not in cls._cache:
            root = Path(__file__).resolve().parents[3]

            icon = root / "assets" / "icons" / f"{name}.svg"

            cls._cache[name] = QIcon(str(icon))

        return cls._cache[name]
